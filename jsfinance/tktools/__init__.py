import tkinter as tk
from tkinter import ttk
from .widgets import FilledButton, StackedFrame

class SmartEntry(ttk.Entry):
    def __init__(self, master=None, **kw):
        super().__init__(master=master, **kw)

    @property
    def content(self):
        return self.get()

    @content.setter
    def content(self, value):
        self.delete(0, tk.END)
        self.insert(0, value)


class IdVar(tk.IntVar):
    def get(self):
        try:
            value = super().get()
            if isinstance(value, int) and value == 0:
                value = None
        except tk.TclError:
            value = None

        return value
