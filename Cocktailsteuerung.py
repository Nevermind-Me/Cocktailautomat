import time
import RPi.GPIO as GPIO
import neopixel
import board
import os

GPIO.cleanup() #alles clearen

pixel_pin = board.D10 #in BCM ist das GPIO 10
num_pixels = 32
ORDER = neopixel.GRB #oder RGB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.1, auto_write=False, pixel_order=ORDER)
pixels.fill((0,0,0))
pixels.show()

pathReadyFile = "./com/Ready.txt"
pathStartFile = "./com/Start.txt"
pathMixenFile = "./com/Mixen.txt"

ReadyFile = open(pathReadyFile, "w")
ReadyStr = ReadyFile.write("True")
ReadyFile.close()

StartFile = open(pathStartFile, "w")
StartFile.write("0")
StartFile.close()

GPIO_LED = 4

GPIO_TRIGGER = 5
GPIO_ECHO = 6

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(16, GPIO.OUT) #Pumpe
GPIO.setup(17, GPIO.OUT) #Pumpe
GPIO.setup(18, GPIO.OUT) #Pumpe
GPIO.setup(19, GPIO.OUT) #Pumpe
GPIO.setup(20, GPIO.OUT) #Pumpe
GPIO.setup(21, GPIO.OUT) #Pumpe
GPIO.setup(22, GPIO.OUT) #Pumpe
GPIO.setup(23, GPIO.OUT) #Pumpe

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

GPIO.setup(GPIO_LED, GPIO.OUT) #steuert Relais für LED an (LED neben Trichter)

curTime = 0

index = 0
STEP = 255/((num_pixels/6)-1)

#Relays Ausgaenge alle auf HIGH stellen
GPIO.output(GPIO_LED, GPIO.HIGH)
for f in range(16,24):
    GPIO.output(f, GPIO.HIGH)


def distance():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
    
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    TimeElapsed = StopTime - StartTime
    #Schallgeschwindigkeit: 34300 cm/s
    distance = (TimeElapsed * 34300) / 2

    return distance


def rainbow(i,max_pixels,step):
    a = 0
    while a <= 255:
        if i == max_pixels:
            i = 0
        pixels[i] = (255,int(a),0)
        i = i + 1
        a = a + step
    a = 255
    while a >= 0:
        if i == max_pixels:
            i = 0
        pixels[i] = (int(a),255,0)
        i = i + 1
        a = a - step
    a = 0
    while a <= 255:
        if i == max_pixels:
            i = 0
        pixels[i] = (0,255,int(a))
        i = i + 1
        a = a + step
    a = 255
    while a >= 0:
        if i == max_pixels:
            i = 0
        pixels[i] = (0,int(a),255)
        i = i + 1
        a = a - step
    a = 0
    while a <= 255:
        if i == max_pixels:
            i = 0
        pixels[i] = (int(a),0,255)
        i = i + 1
        a = a + step
    a = 255
    while a >= 0:
        if i == max_pixels:
            i = 0
        pixels[i] = (255,0,int(a))
        i = i + 1
        a = a - step
    pixels.show()


if __name__ == "__main__":
    while True:
        StartFile = open(pathStartFile, "r")
        StartStr = StartFile.read()
        StartFile.close()
        #Abfrage für Lichteffekte und Entfernung
        if distance() < 17:
            GPIO.output(GPIO_LED, GPIO.LOW) #LED AN
            pixels.fill((255,0,0))
            pixels.show()
        else:
            GPIO.output(GPIO_LED, GPIO.HIGH) #LED AUS
            if index == num_pixels:
                index = 0
            rainbow(index,num_pixels,STEP)
            index = index + 1
        #Abfrage für Pumpen
        if StartStr == "1":
            #Wartung1
            StartFile = open(pathStartFile, "w")
            StartFile.write("0")
            StartFile.close()
            for x in range(16,24):
                GPIO.output(x, GPIO.LOW)
            time.sleep(15)
            for i in range(16,24):
                GPIO.output(i, GPIO.HIGH)
            ReadyFile = open(pathReadyFile, "w")
            ReadyStr = ReadyFile.write("True")
            ReadyFile.close()
        elif StartStr == "2":
            #Wartung2
            StartFile = open(pathStartFile, "w")
            StartFile.write("0")
            StartFile.close()
            for x in range(16,24):
                GPIO.output(x, GPIO.LOW)
            time.sleep(15)
            for i in range(16,24):
                GPIO.output(i, GPIO.HIGH)
            ReadyFile = open(pathReadyFile, "w")
            ReadyStr = ReadyFile.write("True")
            ReadyFile.close()
        elif StartStr == "3":
            #Mixen
            StartFile = open(pathStartFile, "w")
            StartFile.write("0")
            StartFile.close()
            MixenFile = open(pathMixenFile, "r")
            MixenStr = MixenFile.read()
            MixenFile.close()
            MixenList = MixenStr.split(",")
            pump1 = int(MixenList[0])
            pump2 = int(MixenList[1])
            TiAlk = float(MixenList[2])
            TiMix = float(MixenList[3])
            
            if TiAlk > TiMix:
                mix_duration = TiAlk
            else:
                mix_duration = TiMix

            curTime = time.time()
        
            while True:
                if pump1 != 0 and time.time() - curTime < TiAlk:
                    GPIO.output(pump1, GPIO.LOW)
                elif pump1 != 0:
                    GPIO.output(pump1, GPIO.HIGH)
                    
                if pump2 != 0 and time.time() - curTime < TiMix:
                    GPIO.output(pump2, GPIO.LOW)
                elif pump2 != 0:
                    GPIO.output(pump2, GPIO.HIGH)
                
                pixels[int(((32*(time.time()-curTime))/mix_duration)-0.9)] = (0,255,0)
                pixels.show()

                if time.time() - curTime > mix_duration:
                    break
            if pump1 != 0:        
                GPIO.output(pump1, GPIO.HIGH)
            if pump2 != 0:
                GPIO.output(pump2, GPIO.HIGH)
                
            ReadyFile = open(pathReadyFile, "w")
            ReadyStr = ReadyFile.write("True")
            ReadyFile.close()
        elif StartStr == "4":
            #Ansaugen
            StartFile = open(pathStartFile, "w")
            StartFile.write("0")
            StartFile.close()
            for x in range(16,24):
                GPIO.output(x, GPIO.LOW)
            time.sleep(7)
            for i in range(16,24):
                GPIO.output(i, GPIO.HIGH)
            ReadyFile = open(pathReadyFile, "w")
            ReadyStr = ReadyFile.write("True")
            ReadyFile.close()
        elif StartStr == "5":
            #Herunterfahren
            StartFile = open(pathStartFile, "w")
            StartFile.write("0")
            StartFile.close()
            ReadyFile = open(pathReadyFile, "w")
            ReadyStr = ReadyFile.write("True")
            ReadyFile.close()
            pixels.fill((0,0,0))
            pixels.show()
            GPIO.cleanup() #alles clearen
            os.system("sudo shutdown 0")
            break
        time.sleep(0.1)
