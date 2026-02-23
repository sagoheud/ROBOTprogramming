# import tkinter 로 사용시 win=Tk()로 사용하면 에러 발생 한다
# win = tkinter.Tk()로 사용 해야 한다 매우 중요
from tkinter import *
win = Tk()
win.geometry("400x400")
win.title("jang")
txt = Text(win, width=30, height=5)
# 옵션 종류: padx=, pady=,, width=, height=, fg=, bg=, text= 등
txt.pack() # 텍스트 만들때 세트 (이 문장이 없으면 텍스트 박스가 안만들어 짐)
txt.insert(END, "글자를 입력 하세요")
e = Entry(win, width=30)
e.pack()
e.insert(END, "한 줄만 입력 하세요")

def btncmd():
    print(txt.get("1.0", END)) # 처음부터 끝 까지 문자를 가져옴 1은 첫번째라인 0은 컬럼위치
    print(e.get())
def des():
    win.destroy()

btn = Button(win, text="클릭", command=btncmd)
btn1 = Button(win, text="폭파", command=des)
btn.pack()
btn1.pack()
win.mainloop()
