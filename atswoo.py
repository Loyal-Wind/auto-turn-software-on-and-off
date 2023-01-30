import win32api
import os
import time
import sys
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
fpath = filedialog.askopenfilename(title='选择一个exe文件', filetypes=[('Executable file', '*.exe'), ('All Files', '*')])
if fpath == '':
	print('检测到用户关闭，正在关闭窗口')
	time.sleep(1)
	sys.exit(0)
else:
    print('已选中:', fpath)
    time.sleep(1)
dir,file=os.path.split(fpath)
i = 0
goodinput = False
while not goodinput:
    try:
        a = int(input('请输入打开软件后几秒关闭(默认为3s):') or "3")
        if a > 0:
            goodinput = True
        else:
            print("Error:您输入的不是一个正整数")
    except ValueError:
        print("Error:您输入的不是一个正整数")
goodinput = False
while not goodinput:
    try:
        b = int(input('请输入循环次数(默认2次):') or "2")
        if b > 0:
            goodinput = True
        else:
            print("Error:您输入的不是一个正整数")
    except ValueError:
        print("Error:您输入的不是一个正整数")
while i < b: 
	win32api.ShellExecute(0, 'open', fpath, '','',1) 
	time.sleep(a)
	p = "\"" + file + "\""
	os.system('taskkill /f /im %s' % p)
	i += 1 

print("执行完毕！正在关闭窗口")
time.sleep(1) 
sys.exit(0)