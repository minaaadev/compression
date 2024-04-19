from tkinter import *
from tkinter import filedialog
import zipfile
import os

win = Tk()
win.geometry("600x400")
win.title("파일 압축 프로그램")
win.option_add("*Font", "맑은고딕 20")

selected_files = [] # 선택된 파일들을 담을 리스트
zip_file_name = ""

def select_files():
    global selected_files
    selected_files = list(filedialog.askopenfilenames()) # 튜플을 리스트로 변환하여 선택된 파일들 저장
    if selected_files:
        selected_files_label.config(text="선택된 파일: " + ", ".join(selected_files)) # 선택된 파일을 라벨에 표시

def zip_files():
    global selected_files, zip_file_name
    if selected_files:
        zip_file_name = filedialog.asksaveasfilename(defaultextension=".zip", filetypes=[("ZIP 파일", "*.zip")])  # 저장될 압축 파일 이름 지정
        if zip_file_name: # 파일명이 선택되었는지 확인
            with zipfile.ZipFile(zip_file_name, 'w') as zipf:
                for file_path in selected_files:
                    zipf.write(file_path, os.path.basename(file_path)) # 선택된 파일들을 압축 파일에 추가
            compressed_file_label.config(text="압축된 파일: " + zip_file_name)  # 압축 완료 메시지 표시

# 프로그램 타이틀
description_label = Label(win, text='<파이썬 파일 압축 프로그램>', anchor="center", justify="center")
description_label.grid(row=0, column=0, columnspan=3, pady=10)

# 파일 선택 버튼과 압축 버튼
btn_select_files = Button(win, text='파일 선택', command=select_files)
btn_select_files.grid(row=1, column=1)
btn_zip = Button(win, text='파일 압축', command=zip_files)
btn_zip.grid(row=1, column=2)


# 선택된 파일과 압축된 파일을 나타낼 라벨
selected_files_label = Label(win, text="", wraplength=600)
selected_files_label.grid(row=2, column=0, columnspan=3, pady=10)
compressed_file_label = Label(win, text="", wraplength=600)
compressed_file_label.grid(row=3, column=0, columnspan=3, pady=10)

win.mainloop()