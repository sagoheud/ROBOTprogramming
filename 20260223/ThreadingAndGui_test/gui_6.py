from tkinter import *
from tkinter import messagebox

def show_selected():
    selected = []
    if var1.get() == 1:
        selected.append("옵션 1")
    if var2.get() == 1:
        selected.append("옵션 2")
    if var3.get() == 1:
        selected.append("옵션 3")
    if selected:
        messagebox.showinfo("선택된 값", ",\n".join(selected))
    else:
        messagebox.showinfo("선택된 값", "선택된 항목이 없습니다.")

win = Tk()
win.geometry("300x200")
win.title("Chechbox예제")
win.option_add("*font","맑은고딕 15")

var1 = IntVar(); var2 = IntVar(); var3 = IntVar()
cb1 = Checkbutton(win, text="옵션 1", variable=var1)
cb2 = Checkbutton(win, text="옵션 2", variable=var2)
cb3 = Checkbutton(win, text="옵션 3", variable=var3)
cb1.pack(anchor="w", padx=20, pady=5)
cb2.pack(anchor="w", padx=20, pady=5)
cb3.pack(anchor="w", padx=20, pady=5)
btn = Button(win, text="클릭", command=show_selected)
btn.pack()
win.mainloop()