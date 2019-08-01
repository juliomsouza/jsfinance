import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from jsfinance.db import connect
from mysql.connector import errorcode, Error as MysqlError


class CategoryDialog(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.create_widgets()
    
    def create_widgets(self):
        self.idcat = tk.Label(self, text="ID ", fg='black', bg='#CCFFCC')
        self.idcat.grid(row=0, column=0)
        self.editidcat = tk.Entry(self, width=10, bg='lemonchiffon', bd=4)
        self.editidcat.grid(row=0, column=1, sticky=tk.W)
        self.catB = tk.Button(self, text="BUSCAR CATEG.", width=17, font=('Arial', 14, 'bold'), command=self.pesquisar_Cat)
        self.catB.grid(row=0, column=2)
        self.catB.bind("<Return>", self.pesquisar_Cat)
        self.descricao = tk.Label(self, text="DESCRICAO", fg='black', bg='#CCFFCC')
        self.descricao.grid(row=1, column=0)
        self.editdescricao = tk.Entry(self, width=20, bg='lemonchiffon', bd=4)
        self.editdescricao.grid(row=1, column=1, sticky=tk.W)
        self.editdescricao.focus()
        self.obs_cat = tk.Label(self, text='OBSERVAÇÕES', font=('Arial', 16, 'bold'), bg='lightskyblue')
        self.obs_cat.grid(row=2, column=1)
        self.obs_e = tk.Entry(self, width=30, bg='lemonchiffon', bd=4)
        self.obs_e.grid(row=3, column=1)
    
        # ===========================================================================================================================================
        #                                                   BOTÕES                                                                                  =
        # ===========================================================================================================================================
    
        self.grav_cat = tk.Button(self, text='GRAVAR ', pady=2, bg='black', padx=1, bd=2, width=25, height=2,
                               font=('Arial', 12, 'bold'), fg='blue', command=self.gravaCat)  # , state = 'disable')
        self.grav_cat.grid(row=7, column=0)
    
        self.limpa_cat = tk.Button(self, text='LIMPAR ', pady=1, bg='black', padx=2, bd=1, width=25, height=2,
                                font=('Arial', 12, 'bold'), fg='green', command=self.limpa_gravaCat)
        self.limpa_cat.grid(row=7, column=1)
    
        self.boficina = tk.Button(self, text='TODAS CATEGORIAS', pady=1, bg='black', padx=2, bd=1, width=25, height=2,
                               font=('Arial', 12, 'bold'), fg='yellow', command=lambda: CategoryList(self))
        self.boficina.grid(row=8, column=0)
    
        self.sair_categ = tk.Button(self, text='SAIR ', pady=1, bg='black', padx=2, bd=1, width=25, height=2,
                                 font=('Arial', 12, 'bold'), fg='red', command=self.destroy)
        self.sair_categ.grid(row=8, column=1)
    
        self.btn_editar = tk.Button(self, text='ALTERAR', width=20, height=2, bg='black', fg='yellow',
                                 command=self.atualiza_Cat)
        self.btn_editar.grid(row=7, column=2)
    
        self.geometry('890x350+500+500')
        self.title('CADASTRO DE CATEGORIAS')
        self.transient(self.master)
        self.focus_force()
        self.grab_set()
        self.configure(background='#CCFFCC')

    def gravaCat(self):
        cnx = connect()
        cursor = cnx.cursor()

        descricao = self.editdescricao.get().upper()
        if self.editdescricao.get() == '':
            messagebox.showwarning("Erro", "DIGITE A DESCRICAO", parent=self)
        else:
            obs = self.obs_e.get().upper()

            # data = time.strftime('%d/%m/%y %H:%M:%S')

        cursor.execute("INSERT INTO CATEGORIAS (DESC_CAT, OBS_CAT)\
        VALUES ('" + descricao + "','" + obs + "')")

        try:
            cnx.commit()
            # print("Dados gravados com sucesso")
            messagebox.showinfo("SUCESSO", "Dados gravados com sucesso!:)", parent=self)
            self.limpa_gravaCat()

        except MysqlError as err:
            # print("Não conseguiu gravar no banco de dados.:",err)
            messagebox.showrror("Erro ao gravar os dados", err, parent=self)

        cnx.close()

    def limpa_gravaCat(self):  # Mysql
        # self.editlist_ofi.delete(0,END)
        self.editdescricao.delete(0, tk.END)
        self.obs_e.delete(0, tk.END)

        # UPDATE Categorias

    def pesquisar_Cat(self, event=None):
        #self.desabilita_Cat()
        cnx = connect()
        cursor = cnx.cursor()

        cursor.execute("SELECT * FROM CATEGORIAS WHERE ID_CAT = '" + self.editidcat.get() + "' ")

        dadosbanco = cursor.fetchone()
        self.limpa_gravaCat()
        if dadosbanco:
            # self.Limpa_gravar()
            # print(cursor.execute())
            self.editdescricao.insert(0, dadosbanco[1])
            self.obs_e.insert(0, dadosbanco[2])

        cnx.close()

        # UPDATE CATEGORIAS

    def atualiza_Cat(self):
        cnx = connect()
        cursor = cnx.cursor()
        idcat = self.editidcat.get()
        descricao = self.editdescricao.get().upper()
        if self.editdescricao.get() == '':
            messagebox.showwarning("Erro", "DIGITE A DESCRICAO")
        else:

            sql = "UPDATE CATEGORIAS SET DESC_CAT = '" + descricao + "' WHERE ID_CAT = " + idcat
        try:
            cursor.execute(sql)
            cnx.commit()
            # print("Dados gravados com sucesso")
            messagebox.showinfo("Dados Gravados", "Gravação OK! ")
            self.limpa_gravaCat()
            #self.habilita_Cat()

        except MysqlError as err:
            # print("Não conseguiu gravar",err)
            messagebox.showerror("Não conseguiu gravar", err)

        cnx.close()


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
