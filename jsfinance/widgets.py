import tkinter as tk
from tkinter.scrolledtext import ScrolledText


class JSButton(tk.Button):
    def __init__(self, master=None, cnf={}, **kw):

        self.apply_default_styles(kw)
        super().__init__(master=master, cnf=cnf, **kw)

    def pack(self, **kwargs):
        kwargs['fill'] = 'x'
        return super().pack(**kwargs)

    def apply_default_styles(self, kw):
        styles = dict(bg='RoyalBlue1', bd=2,
                      font=('Arial', 12, 'bold'), fg='black')

        for key, value in styles.items():
            if key not in kw:
                kw[key] = value

# class DebugWindow:
#     def __init__(self):
#         self.t = ScrolledText(self.frame2)
#         self.t.pack(side=BOTTOM, fill=BOTH, expand=True)
#
#         def gambi():
#             exec(self.t.get(1.0, END))
#
#         self.b = JSButton(self.frame2, text='Run', command=gambi)
#         self.b.pack(side=BOTTOM)

class StackedFrame(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.top_margin = None

    def _add_expander(self):
        return tk.Frame(self).pack(fill=tk.BOTH, expand=True)

    def add_widget(self, cls, *args, **kwargs):
        if not self.top_margin:
            self.top_margin = self._add_expander()

        widget = cls(*args, **kwargs)
        widget.pack()

        self._add_expander()

        return widget
