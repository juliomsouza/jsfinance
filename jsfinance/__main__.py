import time
from tkinter import  Tk
from jsfinance.core import Sistema
from jsfinance.ui_main import Sistema as MainWindow

root = Tk()
MainWindow(root)
root.geometry("750x640+540+110")
#root.resizable(0,0)
root.title("JS Financas - " + time.strftime("%d/%m/%Y"))
root.configure(background='#004400')
#root.configure(background='pink')
root.configure(highlightbackground='#CC00CC')
root.configure(highlightcolor='black')
root.mainloop()
