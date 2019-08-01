import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from jsfinance.db import connect, category_get, category_insert, category_update, DoesNotExist
from mysql.connector import errorcode, Error as MysqlError


"""
TODO:
1. Ajustar os nomes dos controles;
2. Eliminar parametros de aparência da instanciação.
3. Extrair a lógica do banco de dentro da janela.
4. Unificar a lógica de insert/update.
5. Criar nosso próprio Entry para simplificar manipulação do conteúdo.
"""

class JSEntry(tk.Entry):
    def __init__(self, master=None, cnf={}, **kw):

        self.apply_default_styles(kw)
        super().__init__(master=master, cnf=cnf, **kw)

    def apply_default_styles(self, kw):
        styles = dict(bg='lemonchiffon', bd=4)

        for key, value in styles.items():
            if key not in kw:
                kw[key] = value

    @property
    def content(self):
        return self.get()

    @content.setter
    def content(self, value):
        self.delete(0, tk.END)
        self.insert(0, value)


class CategoryDialog(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.id = tk.IntVar()
        self.id.set("")
        self.descricao = tk.StringVar()
        self.obs = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        self.lb_idcat = tk.Label(self, text="ID ", fg='black', bg='#CCFFCC')
        self.lb_idcat.grid(row=0, column=0)
        self.tb_idcat = JSEntry(self, width=10, textvariable=self.id)
        self.tb_idcat.grid(row=0, column=1, sticky=tk.W)
        self.bt_buscar = tk.Button(self, text="BUSCAR CATEG.", width=17, font=('Arial', 14, 'bold'), command=self.select)
        self.bt_buscar.grid(row=0, column=2)
        self.bt_buscar.bind("<Return>", self.select)
        self.lb_desc = tk.Label(self, text="DESCRICAO", fg='black', bg='#CCFFCC')
        self.lb_desc.grid(row=1, column=0)
        self.tb_desc = JSEntry(self, width=20, textvariable=self.descricao)
        self.tb_desc.grid(row=1, column=1, sticky=tk.W)
        self.tb_desc.focus()
        self.lb_obs = tk.Label(self, text='OBSERVAÇÕES', font=('Arial', 16, 'bold'), bg='lightskyblue')
        self.lb_obs.grid(row=2, column=1)
        self.tb_obs = JSEntry(self, width=30, textvariable=self.obs)
        self.tb_obs.grid(row=3, column=1)
    
        # ===========================================================================================================================================
        #                                                   BOTÕES                                                                                  =
        # ===========================================================================================================================================
    
        self.bt_insert = tk.Button(self, text='GRAVAR ', pady=2, bg='black', padx=1, bd=2, width=25, height=2,
                               font=('Arial', 12, 'bold'), fg='blue', command=self.insert)  # , state = 'disable')
        self.bt_insert.grid(row=7, column=0)
    
        self.bt_clear = tk.Button(self, text='LIMPAR ', pady=1, bg='black', padx=2, bd=1, width=25, height=2,
                                font=('Arial', 12, 'bold'), fg='green', command=self.clear)
        self.bt_clear.grid(row=7, column=1)
    
        self.bt_list = tk.Button(self, text='TODAS CATEGORIAS', pady=1, bg='black', padx=2, bd=1, width=25, height=2,
                               font=('Arial', 12, 'bold'), fg='yellow', command=lambda: CategoryList(self))
        self.bt_list.grid(row=8, column=0)
    
        self.bt_exit = tk.Button(self, text='SAIR ', pady=1, bg='black', padx=2, bd=1, width=25, height=2,
                                 font=('Arial', 12, 'bold'), fg='red', command=self.destroy)
        self.bt_exit.grid(row=8, column=1)
    
        self.bt_update = tk.Button(self, text='ALTERAR', width=20, height=2, bg='black', fg='yellow',
                                 command=self.update)
        self.bt_update.grid(row=7, column=2)
    
        self.geometry('890x350+500+500')
        self.title('CADASTRO DE CATEGORIAS')
        self.transient(self.master)
        self.focus_force()
        self.grab_set()
        self.configure(background='#CCFFCC')

    def insert(self):
        descricao = self.descricao.get().upper()
        obs = self.obs.get().upper()

        if not descricao:
            messagebox.showwarning("Erro", "DIGITE A DESCRICAO", parent=self)
            return

        try:
            category_insert(descricao, obs)
        except MysqlError as e:
            messagebox.showerror("Erro ao gravar os dados", e)

        messagebox.showinfo("SUCESSO", "Dados gravados com sucesso!:)")


    def select(self, event=None):
        idcat = self.id.get()

        try:
            _, self.tb_desc.content, self.tb_obs.content = category_get(idcat)
        except DoesNotExist as e:
            messagebox.showerror(e.message)

    def update(self):
        idcat = self.id.get()
        descricao = self.descricao.get().upper()

        if not descricao:
            messagebox.showwarning("Erro", "DIGITE A DESCRICAO")
            return

        try:
            category_update(idcat, descricao)
        except MysqlError as e:
            messagebox.showerror("Não conseguiu gravar", e)

        messagebox.showinfo("Dados Gravados", "Gravação OK! ")

    def clear(self):
        self.id.set("")
        self.descricao.set("")
        self.obs.set("")


class CategoryList(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.create_widgets()

    def create_widgets(self):
        self.tree2 = ttk.Treeview(self, column=("column", "column1", "column2",
                                                          "column3"))
        self.tree2.column("#0", minwidth=0, width=0)
        self.tree2.heading("#1", text="IDCAT")
        self.tree2.column("#1", minwidth=0, width=78)
        self.tree2.heading("#2", text="DESCRICAO")
        self.tree2.column("#2", minwidth=0, width=280)
        self.tree2.heading("#3", text="OBSERVAÇÕES")
        self.tree2.column("#3", minwidth=0, width=480)
        self.tree2.column("#4", minwidth=0, width=10)

        self.tree2.configure(height=18)
        self.tree2.grid()
        self.View_Cat()

        self.geometry('860x400+50+50')
        self.title('CONSULTA CATEGORIAS')
        self.transient(self.master)
        self.focus_force()
        self.grab_set()

    def View_Cat(self):# categorias
        cnx = connect()
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM CATEGORIAS ORDER  BY ID_CAT ")
        rows=cursor.fetchall()
        for row in rows:
            '''print(row)'''
            self.tree2.insert("",tk.END, values = row)
        cnx.close()
