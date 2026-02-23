from tkinter import *

win = Tk()
win.geometry("400x400")
win.title("jang")

Label(win, text="메뉴를 선택하세요", font='궁서 20').pack()
burgar_var = StringVar()
btn_burgar1 = Radiobutton(win, text="치킨버거", value="치킨버거", variable=burgar_var)
btn_burgar2 = Radiobutton(win, text="햄버거", value="햄버거", variable=burgar_var)
btn_burgar3 = Radiobutton(win, text="치즈버거", value="치즈버거", variable=burgar_var)
btn_burgar4 = Radiobutton(win, text="불고기버거", value="불고기버거", variable=burgar_var)
btn_burgar1.select() # 기본값 선택
btn_burgar1.pack(); btn_burgar2.pack(); btn_burgar3.pack(); btn_burgar4.pack()

Label(win, text="음료를 선택하세요", font='궁서 20').pack()
drink_var = StringVar()
btn_drink1 = Radiobutton(win, text="콜라", value="콜라", variable=drink_var)
btn_drink2 = Radiobutton(win, text="사이다", value="사이다", variable=drink_var)
btn_drink3 = Radiobutton(win, text="환타", value="환타", variable=drink_var)
btn_drink1.select() # 기본값 선택
btn_drink1.pack(); btn_drink2.pack(); btn_drink3.pack()

def btncmd():
    print(burgar_var.get())
    print(drink_var.get())
btn = Button(win, text="주문", font='맑은고딕 15', command=btncmd)
btn.pack()
win.mainloop()