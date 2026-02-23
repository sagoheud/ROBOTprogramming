# import tkinter 로 사용시 win=Tk()로 사용하면 에러 발생 한다
# win = tkinter.Tk()로 사용 해야 한다 매우 중요

from tkinter import * # gui(graphical user interface)
win = Tk() # 창 생성
win.geometry("400x400") # 창 크기
win.title("jang") # 창 제목
win.option_add("*font","맑은고딕 40") # 폰트 결정
btn = Button(win, text='버튼', command=win.destroy) # 버튼
btn.pack() # 버튼 만들때 세트 (이 문장이 없으면 버튼이 안만들어짐)
# side="top","bottom","left","right" 디폴트는 top
win.mainloop() # 창 실행