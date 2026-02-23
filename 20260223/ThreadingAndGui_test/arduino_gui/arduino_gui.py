from tkinter import *
import serial
seri = serial.Serial(port='COM6', baudrate=9600)
win = Tk()
win.title("[파이썬] chechbutton 제어")

def jang1():
    val1 = str(chk1.get())
    if val1 == '1':
        a = 'A'
        a = a.encode()
        print(a)
        la1.config(text="첫번째 LED ON")
        seri.write(a)
    else:
        a = 'B'
        a = a.encode()
        print(a)
        la1.config(text="첫번째 LED OFF")
        seri.write(a)
def jang2():
    val2 = str(chk2.get())
    if val2 == '1':
        b = 'C'
        b = b.encode()
        print(b)
        la2.config(text="두번째 LED ON")
        seri.write(b)
    else:
        b = 'D'
        b = b.encode()
        print(b)
        la2.config(text="두번째 LED OFF")
        seri.write(b)

chk1 = IntVar()
chk2 = IntVar()
bt1 = Checkbutton(win, text="check1", variable=chk1, command=jang1, font=("bold 15"))
bt1.grid(column=0, row=0, sticky=W)
bt2 = Checkbutton(win, text="check2", variable=chk2, command=jang2, font=("bold 15"))
bt2.grid(column=0, row=1, sticky=W)
la1 = Label(win, text="첫번째 LED 결과 표시", width=20, height=2, fg="green", bg="#ff0000", font=("bold"))
la1.grid(column=0, row=2, sticky=W)
la2 = Label(win, text="두번째 LED 결과 표시", width=20, height=2, fg="brown", bg="#ffff00", font=("bold"))
la2.grid(column=0, row=3, sticky=W)
win.mainloop()