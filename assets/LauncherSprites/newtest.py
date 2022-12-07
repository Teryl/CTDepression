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
        self.img_01_Button_Play = tk.PhotoImage(file=os.path.abspath("./ctd1D/assets/LauncherSprites/01_Button_Play.png"))
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
            relief="raised")
        self.play.grid(column=0, padx=10, row=0)
        self.exit = tk.Button(frame3)
        self.img_02_Button_Quit = tk.PhotoImage(file=os.path.abspath("./ctd1D/assets/LauncherSprites/02_Button_Quit.png"))
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
            relief="raised")
        self.exit.grid(column=1, padx=10, row=0)
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
        self.img__Logo_Black = tk.PhotoImage(file=os.path.abspath("./ctd1D/assets/LauncherSprites/.Logo_Black.png"))
        self.title.configure(
            activebackground="#000000",
            anchor="center",
            background="#000000",
            image=self.img__Logo_Black,
            justify="center",
            relief="flat",
            state="normal")
        self.title.grid(column=0, row=0)
        self.resizer = tk.Frame(frame2)
        self.resizer.configure(background="#000000", height=200, width=200)
        button5 = tk.Button(self.resizer)
        self.img_03_Button_Up = tk.PhotoImage(file=os.path.abspath("./ctd1D/assets/LauncherSprites/03_Button_Up.png"))
        button5.configure(
            activebackground="#000000",
            activeforeground="#000000",
            background="#000000",
            highlightbackground="#000000",
            highlightcolor="#000000",
            image=self.img_03_Button_Up,
            relief="raised")
        button5.grid(column=0, row=0, sticky="ew")
        button6 = tk.Button(self.resizer)
        self.img_05_Button_Down = tk.PhotoImage(file=os.path.abspath("./ctd1D/assets/LauncherSprites/05_Button_Down.png"))
        button6.configure(
            activebackground="#000000",
            background="#000000",
            compound="top",
            default="normal",
            highlightbackground="#000000",
            image=self.img_05_Button_Down,
            justify="left",
            relief="raised")
        button6.grid(column=0, row=2, sticky="ew")
        canvas7 = tk.Canvas(self.resizer)
        canvas7.configure(
            background="#000000",
            height=15,
            highlightbackground="#000000",
            highlightcolor="#000000",
            relief="flat",
            selectbackground="#000000",
            state="normal",
            width=15)
        canvas7.grid(column=0, row=1)
        self.resizer.grid(column=0, row=4)
        self.resizer.grid_anchor("center")
        frame6 = tk.Frame(frame2)
        frame6.configure(background="#000000", height=20, width=200)
        frame6.grid(column=0, row=3)
        frame2.pack(side="top")

        # Main widget
        self.mainwindow = self.topLevel

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = LauncherApp()
    app.run()
