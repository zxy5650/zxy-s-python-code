from tkinter import *
import tkinter.filedialog
import re
import sys
import os

root = Tk()
str1 = []
str2 = []
str_dump = []
str3=[]
def xz():
    filename1 = tkinter.filedialog.askopenfilename()
    if filename1 != '':
        fa = open(filename1,'r');
    else:
        lb.config(text = "您没有选择任何文件");


    filename2 = tkinter.filedialog.askopenfilename()
    if filename2 != '':
        fb = open(filename2,'r');
    else:
        lb.config(text = "您没有选择任何文件");
    filename3 = tkinter.filedialog.askdirectory()
    if filename3 != '':
        fc = open(filename3+'/c.txt','w')
        print("数据处理完成！")
        print("版权归属联系qq565052989！")
    else:
        lb.config(text = "您没有选择任何文件");


    # 将第一个txt的内容逐行读到str1中
    for line in fa.readlines():
       str1.append(line.replace("\n", ''))
            # 将第二个txt中的内容逐行读到str2中
    for line in fb.readlines():
       str2.append(line.replace("\n", ''))
            # 将两个文件中重复的行，添加到str_dump中
    for i in str1:
       if i in str2:
           str_dump.append(i)
            # 将两个文件的行合并，并去重
    str_all = set(str1 + str2)
            # 将重复的行，在去重的合并行中，remove掉，剩下的就是不重复的行了
    for i in str_dump:
       if i in str_all:
            str_all.remove(i)
    if max(str2)>max(str1):
        # 取交集
        tmp=[val for val in str1 if val in str_all]
    else:
        tmp=[val for val in str2 if val in str_all]
    # for i in str1:
       #     if i in str_all:
    for i in list(tmp):
        fc.write(i + '\n')
    fa.close()
    fb.close()
    fc.close()
    global root
    root.destroy()
lb = Label(root, text='请选择txt文件')
lb.pack()
btn = Button(root, text="选择文件", command=xz)
btn.pack()
root.mainloop()
# root.destroy()
