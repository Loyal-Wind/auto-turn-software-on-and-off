import tkinter
import win32api
import base64
import os
import subprocess
import time
import sys
import ctypes
from tkinter import messagebox
from tkinter import filedialog

CN = ["文件位置:","设置秒数:","循环次数:","错误:","秒数是一个错误的值\n请尝试输入一个正整数","循环次数是一个错误的值\n请尝试输入一个正整数","文件路径为空","提示：","执行完毕",'选择一个.exe文件',"帮助","先按选择文件按钮选择一个exe文件。然后输入打开后多少秒关闭软件，再然后输入循环次数，最后按开始执行按钮，等待它自动执行完就好了。\n注：请不要在未响应时关闭程序，否则会被强行终止","选择文件","开始执行",'帮助:']
EN = ['File Location:','Set Time:','Number of Cycles:',"Error:",'The number of seconds is an incorrect value.\nPlease try to enter a positive integer.','The number of cycles is an incorrect value.\nPlease try to enter a positive integer.','The file path is empty.','Tip:','Completion of Enforcement!','Select an .exe file','Help','First press the \'Browse\' button to select an exe file.\nThen enter the number of seconds to close the software after opening, then enter the number of cycles, and finally press the start button to wait for it to finish automatically. \nNote: Please do not close the program when it does not respond, otherwise it will be forcibly terminated','Browse','Start','Help:']
SizeList = [320,165]
dll_handle = ctypes.windll.kernel32
sys_lang = hex(dll_handle.GetSystemDefaultUILanguage())
yes = '√'
if sys_lang == "0x804":
    TEXT = CN
    yes1 = yes
    yes2 = "\0"
else:
    TEXT = EN
    yes2 = yes
    yes1 = "\0"
    SizeList = [350,165]
Size = SizeList
def lang1():
    global CN
    global TEXT
    global Size
    global SizeList
    global lbl1
    global lbl2
    global lbl3
    global button1
    global button2
    global button3
    global yes1
    global yes2
    global menubar
    global langmenu
    SizeList = [320,145]
    Size = SizeList
    TEXT = CN
    yes1 = yes
    yes2 = "\0"
    lbl1.destroy()
    lbl1 = tkinter.Label(tk, text=TEXT[0])
    lbl1.grid(column=0, row=0, padx=10, pady=0,columnspan=1)
    lbl2.destroy()
    lbl2 = tkinter.Label(tk, text=TEXT[1])
    lbl2.grid(column=0, row=1, padx=0, pady=0)
    lbl3.destroy()
    lbl3 = tkinter.Label(tk, text=TEXT[2])
    lbl3.grid(column=0, row=2, padx=0, pady=0)
    button1.destroy()
    button1 = tkinter.Button(tk,text=TEXT[12],width=7, height=0,command=click_button1)
    button1.grid(row=0, column=1,padx=(100,0))
    button2.destroy()
    button2 = tkinter.Button(tk,text=TEXT[13],width=10, height=0,command=click_button2)
    button2.grid(row=3, column=1,pady=5,padx=(0,210))
    button3.destroy()
    button3 = tkinter.Button(tk,text=TEXT[10],width=7, height=0,command=click_button3)
    button3.grid(row=3, column=1,columnspan=2)
    menubar.destroy()
    menubar = tkinter.Menu(tk)
    langmenu = tkinter.Menu(menubar,tearoff=False)
    menubar.add_cascade(label="Language", menu=langmenu)
    langmenu.add_command(label="English"+"\0"+yes2,command=lang2)
    langmenu.add_command(label="简体中文"+"\0"+yes1,command=lang1)
    tk.config(menu=menubar)
    tk.resizable(True,True)
    tk.geometry('%dx%d+%d+%d' % (Size[0],Size[1], cen_x,cen_y))
    tk.resizable(False,False)
def lang2():
    global EN
    global TEXT
    global Size
    global SizeList
    global lbl1
    global lbl2
    global lbl3
    global button1
    global button2
    global button3
    global yes1
    global yes2
    global menubar
    global langmenu
    SizeList = [350,145]
    Size = SizeList
    TEXT = EN
    yes2 = yes
    yes1 = "\0"
    lbl1.destroy()
    lbl1 = tkinter.Label(tk, text=TEXT[0])
    lbl1.grid(column=0, row=0, padx=10, pady=0,columnspan=1)
    lbl2.destroy()
    lbl2 = tkinter.Label(tk, text=TEXT[1])
    lbl2.grid(column=0, row=1, padx=0, pady=0)
    lbl3.destroy()
    lbl3 = tkinter.Label(tk, text=TEXT[2])
    lbl3.grid(column=0, row=2, padx=0, pady=0)
    button1.destroy()
    button1 = tkinter.Button(tk,text=TEXT[12],width=7, height=0,command=click_button1)
    button1.grid(row=0, column=1,padx=(100,0))
    button2.destroy()
    button2 = tkinter.Button(tk,text=TEXT[13],width=10, height=0,command=click_button2)
    button2.grid(row=3, column=1,pady=5,padx=(0,210))
    button3.destroy()
    button3 = tkinter.Button(tk,text=TEXT[10],width=7, height=0,command=click_button3)
    button3.grid(row=3, column=1,columnspan=2)
    menubar.destroy()
    menubar = tkinter.Menu(tk)
    langmenu = tkinter.Menu(menubar,tearoff=False)
    menubar.add_cascade(label="Language", menu=langmenu)
    langmenu.add_command(label="English"+"\0"+yes2,command=lang2)
    langmenu.add_command(label="简体中文"+"\0"+yes1,command=lang1)
    tk.config(menu=menubar)
    tk.resizable(True,True)
    tk.geometry('%dx%d+%d+%d' % (Size[0],Size[1], cen_x,cen_y))
    tk.resizable(False,False)
wind_ico = b'AAABAAEAEBAAAAEAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAAAQAAMMOAADDDgAAAAAAAAAAAAD/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////wAAAP8AAAD///////////////////////////8AAAD/AAAA//////////////////////////////////////8AAAD/AAAA////////////////////////////AAAA/wAAAP//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=='
def icon():
    tmp = open("tmp.ico","wb+")  
    tmp.write(base64.b64decode(wind_ico))
    tmp.close()
    tk.iconbitmap("tmp.ico")
    os.remove("tmp.ico")
tk = tkinter.Tk()
tk.title("Atswoo")
icon()
windowX = tk.winfo_screenwidth()
windowY = tk.winfo_screenheight()
cen_x = (windowX-400) / 2
cen_y = (windowY-225) / 2
tk.geometry('%dx%d+%d+%d' % (Size[0],Size[1], cen_x,cen_y))
menubar = tkinter.Menu(tk)
langmenu = tkinter.Menu(menubar,tearoff=False)
menubar.add_cascade(label="Language", menu=langmenu)
langmenu.add_command(label="English"+"\0"+yes2,command=lang2)
langmenu.add_command(label="简体中文"+"\0"+yes1,command=lang1)
tk.resizable(False,False)
tk.config(menu=menubar)
lbl1 = tkinter.Label(tk, text=TEXT[0])
lbl1.grid(column=0, row=0, padx=10, pady=0,columnspan=1)
lbl2 = tkinter.Label(tk, text=TEXT[1])
lbl2.grid(column=0, row=1, padx=0, pady=0)
lbl3 = tkinter.Label(tk, text=TEXT[2])
lbl3.grid(column=0, row=2, padx=0, pady=0)
et1_var = tkinter.StringVar()
et2_var = tkinter.StringVar()
et3_var = tkinter.StringVar()
et1 = tkinter.Entry(tk,textvariable=et1_var,width=20)
et1.grid(row=0, column=1,padx=(0,145),pady=10,columnspan=2)
et2 = tkinter.Entry(tk,textvariable=et2_var,width=5)
et2.grid(row=1, column=1,padx=(0,250),pady=(0,5),columnspan=2)
et3 = tkinter.Entry(tk,textvariable=et3_var,width=5)
et3.grid(row=2, column=1,padx=(0,250),pady=5,columnspan=2)
fpath = ""
def error():
    global ae
    global be
    global fe
    global a
    global b
    try:
        a = et2.get()
        a = int(a)
        if a > 0:
            good = True
            ae = 0
        else:
            tkinter.messagebox.showinfo( TEXT[3], TEXT[4])
            ae = 1
    except ValueError:
        tkinter.messagebox.showinfo( TEXT[3], TEXT[4])
        ae = 1
    try:
        b = et3.get()
        b = int(b)
        if b > 0:
            good = True
            be = 0
        else:
            tkinter.messagebox.showinfo( TEXT[3], TEXT[5])
            be = 1
    except ValueError:
        tkinter.messagebox.showinfo( TEXT[3], TEXT[5])
        be = 1
    if fpath == '':
        tkinter.messagebox.showinfo( TEXT[3], TEXT[6])
        fe = 1
    else:
        fe = 0
def startinit():
    i = 0
    while i < b: 
        win32api.ShellExecute(0, 'open', fpath, '','',1) 
        time.sleep(a)
        p = "\"" + file + "\""
        taskkill = 'taskkill /f /im %s' % p
        subprocess.call(taskkill, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        i += 1
def start():
    error(),
    if ae or be or fe == 1:
        return
    startinit()
    tkinter.messagebox.showinfo( TEXT[7], TEXT[8])
def click_button1():
    global fpath
    global dir
    global file
    fpath = filedialog.askopenfilename(title=TEXT[9], filetypes=[('Executable file', '*.exe'), ('All Files', '*')])
    et1_var.set(fpath)
    dir,file=os.path.split(fpath)
def click_button2():
    start()
def click_button3():
    tkinter.messagebox.showinfo( TEXT[14], TEXT[11])
button1 = tkinter.Button(tk,text=TEXT[12],width=7, height=0,command=click_button1)
button1.grid(row=0, column=1,padx=(100,0))
button2 = tkinter.Button(tk,text=TEXT[13],width=10, height=0,command=click_button2)
button2.grid(row=3, column=1,pady=5,padx=(0,210))
button3 = tkinter.Button(tk,text=TEXT[10],width=7, height=0,command=click_button3)
button3.grid(row=3, column=1,columnspan=2)
tk.mainloop()