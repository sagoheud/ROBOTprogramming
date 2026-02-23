from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("400x400")
root.title("jang")

value = [str(i) + "일" for i in range(1,31)]
# combobo = ttk.Combobox(root, height=5, value=value)
# combobo.set("카드 결제일") # 최초 목록 제목 설정
# combobo.pack()
combobo = ttk.Combobox(root)
combobo.set("카드 결제일") # 최초 목록 제목 설정
combobo.pack()
readonly_combobox = ttk.Combobox(root, height=5, value=value, state="readonly") # 글자 입력이 안되게 읽기
readonly_combobox.current(0) # 0번 인덱스를 기본으로 선택
readonly_combobox.pack()

def btncmd():
    print(combobo.get())
    print(readonly_combobox.get())

btn = Button(root, text="주문", font="맑은고딕 15", command=btncmd)
btn.pack()
root.mainloop()