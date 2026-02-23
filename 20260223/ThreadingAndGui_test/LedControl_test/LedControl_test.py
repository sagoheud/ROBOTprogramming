import serial
from tkinter import *
seri = serial.Serial(port='COM6', baudrate=9600)

class LedControl():
    commads = ['ON', 'OFF', 'BLINKING']
    def __init__(self, seri):
        self.win = Tk()
        self.win.title('[파이썬] 아두이노 LED 제어')
        self.seri = seri
        for i, comm in enumerate(self.commads): # 버튼을 만든다.
            bt = Button(self.win, text=comm, width=40, height=10, 
                        bg='grey', fg='black', 
                        command=lambda cmd=comm: self.button_click(cmd))
            bt.grid(column=i, row=0)
    def button_click(self, value):
        print(value)
        cmm = value
        OK = 'A'; NG = 'B'; GK = 'C'
        if cmm == 'ON':
            OK = OK.encode()
            print(OK)
            seri.write(OK)
        elif cmm == 'OFF':
            NG = NG.encode()
            print(NG)
            seri.write(NG)
        elif cmm == 'BLINKING':
            GK = GK.encode()
            print(GK)
            seri.write(GK)

btn = LedControl(seri)
btn.win.mainloop()