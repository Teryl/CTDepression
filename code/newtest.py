#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import os


class LauncherApp:
    def __init__(self, master=None):
        # build ui
        self.topLevel = tk.Tk() if master is None else tk.Toplevel(master)
        self.topLevel.configure(background="#000000", height=200, width=200)
        self.topLevel.resizable(False, False)
        frame2 = tk.Frame(self.topLevel)
        frame2.configure(background="#000000", height=200, width=200)
        frame3 = tk.Frame(frame2)
        frame3.configure(background="#000000", height=200, width=200)
        self.play = tk.Button(frame3)
        scaler = 3
        self.img_01_Button_Play = tk.PhotoImage(file= os.path.abspath("./assets/LauncherSprites/01_Button_Play.png")).zoom(int(scaler))
        self.play.configure(
            activebackground="#000000",
            activeforeground="#000000",
            background="#000000",
            compound="bottom",
            cursor="arrow",
            disabledforeground="#000000",
            foreground="#000000",
            highlightbackground="#000000",
            highlightcolor="#000000",
            image=self.img_01_Button_Play,
            relief="flat")
        self.play.grid(column=0, padx=10, row=0)
        self.play.configure(command=self.playGame)
        self.exit = tk.Button(frame3)
        self.img_02_Button_Quit = tk.PhotoImage(file=os.path.abspath("./assets/LauncherSprites/02_Button_Quit.png")).zoom(int(scaler))
        self.exit.configure(
            activebackground="#000000",
            activeforeground="#000000",
            background="#000000",
            compound="bottom",
            cursor="arrow",
            disabledforeground="#000000",
            foreground="#000000",
            highlightbackground="#000000",
            highlightcolor="#000000",
            image=self.img_02_Button_Quit,
            relief="flat")
        self.exit.grid(column=1, padx=10, row=0)
        self.exit.configure(command=self.playExit)
        frame3.grid(column=0, row=2)
        self.background = tk.Canvas(frame2)
        self.background.configure(
            background="#000000",
            cursor="arrow",
            highlightbackground="#000000",
            highlightcolor="#000000",
            insertbackground="#000000",
            relief="flat",
            selectbackground="#000000",
            selectforeground="#000000",
            state="disabled",
            takefocus=False)
        self.background.grid(column=0, row=0)
        self.title = tk.Label(frame2)
        self.maxFrames = 51
        self.img__Logo_Black = [tk.PhotoImage(file=os.path.abspath("./assets/LauncherSprites/logo_frames/"+str(i)+'.png')).zoom(int(scaler)).subsample(8) for i in range(self.maxFrames)]
        
        #self.img__Logo_Black = tk.PhotoImage(file=os.path.abspath("./assets/LauncherSprites/logo_frames/0.png")).zoom(scaler).subsample(10)
        self.title.configure(
            activebackground="#000000",
            anchor="center",
            background="#000000",
            font="TkDefaultFont",
            image=self.img__Logo_Black[0],
            justify="center",
            relief="flat",
            state="normal")
        self.title.grid(column=0, row=0)
        self.resizer = tk.Frame(frame2)
        self.resizer.configure(background="#000000", height=200, width=200)
        button5 = tk.Button(self.resizer)
        self.img_03_Button_Up = tk.PhotoImage(file=os.path.abspath("./assets/LauncherSprites/03_Button_Up.png")).zoom(int(scaler/1.5))
        button5.configure(
            activebackground="#000000",
            activeforeground="#000000",
            background="#000000",
            highlightbackground="#000000",
            highlightcolor="#000000",
            image=self.img_03_Button_Up,
            relief="flat")
        button5.grid(column=0, row=0, sticky="ew")
        button5.configure(command=self.zoomIn)
        button6 = tk.Button(self.resizer)
        self.img_05_Button_Down = tk.PhotoImage(file="./assets/LauncherSprites/05_Button_Down.png").zoom(int(scaler/1.5))
        button6.configure(
            activebackground="#000000",
            background="#000000",
            compound="top",
            default="normal",
            highlightbackground="#000000",
            image=self.img_05_Button_Down,
            justify="left",
            relief="flat")
        button6.grid(column=0, row=2, sticky="ew")
        button6.configure(command=self.zoomOut)
        self.zoomWindow = tk.Canvas(self.resizer)
        self.zoomWindow.configure(
            background="#000000",
            height=15,
            highlightbackground="#000000",
            highlightcolor="#000000",
            relief="flat",
            selectbackground="#000000",
            state="normal",
            width=15)
        self.zoomWindow.grid(column=0, row=1)
        self.resizer.grid(column=0, row=4)
        self.resizer.grid_anchor("center")
        frame6 = tk.Frame(frame2)
        frame6.configure(background="#000000", height=20, width=200)
        frame6.grid(column=0, row=3)
        frame2.pack(side="top")

        # Main widget
        self.mainwindow = self.topLevel

        self.logoLoop(self.maxFrames)

    def logoLoop(self, maxFrames, frame = 0):
        if frame == maxFrames:
            frame = 0
        self.title.configure(image=self.img__Logo_Black[frame])
        self.topLevel.after(50, self.logoLoop, maxFrames, frame + 1)
        

    def run(self):
        self.mainwindow.mainloop()

    def playGame(self):
        os.system("python code/visuals.py")
        time.sleep(1)
        exit()
        pass

    def playExit(self):
        exit()

    def zoomIn(self):
        pass

    def zoomOut(self):
        pass


if __name__ == "__main__":
    app = LauncherApp()
    app.run()