import sys
import tkinter
from tkinter import Label, Button, Entry, StringVar, Tk, Frame, Text, Scrollbar, END, INSERT, LEFT, RIGHT, BOTH, Y, X, N, S, E, W, Toplevel, messagebox, filedialog, ttk
from dataclasses import dataclass


@dataclass
class DMLabel(Label):
    name: str
    sensorValue: float


def main():
    ## Setup the GUI
    root = tkinter.Tk()
    root.title('Soracom Harvest')
    root.geometry('400x300')
    root.resizable(False, False)

    ## Label
    Static1 = tkinter.Label(text=u'test')
    Static1.pack()


    root.mainloop()


if __name__ == '__main__':
    main()
