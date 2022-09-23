import sys
import serial
import os

import datetime
from datetime import datetime, timedelta
import time

from threading import Thread
import queue

import json
import requests

import tkinter
from tkinter import ANCHOR, Label, Button, Entry, StringVar, Tk, Frame, Text, Scrollbar, END, INSERT, LEFT, RIGHT, BOTH, Y, X, N, S, E, W, Toplevel, messagebox, filedialog, ttk

#import can

SENSING_DATA = {
    'sample1':0, 
    'sample2':0 
}

def RxSensingData():
    device_dir = '/dev/ttyACM0'
    boudrate   = 115200
    ser = serial.Serial(device_dir, boudrate, timeout=1)
    ser.flush()

    global SENSING_DATA

    while True:
        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').rstrip()

                var_name = line.split(':')[0]
                sensing_val = line.split(':')[1]

                SENSING_DATA[var_name] = sensing_val

                print(SENSING_DATA)


def TxDataForSoracom():
    URL_HARVEST = 'http://harvest.soracom.io'

    global SENSING_DATA

    while True:
        dump_data = json.dumps(SENSING_DATA)

        requests.post(URL_HARVEST, data=SENSING_DATA, headers={'Content-Type':'applicationapp'})
        print('Data sent')
        time.sleep(10)

def GUIwithTK():
    global SENSING_DATA

    ## Setup the GUI
    root = tkinter.Tk()
    root.title('Soracom Harvest')
    root.geometry('1600x900')
    root.configure(bg='black')
    root.resizable(False, False)
   

    c = tkinter.Canvas(width = 1920, height = 1080, background = 'black')
    c.pack()

    while True:
        c.create_arc(60, 60, 840, 840, tag="oval", fill="black", outline="white", width=5, start=300, extent=150)
        c.create_arc(60, 60, 840, 840, tag="oval", fill="black", outline="white", width=5, start=90, extent=150)
        c.create_arc(60, 60, 840, 840, tag="oval", fill="black", outline="white", width=5, start=240, extent=60)
        c.create_arc(60, 60, 840, 840, tag="oval", fill="cornflowerblue", outline="white", width=0, start=300, extent=150)
        c.create_arc(60, 60, 840, 840, tag="oval", fill="orange", outline="white", width=0, start=240, extent=-150)
        c.create_oval(240, 240, 660, 660, tag="oval", fill="black", outline="white", width=5)
        
        c.create_text(450, 450, text = '00', font = ('Arial Black', 100), fill = 'cyan')
        c.create_text(450, 564, text = 'Wh', font = ('Arial Black', 40), fill = 'white')

        #Speed1
        c.create_text(1386, 192, text = str(SENSING_DATA['sample2']), font = ('Arial Black', 60), fill = 'cyan')
        c.create_text(1550, 192, text = 'km/h', font = ('Arial Black', 50), fill = 'cyan')
        c.create_text(1020, 192, text = 'Speed1', font = ('Arial Black', 50), fill = 'white')
        c.create_line(888, 252, 1656, 252, fill='white', width=2)
        #Speed2
        c.create_text(1446, 360, text = '00', font = ('Arial Black', 60), fill = 'cyan')
        c.create_text(1610, 360, text = 'km/h', font = ('Arial Black', 50), fill = 'cyan')
        c.create_text(1080, 360, text = 'Speed2', font = ('Arial Black', 50), fill = 'white')
        c.create_line(948, 420, 1716, 420, fill='white', width=2)
        #Speed3
        c.create_text(1446, 528, text = '00', font = ('Arial Black', 60), fill = 'cyan')
        c.create_text(1610, 528, text = 'km/h', font = ('Arial Black', 50), fill = 'cyan')
        c.create_text(1080, 528, text = 'Speed3', font = ('Arial Black', 50), fill = 'white')
        c.create_line(948, 588, 1716, 588, fill='white', width=2)
        #Speed4
        c.create_text(1386, 696, text = '00', font = ('Arial Black', 60), fill = 'cyan')
        c.create_text(1550, 696, text = 'km/h', font = ('Arial Black', 50), fill = 'cyan')
        c.create_text(1020, 696, text = 'Speed4', font = ('Arial Black', 50), fill = 'white')
        c.create_line(888, 756, 1656, 756, fill='white', width=2)
        
        #time
        c.create_line(180, 1020, 360, 900, 1560, 900, 1740, 1020, fill='white', width=10)
        c.create_line(0, 1020, 1920, 1020, width=10)
        c.create_text(960, 990, text = '00:00', font = ('Arial Black', 70), fill = 'white')


        root.attributes("-fullscreen", True)

        root.mainloop()


if __name__ == '__main__':
    RxDataThread = Thread(target=RxSensingData)
    TxDataThread = Thread(target=TxDataForSoracom)
    DisplayGUI   = Thread(target=GUIwithTK)

    RxDataThread.start()
    TxDataThread.start()
    DisplayGUI.start()