import time
from tkinter import  Tk
from tkinter import ttk
#from jsfinance.core import Sistema
from jsfinance.ui_main import Sistema as MainWindow

root = Tk()
MainWindow(root)
root.title("JS Financas - " + time.strftime("%d/%m/%Y"))
s = ttk.Style()
s.theme_use('default')
root.mainloop()
