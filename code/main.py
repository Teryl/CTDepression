### CTD Calculator Game Version 1.0
### By: F06 Group E
### Code By: Refer to README
### Versioned as of 07/12/22

### Importing Modules
import time
import random
import copy
from math import *
from tkinter import *
from tkinter import messagebox
from tkinter import font
from tkinter.font import Font
import os
import sys
from ctypes import windll, byref, create_unicode_buffer, create_string_buffer
from threading import Thread, Event
from queue import Queue
import winsound

### Navigate one folder above main.py
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.chdir("..")

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class launcher():
    def __init__(self):
        self.root = Tk()
        self.root.title("ENSLauncher")
        self.root.resizable(False, False)
        self.root.geometry("{}x{}".format(WINDOW_SIZE_LAUNCHER[0], WINDOW_SIZE_LAUNCHER[1]))
        self.root.overrideredirect(True)
        self.root.configure(background="black")
        self.itemDict = {}
        self.imageBuffer = {}
        self.sendScale = 1
        self.root.bind("<Escape>", lambda e: exit())
        

        x = (self.root.winfo_screenwidth()/2) - (WINDOW_SIZE_LAUNCHER[0]/2)
        y = (self.root.winfo_screenheight()/2) - (WINDOW_SIZE_LAUNCHER[1]/2)
        self.root.geometry('%dx%d+%d+%d' % (WINDOW_SIZE_LAUNCHER[0], WINDOW_SIZE_LAUNCHER[1], x, y))

        self.initialFrames = [PhotoImage(file = os.path.abspath(os.path.join(ANIM_DIR, str(i) + ".png"))).subsample(2) for i in range(18)]
        self.loopingFrames = [PhotoImage(file = os.path.abspath(os.path.join(ANIM_DIR, str(i) + ".png"))).subsample(2) for i in range(18, 51)]

        self.loopsplash = Canvas(self.root, width = WINDOW_SIZE_LAUNCHER[0], height = WINDOW_SIZE_LAUNCHER[1], background="black", highlightthickness=0, bd=0)
        self.loopingAnim = self.loopsplash.create_image(WINDOW_SIZE_LAUNCHER[0]/2, WINDOW_SIZE_LAUNCHER[1]/2, image = self.initialFrames[0], anchor = CENTER)
        self.loopsplash.place(relx = 0.5, rely = 0.5, anchor = CENTER)

        self.imageBuffer["Start Arrow"] = (PhotoImage(file = os.path.abspath(os.path.join(SPRITE_DIR, "01_Button_Play.png"))).zoom(6))
        self.itemDict["Start Arrow"] = Button(self.root, width = 120, height = 100, image = self.imageBuffer["Start Arrow"], bg="black", borderwidth = 0, highlightthickness = 0,command = lambda: self.begin(self.sendScale))
        self.itemDict["Start Arrow"].place(relx = 0.25, rely = 0.7, anchor = CENTER)

        self.imageBuffer["Exit Arrow"] = (PhotoImage(file = os.path.abspath(os.path.join(SPRITE_DIR, "02_Button_Quit.png"))).zoom(6))
        self.itemDict["Exit Arrow"] = Button(self.root, width = 120, height = 100, image = self.imageBuffer["Exit Arrow"], bg="black", borderwidth = 0, highlightthickness = 0, command = lambda: exit())
        self.itemDict["Exit Arrow"].place(relx = 0.25, rely = 0.85, anchor = CENTER)
        
        self.imageBuffer["Button Up"] = (PhotoImage(file = os.path.abspath(os.path.join(SPRITE_DIR, "03_Button_Up.png"))).zoom(6))
        self.itemDict["Button Up"] = Button(self.root, width = 120, height = 100, image = self.imageBuffer["Button Up"], bg="black", borderwidth = 0, highlightthickness = 0, command= lambda: self.change_scaling(1))
        self.itemDict["Button Up"].place(relx = 0.775, rely = 0.650, anchor = CENTER)

        self.imageBuffer["Button Down"] = (PhotoImage(file = os.path.abspath(os.path.join(SPRITE_DIR, "05_Button_Down.png"))).zoom(6))
        self.itemDict["Button Down"] = Button(self.root, width = 120, height = 100, image = self.imageBuffer["Button Down"], bg="black", borderwidth = 0, highlightthickness = 0, command= lambda: self.change_scaling(-1))
        self.itemDict["Button Down"].place(relx = 0.775, rely = 0.900, anchor = CENTER)

        self.imageBuffer["Scales"] = [PhotoImage(file = os.path.abspath(os.path.join(SPRITE_DIR, "{:02d}".format(i+6) + "_Scale" + str(i) + ".png"))).zoom(6) for i in range(1, 6)]

        self.imageBuffer["Window"] = (PhotoImage(file = os.path.abspath(os.path.join(SPRITE_DIR, "07_Scale1.png"))).zoom(6))
        self.itemDict["Window"] = Label(self.root, width = 120, height = 100, image = self.imageBuffer["Window"], text="3",bg="black", borderwidth = 0, highlightthickness = 0)
        self.itemDict["Window"].place(relx = 0.780, rely = 0.775, anchor = CENTER)

        self.imageBuffer["Scale Label"] = (PhotoImage(file = os.path.abspath(os.path.join(SPRITE_DIR, "06_UIscale.png"))).zoom(6))
        self.itemDict["Scale Label"] = Label(self.root, width = 120, height = 100, image = self.imageBuffer["Scale Label"],bg="black", borderwidth = 0, highlightthickness = 0)
        self.itemDict["Scale Label"].place(relx = 0.580, rely = 0.775, anchor = CENTER)

        self.updateScaleDisplay()
        self.root.after(500, lambda: self.animateLoopingSplash())
        self.keepOnTop()

    def begin(self, scale=1):
        global WINDOW_SCALE
        WINDOW_SCALE = scale
        self.root.destroy()
        ###run main.py

    def keepOnTop(self):
        self.root.attributes("-topmost", True)
        self.root.after(10, lambda: self.keepOnTop())

    def change_scaling(self, direction):
        if self.sendScale + 0.25*direction >= 0.75 and self.sendScale + 0.25*direction <= 1.75:
            self.sendScale += 0.25*direction

    def updateScaleDisplay(self):
        self.itemDict["Window"].configure(image = self.imageBuffer["Scales"][int(self.sendScale*4 - 3)])
        self.itemDict["Window"].update()
        self.root.after(50, lambda: self.updateScaleDisplay())

    def animateLoopingSplash(self, frame = 0):
        if frame < 18:
            self.loopsplash.itemconfig(self.loopingAnim, image = self.initialFrames[frame])
            self.loopsplash.update()
            self.root.after(40, lambda: self.animateLoopingSplash(frame + 1))
        else:
            self.loopsplash.itemconfig(self.loopingAnim, image = self.loopingFrames[frame-18])
            self.loopsplash.update()
            if frame == 50:
                frame = 17
            self.root.after(40, lambda: self.animateLoopingSplash(frame+1))

    def create_canvas(self, width, height, x, y, bg):
        canvas = Canvas(self.root, width = width, height = height, background=bg, highlightthickness=0, bd=0)
        canvas.place(relx = x, rely = y, anchor = CENTER)
        return canvas


WINDOW_SIZE_LAUNCHER = (765, 765)
HOME_DIR = "./code/"
SPRITE_DIR = "./assets/LauncherSprites/"
ANIM_DIR = "./assets/LauncherSprites/logo_frames/"


if __name__ == "__main__":
    tkObj = launcher()
    tkObj.root.mainloop()



### Setting Global Variables
WINDOW_SIZE = (460, 840)
SCALE_UNIT = (115, 220)
#WINDOW_SCALE = 1 #0.75 - 1.75, increments of 0.25, default is 1.0
WINDOW_SIZE_PX = (118, 214)
WINDOW_TITLE = "Eternal Number Slumber"
FR_PRIVATE  = 0x10
FR_NOT_ENUM = 0x20
GLOBAL_PRECISION = 5
ANIMATION_SCALE = 0.8

if len(sys.argv) == 2:
    if sys.argv[1] == int(sys.argv[1]) and (sys.argv[1] >= 1 and sys.argv[1] <= 5):
        WINDOW_SCALE = int(sys.argv[1])*0.25 + 0.75

# Global Scaling Coefficients
scaleMul = {
    "Time" : {0.75: (1.01, 1.53) , 1: (1.00, 1.40) , 1.25: (0.99, 1.30) , 1.5: (0.99, 1.28) , 1.75: (0.99, 1.24)}, #Width, Height
    "Bars" : {0.75: (1.07, 1.53) , 1: (1.02, 1.40) , 1.25: (1.00, 1.30) , 1.5: (1.00, 1.28) , 1.75: (0.98, 1.24)}, #Width, Height
    "Stats": {0.75: (0.92, 1.01) , 1: (0.90, 1.00) , 1.25: (1.00, 0.90) , 1.5: (1.00, 0.93) , 1.75: (0.98, 1.00)}, #Y Offset, Size
    "Display" : {0.75: (1.00, 1.00) , 1: (1.00, 0.92) , 1.25: (1.00, 0.86) , 1.5: (1.00, 0.86) , 1.75: (1.00, 0.97)}, #Y Offset, Size
    "Coin" : {0.75: (0.5, 1.00) , 1: (0.5, 1.00) , 1.25: (0.5, 1.00) , 1.5: (0.5, 1.00) , 1.75: (0.5, 1.00)}, #Y Offset, Size
    "Sprites" : {0.75: (1.00, 1.10) , 1: (1.00, 1.10) , 1.25: (1.00, 1.10) , 1.5: (1.00, 1.10) , 1.75: (1.00, 1.10)}, #Y Offset, Size
    "Info" : {0.75: (0.2, 0.9) , 1: (0.2, 0.85) , 1.25: (0.2, 0.85) , 1.5: (0.2, 0.85) , 1.75: (0.2, 0.85)}, #Y Offset, Size
}

globalStage = 1

class playerClass():
    def __init__(self):
        ## initialize playerStatlist and playerDict 
        self.playerStatlist = {
            "maxHP":{0:30, 1:45, 2:75, 3:100, 4:140, 5:200},
            "Atk":{0:1, 1:1.2, 2:1.4, 3:1.6, 4:1.8, 5:2}, 
            "Def":{0:1, 1:0.97, 2:0.92, 3:0.85, 4:0.75, 5:0.62}, 
            "Time": {0:0, 1:1, 2:2, 3:3, 4:4, 5:5}, 
            "Luck": {0:100, 1:98, 2:96, 3:94, 4:92, 5:90}
        }
        self.playerDict = {
            "maxHP": 0,
            "HP": 0,
            "Atk": 0,
            "Def": 0,
            "Time": 0,
            "Luck": 0,
            "LVL": globalStage,
            "N": 0,
            "Skill": 0
        }

        self.set_stat("HP", self.get_statlist("maxHP"))

    def level_up(self, stat):
        if stat == "maxHP":
            self.set_stat("maxHP", self.get_stat("maxHP") + 1)
            self.set_stat("HP", self.get_statlist("maxHP"))
        else:
            self.set_stat(stat, self.get_stat(stat) + 1)
        self.set_stat("Skill", self.get_stat("Skill") - 1)
        

    def set_stat(self, stat, value):
        self.playerDict[stat] = value

    def get_stat(self, stat):
        return self.playerDict[stat]

    def get_statlist(self, stat):
        return self.playerStatlist[stat][self.get_stat(stat)]


class enemyClass():
    def __init__(self):
        self.currentEnemy = ""
        ## initialize enemyNamelist, enemy.enemyStatlist, enemyTypelist, enemyDict (default enemy is man)
        self.enemyNamelist = [
            "David",
            "Donggeon",
            "Dianthe",
            "Mithun",
            "Evan",
            "Quan Pham",
            "Jon",
            "Muhammad",
            "Tanjiro",
            "Dashawn",
            "Cindy",
            "Tanya",
            "Joseph",
            "Chaya",
            "Brent",
            "Kim Jeong",
            "Chanel",
            "Jamal",
            os.getlogin()
        ]
        self.enemyStatlist = {
            "HP":{0:0.75,1:1,2:1.25},
            "Atk":{0:0.75,1:1,2:1.25},
            "Def":{0:1.25,1:1,2:0.75},
            "Time": {0:10,1:15,2:20},
            "globalNRange": {0:[1,11], 1:[5,26], 2:[25,101], 3:[100,1001]}
        }
        self.enemyTypeList = {}
        self.initStats()
        self.enemyDict = self.enemyTypeList["man"]

    def randomName(self):
        return self.enemyNamelist[random.randrange(len(self.enemyNamelist))]

    def initStats(self):
        self.enemyTypeList = {
            "man":{
                "Name": "man",
                "HP": self.enemyStatlist["HP"][1],
                "Atk": self.enemyStatlist["Atk"][1],
                "Def": self.enemyStatlist["Def"][1],
                "Time": self.enemyStatlist["Time"][1]
            },

            "Cancer":{
                "Name": "Cancer Patient",
                "HP": self.enemyStatlist["HP"][1],
                "Atk": self.enemyStatlist["Atk"][1],
                "Def": self.enemyStatlist["Def"][0],
                "Time": self.enemyStatlist["Time"][0]
            },

            "Florida":{
                "Name": "Florida Man",
                "HP": self.enemyStatlist["HP"][2],
                "Atk": self.enemyStatlist["Atk"][0],
                "Def": self.enemyStatlist["Def"][1],
                "Time": self.enemyStatlist["Time"][1]
            },

            "Bepis":{
                "Name": "Pepsi Man",
                "HP": self.enemyStatlist["HP"][1],
                "Atk": self.enemyStatlist["Atk"][2],
                "Def": self.enemyStatlist["Def"][0],
                "Time": self.enemyStatlist["Time"][1]
            },

            "Therock":{
                "Name": "The Rock",
                "HP": self.enemyStatlist["HP"][1],
                "Atk": self.enemyStatlist["Atk"][1],
                "Def": self.enemyStatlist["Def"][2],
                "Time": self.enemyStatlist["Time"][2]
            },

            "Kanye":{
                "Name": "Kanye East",
                "HP": self.enemyStatlist["HP"][0],
                "Atk": self.enemyStatlist["Atk"][2],
                "Def": self.enemyStatlist["Def"][1],
                "Time": self.enemyStatlist["Time"][1]
            }
        }

def PLACEHOLDER_FUNCTION():
    pass



### Asset Class
class assetHandler():
    def __init__(self):
        self.calcPath = "./assets/CalcUI/"
        self.fightPath = "./assets/FightUI/"
        self.charPath = "./assets/CharSprites/"
        self.animPath = "./assets/CharSprites/char_frames/"
        self.animPath2 = "./assets/CharSprites/char_frames_2/"
        self.cancerPath = "./assets/CharSprites/cancer_frames/"
        self.iconPath = "./assets/LauncherSprites/"
        self.imageDict = {}
        self.fontDict = {}
        self.animate = {}

        # get asset paths
        self.assets = {
            ### CalcUI
            "windowBG" : ['black', 0, 0],
            "mainContainerBG" : ['#EEEEEE', 0, 0],
            "mainBG" : [os.path.join(self.calcPath, "01_Background.png"), 8 ,110, 148],
            "screenBG" : [os.path.join(self.calcPath, "02_Screen.png"), 8, 98, 34],
            "keypadBG" : [os.path.join(self.calcPath, "01_Background.png"), 8, 102, 102],
            "displayBG" : [os.path.join(self.calcPath, "02_Screen.png"), 8, 90, 31],
            "Menu" : [os.path.join(self.calcPath, "99_Menu.png"), 4, 71, 31],
            "Coin" : [os.path.join(self.calcPath, "02_Screen.png"), 8, 12, 12],

            ### CalcButtons
            "C" : [os.path.join(self.calcPath, "03_Button_C.png"), 8, 18, 18],
            "CE" : [os.path.join(self.calcPath, "04_Button_CE.png"), 8, 18, 18],
            "LeftBracket" : [os.path.join(self.calcPath, "05_Button_LeftBracket.png"), 8, 18, 18],
            "RightBracket" : [os.path.join(self.calcPath, "06_Button_RightBracket.png"), 8, 18, 18],
            "Divide" : [os.path.join(self.calcPath, "07_Button_Divide.png"), 8, 18, 18],
            "1" : [os.path.join(self.calcPath, "08_Button_1.png"), 8, 18, 18],
            "2" : [os.path.join(self.calcPath, "09_Button_2.png"), 8, 18, 18],
            "3" : [os.path.join(self.calcPath, "10_Button_3.png"), 8, 18, 18],
            "Multiply" : [os.path.join(self.calcPath, "11_Button_Multiply.png"), 8, 18, 18],
            "4" : [os.path.join(self.calcPath, "12_Button_4.png"), 8, 18, 18],
            "5" : [os.path.join(self.calcPath, "13_Button_5.png"), 8, 18, 18],
            "6" : [os.path.join(self.calcPath, "14_Button_6.png"), 8, 18, 18],
            "Minus" : [os.path.join(self.calcPath, "15_Button_Minus.png"), 8, 18, 18],
            "7" : [os.path.join(self.calcPath, "16_Button_7.png"), 8, 18, 18],
            "8" : [os.path.join(self.calcPath, "17_Button_8.png"), 8, 18, 18],
            "9" : [os.path.join(self.calcPath, "18_Button_9.png"), 8, 18, 18],
            "Home" : [os.path.join(self.calcPath, "19_Button_Home.png"), 8, 18, 18],
            "0" : [os.path.join(self.calcPath, "20_Button_0.png"), 8, 18, 18],
            "Dot" : [os.path.join(self.calcPath, "21_Button_Dot.png"), 8, 18, 18],
            "Equals" : [os.path.join(self.calcPath, "22_Button_Equals.png"), 8, 18, 18],
            "Plus" : [os.path.join(self.calcPath, "23_Button_Plus.png"), 8, 18, 38],
            "UpArrow" : [os.path.join(self.calcPath, "24_Button_UpArrow.png"), 8, 18, 18],
            "RightArrow" : [os.path.join(self.calcPath, "25_Button_RightArrow.png"), 8, 18, 18],
            "LeftArrow" : [os.path.join(self.calcPath, "26_Button_LeftArrow.png"), 8, 18, 18],
            "DownArrow" : [os.path.join(self.calcPath, "27_Button_DownArrow.png"), 8, 18, 18],
            "CenterArrow" : [os.path.join(self.calcPath, "28_Button_CenterArrow.png"), 8, 18, 18],
            "BlankOrange" : [os.path.join(self.calcPath, "29_Button_BlankOrange.png"), 8, 18, 18],
            "BlankLightGrey" : [os.path.join(self.calcPath, "30_Button_BlankLightGrey.png"), 8, 18, 18],
            "BlankDarkGrey" : [os.path.join(self.calcPath, "31_Button_BlankDarkGrey.png"), 8, 18, 18],
            "BlankBlack" : [os.path.join(self.calcPath, "32_Button_BlankBlack.png"), 8, 18, 18],
            "Yes" : [os.path.join(self.calcPath, "33_Button_Yes.png"), 8, 18, 18],
            "No" : [os.path.join(self.calcPath, "34_Button_No.png"), 8, 18, 18],
            "Circle" : [os.path.join(self.calcPath, "35_Button_Circle.png"), 8, 18, 18],
            "Triangle" : [os.path.join(self.calcPath, "36_Button_Triangle.png"), 8, 18, 18],
            "Square" : [os.path.join(self.calcPath, "37_Button_Square.png"), 8, 18, 18],
            "Pound" : [os.path.join(self.calcPath, "38_Button_Pound.png"), 8, 18, 18],
            "BlankPlus" : [os.path.join(self.calcPath, "39_Button_BlankPlus.png"), 8, 18, 38],


            ### FightUI
            "combatBG" : [os.path.join(self.fightPath, "01_Background.png"), 4, 110, 50],
            "Time_10" : [os.path.join(self.fightPath, "02_Time_10.png"), 4, 41, 3],
            "Time_9" : [os.path.join(self.fightPath, "03_Time_9.png"), 4, 41, 3],
            "Time_8" : [os.path.join(self.fightPath, "04_Time_8.png"), 4, 41, 3],
            "Time_7" : [os.path.join(self.fightPath, "05_Time_7.png"), 4, 41, 3],
            "Time_6" : [os.path.join(self.fightPath, "06_Time_6.png"), 4, 41, 3],
            "Time_5" : [os.path.join(self.fightPath, "07_Time_5.png"), 4, 41, 3],
            "Time_4" : [os.path.join(self.fightPath, "08_Time_4.png"), 4, 41, 3],
            "Time_3" : [os.path.join(self.fightPath, "09_Time_3.png"), 4, 41, 3],
            "Time_2" : [os.path.join(self.fightPath, "10_Time_2.png"), 4, 41, 3],
            "Time_1" : [os.path.join(self.fightPath, "11_Time_1.png"), 4, 41, 3],
            "Time_0" : [os.path.join(self.fightPath, "12_Time_0.png"), 4, 41, 3],
            "Atk_5" : [os.path.join(self.fightPath, "13_Atk_5.png"), 4, 10, 3],
            "Atk_4" : [os.path.join(self.fightPath, "14_Atk_4.png"), 4, 10, 3],
            "Atk_3" : [os.path.join(self.fightPath, "15_Atk_3.png"), 4, 10, 3],
            "Atk_2" : [os.path.join(self.fightPath, "16_Atk_2.png"), 4, 10, 3],
            "Atk_1" : [os.path.join(self.fightPath, "17_Atk_1.png"), 4, 10, 3],
            "Atk_0" : [os.path.join(self.fightPath, "18_Atk_0.png"), 4, 10, 3],
            "Def_5" : [os.path.join(self.fightPath, "19_Def_5.png"), 4, 10, 3],
            "Def_4" : [os.path.join(self.fightPath, "20_Def_4.png"), 4, 10, 3],
            "Def_3" : [os.path.join(self.fightPath, "21_Def_3.png"), 4, 10, 3],
            "Def_2" : [os.path.join(self.fightPath, "22_Def_2.png"), 4, 10, 3],
            "Def_1" : [os.path.join(self.fightPath, "23_Def_1.png"), 4, 10, 3],
            "Def_0" : [os.path.join(self.fightPath, "24_Def_0.png"), 4, 10, 3],
            "Luck_5" : [os.path.join(self.fightPath, "25_Luck_5.png"), 4, 10, 3],
            "Luck_4" : [os.path.join(self.fightPath, "26_Luck_4.png"), 4, 10, 3],
            "Luck_3" : [os.path.join(self.fightPath, "27_Luck_3.png"), 4, 10, 3],
            "Luck_2" : [os.path.join(self.fightPath, "28_Luck_2.png"), 4, 10, 3],
            "Luck_1" : [os.path.join(self.fightPath, "29_Luck_1.png"), 4, 10, 3],
            "Luck_0" : [os.path.join(self.fightPath, "30_Luck_0.png"), 4, 10, 3],
            "HP" : ['#424242', 16, 5],
            "LVL" : ['#424242', 14, 5],
            "N" : ['#424242', 14, 5],
            "EnemyHP" : ['#424242', 40, 6],
            "EnemyName" : ['#424242', 40, 6],
            "DamageNum" : ['#424242', 15, 10],
            "DamageNumPlayer" : ['#424242', 15, 10],

            ### Char Sprites
            "Man_1" : [os.path.join(self.charPath, "01_Man_1.png"), 4, 20, 20],
            "Man_2" : [os.path.join(self.charPath, "02_Man_2.png"), 4, 20, 20],
            "Man_3" : [os.path.join(self.charPath, "03_Man_3.png"), 4, 20, 20],
            "Man_4" : [os.path.join(self.charPath, "04_Man_4.png"), 4, 20, 20],
            "Man_5" : [os.path.join(self.charPath, "05_Man_5.png"), 4, 20, 20],
            "Man_6" : [os.path.join(self.charPath, "06_Man_6.png"), 4, 20, 20],
            "Cancer" : [os.path.join(self.charPath, "07_Cancer.png"), 4, 20, 20],
            "Florida" : [os.path.join(self.charPath, "08_Florida.png"), 4, 20, 20],
            "Bepis" : [os.path.join(self.charPath, "09_Bepis.png"), 4, 20, 20],
            "Therock" : [os.path.join(self.charPath, "10_Therock.png"), 4, 20, 20],
            "Kanye" : [os.path.join(self.charPath, "11_Kanye.png"), 4, 20, 20],
            "Player" : [os.path.join(self.animPath, "1.png"), 4, 64, 20],
            "Player2" : [os.path.join(self.animPath2, "1.png"), 4, 64, 20],

            "icon" : os.path.join(self.iconPath, ".Titleicon.ico"),
        }

        self.animate["playerAttack"] = [os.path.join(self.animPath, str(i) + ".png") for i in range(1, 26)], [75, 100, 300, 100, 300, 300, 300, 75, 75, 75, 75, 75, 75, 75, 75, 75, 300, 75, 75, 75, 75, 75, 75, 75, 75]
        self.animate["cancerFlip"] = [os.path.join(self.cancerPath, str(i) + ".png") for i in range(1, 6)], [75, 125, 125, 125, 125]
    
        

    ### Asset get method
    def getAsset(self, assetName):
        if assetName == "man":
            assetName = "Man_" + str(random.randint(1, 6))
        if len(self.assets[assetName]) == 3:
            return self.assets[assetName][0]
        elif assetName in self.imageDict:
            return self.imageDict[assetName]
        else:
            self.imageDict[assetName] = PhotoImage(file=os.path.abspath(self.assets[assetName][0])).zoom(int(self.assets[assetName][1] * WINDOW_SCALE))
            return self.imageDict[assetName]

    def getAnimate(self, idAnimation):
        return [PhotoImage(file=os.path.abspath(i)).zoom(int(4 * WINDOW_SCALE)) for i in self.animate[idAnimation][0]]

    def getDelay(self, idAnimation):
        return self.animate[idAnimation][1]

    # load fonts
    def initialise_fonts(self):
        self.load_font(os.path.abspath("./assets/fonts/monogramRevised.otf"))

    ### Font loader
    def load_font(self, fontpath, private=True, enumerable=False):
        '''
        Makes fonts located in file `fontpath` available to the font system.

        `private`     if True, other processes cannot see this font, and this 
                    font will be unloaded when the process dies
        `enumerable`  if True, this font will appear when enumerating fonts

        See https://msdn.microsoft.com/en-us/library/dd183327(VS.85).aspx

        '''
        if isinstance(fontpath, bytes):
            pathbuf = create_string_buffer(fontpath)
            AddFontResourceEx = windll.gdi32.AddFontResourceExA
        elif isinstance(fontpath, str):
            pathbuf = create_unicode_buffer(fontpath)
            AddFontResourceEx = windll.gdi32.AddFontResourceExW
        else:
            raise TypeError('fontpath must be of type str or unicode')

        flags = (FR_PRIVATE if private else 0) | (FR_NOT_ENUM if not enumerable else 0)
        numFontsAdded = AddFontResourceEx(byref(pathbuf), flags, 0)
        return bool(numFontsAdded)

    def create_font(self, fontName, size, **kwargs):
        self.fontDict[fontName] = Font(family=fontName, size=int(size * WINDOW_SCALE), **kwargs)

    def getFont(self, fontName, size):
        self.create_font(fontName, size)
        return self.fontDict[fontName]  


### Game Class
class gameInstance(Tk):

    #initialise
    def __init__(self, size, title, assets, queue, spriteQueue, shopQueue, enemyQueue, enemyHPQueue, damageQueue, critQueue):
        Tk.__init__(self)
        self.size = size[0]*WINDOW_SCALE, size[1]*WINDOW_SCALE
        self.px = self.size[0] / WINDOW_SIZE_PX[0]
        self.title(title)
        self.iconbitmap(assets.assets["icon"])
        self.assets = assets
        self.frameDict = {}
        self.container = []
        self.buttonDict = {}
        self.textfields = {}
        self.imagefields = {}
        self.buffer = ""
        self.result = ""
        self.finishCalc = False
        self.queueResult = queue
        self.spriteQueue = spriteQueue
        self.shopQueue = shopQueue
        self.enemyQueue = enemyQueue
        self.enemyHPQueue = enemyHPQueue
        self.damageQueue = damageQueue
        self.critQueue = critQueue
        self.actions = actions(self)
        self.player = player
        self.enemy = enemy
        self.binds = {}
        self.clockTime = self.clock(self)
        self.Player = "Player"
        self.currentEnemy = ""

        # timer pseudothreads
        self.threads = [0, 0, 0]
        self.threadbuffer = [0, 0, 0]

        self.configure(background=self.assets.getAsset("windowBG"))
       
       # Calculate Starting X and Y coordinates for Window
        x = (self.winfo_screenwidth()/2) - (WINDOW_SIZE[0]/2)
        y = (self.winfo_screenheight()/2) - (WINDOW_SIZE[1]/2)
      
        self.geometry('%dx%d+%d+%d' % (self.size[0], self.size[1], x, y))
        self.resizable(True, True)
        self.minsize(int(WINDOW_SIZE[0]*WINDOW_SCALE), int(WINDOW_SIZE[1]*WINDOW_SCALE))

        self.create_main()
        
        press = buttonPresses(self.actions)

        # Button Function Allocation
        self.buttons = {
            "C" : press.press_C,
            "CE" : press.press_CE,
            "LeftBracket" : press.press_LeftBracket,
            "RightBracket" : press.press_RightBracket,
            "Divide" : press.press_Divide,
            "1" : press.press_1,
            "2" : press.press_2,
            "3" : press.press_3,
            "Multiply" : press.press_Multiply,
            "4" : press.press_4,
            "5" : press.press_5,
            "6" : press.press_6,
            "Minus" : press.press_Minus,
            "7" : press.press_7,
            "8" : press.press_8,
            "9" : press.press_9,
            "Home" : press.press_Home,
            "0" : press.press_0,
            "Dot" : press.press_Dot,
            "Equals" : press.press_Equals,
            "Plus" : press.press_Plus,
            "UpArrow" : press.press_UpArrow,
            "RightArrow" : press.press_RightArrow,
            "LeftArrow" : press.press_LeftArrow,
            "DownArrow" : press.press_DownArrow,
            "CenterArrow" : press.press_CenterArrow,
            "BlankOrange" : press.press_BlankOrange,
            "BlankLightGrey" : press.press_BlankLightGrey,
            "BlankDarkGrey" : press.press_BlankDarkGrey,
            "BlankBlack" : press.press_BlankBlack,
            "Yes" : press.press_Yes,
            "No" : press.press_No,
            "Circle" : press.press_Circle,
            "Triangle" : press.press_Triangle,
            "Square" : press.press_Square,
            "Pound" : press.press_Pound,
            "BlankPlus" : press.press_BlankPlus,
        }

        self.defaultLayout = [
            ["C", "CE", "LeftBracket", "RightBracket", "Divide"],
            ["BlankBlack", "1", "2", "3", "Multiply"],
            ["BlankBlack", "4", "5", "6", "Minus"],
            ["BlankBlack", "7", "8", "9", "Plus"],
            ["BlankBlack", "0", "Dot", "Equals", None],
        ]

        self.startLayout = [
            ["BlankOrange", "BlankOrange", "BlankLightGrey", "BlankLightGrey", "BlankLightGrey"],
            ["BlankBlack", "BlankDarkGrey", "BlankDarkGrey", "BlankDarkGrey", "BlankLightGrey"],
            ["BlankBlack", "BlankDarkGrey", "BlankDarkGrey", "BlankDarkGrey", "BlankLightGrey"],
            ["BlankBlack", "BlankDarkGrey", "BlankDarkGrey", "BlankDarkGrey", "BlankPlus"],
            ["BlankBlack", "BlankDarkGrey", "BlankDarkGrey", "BlankLightGrey", None],
        ]

        self.create_calc()
        self.create_buttons()
        self.assets.initialise_fonts()
        self.create_display()
        self.create_combat()
        self.create_combat_elements()
        self.secret()
        self.begin_countdown(3)
        self.protocol("WM_DELETE_WINDOW", self.actions.quitGame)
        
        
    def modify_timer(self, thread, time):
        self.threads[thread] = time
    
    def increment_timers(self):
        for i in range(len(self.threads)):
            self.threads[i] += 1
    
    def stall_timer(self, thread):
        self.threadbuffer[thread] = self.threads[thread]
        self.threads[thread] = 0

    def get_saved_timer(self, thread):
        return self.threadbuffer[thread]

       
    # set keybinds
    def keybinds(self):
        for key in self.binds:
            self.bind(key, lambda e : self.binds[key]())

    def rebind(self, key, func):
        self.binds[key] = func
        self.bind(key, lambda e : self.binds[key]())


    # create main frame structure
    def create_main(self):
        self.create_frame(self, "mainContainer", background=self.assets.getAsset("mainContainerBG"))
        self.frameDict["mainContainer"].config(width=self.size[0], height=self.size[1])

        self.create_canvas(self.frameDict["mainContainer"], "main", image=self.assets.getAsset("mainBG"), width=self.assets.assets["mainBG"][2]*self.px, height=self.assets.assets["mainBG"][3]*self.px, padx=2*self.px, pady=3*self.px, relx=0.5, rely=1 - 3 /WINDOW_SIZE_PX[1], anchor=S)
        self.create_canvas(self.frameDict["mainContainer"], "combat", image=self.assets.getAsset("combatBG"), width=self.assets.assets["combatBG"][2]*self.px, height=self.assets.assets["combatBG"][3]*self.px, padx=4*self.px, pady=3*self.px, relx=0.5, rely=3 /WINDOW_SIZE_PX[1], anchor=N)

    # create calculator frame structure
    def create_calc(self):
        self.create_canvas(self.frameDict["main"], "screen", image=self.assets.getAsset("screenBG"), width=self.assets.assets["screenBG"][2]*self.px, height=self.assets.assets["screenBG"][3]*self.px, padx=2*self.px, pady=0, relx=0.5, rely=0.15, anchor=CENTER)
        self.create_canvas(self.frameDict["main"], "keypad", image=self.assets.getAsset("keypadBG"), width=self.assets.assets["keypadBG"][2]*self.px, height=self.assets.assets["keypadBG"][3]*self.px, padx=0, pady=0, relx=0.5, rely=0.625, anchor=CENTER)

    def create_display(self):
        self.create_canvas(self.frameDict["screen"], "display", bg = "#438F4C", width=self.assets.assets["displayBG"][2]*self.px, height=self.assets.assets["displayBG"][3]*self.px, padx=0, pady=0, relx=0.5, rely=0.5*scaleMul["Display"][WINDOW_SCALE][0], anchor=CENTER)
        self.imagefields['screenImage'] = self.frameDict["display"].create_image(self.assets.assets["displayBG"][2]*self.px/2, self.assets.assets["displayBG"][3]*self.px/2, image=self.assets.getAsset("displayBG"))
        self.textfields['screenText'] = self.frameDict["display"].create_text(self.assets.assets["displayBG"][2]*self.px, self.assets.assets["displayBG"][3]*self.px/2 - 4*self.px, text="START", font=self.assets.getFont("monogramRevised", WINDOW_SCALE*-(80 - (WINDOW_SCALE-1)*50)*scaleMul["Display"][WINDOW_SCALE][1]), anchor=E)
        self.create_canvas(self.frameDict["screen"], "coin", bg = "#438F4C", width=self.assets.assets["Coin"][2]*self.px, height=self.assets.assets["Coin"][3]*self.px, padx=0, pady=0, relx=0.8875, rely=0.68, anchor=CENTER)
        self.textfields['coinText'] = self.frameDict["coin"].create_text(self.assets.assets["Coin"][2]*self.px/2, self.assets.assets["Coin"][3]*self.px*scaleMul["Coin"][WINDOW_SCALE][0]/2, text="0", font=self.assets.getFont("monogramRevised", 0.8*WINDOW_SCALE*-(80 - (WINDOW_SCALE-1)*50)*scaleMul["Coin"][WINDOW_SCALE][1]), anchor=CENTER)
        self.frameDict["coin"].place_forget()

    # create combat screen frame structure
    def create_combat(self):
        self.create_canvas(self.frameDict["combat"], "Time", width=self.assets.assets["Time_0"][2]*self.px*scaleMul["Time"][WINDOW_SCALE][0], height=self.assets.assets["Time_0"][3]*self.px*scaleMul["Time"][WINDOW_SCALE][1], padx=0, pady=0, relx=0.795, rely=0.24, anchor=CENTER)
        self.imagefields['Time'] = self.frameDict["Time"].create_image(0, self.assets.assets["Time_0"][3]*self.px/2, image=self.assets.getAsset("Time_10"), anchor=W)

        self.create_canvas(self.frameDict["combat"], "Atk", width=self.assets.assets["Atk_0"][2]*self.px*scaleMul["Bars"][WINDOW_SCALE][0], height=self.assets.assets["Atk_0"][3]*self.px*scaleMul["Bars"][WINDOW_SCALE][1], padx=0, pady=0, relx=0.455, rely=0.101, anchor=CENTER)
        self.imagefields['Atk'] = self.frameDict["Atk"].create_image(0, self.assets.assets["Atk_0"][3]*self.px/2, image=self.assets.getAsset("Atk_5"), anchor=W)

        self.create_canvas(self.frameDict["combat"], "Def", width=self.assets.assets["Def_0"][2]*self.px*scaleMul["Bars"][WINDOW_SCALE][0], height=self.assets.assets["Def_0"][3]*self.px*scaleMul["Bars"][WINDOW_SCALE][1], padx=0, pady=0, relx=0.6825, rely=0.101, anchor=CENTER)
        self.imagefields['Def'] = self.frameDict["Def"].create_image(0, self.assets.assets["Def_0"][3]*self.px/2, image=self.assets.getAsset("Def_5"), anchor=W)

        self.create_canvas(self.frameDict["combat"], "Luck", width=self.assets.assets["Luck_0"][2]*self.px*scaleMul["Bars"][WINDOW_SCALE][0], height=self.assets.assets["Luck_0"][3]*self.px*scaleMul["Bars"][WINDOW_SCALE][1], padx=0, pady=0, relx=0.93, rely=0.101, anchor=CENTER)
        self.imagefields['Luck'] = self.frameDict["Luck"].create_image(0, self.assets.assets["Luck_0"][3]*self.px/2, image=self.assets.getAsset("Luck_5"), anchor=W)

        self.create_canvas(self.frameDict["combat"], "HP", bg=self.assets.getAsset("HP"), width=self.assets.assets["HP"][1]*self.px, height=self.assets.assets["HP"][2]*self.px, padx=0, pady=0, relx=0.203, rely=0.1025, anchor=CENTER)
        self.textfields["HP"] = self.frameDict["HP"].create_text(0, self.px*5*scaleMul["Stats"][WINDOW_SCALE][0], text="10", font=self.assets.getFont("monogramRevised", WINDOW_SCALE*-(32 - (WINDOW_SCALE-1)*20)*scaleMul["Stats"][WINDOW_SCALE][1]), fill="white", anchor=SW)

        self.create_canvas(self.frameDict["combat"], "LVL", bg=self.assets.getAsset("LVL"), width=self.assets.assets["LVL"][1]*self.px, height=self.assets.assets["LVL"][2]*self.px, padx=0, pady=0, relx=0.21, rely=0.2415, anchor=CENTER)
        self.textfields["LVL"] = self.frameDict["LVL"].create_text(0, self.px*5*scaleMul["Stats"][WINDOW_SCALE][0], text="10", font=self.assets.getFont("monogramRevised", WINDOW_SCALE*-(32 - (WINDOW_SCALE-1)*20)*scaleMul["Stats"][WINDOW_SCALE][1]), fill="white", anchor=SW)

        self.create_canvas(self.frameDict["combat"], "N", bg=self.assets.getAsset("N"), width=self.assets.assets["N"][1]*self.px, height=self.assets.assets["N"][2]*self.px, padx=0, pady=0, relx=0.403, rely=0.2415, anchor=CENTER)
        self.textfields["N"] = self.frameDict["N"].create_text(0, self.px*5*scaleMul["Stats"][WINDOW_SCALE][0], text="10", font=self.assets.getFont("monogramRevised", WINDOW_SCALE*-(32 - (WINDOW_SCALE-1)*20)*scaleMul["Stats"][WINDOW_SCALE][1]), fill="yellow", anchor=SW)

    # create combat elements (sprites, text)
    def create_combat_elements(self):
        self.create_canvas(self.frameDict["combat"], "enemy", width=self.assets.assets["Man_1"][2]*self.px*scaleMul["Sprites"][WINDOW_SCALE][0], height=self.assets.assets["Man_1"][3]*self.px*scaleMul["Sprites"][WINDOW_SCALE][1], bg="#424242", padx=0, pady=0, relx=0.88, rely=0.65, anchor=E)
        self.imagefields["enemy"] = self.frameDict["enemy"].create_image(0, 0, image=self.assets.getAsset("Man_1"), anchor = NW, state=HIDDEN)
        self.create_canvas(self.frameDict["combat"], "Player", width=self.assets.assets["Player"][2]*self.px*scaleMul["Sprites"][WINDOW_SCALE][0], height=self.assets.assets["Player"][3]*self.px*scaleMul["Sprites"][WINDOW_SCALE][1], bg="#424242", padx=0, pady=0, relx=0.03, rely=0.65, anchor=W)
        self.imagefields["Player"] = self.frameDict["Player"].create_image(0, 0, image=self.assets.getAsset("Player"), anchor = NW)
        self.create_canvas(self.frameDict["combat"], "enemyName", width=self.assets.assets["EnemyName"][1]*self.px, height=self.assets.assets["EnemyName"][2]*self.px, bg="#424242", padx=0, pady=0, relx=0.8, rely=0.4, anchor=CENTER)
        self.textfields["enemyName"] = self.frameDict["enemyName"].create_text(self.assets.assets["EnemyName"][1]*self.px/2, self.assets.assets["EnemyName"][2]*self.px*scaleMul["Info"][WINDOW_SCALE][0], text="", font=self.assets.getFont("monogramRevised", WINDOW_SCALE*-(32 - (WINDOW_SCALE-1)*20)*scaleMul["Info"][WINDOW_SCALE][1]), fill="red", anchor=CENTER)
        self.create_canvas(self.frameDict["combat"], "enemyHP", width=self.assets.assets["EnemyHP"][1]*self.px, height=self.assets.assets["EnemyHP"][2]*self.px, bg="#424242", padx=0, pady=0, relx=0.8, rely=0.9, anchor=CENTER)
        self.textfields["enemyHP"] = self.frameDict["enemyHP"].create_text(self.assets.assets["EnemyHP"][1]*self.px/2, self.assets.assets["EnemyHP"][2]*self.px*scaleMul["Info"][WINDOW_SCALE][0], text="", font=self.assets.getFont("monogramRevised", WINDOW_SCALE*-(32 - (WINDOW_SCALE-1)*20)*scaleMul["Info"][WINDOW_SCALE][1]), fill="red", anchor=CENTER)
        self.create_canvas(self.frameDict["combat"], "damageNum", width=self.assets.assets["DamageNum"][1]*self.px, height=self.assets.assets["DamageNum"][2]*self.px, bg="#424242", padx=0, pady=0, relx=0.64, rely=0.65, anchor=CENTER)
        self.textfields["damageNum"] = self.frameDict["damageNum"].create_text(self.assets.assets["DamageNum"][1]*self.px/2, self.assets.assets["DamageNum"][2]*self.px*scaleMul["Info"][WINDOW_SCALE][0], text="", font=self.assets.getFont("monogramRevised", 1.75*WINDOW_SCALE*-(32 - (WINDOW_SCALE-1)*20)*scaleMul["Info"][WINDOW_SCALE][1]), fill="red", anchor=CENTER)
        self.create_canvas(self.frameDict["combat"], "damageNumPlayer", width=self.assets.assets["DamageNumPlayer"][1]*self.px, height=self.assets.assets["DamageNumPlayer"][2]*self.px, bg="#424242", padx=0, pady=0, relx=0.21, rely=0.418, anchor=CENTER)
        self.textfields["damageNumPlayer"] = self.frameDict["damageNumPlayer"].create_text(self.assets.assets["DamageNumPlayer"][1]*self.px/2, self.assets.assets["DamageNumPlayer"][2]*self.px*scaleMul["Info"][WINDOW_SCALE][0], text="", font=self.assets.getFont("monogramRevised", 1.75*WINDOW_SCALE*-(32 - (WINDOW_SCALE-1)*20)*scaleMul["Info"][WINDOW_SCALE][1]), fill="red", anchor=CENTER)
        self.update_combat_display()

    def create_buttons(self):
        for y in range(len(self.startLayout)):
            for x in range(len(self.startLayout[y])):
                if self.startLayout[y][x] != None:
                    self.create_button(self.frameDict["keypad"], (y, x), image=self.assets.getAsset(self.startLayout[y][x]), bg="#424242", width=self.assets.assets[self.startLayout[y][x]][2]*self.px, height=self.assets.assets[self.startLayout[y][x]][3]*self.px, padx=0, pady=0, bd=0, command=self.buttons[self.startLayout[y][x]])
                    if self.startLayout[y][x] == "BlankPlus":
                        self.grid_item(self.buttonDict[(y, x)], row=y, column=x, padx=self.px, pady=self.px ,rowspan=2, sticky=NSEW)
                        continue
                    self.grid_item(self.buttonDict[(y,x)], row=y, column=x, padx=self.px, pady=self.px, sticky=NSEW)
    
    def change_button(self, location, new):
        self.update_button(location, image=self.assets.getAsset(new), command=self.buttons[new])

    def reset_buttons(self):
        for y in range(len(self.defaultLayout)):
            for x in range(len(self.defaultLayout[y])):
                if self.defaultLayout[y][x] != None:
                    self.change_button((y, x), self.defaultLayout[y][x])


    # compartmentalisation functions
    def create_frame(self, master, id, **kwargs):
        if "background" in kwargs:
            self.frameDict[id] = Frame(master, background=kwargs["background"])
            self.frameDict[id].place(relx=0.5, rely=0.5, anchor=CENTER)
        else:
            image = Label(master, borderwidth=0, image=kwargs['image'])
            kwargs.pop("image", None)
            image.place(**kwargs)
            self.frameDict[id] = Frame(image, bg="")
            self.frameDict[id].place(in_=image, relx=0.5, rely=0.5, anchor=CENTER)
            self.container.append(image)

    def create_canvas(self, master, id, **kwargs):
            width = kwargs.pop("width", None) + kwargs.pop("padx", None)
            height = kwargs.pop("height", None) + kwargs.pop("pady", None)
            bg = kwargs.pop("bg", None)
            self.frameDict[id] = Canvas(master, bd=-2, bg=bg, highlightthickness=0, width=width, height=height)
            if "image" in kwargs:
                image = kwargs.pop("image", None)
                self.frameDict[id].create_image(width/2, height/2, image=image, anchor=CENTER)
            self.frameDict[id].place(**kwargs)
            

    def create_button(self, master, id, **kwargs):
        self.buttonDict[id] = Button(master, **kwargs)

    def update_button(self, id, **kwargs):
        self.buttonDict[id].config(**kwargs)

    def update_displaytext(self, text):
        self.frameDict["display"].itemconfig(self.textfields['screenText'], text=text)

    def grid_item(self, item, **kwargs):
        item.grid(**kwargs)
   
    # Create Combat Display Update Loop
    def update_combat_display(self):
        self.frameDict["HP"].itemconfig(self.textfields["HP"], text=str(self.player.get_stat("HP")))
        self.frameDict["LVL"].itemconfig(self.textfields["LVL"], text=str(self.player.get_stat("LVL")))
        self.frameDict["N"].itemconfig(self.textfields["N"], text=str(self.player.get_stat("N")))
        self.frameDict["Time"].itemconfig(self.imagefields["Time"], image=self.assets.getAsset("Time_" + str(ceil(self.clockTime.percent / 10))))
        self.frameDict["Atk"].itemconfig(self.imagefields["Atk"], image=self.assets.getAsset("Atk_" + str(self.player.get_stat("Atk"))))
        self.frameDict["Def"].itemconfig(self.imagefields["Def"], image=self.assets.getAsset("Def_" + str(self.player.get_stat("Def"))))
        self.frameDict["Luck"].itemconfig(self.imagefields["Luck"], image=self.assets.getAsset("Luck_" + str(self.player.get_stat("Luck"))))

        if not(self.enemyHPQueue.empty()):
            status = self.enemyHPQueue.get()
            self.frameDict["enemyHP"].itemconfig(self.textfields["enemyHP"], text=str(int(status))+" HP")

        if not(self.enemyQueue.empty()):
            status = self.enemyQueue.get()
            self.frameDict["enemyName"].itemconfig(self.textfields["enemyName"], text=status)
            if self.currentEnemy != "Done":
                self.currentEnemy = status

        if not(self.critQueue.empty()):
            status = self.critQueue.get()
            if status:
                self.frameDict["damageNum"].itemconfig(self.textfields["damageNum"], fill="red")
                self.frameDict["damageNumPlayer"].itemconfig(self.textfields["damageNumPlayer"], fill="green")
            else:
                self.frameDict["damageNum"].itemconfig(self.textfields["damageNum"], fill="yellow")
                self.frameDict["damageNumPlayer"].itemconfig(self.textfields["damageNumPlayer"], fill="yellow")

        if not(self.spriteQueue.empty()):
            status = self.spriteQueue.get()
            if status == "enemyKilled":
                self.toggle_switch_sprites("enemy", False)
                self.frameDict["enemyName"].itemconfig(self.textfields["enemyName"], text="")
                self.frameDict["enemyHP"].itemconfig(self.textfields["enemyHP"], text="")
            elif status == "enemySpawned":
                self.frameDict["enemy"].itemconfig(self.imagefields["enemy"], image=self.enemy.currentEnemy)
                self.toggle_switch_sprites("enemy", True)
            elif status == "enemyHit":
                self.after(0, self.actions.do_animate(self.Player, self.assets.getAnimate("playerAttack"), self.assets.getDelay("playerAttack"), self.Player))
                self.after(1800, lambda: self.actions.text_animate("damageNum", "damageNum", text="-" + str(ceil(damageQueue.get())), delay=125))
            elif status == "playerHit":
                self.after(0, lambda: self.actions.text_animate("display", "screenText", text="INCORRECT", delay=200, frame=6, endstate="SHOW"))
                self.after(1000, lambda: self.actions.text_animate("damageNumPlayer", "damageNumPlayer", text="-" + str(ceil(damageQueue.get())), delay=200))
            elif status == "playerHitTime":
                self.after(0, lambda: self.actions.text_animate("display", "screenText", text="TOO SLOW", delay=200, frame=6, endstate="SHOW"))
                self.after(1000, lambda: self.actions.text_animate("damageNumPlayer", "damageNumPlayer", text="-" + str(ceil(damageQueue.get())), delay=200))
            elif status == "timeout":
                self.after(0, lambda: self.actions.text_animate("display", "screenText", text="OUT OF TIME", delay=200, frame=6, endstate="SHOW"))
                self.after(1000, lambda: self.actions.text_animate("damageNumPlayer", "damageNumPlayer", text="-" + str(ceil(damageQueue.get())), delay=200))
                
        if not(self.shopQueue.empty()):
            status = self.shopQueue.get()
            if status == "shopOpen":
                self.actions.keypad_state_change("shop")
                self.actions.clear_buffer()
                self.actions.clear_screen()
                self.frameDict["display"].itemconfig(self.imagefields["screenImage"], image = self.assets.getAsset("Menu"))
                self.frameDict["coin"].place(relx=0.8875, rely=0.68, anchor=CENTER)
                self.frameDict["coin"].itemconfig(self.textfields["coinText"], text = self.player.get_stat("Skill"))
            elif status == "shopClose":
                self.frameDict["display"].itemconfig(self.imagefields["screenImage"], image = self.assets.getAsset("displayBG"))
                self.frameDict["coin"].place_forget()
                self.actions.keypad_state_reset()
                time.sleep(1)
            elif status == "maxLevel":
                self.frameDict["display"].itemconfig(self.imagefields["screenImage"], image = self.assets.getAsset("displayBG"))
                self.frameDict["coin"].place_forget()
                self.after(100, lambda: self.actions.text_animate("display", "screenText", text="MAX LEVEL", delay=200, frame=6, endstate="SHOW"))
                

        if player.get_stat("HP") <= 0:
            self.destroy()
        
        self.increment_timers()

        self.after(5, self.update_combat_display)

    def begin_countdown(self, start):
        if start > 0:
            self.actions.push_to_screen("START IN " + str(start))
            self.after(1000, lambda: self.begin_countdown(start-1))
        else:
            self.after(0, lambda: self.actions.text_scroll(text="FIGHT!!!"))
            self.after(1000, lambda: self.actions.keypad_state_reset())

    def secret(self):
        if self.buffer == "3337773333224447773":
            self.actions.freebird()
        if self.buffer == "6666666666.":
            self.actions.evan()
        if self.currentEnemy == "Cancer Patient" and self.player.get_stat("HP") <= 10:
            self.actions.thei()
            self.currentEnemy = "Done"
        self.after(50, lambda : self.secret())

    def toggle_switch_sprites(self, idFrame, visible=True, idSprite=None):
        if idSprite != None:
            self.frameDict[idFrame].itemconfig(self.imagefields[idFrame], image=self.assets.getAsset(idSprite))
        self.frameDict[idFrame].itemconfig(self.imagefields[idFrame], state=NORMAL if visible else HIDDEN, anchor=NW)
    
    def update_animation(self, idFrame, image):
        self.frameDict[idFrame].itemconfig(self.imagefields[idFrame], image=image)

    class clock():
        def __init__(self, host):
            self.host = host
            self.time = 0
            self.buffer = 0
            self.max = 1
            self.percent = 100
            self.stop = True


        def start_timer(self, time):
            self.time = time
            self.percent = self.time/self.max * 100
            if self.stop:
                return
            if self.time <= 0:
                self.host.queueResult.put(-999999)
                return
            self.host.after(10, self.start_timer, self.time-0.0145)
        
        def stop_get_time(self):
            self.buffer = copy.deepcopy(self.time)
            self.stop = True
            return self.buffer
        
        def set_max_start(self, max):
            self.max = max
            self.stop = False
            self.start_timer(max)

        
        

class actions():
    def __init__(self, game):
        self.game = game
        self.game.bind("<Escape>", lambda e : self.quitGame())
        self.soundPlaying = False

    def quitGame(self):
        quitQuery = messagebox.askyesno("Quit", "Are you sure you want to quit?", icon="warning")
        if quitQuery:
            self.game.queueResult.put("quit")
            time.sleep(0.1)
            exit()

    def keypad_state_change(self, layout):
        self.altLayout = {
            "shop":[
                ["BlankOrange", "BlankOrange", "BlankLightGrey", "BlankLightGrey", "BlankLightGrey"],
                ["BlankBlack", "BlankBlack", "UpArrow", "BlankBlack", "BlankLightGrey"],
                ["BlankBlack", "LeftArrow", "CenterArrow", "RightArrow", "BlankLightGrey"],
                ["BlankBlack", "BlankBlack", "DownArrow", "BlankBlack", "BlankPlus"],
                ["Pound", "BlankBlack", "No", "BlankBlack", None]
            ],

            "secret":[
                ["BlankOrange", "BlankOrange", "BlankLightGrey", "BlankLightGrey", "BlankLightGrey"],
                ["Circle", "BlankBlack", "UpArrow", "BlankBlack", "BlankLightGrey"],
                ["Triangle", "LeftArrow", "CenterArrow", "RightArrow", "BlankLightGrey"],
                ["Square", "BlankBlack", "DownArrow", "BlankBlack", "BlankPlus"],
                ["Pound", "BlankBlack", "No", "BlankBlack", None]
            ]
        }

        for y in range(len(self.game.defaultLayout)):
            for x in range(len(self.game.defaultLayout[y])):
                if self.altLayout[layout][y][x] != None and self.game.defaultLayout[y][x] != None and self.game.defaultLayout[y][x] != self.altLayout[layout][y][x]:
                    self.game.change_button((y, x), self.altLayout[layout][y][x])

    def keypad_state_reset(self):
        self.game.reset_buttons()

    def push_to_screen(self, text):
        self.game.update_displaytext(text)
    
    def clear_screen(self):
        self.game.update_displaytext("")
        self.game.finishCalc = False

    def add_to_buffer(self, text):
        self.game.buffer += text
        self.push_to_screen(self.game.buffer)
        self.game.finishCalc = False

    def clear_buffer(self):
        self.game.buffer = ""

    def backspace(self):
        self.game.buffer = self.game.buffer[:-1]
        self.push_to_screen(self.game.buffer)
    
    def evaluate_buffer(self, queueResult):
        try:
            if self.game.buffer.replace(".", "").replace("(", "").replace(")", "").replace("+1-1", "").replace("+0", "").replace("-0", "").replace("-1+1","").replace("*1", "").replace("/1", "").isalnum():
                raise CheatException("You can't do that!")
            result = eval(self.game.buffer)
            if not(isinstance(result, int)):
                if result.is_integer():
                    final = int(result)
                else:
                    final = round(result, GLOBAL_PRECISION)
            else:
                final = result
        except:
            self.push_to_screen("ERROR")
            self.game.buffer = ""
        else:
            self.push_to_screen(final)
            self.game.result = str(result)
            self.game.buffer = ""
            self.game.finishCalc = True
            queueResult.put(final)


    def retrieve_result(self):
        #self.add_to_buffer(self.game.result)
        #self.push_to_screen(self.game.result)
        pass ###feature disabled

    def make_shop_choice(self, choice):
        if (choice != "N" and player.get_stat(choice) < 5) or choice == "maxHP":
            self.game.frameDict["coin"].itemconfig(self.game.textfields["coinText"], text = self.game.player.get_stat("Skill")-1)
        self.game.after(100, lambda: queueResult.put(choice))

    def toggle_switch_sprites(self, idFrame, visible=True, idSprite=None):
        self.game.toggle_switch_sprites(idFrame, visible, idSprite)
        

    def do_animate(self, idFrame, framesArr, delayArr, original, frame=0):
        if frame < len(framesArr):
            self.game.update_animation(idFrame, framesArr[frame])
            self.game.after(int(delayArr[frame] * ANIMATION_SCALE), lambda: self.do_animate(idFrame, framesArr, delayArr, original, frame+1))
        else:
            self.toggle_switch_sprites(idFrame, True, original)

    def text_animate(self, idFrame, idText, text, delay=250, frame=6, endstate = "HIDE"):
        if frame > 0 and not(endstate == "SHOW" and frame == 1):
            if frame % 2 == 0:
                self.game.frameDict[idFrame].itemconfig(self.game.textfields[idText], text=text)
            else:
                self.game.frameDict[idFrame].itemconfig(self.game.textfields[idText], text="")
            self.game.after(delay, lambda: self.text_animate(idFrame, idText, text, delay, frame-1))
    
    def text_scroll(self, text, delay=50, frame=13):
        if frame+len(text) > 13:
            self.push_to_screen(text[0:14-frame])
            self.game.after(delay, lambda: self.text_scroll(text, delay, frame-1))
        elif frame+len(text) == 13:
            self.push_to_screen(text)
            self.game.after(delay-25, lambda: self.text_scroll(text, delay, frame-1))
        elif frame > -len(text):
            self.push_to_screen(text + " "*abs((frame - 13 + len(text))))
            self.game.after(delay, lambda: self.text_scroll(text, delay, frame-1))
        else:
            self.clear_screen()

    def freebird(self):
        if not(self.soundPlaying):
            winsound.PlaySound("./assets/Sound/freebird.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
            self.soundPlaying = True
        else:
            winsound.PlaySound(None, winsound.SND_FILENAME)
            self.soundPlaying = False
        self.clear_buffer()
        self.clear_screen()


    def mithun(self):
        messagebox.showinfo("bruh", message="You actual moron of a human being!\nStop pressing unnecessary buttons "+os.getlogin()+"!", icon="warning")
        enemy.enemyStatlist = {
            "HP":{0:1.25,1:3,2:7},
            "Atk":{0:0,1:0,2:0},
            "Def":{0:2,1:3,2:4},
            "Time": {0:7,1:7,2:10},
            "globalNRange": {0:[1,11], 1:[5,26], 2:[25,101], 3:[100,1001]}
        }
        enemy.initStats()

    
    def evan(self):
        self.game.frameDict["Player"].delete('all')
        self.game.Player = "Player2"
        self.game.assets.animate["playerAttack"] = [os.path.join(self.game.assets.animPath2, str(i) + ".png") for i in range(1, 26)], [75, 100, 300, 100, 300, 300, 300, 75, 75, 75, 75, 75, 75, 75, 75, 75, 300, 75, 75, 75, 75, 75, 75, 75, 75]
        self.game.create_canvas(self.game.frameDict["combat"], "Player2", width=self.game.assets.assets["Player2"][2]*self.game.px*scaleMul["Sprites"][WINDOW_SCALE][0], height=self.game.assets.assets["Player2"][3]*self.game.px*scaleMul["Sprites"][WINDOW_SCALE][1], bg="#424242", padx=0, pady=0, relx=0.03, rely=0.7, anchor=W)
        self.game.imagefields["Player2"] = self.game.frameDict["Player2"].create_image(0, 0, image=self.game.assets.getAsset("Player2"), anchor = NW)
        self.clear_buffer()
        self.clear_screen()
        
    
    def michael(self):
        if not(self.soundPlaying):
            self.game.after(750, lambda: winsound.PlaySound("./assets/Sound/sans.wav", winsound.SND_FILENAME | winsound.SND_ASYNC))
            messagebox.showinfo("get dunked on", message="* You feel like you're going to have a bad time.", icon="warning")
            self.soundPlaying = True
        else:
            winsound.PlaySound(None, winsound.SND_FILENAME)
            self.soundPlaying = False

        
    def thei(self):
        self.do_animate("enemy", self.game.assets.getAnimate("cancerFlip"), self.game.assets.getDelay("cancerFlip"), self.game.enemy.currentEnemy)


    def finn(self):
        winsound.PlaySound("./assets/Sound/bepis.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)



class buttonPresses():
    def __init__(self, actions):
        self.action = actions
        self.secretOpen = False
    
    def press_C(self):
        self.action.backspace()
    
    def press_CE(self):
        self.action.clear_buffer()
        self.action.clear_screen()
     
    def press_LeftBracket(self):
        self.action.add_to_buffer("(")

    def press_RightBracket(self):
        self.action.add_to_buffer(")")

    def press_1(self):
        self.action.add_to_buffer("1")
    
    def press_2(self):
        self.action.add_to_buffer("2")

    def press_3(self):
        self.action.add_to_buffer("3")

    def press_4(self):
        self.action.add_to_buffer("4")

    def press_5(self):
        self.action.add_to_buffer("5")

    def press_6(self):
        self.action.add_to_buffer("6")

    def press_7(self):
        self.action.add_to_buffer("7")

    def press_8(self):
        self.action.add_to_buffer("8")

    def press_9(self):
        self.action.add_to_buffer("9")

    def press_0(self):
        self.action.add_to_buffer("0")

    def press_Dot(self):
        self.action.add_to_buffer(".")

    def press_Plus(self):
        if self.action.game.finishCalc:
            self.action.retrieve_result()
        self.action.add_to_buffer("+")

    def press_Minus(self):
        if self.action.game.finishCalc:
            self.action.retrieve_result()
        self.action.add_to_buffer("-")

    def press_Multiply(self):
        if self.action.game.finishCalc:
            self.action.retrieve_result()
        self.action.add_to_buffer("*")

    def press_Divide(self):
        if self.action.game.finishCalc:
            self.action.retrieve_result()
        self.action.add_to_buffer("/")
    
    def press_Equals(self):
        self.action.evaluate_buffer(self.action.game.queueResult)
    
    def press_Pound(self):
        if self.secretOpen == False:
            self.action.keypad_state_change("secret")
            self.secretOpen = True
        else:
            self.action.keypad_state_reset()
            self.action.keypad_state_change("shop")
            self.secretOpen = False

    def press_Home(self):
        pass
    
    def press_UpArrow(self):
        self.action.make_shop_choice("Time")

    def press_DownArrow(self):
        self.action.make_shop_choice("Luck")

    def press_LeftArrow(self):
        self.action.make_shop_choice("Def")

    def press_RightArrow(self):
        self.action.make_shop_choice("Atk")

    def press_CenterArrow(self):
        self.action.make_shop_choice("maxHP")

    def press_Yes(self):
        pass

    def press_No(self):
        self.action.make_shop_choice("N")

    def press_Circle(self):
        self.action.mithun()

    def press_Triangle(self):
        self.action.michael()

    def press_Square(self):
        self.action.finn()

    def press_BlankOrange(self):
        pass

    def press_BlankBlack(self):
        pass

    def press_BlankDarkGrey(self):
        pass

    def press_BlankLightGrey(self):
        pass

    def press_BlankPlus(self):
        pass




# Randomize Number Range:
def randomizeN(globalStage, enemyStatlist):
    # range of n is selected based on the globalStage
    # the higher the stage, range is increased 
    
    if globalStage <= 2:
        globalNRange = enemyStatlist["globalNRange"][0]
    
    elif globalStage > 2 and globalStage <= 4:
        globalNRange = enemyStatlist["globalNRange"][1]
    
    elif globalStage > 4 and globalStage <= 10:
        globalNRange = enemyStatlist["globalNRange"][2]
    
    elif globalStage > 10:
        globalNRange = enemyStatlist["globalNRange"][3]

    # choose n based on the globalNRange
    n = random.randrange(globalNRange[0], globalNRange[1])
    return n

# Randomize Enemy Type:
def randomizeEnemy():
    enchance = random.randrange(0,101)
    if enchance <= 50:
        return "man"

    elif enchance > 50 and enchance <= 60:
        return "Cancer"

    elif enchance > 60 and enchance <= 70:
        return "Florida"

    elif enchance > 70 and enchance <= 80:
        return "Bepis"

    elif enchance > 80 and enchance <= 90:
        return "Therock"

    elif enchance > 90:
        return "Kanye"
    pass

# Calculate Damage done by enemy
def calcEnemyDmg(enemyDict, globalStage):
    enemyDmg = enemyDict["Atk"] * globalStage
    return enemyDmg

# Calcualate Damage done by Player for each attack
def calcPlayerDmg(timeRemaining, inputPerm, randN):
    # for now, player input taken using keyboard
    # during integration with UI, input taken from click
    if inputPerm == randN:
        playerDmg = (player.get_statlist("Atk") * timeRemaining)**1.05
    else:
        playerDmg = 0
        pass
    return playerDmg

# Calculate critical damage or damage reduction
def isCrit(playerLuck):
    return random.randrange(0,101) > playerLuck

def calcPlayerCrit(playerDmg, enemyDmg, result):
    if result:
        if playerDmg > enemyDmg:
            playerCritRed = 1.6
        elif playerDmg < enemyDmg:
            playerCritRed = 0.6
        else:
            playerCritRed = 1
    else:
        playerCritRed = 1
    return playerCritRed

# Present option to upgrade abilities
def upgradeAbility():
    shopQueue.put("shopOpen")
    while player.get_stat("Skill") > 0:
        playerUpgradeChoice = queueResult.get()
        if playerUpgradeChoice == "quit":
            exit()
        if playerUpgradeChoice == "Atk":
            if player.get_stat("Atk") < 5:
                player.level_up("Atk")
                print("You have upgraded your attack!")
                print("You have {} upgrade coin(s)!".format(player.get_stat("Skill")))
                continue
            else:
                shopQueue.put("maxLevel")
                print("You have reached the maximum level for attack!")
                time.sleep(1)
                shopQueue.put("shopOpen")
                continue

        elif playerUpgradeChoice == "Def":
            if player.get_stat("Def") < 5:
                player.level_up("Def")
                print("You have upgraded your defense!")
                print("You have {} upgrade coin(s)!".format(player.get_stat("Skill")))
                continue
            else:
                shopQueue.put("maxLevel")
                print("You have reached the maximum level for defense!")
                time.sleep(1)
                shopQueue.put("shopOpen")
                continue

        elif playerUpgradeChoice == "Time":
            if player.get_stat("Time") < 5:
                player.level_up("Time")
                print("You have upgraded your time!")
                print("You have {} upgrade coin(s)!".format(player.get_stat("Skill")))
                continue
            else:
                shopQueue.put("maxLevel")
                print("You have reached the maximum level for time!")
                time.sleep(1)
                shopQueue.put("shopOpen")
                continue

        elif playerUpgradeChoice == "Luck":
            if player.get_stat("Luck") < 5:
                player.level_up("Luck")
                print("You have upgraded your luck!")
                print("You have {} upgrade coin(s)!".format(player.get_stat("Skill")))
                continue
            else:
                shopQueue.put("maxLevel")
                print("You have reached the maximum level for luck!")
                time.sleep(1)
                shopQueue.put("shopOpen")
                continue

        elif playerUpgradeChoice == "maxHP":
            if player.get_stat("maxHP") < 5:
                player.level_up("maxHP")
                print("You have upgraded your HP!")
                print("You have {} upgrade coin(s)!".format(player.get_stat("Skill")))
                continue
            elif player.get_stat("maxHP") == 5:
                shopQueue.put("maxLevel")
                print("You have reached the maximum level for HP!")
                time.sleep(1)
                shopQueue.put("shopOpen")
                player.set_stat("maxHP", 4)
                player.level_up("maxHP")
                continue

        elif playerUpgradeChoice == "N":
            break

        elif playerUpgradeChoice != "Atk" or "Def" or "Time" or "Luck" or "maxHP" or "N":
            print("You can't upgrade that! Enter a valid input this time...")
            pass
    shopQueue.put("shopClose")

def playerEndgame():
    print("Game Over! What an L!")
    os.system("start \"\" https://www.youtube.com/watch?v=xvFZjo5PgG0")
    time.sleep(10)
    print("Now leave my presence, peasant!")
    # os.system("shutdown -l")
    queueResult.put("quit")
    exit()


def maingame():

## Game runs as long as playerHP > 0, increase globalStage every time
    assets = assetHandler()
    global globalStage
    globalStage = 1
    while player.get_stat("HP") > 0:

        # playerDict is default player stats
        print("Your Player Attributes: ", {k: player.get_statlist(k) for k in list(player.playerDict.keys()) if k not in ['Skill', 'HP', 'LVL', 'N']})
        print("Your Current Stats:\nHP: {HP}\nSkill Points: {Skill}".format(HP = player.get_stat("HP"), Skill = player.get_stat("Skill")))

        # Selecting random enemy
        # Deepcopy the dictionary so that when same enemy is selected HP resets
        # Ensure enemyDict is just a copy not an alias
        global enemyDict
        
        newEnemy = randomizeEnemy()
        enemy.currentEnemy = assets.getAsset(newEnemy)
        enemyDict = copy.deepcopy(enemy.enemyTypeList[newEnemy])
        if enemyDict["Name"] == "man":
            enemyName = enemy.randomName()
        else:
            enemyName = enemyDict["Name"]
        
        
        # Scale intial enemy HP, Atk value, and Defense value 
        enemyDict["HP"] = enemyDict["HP"] * (globalStage**1.07 + 10)
        enemyDict["Atk"] = enemyDict["Atk"] * (globalStage**1.07 / globalStage)
        enemyDict["Def"] = enemyDict["Def"] * (globalStage / globalStage**1.07)
        print("global stage: {}, enemy: {}".format(globalStage,enemyDict))
        enemyHPQueue.put(enemyDict["HP"])
        spriteQueue.put("enemySpawned")
        enemyQueue.put(enemyName)
        # Setting global time
        globalTime = enemyDict["Time"] + player.get_statlist("Time")
        
        # Setting values of initial variables
        playerDmg = 0
        enemyDmg = 0

        # Add while loop for enemyHP > 0
        while enemyDict["HP"] > 0:
            enemyDmg = calcEnemyDmg(enemyDict, globalStage)
            timeRemaining = clock.stop_get_time()
            while True:
                clock.set_max_start(globalTime)
                # Set a random N
                randN = int(randomizeN(globalStage, enemy.enemyStatlist))
                player.set_stat("N", randN)
                print("n:",randN)
                critBool = isCrit(player.get_statlist("Luck"))
                critQueue.put(critBool)

                # Prompt user input 
                inputPerm = queueResult.get()
                print(inputPerm)

                correct = (randN == inputPerm)

                if inputPerm == -999999:
                    spriteQueue.put("timeout")
                    time.sleep(1.5)
                    
                if inputPerm == "quit":
                    exit()

                timeRemaining = clock.stop_get_time()
                print("Time Remaining: ", timeRemaining)
                # Calculate damage done by player, if wrong, playerDmg = 0    
                playerDmg = calcPlayerDmg(timeRemaining, inputPerm, randN)

                # Critical hit calculation
                playerCritRed = calcPlayerCrit(playerDmg, enemyDmg, critBool)

                
                
                
                # Calculate Final Damage
                finalDmg = int(playerDmg - enemyDmg)            
                print(playerDmg, enemyDmg)
                
                
                
                '''TEST FUNCTION'''
                if playerDmg >= enemyDmg:
                    if inputPerm != -999999:
                        spriteQueue.put("enemyHit")
                    enemyDict["HP"] = int(enemyDict["HP"] - ((finalDmg * enemyDict["Def"]) * playerCritRed))
                    damageQueue.put(((finalDmg * enemyDict["Def"]) * playerCritRed))
                    time.sleep(3)
                    enemyHPQueue.put(enemyDict["HP"])
                    print("You did {} damage!".format(finalDmg), "TIMES", playerCritRed)

                elif playerDmg < enemyDmg:
                    if inputPerm != -999999:
                        if correct == False:
                            spriteQueue.put("playerHit")
                        else:
                            spriteQueue.put("playerHitTime")
                    player.set_stat("HP", int(player.get_stat("HP") - ((abs(finalDmg) * player.get_statlist("Def")) * playerCritRed)))
                    damageQueue.put(((abs(finalDmg) * player.get_statlist("Def")) * playerCritRed))
                    time.sleep(2)
                    print("You took {} damage!".format(abs(finalDmg)), "TIMES", playerCritRed)
                
                print("Final HP - You: {}, Enemy: {}".format(player.get_stat("HP"), enemyDict["HP"]))
                
                # Exit while loop and change enemy
                if enemyDict["HP"] <= 0:
                    break

                if player.get_stat("HP") <= 0:
                    playerEndgame()

        
        spriteQueue.put("enemyKilled")

        # Increase globalStage
        globalStage += 1
        
        
        # Give Skill Points
        player.set_stat("Skill", player.get_stat("Skill") + 1)
        print("You have gained an upgrade coin!")
        print("You have {} upgrade coin(s)!".format(player.get_stat("Skill")))

        # Upgrade Abilities
        upgradeAbility()
        player.set_stat("LVL", globalStage)
        print("done")
        







### Main Game Loop
player = playerClass()
enemy = enemyClass()


def main(queue, spriteQueue, shopQueue, enemyQueue, enemyHPQueue, damageQueue, critQueue):
    assets = assetHandler()
    game = gameInstance(WINDOW_SIZE, WINDOW_TITLE, assets, queue, spriteQueue, shopQueue, enemyQueue, enemyHPQueue, damageQueue, critQueue)
    metaQueue.put(game)
    game.mainloop()


metaQueue = Queue()
queueResult = Queue()
spriteQueue = Queue()
shopQueue = Queue()
enemyQueue = Queue()
enemyHPQueue = Queue()
damageQueue = Queue()
critQueue = Queue()

gui = Thread(target=main, args=(queueResult, spriteQueue, shopQueue, enemyQueue, enemyHPQueue, damageQueue, critQueue))
gui.start()

clock = metaQueue.get().clockTime
time.sleep(4)

eternum = Thread(target=maingame)
eternum.start()






