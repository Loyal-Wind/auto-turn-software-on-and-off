import win32api
import os
import time
import sys
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
fpath = filedialog.askopenfilename(title='Select an .exe file', filetypes=[('Executable file', '*.exe'), ('All Files', '*')])
if fpath == '':
	print('User shutdown detected,closing window')
	time.sleep(1)
	sys.exit(0)
else:
    print('Selected:', fpath)
    time.sleep(1)
dir,file=os.path.split(fpath)
i = 0
goodinput = False
while not goodinput:
    try:
        a = int(input('Please enter seconds from opening to close (3s by default):') or "3")
        if a > 0:
            goodinput = True
        else:
            print("Error:The value you entered is not a positive integer")
    except ValueError:
        print("Error:The value you entered is not a positive integer")
goodinput = False
while not goodinput:
    try:
        b = int(input('Please enter the number of cycles (2 by default):') or "2")
        if b > 0:
            goodinput = True
        else:
            print("Error:The value you entered is not a positive integer")
    except ValueError:
        print("Error:The value you entered is not a positive integer")
while i < b: 
	win32api.ShellExecute(0, 'open', fpath, '','',1) 
	time.sleep(a)
	p = "\"" + file + "\""
	os.system('taskkill /f /im %s' % p)
	i += 1 

print("Execution succeeded!Closing window")
time.sleep(1) 
sys.exit(0)