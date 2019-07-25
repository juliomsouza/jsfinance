# encoding: utf-8
import time;
from tkinter import *
from tkinter.scrolledtext import ScrolledText

from PIL import Image, ImageTk
from pathlib import Path

ASSET_DIR = Path(__file__).parent / Path('assets')

def fake_command(*args):
    print(args)


class JSButton(Button):
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

class StackedFrame(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.top_margin = None

    def _add_expander(self):
        return Frame(self).pack(fill=BOTH, expand=True)

    def add_widget(self, cls, *args, **kwargs):
        if not self.top_margin:
            self.top_margin = self._add_expander()

        widget = cls(*args, **kwargs)
        widget.pack()

        self._add_expander()

        return widget


class Sistema(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

        self.create_menu(self.master)
        self.create_widgets()

    def create_menu(self, master):
        menus = (
            'CADASTRAR',
            (
                ("Categorias", fake_command),
                ("Lançamentos", fake_command),
                ("Faturas Cartôes", fake_command),
                ("Tipos Pagamentos", fake_command),
                ("Sair", master.destroy),
            ),
            'CONSULTAR',
            (
                ("Todas as Contas", fake_command),
                ("Faturas Cartões", fake_command),
                ("Todas as Categorias", fake_command),
                ("Contas/Filtro", fake_command),
                ("Categorias/Fitro", fake_command),
                ("Tipos/Pagamentos", fake_command),
            ),
            'RELATORIOS',
            (
                ("Excel Mês Atual", fake_command),
            ),
            'AJUDA',
            (
                ("VERSAO 1.1", ''),
                ("HELPDESK", fake_command),
                ("MANUAL", ''),
            ),
        )

        main_menu = Menu(master)

        for name, children in zip(menus[:-1:2], menus[1::2]):
            submenu = Menu(main_menu)
            for label, command in children:
                submenu.add_command(label=label, command=command)
            main_menu.add_cascade(label=name, menu=submenu)

        master.config(menu=main_menu)

    def create_widgets(self):
        self.pack()

        self.imagem1 = ImageTk.PhotoImage(file=str(ASSET_DIR / 'exit.gif'))
        self.imagem3 = ImageTk.PhotoImage(file=str(ASSET_DIR / 'logo.gif'))

        self.frame1 = StackedFrame(self, bd=8, relief="raise")
        self.frame1.pack(side=LEFT, expand=True, fill=BOTH)

        self.btn_contas = self.frame1.add_widget(JSButton, self.frame1, text='LANÇAMENTOS-DÉBITOS', command=fake_command)
        self.btn_creditos = self.frame1.add_widget(JSButton, self.frame1, text='LANÇAMENTOS-CRÉDITOS', command=fake_command)
        self.btn_sair = self.frame1.add_widget(Button, self.frame1, pady=1, bg='light blue', padx=1, bd=2, width=120, height=120,
                               command=fake_command, image=self.imagem1)

        self.texto_logo = self.frame1.add_widget(Label, self.frame1, text='DESENVOLVIDO POR JS INFORMÁTICA ', pady=2, bg='RoyalBlue1', padx=2,
                                bd=2, width=47, height=2, font=('Arial', 12, 'bold'), fg='black')

        self.btn_logo = self.frame1.add_widget(Label, self.frame1, text='', pady=1, bg='light blue', padx=1, bd=2, width=427, height=250,
                              image=self.imagem3)


        self.frame2 = StackedFrame(self, bd=8, relief="raise")
        self.frame2.pack(side=RIGHT, expand=True, fill=BOTH)

        self.busca_persomes = self.frame2.add_widget(JSButton, self.frame2, text='LISTAR CONTAS MES ATUAL ',
                                                     command=fake_command)
        self.busca_persomes_paga = self.frame2.add_widget(JSButton, self.frame2, text='CONTAS MES ATUAL PAGAS ',
                                                          command=fake_command)
        self.busca_persomes_aberto = self.frame2.add_widget(JSButton, self.frame2, text='CONTAS MES ATUAL ABERTO ',
                                                            command=fake_command)
        self.btn_busca_Totais = self.frame2.add_widget(JSButton, self.frame2, text='TOTAIS POR TIPO DE PGTO',
                                                       command=fake_command)
        self.btn_busca_conta = self.frame2.add_widget(JSButton, self.frame2, text='LISTAR POR CATEGORIAS',
                                                      command=fake_command)
        self.btn_busca_todos = self.frame2.add_widget(JSButton, self.frame2, text='CONTAS PERSONALIZ.',
                                                      command=fake_command)


