from tkinter import *

win = Tk()
win.geometry("400x600")
win.title("jang")

Label(win, text="메뉴를 선택하세요", font='궁서 20').pack()
burgar_var = StringVar()
burgar_var.set("치킨버거") # 기본값 선택
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

order_count = 0; total_price = 0; order_prices =[]
total_label = Label(win, text="총 금액: 0원", font=("Arial", 12, "bold"))
total_label.pack()

def btncmd():
    global order_count, total_price
    order_count += 1
    if burgar_var.get() == "치킨버거":
        burger = "치킨버거"
        burgar_price = 4300
    elif burgar_var.get() == "햄버거":
        burger = "햄버거"
        burgar_price = 3700
    elif burgar_var.get() == "치즈버거":
        burger = "치즈버거"
        burgar_price = 4100
    else:
        burger = "불고기버거"
        burgar_price = 4500

    if drink_var.get() == "콜라":
        drink = "콜라"
        drink_price = 1400
    elif drink_var.get() == "사이다":
        drink = "사이다"
        drink_price = 1600
    else:
        drink = "환타"
        drink_price = 1200
    
    order_price = burgar_price + drink_price
    total_price += order_price
    order_prices.append(order_price)
    order_text = f"{order_count}번: {burger} + {drink} = {order_price}원"
    order_list.insert(END, order_text)
    total_label.config(text=f"총 금액: {total_price}원")

btn = Button(win, text="주문", font='맑은고딕 15', command=btncmd)
btn.pack()
win.mainloop()