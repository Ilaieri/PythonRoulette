#imports
import os
import sys
import random
import tkinter as tk
#checking if all reqs are installed
def check(module1):
    modulename = module1
    if modulename not in sys.modules:
        os.system('cmd /k'"pip3 install"f"{modulename}")
#running checks on non preinstalled modules
check("sys")
check("tkinter")
#reading config.txt
with open('config.txt') as f:
    contents = f.read()
root=tk.Tk()
canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()
root.title('Python Roulette')
#defining the russian roulette system
def hello ():  
    roulette=random.randint(1,6)
    if roulette==1:
        os.remove(contents)
        label1 = tk.Label(root, text= 'You Lost. Check the file.', fg='Red', font=('helvetica', 12, 'bold'))
        root.after(2000, label1.destroy)
        
    else:
        label1 = tk.Label(root, text= 'You won, for now', fg='green', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 200, window=label1)
    root.after(2000, label1.destroy)
        
button1 = tk.Button(text='Click Me To Play',command=hello, bg='brown',fg='white')
canvas1.create_window(150, 150, window=button1)

root.mainloop()



    
