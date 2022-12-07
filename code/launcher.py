### CTD Calc Game Launcher

# By David Ling

from tkinter import *
import os
import sys

WINDOW_SIZE_LAUNCHER_LAUNCHER = (765, 765)
HOME_DIR = "./code/"
SPRITE_DIR = "./assets/LauncherSprites/"
ANIM_DIR = "./assets/LauncherSprites/logo_frames/"

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
        self.root.bind("<Escape>", lambda e: self.root.destroy())
        

        x = (self.root.winfo_screenwidth()/2) - (WINDOW_SIZE_LAUNCHER[0]/2)
        y = (self.root.winfo_screenheight()/2) - (WINDOW_SIZE_LAUNCHER[1]/2)
        self.root.geometry('%dx%d+%d+%d' % (WINDOW_SIZE_LAUNCHER[0], WINDOW_SIZE_LAUNCHER[1], x, y))

        self.initialFrames = [PhotoImage(file = os.path.abspath(os.path.join(ANIM_DIR, str(i) + ".png"))).subsample(2) for i in range(18)]
        self.loopingFrames = [PhotoImage(file = os.path.abspath(os.path.join(ANIM_DIR, str(i) + ".png"))).subsample(2) for i in range(18, 51)]

        self.loopsplash = Canvas(self.root, width = WINDOW_SIZE_LAUNCHER[0], height = WINDOW_SIZE_LAUNCHER[1], background="black", highlightthickness=0, bd=0)
        self.loopingAnim = self.loopsplash.create_image(WINDOW_SIZE_LAUNCHER[0]/2, WINDOW_SIZE_LAUNCHER[1]/2, image = self.initialFrames[0], anchor = CENTER)
        self.loopsplash.place(relx = 0.5, rely = 0.5, anchor = CENTER)

        self.imageBuffer["Start Arrow"] = (PhotoImage(file = os.path.abspath(os.path.join(SPRITE_DIR, "01_Button_Play.png"))).zoom(6))
        self.itemDict["Start Arrow"] = Button(self.root, width = 120, height = 100, image = self.imageBuffer["Start Arrow"], bg="black", borderwidth = 0, highlightthickness = 0,command = lambda: self.begin())
        self.itemDict["Start Arrow"].place(relx = 0.25, rely = 0.7, anchor = CENTER)

        self.imageBuffer["Exit Arrow"] = (PhotoImage(file = os.path.abspath(os.path.join(SPRITE_DIR, "02_Button_Quit.png"))).zoom(6))
        self.itemDict["Exit Arrow"] = Button(self.root, width = 120, height = 100, image = self.imageBuffer["Exit Arrow"], bg="black", borderwidth = 0, highlightthickness = 0, command = lambda: self.root.destroy())
        self.itemDict["Exit Arrow"].place(relx = 0.25, rely = 0.85, anchor = CENTER)
        
        self.imageBuffer["Button Up"] = (PhotoImage(file = os.path.abspath(os.path.join(SPRITE_DIR, "03_Button_Up.png"))).zoom(6))
        self.itemDict["Button Up"] = Button(self.root, width = 120, height = 100, image = self.imageBuffer["Button Up"], bg="black", borderwidth = 0, highlightthickness = 0, command= lambda: self.change_scaling(1))
        self.itemDict["Button Up"].place(relx = 0.775, rely = 0.650, anchor = CENTER)

        self.imageBuffer["Button Down"] = (PhotoImage(file = os.path.abspath(os.path.join(SPRITE_DIR, "05_Button_Down.png"))).zoom(6))
        self.itemDict["Button Down"] = Button(self.root, width = 120, height = 100, image = self.imageBuffer["Button Down"], bg="black", borderwidth = 0, highlightthickness = 0, command= lambda: self.change_scaling(-1))
        self.itemDict["Button Down"].place(relx = 0.775, rely = 0.900, anchor = CENTER)

        #self.imageBuffer[""]


        self.root.after(1000, lambda: self.animateLoopingSplash())
        self.keepOnTop()

    def begin(self):
        self.root.destroy()
        ###run main.py


    def keepOnTop(self):
        self.root.attributes("-topmost", True)
        self.root.after(10, lambda: self.keepOnTop())


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


if __name__ == "__main__":
    tkObj = launcher()
    tkObj.root.mainloop()








