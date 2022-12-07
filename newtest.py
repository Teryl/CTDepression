#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


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
        button2 = ttk.Button(frame3)
        self.img_01_Button_Play = tk.PhotoImage(file="assets/LauncherSprites/01_Button_Play.png")
        button2.configure(
            default="normal",
            image=self.img_01_Button_Play,
            takefocus=False,
            text='play')
        button2.grid(column=0, padx=10, row=0)
        button2.configure(command=self.runGame)
        button4 = ttk.Button(frame3)
        self.img_02_Button_Quit = tk.PhotoImage(file="assets/LauncherSprites/02_Button_Quit.png")
        button4.configure(
            default="normal",
            image=self.img_02_Button_Quit,
            state="normal",
            takefocus=False,
            text='play')
        button4.grid(column=1, padx=10, row=0)
        button4.configure(command=self.runExit)
        frame3.grid(column=0, row=2)
        canvas5 = tk.Canvas(frame2)
        canvas5.configure(
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
        canvas5.grid(column=0, row=1)
        label3 = tk.Label(frame2)
        self.img__Logo_Black = tk.PhotoImage(file="assets/LauncherSprites/.Logo_Black.png")
        label3.configure(
            activebackground="#000000",
            background="#000000",
            image=self.img__Logo_Black,
            justify="center",
            relief="flat",
            state="normal",
            text='label3')
        label3.grid(column=0, row=1)
        frame5 = tk.Frame(frame2)
        frame5.configure(background="#000000", height=200, width=200)
        button5 = tk.Button(frame5)
        self.img_03_Button_Up = tk.PhotoImage(file="assets/LauncherSprites/03_Button_Up.png")
        button5.configure(image=self.img_03_Button_Up, text='button5')
        button5.grid(column=0, row=0, sticky="ew")
        button6 = tk.Button(frame5)
        self.img_05_Button_Down = tk.PhotoImage(file="assets/LauncherSprites/05_Button_Down.png")
        button6.configure(
            image=self.img_05_Button_Down,
            justify="left",
            text='button6')
        button6.grid(column=0, row=2, sticky="ew")
        canvas6 = tk.Canvas(frame5)
        canvas6.configure(
            background="#000000",
            height=15,
            highlightbackground="#000000",
            highlightcolor="#000000",
            insertbackground="#000000",
            relief="flat",
            state="disabled",
            width=15)
        canvas6.grid(column=0, row=1, sticky="ew")
        frame5.grid(column=0, row=4, sticky="ew")
        frame5.grid_anchor("center")
        frame6 = tk.Frame(frame2)
        frame6.configure(background="#000000", height=20, width=200)
        frame6.grid(column=0, row=3)
        frame2.pack(side="top")

        # Main widget
        self.mainwindow = self.topLevel

    def run(self):
        self.mainwindow.mainloop()

    def runGame(self):
        pass

    def runExit(self):
        pass


if __name__ == "__main__":
    app = LauncherApp()
    app.run()