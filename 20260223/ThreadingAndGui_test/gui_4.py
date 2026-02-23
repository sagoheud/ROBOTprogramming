from tkinter import *

win = Tk()
win.geometry("500x400")
win.title("jang")
win.option_add("*font","맑은고딕 15")

listbox = Listbox(win, selectmode="extended", height=0)
# height에 숫자를 조절하면 숫자만큼만 보임
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "키위")
listbox.insert(3, "바나나")
listbox.insert(4, "포도")
listbox.insert(END, "끝")
listbox.pack()
entry = Entry(win, width=20)
entry.pack(pady=10)

def btncmd():
    listbox.delete(END) # 뒤에서부터 삭제
    # listbox.delete(0) # 처음부터 삭제
    # 항목확인
    print("1번째 부터 3번째 까지의 항목 :", listbox.get(0,3))
    # 선택된 항목 확인(인텍스 위치 확인)
    print("선택된 항목 :", listbox.curselection())
def btnadd():
    content = entry.get() # 입력창에 쓰인 글자 가져오기
    if content != "":     # 비어있지 않을 때만 추가
        listbox.insert(END, content)
        entry.delete(0, END) # 추가 후 입력창 비우기 (센스!)
    print("1번째 부터 3번째 까지의 항목 :", listbox.get(0,3))
    print("선택된 항목 :", listbox.curselection())

btn = Button(win, text="클릭", command=btncmd)
btn.pack(side="bottom")
btn1 = Button(win, text="추가", command=btnadd)
btn1.pack(side="bottom")
win.mainloop()