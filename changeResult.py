# 登録内容の照会・変更ツール

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def printResult(event):
    global results
    
    # 入力情報の取得
    year    = year_entry.get()
    section = section_entry.get()

    if not section:
        text = '「節」の入力がありません'
        messagebox.showerror('error', text)

    # 結果ファイルの取得
    results = []
    with open('result.csv', 'r', encoding='utf-8') as f:
        for row in f:
            columns = row.rstrip().split(',')
            
            Wsection = columns[0]
            if section == Wsection:
                results.append(columns)
    count = 0
    resultText = ''
    for result in results:
        # 表示データの格納
        count += 1
        result_date = result[1]
        Hteam = result[2]
        Ateam = result[3]
        HGoal = result[4]
        AGoal = result[5]

        # 試合結果一覧の表示
        resultText = str(count) + ' ' + result_date + ' '\
                     + Hteam + ' ' + HGoal + '-' + AGoal \
                     + ' ' + Ateam  
        text_widget.insert('end', resultText + '\n')

def selectResult(event):
    # 項番の取得
    indent = int(select_entry.get()) - 1
    print(results[indent])
    

if __name__ == '__main__':
    # rootの作成
    root = Tk()
    root.title('登録内容照会画面')
    root.resizable(False, False)
    root.geometry('380x280')

    # 「年度」ラベルの作成
    year_label = ttk.Label(text='年度＞＞')
    year_label.place(x=20, y=10)

    # 「年度」エントリーの作成
    entry1 = StringVar()
    year_entry = ttk.Combobox(textvariable=entry1, width=7)
    year_entry['values']=('2019')
    year_entry.set('2019')
    year_entry.place(x=75, y=10)

    # 「節」ラベルの作成
    section_label = ttk.Label(text='　節＞＞')
    section_label.place(x=140, y=10)

    # 「節」エントリーの作成
    entry2 = StringVar()
    section_entry = ttk.Entry(textvariable=entry2, width=5)
    section_entry.place(x=200, y=10)

    # 試合一覧ボタンの設置
    button1 = ttk.Button(text='①試合一覧')
    button1.bind("<Button-1>", printResult)
    button1.place(x=250, y=10)

    # 試合結果一覧ラベルの設置
    listResult_label = ttk.Label(text='■試合結果一覧')
    listResult_label.place(x=20, y=40)

    # 試合結果一覧テキストの設置
    text_widget = tk.Text(root, width=43, height=10)
    text_widget.place(x=20, y=60)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # 「試合選択」ラベルの作成
    select_label = ttk.Label(text='試合選択＞＞')
    select_label.place(x=20, y=210)
    
    # 「試合選択」エントリーの作成
    entry3 = StringVar()
    select_entry = ttk.Entry(textvariable=entry3, width=5)
    select_entry.place(x=100, y=210)
    
    # 選択ボタンの設置
    button2 = ttk.Button(text='②選択')
    button2.bind("<Button-1>", selectResult)
    button2.place(x=150, y=210)
    
    root.mainloop()
