from tkinter import *

win = Tk()
win.geometry("400x400")
win.title("jang")
chkvar = IntVar() # chkvar에 int 형으로 값을 저장한다
chkbox = Checkbutton(win, text="오늘 하루 보지 않기", variable=chkvar)
# chkbox.select() # 자동 선택 처리
# chkbox.deselect() # 자동 해제 처리
chkbox.pack()

def btncmd():
    print(chkvar.get()) # 0:체크해제, 1:체크
btn = Button(win, text="클릭", command=btncmd)
btn.pack()
btn1 = Button(win, text="종료", command=win.destroy)
btn1.pack()
win.mainloop()