import tkinter as tk
from tkinter import ttk
from jsfinance.tktools import FilledButton, StackedFrame
from jsfinance.ui_categoria import CategoryDialog
from pathlib import Path

ASSET_DIR = Path(__file__).parent / Path('assets')

def fake_command(*args):
    print(args)


class Sistema(ttk.Frame):
    def __init__(self, *args, **kwargs):
        ttk.Frame.__init__(self, *args, **kwargs)

        self.create_menu(self.master)
        self.create_widgets()

    def create_menu(self, master):
        menus = (
            'CADASTRAR',
            (
                ("Categorias", lambda: CategoryDialog(master=self)),
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

        main_menu = tk.Menu(master)

        for name, children in zip(menus[:-1:2], menus[1::2]):
            submenu = tk.Menu(main_menu)
            for label, command in children:
                submenu.add_command(label=label, command=command)
            main_menu.add_cascade(label=name, menu=submenu)

        master.config(menu=main_menu)

    def create_widgets(self):
        self.pack(fill=tk.BOTH, expand=True)

        self.img_exit = tk.PhotoImage(file=str(ASSET_DIR / 'exit.gif'))
        self.img_logo = tk.PhotoImage(file=str(ASSET_DIR / 'logo.gif'))

        self.frm_left = StackedFrame(self)
        self.frm_left.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        self.btn_contas = self.frm_left.add_widget(FilledButton, self.frm_left, text='LANÇAMENTOS-DÉBITOS', command=fake_command)
        self.btn_creditos = self.frm_left.add_widget(FilledButton, self.frm_left, text='LANÇAMENTOS-CRÉDITOS', command=fake_command)
        self.btn_sair = self.frm_left.add_widget(ttk.Button, self.frm_left, command=fake_command, image=self.img_exit)
        self.texto_logo = self.frm_left.add_widget(ttk.Label, self.frm_left, text='DESENVOLVIDO POR JS INFORMÁTICA ')
        self.btn_logo = self.frm_left.add_widget(ttk.Label, self.frm_left, image=self.img_logo)

        self.frm_right = StackedFrame(self)
        self.frm_right.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

        self.busca_persomes = self.frm_right.add_widget(FilledButton, self.frm_right, text='LISTAR CONTAS MES ATUAL ',
                                                        command=fake_command)
        self.busca_persomes_paga = self.frm_right.add_widget(FilledButton, self.frm_right, text='CONTAS MES ATUAL PAGAS ',
                                                             command=fake_command)
        self.busca_persomes_aberto = self.frm_right.add_widget(FilledButton, self.frm_right, text='CONTAS MES ATUAL ABERTO ',
                                                               command=fake_command)
        self.btn_busca_Totais = self.frm_right.add_widget(FilledButton, self.frm_right, text='TOTAIS POR TIPO DE PGTO',
                                                          command=fake_command)
        self.btn_busca_conta = self.frm_right.add_widget(FilledButton, self.frm_right, text='LISTAR POR CATEGORIAS',
                                                         command=fake_command)
        self.btn_busca_todos = self.frm_right.add_widget(FilledButton, self.frm_right, text='CONTAS PERSONALIZ.',
                                                         command=fake_command)


