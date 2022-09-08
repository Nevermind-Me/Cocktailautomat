try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2
import os

global pathPasswFile
pathPasswFile = "./com/Schmutz.txt"
global pathReadyFile
pathReadyFile = "./com/Ready.txt"
global pathMixenFile
pathMixenFile = "./com/Mixen.txt"
global pathStartFile
pathStartFile = "./com/Start.txt"

global passw
passw = []
global savedpassw
savedpassw = []
passwFile = open(pathPasswFile, "r")
passwStr = passwFile.read()
passwFile.close()
for y in passwStr:
    savedpassw.append(int(y))
global AlkPickList
AlkPickList = ["kein Alkohol","Jack Daniels","Bacardi","Wodka","Bacardi Razz"]
global MixPickList
MixPickList = ["kein Mischgetränk","Cola","Bitter Lemon","Sprite","Orangen Saft"]
global PumpList
PumpList = ["Jack Daniels","Bacardi","Wodka","Bacardi Razz","Cola","Bitter Lemon","Sprite","Orangen Saft"]
global MischprozentPickList
MischprozentPickList = ["Alkohol:Mischgetränk","90:10","80:20","70:30","60:40","50:50","40:60","30:70","20:80","10:90"]
global strong_Var
strong_Var = 0


def update_all():
    if strong_Var == 1:
        bStrong.config(image=photo_Slider_Strong)
    else:
        bStrong.config(image=photo_Slider_Schwach)
    if ("Jack Daniels" in PumpList) and ("Cola" in PumpList):
        bMix1.config(state=tk.NORMAL)
    else:
        bMix1.config(state=tk.DISABLED)
    if "Bacardi" in PumpList:
        if "Cola" in PumpList:
            bMix2.config(state=tk.NORMAL)
        else:
            bMix2.config(state=tk.DISABLED)
        if "Bitter Lemon" in PumpList:
            bMix4.config(state=tk.NORMAL)
        else:
            bMix4.config(state=tk.DISABLED)
    else:
        bMix2.config(state=tk.DISABLED)
        bMix4.config(state=tk.DISABLED)
    if "Bacardi Razz" in PumpList:
        if "Sprite" in PumpList:
            bMix3.config(state=tk.NORMAL)
        else:
            bMix3.config(state=tk.DISABLED)
    else:
        bMix3.config(state=tk.DISABLED)
    if "Wodka" in PumpList:
        if "Bitter Lemon" in PumpList:
            bMix5.config(state=tk.NORMAL)
        else:
            bMix5.config(state=tk.DISABLED)
        if "Orangen Saft" in PumpList:
            bMix6.config(state=tk.NORMAL)
        else:
            bMix6.config(state=tk.DISABLED)
    else:
        bMix5.config(state=tk.DISABLED)
        bMix6.config(state=tk.DISABLED)

    if passw == savedpassw:
        WeiterB.config(state=tk.NORMAL)
    else:
        WeiterB.config(state=tk.DISABLED)
    ReadyFile = open(pathReadyFile, "r")
    if ReadyFile.read() == "True":
        Wartung1B.config(state=tk.NORMAL, bg="green")
        Wartung2B.config(state=tk.NORMAL, bg="green")
        AnsaugenB.config(state=tk.NORMAL, bg="green")
        StartB.config(state=tk.NORMAL, bg="green", fg="black")
    else:
        Wartung1B.config(state=tk.DISABLED, bg="grey")
        Wartung2B.config(state=tk.DISABLED, bg="grey")
        AnsaugenB.config(state=tk.DISABLED, bg="grey")
        StartB.config(state=tk.DISABLED, bg="grey", fg="black")
    ReadyFile.close()
    passwVar.set(passw)
    os.system(f'sudo sh -c \"echo \'{BrightSlider.get()}\' >> /sys/class/backlight/rpi_backlight/brightness\"')
    app.after(100, update_all)


def clearPassw():
    passw.clear()

def changePassw():
    savedpassw.clear()
    passwFile = open(pathPasswFile, "w")
    for i in passw:
        savedpassw.append(i)
        passwFile.write(str(i))
    passwFile.close()
    clearPassw()

def Wartung1():
    ReadyFile = open(pathReadyFile, "w")
    ReadyStr = ReadyFile.write("False")
    ReadyFile.close()
    StartFile = open(pathStartFile, "w")
    StartStr = StartFile.write("1")
    StartFile.close()

def Wartung2():
    ReadyFile = open(pathReadyFile, "w")
    ReadyStr = ReadyFile.write("False")
    ReadyFile.close()
    StartFile = open(pathStartFile, "w")
    StartStr = StartFile.write("2")
    StartFile.close()

def Ansaugen():
    ReadyFile = open(pathReadyFile, "w")
    ReadyStr = ReadyFile.write("False")
    ReadyFile.close()
    StartFile = open(pathStartFile, "w")
    StartStr = StartFile.write("4")
    StartFile.close()

def PickCallback(f,g,h):
    if AlkVar.get() == "kein Alkohol" and MixVar.get() == "kein Mischgetränk":
        AuswahlWeiterB.config(state=tk.DISABLED)
    elif AlkVar.get() != "kein Alkohol" and MixVar.get() != "kein Mischgetränk" and MischprozentVar.get() == "Alkohol:Mischgetränk":
        AuswahlWeiterB.config(state=tk.DISABLED)
    else:
        AuswahlWeiterB.config(state=tk.NORMAL)
    if AlkVar.get() == "kein Alkohol" or MixVar.get() == "kein Mischgetränk":
        MischprozentOpt.config(state=tk.DISABLED)
    else:
        MischprozentOpt.config(state=tk.NORMAL)
        

def ChangeDrink():
    PumpList[0] = ePump1.get()
    PumpList[1] = ePump2.get()
    PumpList[2] = ePump3.get()
    PumpList[3] = ePump4.get()
    PumpList[4] = ePump5.get()
    PumpList[5] = ePump6.get()
    PumpList[6] = ePump7.get()
    PumpList[7] = ePump8.get()
    AlkPickList = ["kein Alkohol"]
    MixPickList = ["kein Mischgetränk"]
    if cAlk1_Var.get() == 1:
        AlkPickList.append(ePump1.get())
    else:
        MixPickList.append(ePump1.get())
    if cAlk2_Var.get() == 1:
        AlkPickList.append(ePump2.get())
    else:
        MixPickList.append(ePump2.get())
    if cAlk3_Var.get() == 1:
        AlkPickList.append(ePump3.get())
    else:
        MixPickList.append(ePump3.get())
    if cAlk4_Var.get() == 1:
        AlkPickList.append(ePump4.get())
    else:
        MixPickList.append(ePump4.get())
    if cAlk5_Var.get() == 1:
        AlkPickList.append(ePump5.get())
    else:
        MixPickList.append(ePump5.get())
    if cAlk6_Var.get() == 1:
        AlkPickList.append(ePump6.get())
    else:
        MixPickList.append(ePump6.get())
    if cAlk7_Var.get() == 1:
        AlkPickList.append(ePump7.get())
    else:
        MixPickList.append(ePump7.get())
    if cAlk8_Var.get() == 1:
        AlkPickList.append(ePump8.get())
    else:
        MixPickList.append(ePump8.get())
    menu = AlkOpt["menu"]
    menu.delete(0, "end")
    for string in AlkPickList:
        menu.add_command(label=string,
                         command=lambda value=string: AlkVar.set(value))
    menu = MixOpt["menu"]
    menu.delete(0, "end")
    for string in MixPickList:
        menu.add_command(label=string,
                         command=lambda value=string: MixVar.set(value))


def setEntry():
    ePump1.delete(0,tk.END)
    ePump1.insert(0,PumpList[0])
    ePump2.delete(0,tk.END)
    ePump2.insert(0,PumpList[1])
    ePump3.delete(0,tk.END)
    ePump3.insert(0,PumpList[2])
    ePump4.delete(0,tk.END)
    ePump4.insert(0,PumpList[3])
    ePump5.delete(0,tk.END)
    ePump5.insert(0,PumpList[4])
    ePump6.delete(0,tk.END)
    ePump6.insert(0,PumpList[5])
    ePump7.delete(0,tk.END)
    ePump7.insert(0,PumpList[6])
    ePump8.delete(0,tk.END)
    ePump8.insert(0,PumpList[7])
    if PumpList[0] in AlkPickList:
        cAlk1.select()
    else:
        cAlk1.deselect()
    if PumpList[1] in AlkPickList:
        cAlk2.select()
    else:
        cAlk2.deselect()
    if PumpList[2] in AlkPickList:
        cAlk3.select()
    else:
        cAlk3.deselect()
    if PumpList[3] in AlkPickList:
        cAlk4.select()
    else:
        cAlk4.deselect()
    if PumpList[4] in AlkPickList:
        cAlk5.select()
    else:
        cAlk5.deselect()
    if PumpList[5] in AlkPickList:
        cAlk6.select()
    else:
        cAlk6.deselect()
    if PumpList[6] in AlkPickList:
        cAlk7.select()
    else:
        cAlk7.deselect()
    if PumpList[7] in AlkPickList:
        cAlk8.select()
    else:
        cAlk8.deselect()

def Getränk_zubereiten():
    index = 0
    
    if AlkVar.get() == "kein Alkohol":
        pump1 = 0
    else:
        for a in PumpList:
            if a == AlkVar.get():
                pump1 = index + 16
                break
            index = index + 1
            
    index = 0
    
    if MixVar.get() == "kein Mischgetränk":
        pump2 = 0
    else:
        for b in PumpList:
            if b == MixVar.get():
                pump2 = index + 16
                break
            index = index + 1
            
    index = 0
    
    if pump1 == 0:
        TimeAlk = 0
        TimeMix = 10 * (MengenSlider.get()/2.5/10)
    elif pump2 == 0:
        TimeAlk = 10 * (MengenSlider.get()/2.5/10)
        TimeMix = 0
        
    
    if pump1 > 0 and pump2 > 0:
        for c in MischprozentPickList:
            if c == MischprozentVar.get():
                TimeAlk = (10 - index) * (MengenSlider.get()/2.5/10)
                TimeMix = (index) * (MengenSlider.get()/2.5/10)
                break
            index = index + 1
    #Korrektur der ersten Pumpe (nicht so leistungsstark wie die anderen)
    if pump1 == 20:
        TimeAlk = TimeAlk * 0.66667
    elif pump2 == 20:
        TimeMix = TimeMix * 0.66667
        
    MixenFile = open(pathMixenFile, "w")
    MixenFile.write(f"{pump1},{pump2},{TimeAlk},{TimeMix}")
    MixenFile.close()
    ReadyFile = open(pathReadyFile, "w")
    ReadyStr = ReadyFile.write("False")
    ReadyFile.close()
    StartFile = open(pathStartFile, "w")
    StartStr = StartFile.write("3")
    StartFile.close()


def startMix(num):
    if num == 1:
        Alk = "Jack Daniels"
        Mix = "Cola"
    elif num == 2:
        Alk = "Bacardi"
        Mix = "Cola"
    elif num == 3:
        Alk = "Bacardi Razz"
        Mix = "Sprite"
    elif num == 4:
        Alk = "Bacardi"
        Mix = "Bitter Lemon"
    elif num == 5:
        Alk = "Wodka"
        Mix = "Bitter Lemon"
    elif num == 6:
        Alk = "Wodka"
        Mix = "Orangen Saft"

    if strong_Var == 1:
        TimeAlk = 24.0
        TimeMix = 36.0
    else:
        TimeAlk = 12.0
        TimeMix = 48.0

    index = 0

    for p in PumpList:
        if p == Alk:
            pump1 = index + 16
        if p == Mix:
            pump2 = index + 16
        index = index + 1

    #Korrektur der ersten Pumpe (nicht so leistungsstark wie die anderen)
    if pump1 == 20:
        TimeAlk = TimeAlk * 0.66667
    elif pump2 == 20:
        TimeMix = TimeMix * 0.66667
        
    MixenFile = open(pathMixenFile, "w")
    MixenFile.write(f"{pump1},{pump2},{TimeAlk},{TimeMix}")
    MixenFile.close()
    ReadyFile = open(pathReadyFile, "w")
    ReadyStr = ReadyFile.write("False")
    ReadyFile.close()
    StartFile = open(pathStartFile, "w")
    StartStr = StartFile.write("3")
    StartFile.close()


def b_Callback():
    global strong_Var
    if strong_Var == 0:
        strong_Var = 1
    else:
        strong_Var = 0


def Shutdown():
    StartFile = open(pathStartFile, "w")
    StartStr = StartFile.write("5")
    StartFile.close()



class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=25, weight="bold", slant="italic")
        self.info_font = tkfont.Font(family='Helvetica', size=20, slant="italic")
        self.B_font = tkfont.Font(family='Helvitica', size=16, weight="bold", slant="italic")
        self.StartB_font = tkfont.Font(family='Helvitica', size=40, weight="bold", slant="italic")
        self.StartTitle_font = tkfont.Font(family='Helvitica', size=40, weight="bold", slant="italic")
        self.NumB_font = tkfont.Font(family='Helvitica', size=25, weight="bold", slant="italic")
        self.OptMenu_font = tkfont.Font(family='Helvitica', size=15)
        self.Text_font = tkfont.Font(family='Helvitica', size=15)

        self.photo_Jacky_Cola = tk.PhotoImage(file="./res/Jacky-Cola.png")
        self.photo_Jacky_Cola = self.photo_Jacky_Cola.subsample(2,2)
        self.photo_Bacardi_Cola = tk.PhotoImage(file="./res/Bacardi-Cola.png")
        self.photo_Bacardi_Cola = self.photo_Bacardi_Cola.subsample(2,2)
        self.photo_Bacardi_Sprite = tk.PhotoImage(file="./res/Bacardi-Sprite.png")
        self.photo_Bacardi_Sprite = self.photo_Bacardi_Sprite.subsample(2,2)
        self.photo_Bacardi_Razz_Sprite = tk.PhotoImage(file="./res/Bacardi-Razz-Sprite.png")
        self.photo_Bacardi_Razz_Sprite = self.photo_Bacardi_Razz_Sprite.subsample(2,2)
        self.photo_Bacardi_Lemon = tk.PhotoImage(file="./res/Bacardi-Lemon.png")
        self.photo_Bacardi_Lemon = self.photo_Bacardi_Lemon.subsample(2,2)
        self.photo_Wodka_Lemon = tk.PhotoImage(file="./res/Wodka-Lemon.png")
        self.photo_Wodka_Lemon = self.photo_Wodka_Lemon.subsample(2,2)
        self.photo_Wodka_Orange = tk.PhotoImage(file="./res/Wodka-Orange.png")
        self.photo_Wodka_Orange = self.photo_Wodka_Orange.subsample(2,2)
        global photo_Slider_Strong
        photo_Slider_Strong = tk.PhotoImage(file="./res/Slider(STARK).png")
        photo_Slider_Strong = photo_Slider_Strong.subsample(4,4)
        global photo_Slider_Schwach
        photo_Slider_Schwach = tk.PhotoImage(file="./res/Slider(SCHWACH).png")
        photo_Slider_Schwach = photo_Slider_Schwach.subsample(4,4)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, Einstellungen, DrinkChangeW, AuswahlW, AuswahlWexp, WartungW1, WartungW2, PasswInput, PasswChangeW):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()



class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="white")
        label = tk.Label(self, text="Barkeeper NEXT GEN", bg="white", font=controller.StartTitle_font)
        label.place(x=75, y=125)
        global StartB
        StartB = tk.Button(self, text="Start", state=tk.DISABLED, font=controller.StartB_font, bg="green", fg="black",
                            command=lambda: controller.show_frame("AuswahlW"))
        StartB.place(x=315, y=300)
        OptB = tk.Button(self, text="Einstellungen", font=controller.B_font,
                            command=lambda: controller.show_frame("PasswInput"))
        OptB.place(x=5, y=435)



class Einstellungen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Einstellungen", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Zurück zur Startseite", font=controller.B_font,
                           command=lambda: controller.show_frame("StartPage"))
        button.pack(pady=10)
        PasswChangeB = tk.Button(self, text="Passwort ändern", font=controller.B_font,
                                 command=lambda: controller.show_frame("PasswChangeW"))
        PasswChangeB.pack(pady=10)
        label = tk.Label(self, text="Helligkeit einstellen:", font=controller.B_font)
        label.pack(pady=10)
        global BrightSlider
        BrightSlider = tk.Scale(self, from_=20, to=255, showvalue=False, length=250, width=25, orient=tk.HORIZONTAL)
        BrightSlider.set(255)
        BrightSlider.pack(pady=10)
        global AnsaugenB
        AnsaugenB = tk.Button(self, text="Ansaugen", state=tk.DISABLED, font=controller.B_font,
                              command=Ansaugen)
        AnsaugenB.pack(pady=10)
        DrinkChangeB = tk.Button(self, text="GetränkeWechseln", font=controller.B_font,
                            command=lambda: [setEntry(), controller.show_frame("DrinkChangeW")])
        DrinkChangeB.pack(pady=10)
        WartungB = tk.Button(self, text="Wartung", font=controller.B_font,
                            command=lambda: [controller.show_frame("WartungW1")])
        WartungB.place(x=5, y=435)
        ShutdownB = tk.Button(self, text="Herunterfahren", font=controller.B_font, command=Shutdown)
        ShutdownB.place(x=595, y=435)



class AuswahlW(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        AuswahlExpB = tk.Button(self, text="Selbstmischen", font=controller.B_font,
                                command=lambda: controller.show_frame("AuswahlWexp"))
        AuswahlExpB.place(x=593,y=435)
        button = tk.Button(self, text="Zurück", font=controller.B_font,
                           command=lambda: controller.show_frame("StartPage"))
        button.place(x=345,y=435)
        global bStrong
        bStrong = tk.Button(self, text="Mischungverhältnis", image=photo_Slider_Schwach, font=controller.NumB_font,
                            command=b_Callback)
        bStrong.place(x=310,y=335)
        global bMix1
        bMix1 = tk.Button(self, state=tk.DISABLED, image=controller.photo_Jacky_Cola,
                            command=lambda: [startMix(1), controller.show_frame("StartPage")])
        bMix1.place(x=30,y=50)
        global bMix2
        bMix2 = tk.Button(self, state=tk.DISABLED, image=controller.photo_Bacardi_Cola,
                            command=lambda: [startMix(2), controller.show_frame("StartPage")])
        bMix2.place(x=310,y=50)
        global bMix3
        bMix3 = tk.Button(self, state=tk.DISABLED, image=controller.photo_Bacardi_Razz_Sprite,
                            command=lambda: [startMix(3), controller.show_frame("StartPage")])
        bMix3.place(x=590,y=50)
        global bMix4
        bMix4 = tk.Button(self, state=tk.DISABLED, image=controller.photo_Bacardi_Lemon,
                            command=lambda: [startMix(4), controller.show_frame("StartPage")])
        bMix4.place(x=30,y=200)
        global bMix5
        bMix5 = tk.Button(self, state=tk.DISABLED,  image=controller.photo_Wodka_Lemon,
                            command=lambda: [startMix(5), controller.show_frame("StartPage")])
        bMix5.place(x=310,y=200)
        global bMix6
        bMix6 = tk.Button(self, state=tk.DISABLED, image=controller.photo_Wodka_Orange,
                            command=lambda: [startMix(6), controller.show_frame("StartPage")])
        bMix6.place(x=590,y=200)


class AuswahlWexp(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        global AlkVar
        AlkVar = tk.StringVar()
        AlkVar.set(AlkPickList[0])
        global MischprozentVar
        MischprozentVar = tk.StringVar()
        MischprozentVar.set(MischprozentPickList[0])
        global MixVar
        MixVar = tk.StringVar()
        MixVar.set(MixPickList[0])
        label = tk.Label(self, text="Mischung wählen", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        global AlkOpt
        AlkOpt = tk.OptionMenu(self, AlkVar, *AlkPickList)
        AlkOpt.config(font=controller.OptMenu_font)
        AlkOptMenu = self.nametowidget(AlkOpt.menuname)
        AlkOptMenu.config(font=controller.OptMenu_font)
        AlkOpt.pack(pady=10)
        global MixOpt
        MixOpt = tk.OptionMenu(self, MixVar, *MixPickList)
        MixOpt.config(font=controller.OptMenu_font)
        MixOptMenu = self.nametowidget(MixOpt.menuname)
        MixOptMenu.config(font=controller.OptMenu_font)
        MixOpt.pack(pady=10)
        global MischprozentOpt
        MischprozentOpt = tk.OptionMenu(self, MischprozentVar, *MischprozentPickList)
        MischprozentOpt.config(state=tk.DISABLED, font=controller.OptMenu_font)
        MischprozentOptMenu = self.nametowidget(MischprozentOpt.menuname)
        MischprozentOptMenu.config(font=controller.OptMenu_font)
        MischprozentOpt.pack(pady=10)
        global MengenSlider
        MengenSlider = tk.Scale(self, label="Menge in ml", from_=10, to=200, resolution=5, length=500, width=35, orient=tk.HORIZONTAL)
        MengenSlider.set(255)
        MengenSlider.pack(pady=5)
        button = tk.Button(self, text="Zurück", font=controller.B_font,
                           command=lambda: controller.show_frame("AuswahlW"))
        button.pack(side='bottom', pady=20)
        global AuswahlWeiterB
        AuswahlWeiterB = tk.Button(self, text="Getränk zubereiten", state=tk.DISABLED, font=controller.B_font,
                               command=lambda: [controller.show_frame("StartPage"), Getränk_zubereiten()])
        AuswahlWeiterB.pack(side='bottom')
        AlkVar.trace("w", PickCallback)
        MixVar.trace("w", PickCallback)
        MischprozentVar.trace("w", PickCallback)


class PasswInput(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Bitte Passwort eingeben", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        BackB = tk.Button(self, text="Zurück", font=controller.B_font,
                           command=lambda: [clearPassw(), controller.show_frame("StartPage")])
        BackB.place(x=5, y=435)
        global WeiterB
        WeiterB = tk.Button(self, text="Weiter", state=tk.DISABLED, font=controller.B_font,
                           command=lambda: [clearPassw(), controller.show_frame("Einstellungen")])
        WeiterB.place(x=685, y=435)
        ClearB = tk.Button(self, text="Clear", font=controller.B_font, command=clearPassw)
        ClearB.place(x=350, y=435)
        ZeroB = tk.Button(self, text="0", font=controller.NumB_font, command=lambda: passw.append(0))
        ZeroB.place(x=375, y=290)
        OneB = tk.Button(self, text="1", font=controller.NumB_font, command=lambda: passw.append(1))
        OneB.place(x=320, y=125)
        TwoB = tk.Button(self, text="2", font=controller.NumB_font, command=lambda: passw.append(2))
        TwoB.place(x=375, y=125)
        ThreeB = tk.Button(self, text="3", font=controller.NumB_font, command=lambda: passw.append(3))
        ThreeB.place(x=430, y=125)
        FourB = tk.Button(self, text="4", font=controller.NumB_font, command=lambda: passw.append(4))
        FourB.place(x=320, y=180)
        FiveB = tk.Button(self, text="5", font=controller.NumB_font, command=lambda: passw.append(5))
        FiveB.place(x=375, y=180)
        SixB = tk.Button(self, text="6", font=controller.NumB_font, command=lambda: passw.append(6))
        SixB.place(x=430, y=180)
        SevenB = tk.Button(self, text="7", font=controller.NumB_font, command=lambda: passw.append(7))
        SevenB.place(x=320, y=235)
        EightB = tk.Button(self, text="8", font=controller.NumB_font, command=lambda: passw.append(8))
        EightB.place(x=375, y=235)
        NineB = tk.Button(self, text="9", font=controller.NumB_font, command=lambda: passw.append(9))
        NineB.place(x=430, y=235)


class PasswChangeW(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        global passwVar
        passwVar = tk.StringVar()
        label = tk.Label(self, text="Passwort ändern", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        ChangePasswL = tk.Label(self, textvariable=passwVar)
        ChangePasswL.pack()
        BackB = tk.Button(self, text="Zurück", font=controller.B_font,
                           command=lambda: [clearPassw(), controller.show_frame("Einstellungen")])
        BackB.place(x=5, y=435)
        ClearB = tk.Button(self, text="Clear", font=controller.B_font, command=clearPassw)
        ClearB.place(x=350, y=435)
        ZeroB = tk.Button(self, text="0", font=controller.NumB_font, command=lambda: passw.append(0))
        ZeroB.place(x=375, y=290)
        OneB = tk.Button(self, text="1", font=controller.NumB_font, command=lambda: passw.append(1))
        OneB.place(x=320, y=125)
        TwoB = tk.Button(self, text="2", font=controller.NumB_font, command=lambda: passw.append(2))
        TwoB.place(x=375, y=125)
        ThreeB = tk.Button(self, text="3", font=controller.NumB_font, command=lambda: passw.append(3))
        ThreeB.place(x=430, y=125)
        FourB = tk.Button(self, text="4", font=controller.NumB_font, command=lambda: passw.append(4))
        FourB.place(x=320, y=180)
        FiveB = tk.Button(self, text="5", font=controller.NumB_font, command=lambda: passw.append(5))
        FiveB.place(x=375, y=180)
        SixB = tk.Button(self, text="6", font=controller.NumB_font, command=lambda: passw.append(6))
        SixB.place(x=430, y=180)
        SevenB = tk.Button(self, text="7", font=controller.NumB_font, command=lambda: passw.append(7))
        SevenB.place(x=320, y=235)
        EightB = tk.Button(self, text="8", font=controller.NumB_font, command=lambda: passw.append(8))
        EightB.place(x=375, y=235)
        NineB = tk.Button(self, text="9", font=controller.NumB_font, command=lambda: passw.append(9))
        NineB.place(x=430, y=235)
        PasswOkB = tk.Button(self, text="Passwort bestätigen", font=controller.B_font, command=lambda: [changePassw(), controller.show_frame("Einstellungen")])
        PasswOkB.place(x=520, y=435)


class DrinkChangeW(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Getränke Wechseln", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        labelP1 = tk.Label(self, text="Pumpe 1:", font=controller.Text_font)
        labelP1.place(x=25,y=75)
        labelP2 = tk.Label(self, text="Pumpe 2:", font=controller.Text_font)
        labelP2.place(x=25,y=115)
        labelP3 = tk.Label(self, text="Pumpe 3:", font=controller.Text_font)
        labelP3.place(x=25,y=155)
        labelP4 = tk.Label(self, text="Pumpe 4:", font=controller.Text_font)
        labelP4.place(x=25,y=195)
        labelP5 = tk.Label(self, text="Pumpe 5:", font=controller.Text_font)
        labelP5.place(x=25,y=235)
        labelP6 = tk.Label(self, text="Pumpe 6:", font=controller.Text_font)
        labelP6.place(x=25,y=275)
        labelP7 = tk.Label(self, text="Pumpe 7:", font=controller.Text_font)
        labelP7.place(x=25,y=315)
        labelP8 = tk.Label(self, text="Pumpe 8:", font=controller.Text_font)
        labelP8.place(x=25,y=355)
        global ePump1
        ePump1 = tk.Entry(self, font=controller.Text_font)
        ePump1.place(x=150,y=75)
        global cAlk1_Var
        cAlk1_Var = tk.IntVar()
        global cAlk1
        cAlk1 = tk.Checkbutton(self, text="Alkoholisch?", variable=cAlk1_Var, font=controller.Text_font)
        cAlk1.place(x=550,y=75)
        global ePump2
        ePump2 = tk.Entry(self, font=controller.Text_font)
        ePump2.place(x=150,y=115)
        global cAlk2_Var
        cAlk2_Var = tk.IntVar()
        global cAlk2
        cAlk2 = tk.Checkbutton(self, text="Alkoholisch?", variable=cAlk2_Var, font=controller.Text_font)
        cAlk2.place(x=550,y=115)
        global ePump3
        ePump3 = tk.Entry(self, font=controller.Text_font)
        ePump3.place(x=150,y=155)
        global cAlk3_Var
        cAlk3_Var = tk.IntVar()
        global cAlk3
        cAlk3 = tk.Checkbutton(self, text="Alkoholisch?", variable=cAlk3_Var, font=controller.Text_font)
        cAlk3.place(x=550,y=155)
        global ePump4
        ePump4 = tk.Entry(self, font=controller.Text_font)
        ePump4.place(x=150,y=195)
        global cAlk4_Var
        cAlk4_Var = tk.IntVar()
        global cAlk4
        cAlk4 = tk.Checkbutton(self, text="Alkoholisch?", variable=cAlk4_Var, font=controller.Text_font)
        cAlk4.place(x=550,y=195)
        global ePump5
        ePump5 = tk.Entry(self, font=controller.Text_font)
        ePump5.place(x=150,y=235)
        global cAlk5_Var
        cAlk5_Var = tk.IntVar()
        global cAlk5
        cAlk5 = tk.Checkbutton(self, text="Alkoholisch?", variable=cAlk5_Var, font=controller.Text_font)
        cAlk5.place(x=550,y=235)
        global ePump6
        ePump6 = tk.Entry(self, font=controller.Text_font)
        ePump6.place(x=150,y=275)
        global cAlk6_Var
        cAlk6_Var = tk.IntVar()
        global cAlk6
        cAlk6 = tk.Checkbutton(self, text="Alkoholisch?", variable=cAlk6_Var, font=controller.Text_font)
        cAlk6.place(x=550,y=275)
        global ePump7
        ePump7 = tk.Entry(self, font=controller.Text_font)
        ePump7.place(x=150,y=315)
        global cAlk7_Var
        cAlk7_Var = tk.IntVar()
        global cAlk7
        cAlk7 = tk.Checkbutton(self, text="Alkoholisch?", variable=cAlk7_Var, font=controller.Text_font)
        cAlk7.place(x=550,y=315)
        global ePump8
        ePump8 = tk.Entry(self, font=controller.Text_font)
        ePump8.place(x=150,y=355)
        global cAlk8_Var
        cAlk8_Var = tk.IntVar()
        global cAlk8
        cAlk8 = tk.Checkbutton(self, text="Alkoholisch?", variable=cAlk8_Var, font=controller.Text_font)
        cAlk8.place(x=550,y=355)
        UebernehmenB = tk.Button(self, text="Übernehmen", font=controller.B_font,
                           command=lambda: [ChangeDrink(), controller.show_frame("Einstellungen")])
        UebernehmenB.place(x=615, y=435)
        RuecksetzenB = tk.Button(self, text="Rücksetzen", font=controller.B_font,
                                 command=setEntry)
        RuecksetzenB.place(x=300, y=435)
        BackB = tk.Button(self, text="Zurück", font=controller.B_font,
                           command=lambda: [controller.show_frame("Einstellungen")])
        BackB.place(x=5, y=435)


class WartungW1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Automat spülen", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label = tk.Label(self, text="""Getränkeflaschen mit Wasserflaschen bzw. einem Eimer austauschen \n Leeren Becher unterstellen \n "Spülen beginnen" drücken.""", font=controller.Text_font)
        label.pack()
        global Wartung1B
        Wartung1B = tk.Button(self, text="Spülen beginnen", state=tk.DISABLED, font=controller.B_font,
                           command=lambda: [Wartung1(), controller.show_frame("WartungW2")])
        Wartung1B.pack(pady=25)
        BackB = tk.Button(self, text="Zurück", font=controller.B_font,
                           command=lambda: [controller.show_frame("Einstellungen")])
        BackB.place(x=5, y=435)


class WartungW2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Schläuche leersaugen", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label = tk.Label(self, text="""Schläuche aus Wasser herausnehmen \n "Spühlen fortsetzen" drücken""", font=controller.Text_font)
        label.pack()
        global Wartung2B
        Wartung2B = tk.Button(self, text="Spülen fortsetzen", state=tk.DISABLED, font=controller.B_font,
                           command=lambda: [Wartung2(), controller.show_frame("Einstellungen")])
        Wartung2B.pack(pady=25)
        BackB = tk.Button(self, text="Zurück", font=controller.B_font,
                           command=lambda: [controller.show_frame("Einstellungen")])
        BackB.place(x=5, y=435)



if __name__ == "__main__":
    app = SampleApp()
    app.attributes('-fullscreen', True)
    update_all()
    app.mainloop()