from tkinter import *
from matplotlib import pyplot as plt
import numpy as np
import tkinter.messagebox as mb

program = Tk()
program.resizable(0,0)
program.title('Grafik Çizici')

def createGraph():
    try:
        x_data = entry_for_x.get()
        y_data = entry_for_y.get()
        plt.plot(np.array(x_data.split(','),dtype='float64'),np.array(y_data.split(','),dtype='float64'))
        plt.xlabel(title_for_x.get())
        plt.ylabel(title_for_y.get())
        plt.title(entry_for_title.get())
        plt.show()
    except:
        mb.showerror('Grafik Çizici','Verileri düzgünce virgülle ayrılmış şekilde (1,2,3) girdiğinizden emin olunuz.')



titlelbl = Frame(program,background='gray')
Label(titlelbl,text='Tablonuz için başlık giriniz:',background='gray',width=25).grid(column=1,row=1,pady=(30,30))
entry_for_title = Entry(titlelbl)
entry_for_title.grid(row=1,column=2,padx=(0,20),pady=(30,30))
titlelbl.pack()

frame1 = Frame(program,background='gray')
Label(frame1,text='X ekseni için başlık giriniz:',background='gray',width=25).grid(column=1,row=2)
title_for_x = Entry(frame1)
title_for_x.grid(row=2,column=2,padx=(0,20))
frame1.pack()

subframe = Frame(program,background='gray')
Label(subframe,text='X ekseni için verileri giriniz:',background='gray',width=25).grid(row=3,column=1,pady=(0,30))
entry_for_x = Entry(subframe)
entry_for_x.grid(row=3,column=2,padx=(0,20),pady=(0,30))
subframe.pack()


frame2 = Frame(program,background='gray')
Label(frame2,text='Y ekseni için başlık giriniz:',background='gray',width=25).grid(row=4,column=1)
title_for_y = Entry(frame2)
title_for_y.grid(row=4,column=2,padx=(0,20))
frame2.pack()

subframe2 = Frame(program,background='gray')
Label(subframe2,text='Y ekseni için verileri giriniz:',background='gray',width=25).grid(row=5,column=1,pady=(0,30))
entry_for_y = Entry(subframe2)
entry_for_y.grid(row=5,column=2,padx=(0,20),pady=(0,30))
subframe2.pack()


show_btn = Button(program,text='GÖSTER',command=createGraph)
show_btn.pack(side=BOTTOM,fill=X)


program.mainloop()
