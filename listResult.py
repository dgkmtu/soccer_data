import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import datetime

def readResult(event):
    IFile = 'result.csv'

    year    = year_entry.get()    # 対象年度の取得
    section = section_entry.get() # 対象節の取得

    # 試合結果表示
    print('第', section, '節 試合結果')

    with open(IFile, mode='r', encoding='utf-8')as f:
        for row in f:
            columns = row.rstrip().split(',')
            # 取得データの格納
            Wsection = columns[0]
            Wdate    = columns[1]

            # 日付の分離
            Wdate = Wdate.split('/')
            
            
            if Wdate[0] == '2019' and section == Wsection:
                result = ''

                result += columns[1]
                result += ' '
                result += columns[2]
                result += ' '
                result += columns[4]
                result += '-'
                result += columns[5]
                result += ' '
                result += columns[3]

                print(result) # 試合結果の表示
    
if __name__ == '__main__':

    # rootの作成
    root = Tk()
    root.title('試合結果照会画面')

    # Frame1の作成（対象年度選択欄）
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid(row=0, column=0, sticky=W)

    # 「年度」ラベルの作成
    year_label = ttk.Label(frame1, text='年度  ＞＞')
    year_label.pack(side=LEFT)

    # 「年度」エントリーの作成
    entry1 = StringVar()
    year_entry = ttk.Combobox(frame1, textvariable=entry1, width=10)
    year_entry['values']=('2019')
    year_entry.set('2019') # 2019年度をデフォルトとする
    year_entry.pack(side=LEFT)

    # Frame2の作成（対象節選択欄）
    frame2 = ttk.Frame(root, padding=10)
    frame2.grid(row=1, column=0, sticky=W)

    # 「節」ラベルの作成
    section_label = ttk.Label(frame2, text='節   ＞＞')
    section_label.pack(side=LEFT)

    # 「節」エントリーの作成
    entry2 = StringVar()
    section_entry = ttk.Entry(frame2, textvariable=entry2, width=5)
    section_entry.pack(side=LEFT)
    
    # Frame3の作成（実行ボタンおよび閉じるボタンの作成）
    frame3 = ttk.Frame(root, padding=10)
    frame3.grid(row=2, column=0,sticky=E)

    # 実行ボタンの設置
    button1 = ttk.Button(frame3, text='実行')
    button1.bind("<Button-1>", readResult)
    button1.pack(side=LEFT)

    # 閉じるボタンの設置
    button2 = ttk.Button(frame3, text='閉じる', command=quit)
    button2.pack(side=LEFT)

    root.mainloop()
