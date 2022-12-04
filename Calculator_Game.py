### CTD Calculator Game Prototype 0.5
### By: David Ling
### Versioned as of 04/12/22

### Importing Modules
import time
from math import *
from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
import os
import winsound
from ctypes import windll, byref, create_unicode_buffer, create_string_buffer

### Setting Global Variables
WINDOW_SIZE = (460, 840)
SCALE_UNIT = (115, 220)
WINDOW_SCALE = 1
WINDOW_SIZE_PX = (118, 214)
WINDOW_TITLE = "Mortal Math"
FR_PRIVATE  = 0x10
FR_NOT_ENUM = 0x20


def PLACEHOLDER_FUNCTION():
    pass



### Asset Class
class assetHandler():
    def __init__(self):
        self.calcPath = "./assets/CalcUI/"
        self.fightPath = "./assets/FightUI/"
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



        }
    
        

    ### Asset get method
    def getAsset(self, assetName):
        if self.assets[assetName][0].isalpha() or self.assets[assetName][0][0] == "#":
            return self.assets[assetName][0]
        elif assetName in self.imageDict:
            return self.imageDict[assetName]
        else:
            self.imageDict[assetName] = PhotoImage(file=os.path.abspath(self.assets[assetName][0])).zoom(int(self.assets[assetName][1] * WINDOW_SCALE))
            return self.imageDict[assetName]

    # load fonts
    def initialise_fonts(self):
        self.load_font(os.path.abspath("./assets/fonts/monogram.ttf"))

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
        self.buffer = ""

        self.binds = {}

        self.configure(background=self.assets.getAsset("windowBG"))
        self.title(self.name)
       
       # Calculate Starting X and Y coordinates for Window
        x = (self.winfo_screenwidth()/2) - (WINDOW_SIZE[0]/2)
        y = (self.winfo_screenheight()/2) - (WINDOW_SIZE[1]/2)
        
        self.geometry('%dx%d+%d+%d' % (self.size[0], self.size[1], x, y))
        self.resizable(True, True)
        self.minsize(int(WINDOW_SIZE[0]*WINDOW_SCALE), int(WINDOW_SIZE[1]*WINDOW_SCALE))

        self.create_main()
        action = actions(self)

        self.buttons = {
            "C" : action.keypad_state_reset,
            "CE" : PLACEHOLDER_FUNCTION,
            "LeftBracket" : PLACEHOLDER_FUNCTION,
            "RightBracket" : PLACEHOLDER_FUNCTION,
            "Divide" : PLACEHOLDER_FUNCTION,
            "1" : PLACEHOLDER_FUNCTION,
            "2" : PLACEHOLDER_FUNCTION,
            "3" : PLACEHOLDER_FUNCTION,
            "Multiply" : PLACEHOLDER_FUNCTION,
            "4" : PLACEHOLDER_FUNCTION,
            "5" : PLACEHOLDER_FUNCTION,
            "6" : PLACEHOLDER_FUNCTION,
            "Minus" : PLACEHOLDER_FUNCTION,
            "7" : PLACEHOLDER_FUNCTION,
            "8" : PLACEHOLDER_FUNCTION,
            "9" : PLACEHOLDER_FUNCTION,
            "Home" : action.keypad_state_change,
            "0" : PLACEHOLDER_FUNCTION,
            "Dot" : PLACEHOLDER_FUNCTION,
            "Equals" : PLACEHOLDER_FUNCTION,
            "Plus" : PLACEHOLDER_FUNCTION,
            "UpArrow" : PLACEHOLDER_FUNCTION,
            "RightArrow" : PLACEHOLDER_FUNCTION,
            "LeftArrow" : PLACEHOLDER_FUNCTION,
            "DownArrow" : PLACEHOLDER_FUNCTION,
            "Disabled" : PLACEHOLDER_FUNCTION,
            "BlankOrange" : PLACEHOLDER_FUNCTION,
            "BlankLightGrey" : PLACEHOLDER_FUNCTION,
            "BlankDarkGrey" : PLACEHOLDER_FUNCTION,
            "BlankBlack" : PLACEHOLDER_FUNCTION,
            "Yes" : PLACEHOLDER_FUNCTION,
            "No" : PLACEHOLDER_FUNCTION,
            "Circle" : PLACEHOLDER_FUNCTION,
            "Triangle" : PLACEHOLDER_FUNCTION,
            "Square" : PLACEHOLDER_FUNCTION,
            "Pound" : PLACEHOLDER_FUNCTION,
            "BlankPlus" : PLACEHOLDER_FUNCTION, 
        }

        self.defaultLayout = [
            ["C", "CE", "LeftBracket", "RightBracket", "Divide"],
            ["BlankBlack", "1", "2", "3", "Multiply"],
            ["BlankBlack", "4", "5", "6", "Minus"],
            ["BlankBlack", "7", "8", "9", "Plus"],
            ["Home", "0", "Dot", "Equals", None],
        ]

        self.create_calc()
        self.create_buttons()
        self.assets.initialise_fonts()
        self.create_display()
        
        

       
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
        self.create_canvas(self.frameDict["mainContainer"], "combat", image=self.assets.getAsset("combatBG"), width=self.assets.assets["combatBG"][2]*self.px, height=self.assets.assets["combatBG"][3]*self.px, padx=2*self.px, pady=self.px, relx=0.5, rely=3 /WINDOW_SIZE_PX[1], anchor=N)

    # create calculator frame structure
    def create_calc(self):
        self.create_canvas(self.frameDict["main"], "screen", image=self.assets.getAsset("screenBG"), width=self.assets.assets["screenBG"][2]*self.px, height=self.assets.assets["screenBG"][3]*self.px, padx=2*self.px, pady=0, relx=0.5, rely=0.15, anchor=CENTER)
        self.create_canvas(self.frameDict["main"], "keypad", image=self.assets.getAsset("keypadBG"), width=self.assets.assets["keypadBG"][2]*self.px, height=self.assets.assets["keypadBG"][3]*self.px, padx=0, pady=0, relx=0.5, rely=0.625, anchor=CENTER)

    def create_display(self):
        self.create_canvas(self.frameDict["screen"], "display", image=self.assets.getAsset("displayBG"), width=self.assets.assets["displayBG"][2]*self.px, height=self.assets.assets["displayBG"][3]*self.px, padx=0, pady=0, relx=0.5, rely=0.5, anchor=CENTER)
        self.textfields['screenText'] = self.frameDict["display"].create_text(self.assets.assets["displayBG"][2]*self.px, self.assets.assets["displayBG"][3]*self.px/2 - self.px, text="300", font=self.assets.getFont("monogram", WINDOW_SCALE*-(80 - (WINDOW_SCALE-1)*50)), anchor=E)


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
            self.frameDict[id] = Canvas(master, bd=-2, bg=bg, width=width, height=height)
            if "image" in kwargs:
                image = kwargs.pop("image", None)
                self.frameDict[id].create_image(width/2, height/2, image=image, anchor=CENTER)
            self.frameDict[id].place(**kwargs)
            

    def create_button(self, master, id, **kwargs):
        self.buttonDict[id] = Button(master, **kwargs)

    def update_button(self, id, **kwargs):
        self.buttonDict[id].config(**kwargs)

    def update_display(self, text):
        self.frameDict["display"].itemconfig(self.textfields['screenText'], text=text)

    def grid_item(self, item, **kwargs):
        item.grid(**kwargs)
   
    

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
            ["C", "BlankOrange", "BlankLightGrey", "BlankLightGrey", "BlankLightGrey"],
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
        self.game.update_display(text)
    
    def clear_screen(self):
        self.game.update_display("")

    def add_to_buffer(self, text):
        self.game.buffer += text
        self.push_to_screen(self.game.buffer)

    def clear_buffer(self):
        self.game.buffer = ""
        self.push_to_screen(self.game.buffer)

    def backspace(self):
        self.game.buffer = self.game.buffer[:-1]
        self.push_to_screen(self.game.buffer)
    



class buttonPresses():
    def __init__(self, actions):
        self.action = actions
    


        
### Main Game Loop
def main():
    assets = assetHandler()
    game = gameInstance(WINDOW_SIZE, WINDOW_TITLE, assets)

    game.mainloop()
    
main()
