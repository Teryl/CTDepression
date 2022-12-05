### CTD Calculator Game Prototype 0.5
### By: David Ling
### Versioned as of 04/12/22

### Importing Modules
from time import sleep
from math import *
from tkinter import *
from tkinter import messagebox
from tkinter import font
from tkinter.font import Font
import os
import sys
from ctypes import windll, byref, create_unicode_buffer, create_string_buffer


### Setting Global Variables
WINDOW_SIZE = (460, 840)
SCALE_UNIT = (115, 220)
WINDOW_SCALE = 1.0 #0.75 - 1.75, increments of 0.25, default is 1.0
WINDOW_SIZE_PX = (118, 214)
WINDOW_TITLE = "Eternal Number Slumber"
FR_PRIVATE  = 0x10
FR_NOT_ENUM = 0x20
GLOBAL_PRECISION = 5

if len(sys.argv) == 2:
    if sys.argv[1] == int(sys.argv[1]) and (sys.argv[1] >= 1 and sys.argv[1] <= 5):
        WINDOW_SCALE = int(sys.argv[1])*0.25 + 0.75

# Global Scaling Coefficients
scaleMul = {
    "Time" : {0.75: (1.01, 1.53) , 1: (1.00, 1.40) , 1.25: (0.99, 1.30) , 1.5: (0.99, 1.28) , 1.75: (0.99, 1.24)}, #Width, Height
    "Bars" : {0.75: (1.07, 1.53) , 1: (1.02, 1.40) , 1.25: (1.00, 1.30) , 1.5: (1.00, 1.28) , 1.75: (0.98, 1.24)}, #Width, Height
    "Stats": {0.75: (0.92, 1.01) , 1: (0.90, 1.00) , 1.25: (1.00, 0.90) , 1.5: (1.00, 0.93) , 1.75: (0.98, 1.00)}, #Y Offset, Size
    "Display" : {0.75: (1.00, 1.00) , 1: (1.00, 0.92) , 1.25: (1.00, 0.86) , 1.5: (1.00, 0.86) , 1.75: (1.00, 0.97)}, #Y Offset, Size
}

class player():
    def __init__(self):
        self.playerDict = {
            "HP" : 0,
            "Atk" : 0,
            "Def" : 0,
            "Luck" : 0,
            "LVL" : 0,
            "N" : 0,
            "Time" : 0,
        }

    def update_playerDict(self, key, value):
        self.playerDict[key] = value


def PLACEHOLDER_FUNCTION():
    pass



### Asset Class
class assetHandler():
    def __init__(self):
        self.calcPath = "././assets/CalcUI/"
        self.fightPath = "././assets/FightUI/"
        self.imageDict = {}
        self.fontDict = {}

        # get asset paths
        self.assets = {
            ### CalcUI
            "windowBG" : ['black', 0, 0],
            "mainContainerBG" : ['#EEEEEE', 0, 0],
            "mainBG" : [os.path.join(self.calcPath, "01_Background.png"), 8 ,110, 148],
            "screenBG" : [os.path.join(self.calcPath, "02_Screen.png"), 8, 98, 34],
            "keypadBG" : [os.path.join(self.calcPath, "01_Background.png"), 8, 102, 102],
            "displayBG" : [os.path.join(self.calcPath, "02_Screen.png"), 8, 90, 26],

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
            "Disabled" : [os.path.join(self.calcPath, "28_Disabled.png"), 8, 18, 18],
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
        }
    
        

    ### Asset get method
    def getAsset(self, assetName):
        if len(self.assets[assetName]) == 3:
            return self.assets[assetName][0]
        elif assetName in self.imageDict:
            return self.imageDict[assetName]
        else:
            self.imageDict[assetName] = PhotoImage(file=os.path.abspath(self.assets[assetName][0])).zoom(int(self.assets[assetName][1] * WINDOW_SCALE))
            return self.imageDict[assetName]

    # load fonts
    def initialise_fonts(self):
        self.load_font(os.path.abspath("././assets/fonts/monogramRevised.otf"))

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
    def __init__(self, size, title, assets):
        Tk.__init__(self)
        self.size = size[0]*WINDOW_SCALE, size[1]*WINDOW_SCALE
        self.px = self.size[0] / WINDOW_SIZE_PX[0]
        self.name = title
        self.assets = assets
        self.frameDict = {}
        self.container = []
        self.buttonDict = {}
        self.textfields = {}
        self.imagefields = {}
        self.buffer = ""
        self.result = ""
        self.finishCalc = False

        self.player = player()
        self.binds = {}

        # timer pseudothreads
        self.threads = [0, 0, 0]
        self.threadbuffer = [0, 0, 0]

        self.configure(background=self.assets.getAsset("windowBG"))
        self.title(self.name)
       
       # Calculate Starting X and Y coordinates for Window
        x = (self.winfo_screenwidth()/2) - (WINDOW_SIZE[0]/2)
        y = (self.winfo_screenheight()/2) - (WINDOW_SIZE[1]/2)
      
        self.geometry('%dx%d+%d+%d' % (self.size[0], self.size[1], x, y))
        self.resizable(True, True)
        self.minsize(int(WINDOW_SIZE[0]*WINDOW_SCALE), int(WINDOW_SIZE[1]*WINDOW_SCALE))

        self.create_main()
        press = buttonPresses(actions(self))

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
            "Disabled" : press.press_Disabled,
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
            ["Pound", "0", "Dot", "Equals", None],
        ]

        self.create_calc()
        self.create_buttons()
        self.assets.initialise_fonts()
        self.create_display()
        self.create_combat()
        
        
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
        self.create_canvas(self.frameDict["screen"], "display", image=self.assets.getAsset("displayBG"), width=self.assets.assets["displayBG"][2]*self.px, height=self.assets.assets["displayBG"][3]*self.px, padx=0, pady=0, relx=0.5, rely=0.5*scaleMul["Display"][WINDOW_SCALE][0], anchor=CENTER)
        self.textfields['screenText'] = self.frameDict["display"].create_text(self.assets.assets["displayBG"][2]*self.px, self.assets.assets["displayBG"][3]*self.px/2 - 4*self.px, text="START", font=self.assets.getFont("monogramRevised", WINDOW_SCALE*-(80 - (WINDOW_SCALE-1)*50)*scaleMul["Display"][WINDOW_SCALE][1]), anchor=E)

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
        self.textfields["N"] = self.frameDict["N"].create_text(0, self.px*5*scaleMul["Stats"][WINDOW_SCALE][0], text="10", font=self.assets.getFont("monogramRevised", WINDOW_SCALE*-(32 - (WINDOW_SCALE-1)*20)*scaleMul["Stats"][WINDOW_SCALE][1]), fill="white", anchor=SW)

        self.update_combat_display()

    def create_buttons(self):
        for y in range(len(self.defaultLayout)):
            for x in range(len(self.defaultLayout[y])):
                if self.defaultLayout[y][x] != None:
                    self.create_button(self.frameDict["keypad"], (y, x), image=self.assets.getAsset(self.defaultLayout[y][x]), width=self.assets.assets[self.defaultLayout[y][x]][2]*self.px, height=self.assets.assets[self.defaultLayout[y][x]][3]*self.px, padx=0, pady=0, bd=0, command=self.buttons[self.defaultLayout[y][x]])
                    if self.defaultLayout[y][x] == "Plus":
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
        self.frameDict["HP"].itemconfig(self.textfields["HP"], text=str(self.player.playerDict["HP"]))
        self.frameDict["LVL"].itemconfig(self.textfields["LVL"], text=str(self.player.playerDict["LVL"]))
        self.frameDict["N"].itemconfig(self.textfields["N"], text=str(self.player.playerDict["N"]))
        self.frameDict["Time"].itemconfig(self.imagefields["Time"], image=self.assets.getAsset("Time_" + str(self.player.playerDict["Time"])))
        self.frameDict["Atk"].itemconfig(self.imagefields["Atk"], image=self.assets.getAsset("Atk_" + str(self.player.playerDict["Atk"])))
        self.frameDict["Def"].itemconfig(self.imagefields["Def"], image=self.assets.getAsset("Def_" + str(self.player.playerDict["Def"])))
        self.frameDict["Luck"].itemconfig(self.imagefields["Luck"], image=self.assets.getAsset("Luck_" + str(self.player.playerDict["Luck"])))

        self.increment_timers()

        self.after(10, self.update_combat_display)

class actions():
    def __init__(self, game):
        self.game = game
        self.game.bind("<Escape>", lambda e : self.quitGame())

    def quitGame(self):
        quitQuery = messagebox.askyesno("Quit", "Are you sure you want to quit?", icon="warning")
        if quitQuery:
            self.game.destroy()

    def keypad_state_change(self):
        self.altLayout = [
            ["BlankOrange", "BlankOrange", "BlankLightGrey", "BlankLightGrey", "BlankLightGrey"],
            ["Circle", "BlankBlack", "UpArrow", "BlankBlack", "BlankLightGrey"],
            ["Triangle", "LeftArrow", "BlankDarkGrey", "RightArrow", "BlankLightGrey"],
            ["Square", "BlankBlack", "DownArrow", "BlankBlack", "BlankPlus"],
            ["Home", "No", "BlankDarkGrey", "Yes", None]
        ]

        for y in range(len(self.game.defaultLayout)):
            for x in range(len(self.game.defaultLayout[y])):
                if self.altLayout[y][x] != None and self.game.defaultLayout[y][x] != None and self.game.defaultLayout[y][x] != self.altLayout[y][x]:
                    self.game.change_button((y, x), self.altLayout[y][x])

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
    
    def evaluate_buffer(self):
        try:
            if self.game.buffer.replace(".", "").replace("(", "").replace(")", "").isalnum():
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

    def retrieve_result(self):
        #self.add_to_buffer(self.game.result)
        #self.push_to_screen(self.game.result)
        pass ###feature disabled

class buttonPresses():
    def __init__(self, actions):
        self.action = actions
    
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
        self.action.evaluate_buffer()
    
    def press_Pound(self):
        self.action.keypad_state_change()

    def press_Home(self):
        self.action.keypad_state_reset()
    
    def press_UpArrow(self):
        pass

    def press_DownArrow(self):
        pass

    def press_LeftArrow(self):
        pass

    def press_RightArrow(self):
        pass

    def press_Yes(self):
        for key in self.action.game.player.playerDict:
            self.action.game.player.playerDict[key] += 1

    def press_No(self):
        pass

    def press_Circle(self):
        pass

    def press_Triangle(self):
        pass

    def press_Square(self):
        pass

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

    def press_Disabled(self):
        pass

        
### Main Game Loop
def main():
    assets = assetHandler()
    game = gameInstance(WINDOW_SIZE, WINDOW_TITLE, assets)
 
    game.mainloop()
    
main()
