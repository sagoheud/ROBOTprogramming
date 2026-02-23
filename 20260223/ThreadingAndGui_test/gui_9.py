from tkinter import *

win = Tk()
win.geometry("400x600")
win.title("jang")

Label(win, text="메뉴를 선택하세요", font='궁서 20').pack()
burgar_var = StringVar()
burgar_var.set(1) # 기본값 선택
Radiobutton(win, text="치킨버거 (4300원)", value="치킨버거", variable=burgar_var).pack()
Radiobutton(win, text="햄버거 (3700원)", value="햄버거", variable=burgar_var).pack()
Radiobutton(win, text="치즈버거 (4100원)", value="치즈버거", variable=burgar_var).pack()
Radiobutton(win, text="불고기버거 (4500원)", value="불고기버거", variable=burgar_var).pack()

Label(win, text="음료를 선택하세요", font='궁서 20').pack()
drink_var = StringVar()
drink_var.set("콜라") # 기본값 선택
Radiobutton(win, text="콜라 (1400원)", value="콜라", variable=drink_var).pack()
Radiobutton(win, text="사이다 (1600원)", value="사이다", variable=drink_var).pack()
Radiobutton(win, text="환타 (1200원)", value="환타", variable=drink_var).pack()

Label(win, text="주문 내역", font='15').pack()
order_list = Listbox(win, height=10)
order_list.pack(fill="both", expand=True)

def btncmd():
    global order_count
    order_count += 1
    if burgar_var.get() == 1:
        burger = "치킨버거"
    elif burgar_var.get() == 2:
        burger = "햄버거"
    elif burgar_var.get() == 3:
        burger = "치즈버거"
    elif burgar_var.get() == 4:
        burger = "불고기버거"
    
    print(burgar_var.get())
    print(drink_var.get())

btn = Button(win, text="주문", font='맑은고딕 15', command=btncmd)
btn.pack()
win.mainloop()