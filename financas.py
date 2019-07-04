# encoding: utf-8
import mysql.connector
from mysql.connector import errorcode
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser
import datetime
import os
import sys
import time;
import xlwt
#import csv


def connect():
    return mysql.connector.connect(
        user='root',
        password='',
        host='127.0.0.1',
        database='FINANCAS',
        port='3306'
    )


def load_image(filename):
    image = Image.open(filename)
    photo = ImageTk.PhotoImage(image)
    return photo


class Sistema():
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        self.menu = Menu(master)
        self.menuCadastro = Menu(self.menu)
        self.menuCadastro.add_command(label = "CATEGORIAS", command = self.cad_Cat)
        self.menuCadastro.add_command(label = "LANCAMENTOS", command = self.cadastraContas)
        self.menuCadastro.add_command(label = "FATURAS CARTOES", command = self.cad_Faturas)
        self.menuCadastro.add_command(label = "TIPOS PAGAMENTOS", command = self.cad_Tipos_Pgto)
        self.menuCadastro.add_command(label = "Sair",command = root.destroy)
        self.menu.add_cascade(label='CADASTRAR', menu = self.menuCadastro)


        self.menuConsulta = Menu(self.menu)
        self.menuConsulta.add_command(label = "TODAS AS CONTAS", command = self.pesquisa_Contas)
        self.menuConsulta.add_command(label = "FATURAS CARTÕES")#, command = self.cad_Faturas)
        self.menuConsulta.add_command(label = "TODAS AS CATEGORIAS", command = self.pesquisa_Cat)
        self.menuConsulta.add_command(label = "CONTAS/FILTRO", command = self.lista_Personalizada)
        self.menuConsulta.add_command(label = "CATEGORIAS/FILTRO", command = self.lista_PersonaCat)
        self.menuConsulta.add_command(label = "TIPOS DE PAGAMENTOS", command = self.lista_tipos_pgto)
        self.menu.add_cascade(label='CONSULTAR', menu=self.menuConsulta)

        self.menuSaida = Menu(self.menu)
        self.menuSaida.add_command(label = "EXCEL MES ATUAL", command = self.gera_planilha)
        self.menu.add_cascade(label='RELATORIOS', menu = self.menuSaida)

        self.menuEdita = Menu(self.menu)
        self.menuEdita.add_command(label = "VERSAO 1.1")
        self.menuEdita.add_command(label = "HELPDESK", command = self.help_Desk)
        self.menuEdita.add_command(label = "MANUAL")
        self.menu.add_cascade(label='AJUDA', menu = self.menuEdita)

        master.config(menu = self.menu)


        Date1 = StringVar()
        Time1 = StringVar()

        Date1.set(time.strftime("%d/%m/%Y"))
        
        
        self.lblDate = Label(master, textvariable = Date1, font=('arial',18,'bold'),padx=1 ,pady=1,
                        bd=10, bg="#004400",fg="Cornsilk",justify=LEFT,width = 20)
        self.lblDate.pack()

        self.imagem1 = load_image('Button-exit-icon.png')
        self.imagem3 = load_image('logo.png')
        
        
        self.frame1 = Frame(master, width = 450, height = 600, bd = 8,relief = "raise")
        self.frame1.pack(side = LEFT)

        self.frame2 = Frame(master, width = 300, height = 600, bd = 8,relief = "raise")
        self.frame2.pack(side = RIGHT)

     
        self.busca_persomes = Button(self.frame2, text ='LISTAR CONTAS MES ATUAL ',pady=1,bg ='RoyalBlue1', padx=1,bd=2, width = 30, height = 2,
                          font = ('Arial', 12,'bold'), fg ='black', command = self.pesquisa_Contas_mes)
        self.busca_persomes.place(x = 0, y=0)

        self.busca_persomes_paga = Button(self.frame2, text ='CONTAS MES ATUAL PAGAS ',pady=1,bg ='RoyalBlue1', padx=1,bd=2, width = 30, height = 2,
                          font = ('Arial', 12,'bold'), fg ='black', command = self.pesquisa_Contas_mes_pagas)
        self.busca_persomes_paga.place(x = 0, y=60)

        self.busca_persomes_aberto = Button(self.frame2, text ='CONTAS MES ATUAL ABERTO ',pady=1,bg ='RoyalBlue1', padx=1,bd=2, width = 30, height = 2,
                          font = ('Arial', 12,'bold'), fg ='black', command = self.pesquisa_Contas_mes_Aberto)
        self.busca_persomes_aberto.place(x = 0, y=120)

        self.btn_contas = Button(self.frame1, text='LANÇAMENTOS-DÉBITOS', pady=1,bg ='RoyalBlue1', padx=1,bd=2, width = 30, height = 2,
                          font = ('Arial', 12,'bold'), fg ='black',command= self.cadastraContas)
        self.btn_contas.place(x = 0, y=0)

        self.btn_creditos = Button(self.frame1, text='LANÇAMENTOS-CRÉDITOS', pady=1,bg ='RoyalBlue1', padx=1,bd=2, width = 30, height = 2,
                          font = ('Arial', 12,'bold'), fg ='black',command= self.add_entradas)
        self.btn_creditos.place(x = 0, y=50)


        self.btn_sair = Button(self.frame1, pady=1,bg ='light blue', padx=1,bd=2, width = 120, height = 120,
                             command=root.destroy, image=self.imagem1)
        self.btn_sair.place(x= 305, y=0)
        

        self.texto_logo = Label(self.frame1, text='DESENVOLVIDO POR JS INFORMÁTICA ',pady=2,bg ='RoyalBlue1', padx=2,bd=2, width = 47, height = 2,
                          font = ('Arial', 12,'bold'), fg ='black')
        self.texto_logo.place(x=0, y=270)
        self.btn_logo = Label(self.frame1, text='', pady=1,bg ='light blue', padx=1,bd=2, width = 427, height = 250, image=self.imagem3)
        self.btn_logo.place(x= 0, y=317)
        

        self.btn_busca_Totais = Button(self.frame2, text='TOTAIS POR TIPO DE PGTO',bg='RoyalBlue1',pady=1,padx=1,bd=2, width = 30, height = 2,
                          font = ('Arial', 12,'bold'), fg ='black', command = self.lista_Totais_pgto)
        self.btn_busca_Totais.place(x = 0, y=180)
        
        self.btn_busca_conta = Button(self.frame2, text='LISTAR POR CATEGORIAS',bg='RoyalBlue1',pady=1,padx=1,bd=2, width = 30, height = 2,
                          font = ('Arial', 12,'bold'), fg ='black',command = self.lista_Personalizada_Cat)
        self.btn_busca_conta.place(x = 0, y=240)

        self.btn_busca_todos = Button(self.frame2, text='CONTAS PERSONALIZ.',bg='RoyalBlue1',pady=1,padx=1,bd=2, width = 30, height = 2,
                          font = ('Arial', 12,'bold'), fg ='black', command = self.lista_Personalizada)
        self.btn_busca_todos.place(x = 0, y = 300)


    
    def help_Desk(self):
        url = "http://192.168.10.90/glpi/"
        webbrowser.open(url)
        
    def ultimo_registro(self):
        cnx = connect()
        
        cursor = cnx.cursor()
        
        try:
            cursor.execute("SELECT MAX(IDCONTA) +1 FROM CONTAS_PAGAR")
            dadosbanco = cursor.fetchone()
            #print(cursor.execute)
            if dadosbanco:
               self.id_contae.insert(0,dadosbanco[0])
               #self.desabilitaGravar()
                        
        except mysql.connector.Error as err:
            messagebox.showerror("Erro ao buscar ID",err)

            cnx.close()        

    def cadastraContas(self,id_conta=None):
        self.tela1 = Toplevel()
        self.id_conta = Label(self.tela1, text ='IDCONTA :',font=('Arial',16, 'bold'),bg='light blue',relief=SUNKEN)
        self.id_conta.place(x = 0, y = 0)
   
        self.id_contae = Entry(self.tela1,width = 10,bg='lemonchiffon',bd=4)
        self.id_contae.place(x = 140, y = 0)


        self.btn_buscar = Button(self.tela1, text='BUSCAR CONTA',bg='light blue')
        self.btn_buscar.place(x = 270, y = 0)
        self.btn_buscar.bind("<Return>", self.pesquisar_Contas)
        
        self.editcategoria = Entry(self.tela1,width = 20,bg='lemonchiffon',bd=4)
        self.editcategoria.place(x = 440, y = 0)
        self.cat = Button(self.tela1, text="BUSCAR CATEG.", bg='light blue')
        self.cat.place(x = 660, y = 0)
        self.cat.bind("<Return>", self.Completar)
        
        
        #self.Proximo_Id()
        



        self.idcat = Label(self.tela1, text ='ID.CATEG.:',font=('Arial',16, 'bold'),bg='light blue')
        self.idcat.place(x = 0, y = 50)

        self.id_cat = Entry(self.tela1,width = 10,bg='lemonchiffon',bd=4)
        self.id_cat.place(x = 140, y = 50)
        
        self.cat = Label(self.tela1, text ='CATEGORIA ',font=('Arial',16, 'bold'),bg='light blue')
        self.cat.place(x = 270, y = 50)

                              

    
        self.categoria = Entry(self.tela1,width = 20,bg='lemonchiffon',bd=4)
        self.categoria.place(x = 440, y = 50)


        self.valorconta = Label(self.tela1, text ='VALOR :',font=('Arial',16, 'bold'),bg='light blue')
        self.valorconta.place(x = 0, y = 100)

        self.valorcontae = Entry(self.tela1,width = 10,bg='lemonchiffon',bd=4)
        self.valorcontae.place(x = 140, y = 100)

        self.data_compra = Label(self.tela1, text ='DATA COMPRA ',font=('Arial',16, 'bold'),bg='light blue')
        self.data_compra.place(x = 270, y = 100)

        self.data_comprae = Entry(self.tela1,width = 20,bg='lemonchiffon',bd=4)
        self.data_comprae.place(x = 440, y = 100)

        self.venc = Label(self.tela1, text ='VENCTO ',font=('Arial',16, 'bold'),bg='light blue')
        self.venc.place(x = 660, y = 100)

        self.vence = Entry(self.tela1,width = 20,bg='lemonchiffon',bd=4)
        self.vence.place(x = 770, y = 100)

        self.pago = Label(self.tela1, text ='PAGO ',font=('Arial',16, 'bold'),bg='light blue')
        self.pago.place(x = 0, y = 150)

        self.combo1 = ttk.Combobox(self.tela1, height= 4,width = 10)
        self.combo1['values']=('SIM','NAO')
        self.combo1.current(1)
        self.combo1.place(x = 140, y = 150)


        self.data_pgto = Label(self.tela1, text ='DATA PGTO ',font=('Arial',16, 'bold'),bg='light blue')
        self.data_pgto.place(x = 270, y = 150)

        self.data_pgtoe = Entry(self.tela1,width = 20,bg='lemonchiffon',bd=4)
        self.data_pgtoe.place(x = 440, y = 150)

        self.tipo_pgto = Label(self.tela1, text ='TIPO PGTO ',font=('Arial',16, 'bold'),bg='light blue')
        
        self.tipo_pgto.place(x = 0, y = 200)

        self.combo = ttk.Combobox(self.tela1, height= 4,width = 25)
        self.combo['values']= self.list_pgto()
        self.combo.current(0)
        self.combo.place(x = 140, y = 205)

        self.observa = Label(self.tela1, text='OBSERVAÇÕES',font=('Arial',16, 'bold'),bg='lightskyblue')
        self.observa.place(x = 20, y =250)

        self.observae =  Entry(self.tela1,width = 30,bg='lemonchiffon',bd=4)
        self.observae.place(x = 5,y = 280)
        #self.obs.get(1.0,END)
        

    # ===========================================================================================================================================
    #                                                   BOTÕES                                                                                  =
    # =========================================================================================================================================== 

        
        self.btn_gravar = Button(self.tela1, text='Gravar',width = 20,height = 2,bg='green', command = self.grav_contas)
        self.btn_gravar.place(x = 0, y = 390)

        self.btn_busca_forn = Button(self.tela1, text='LIMPAR',width = 20,height = 2,bg='yellow', command = self.Limpa_gravar_Limpa_Id)
        self.btn_busca_forn.place(x = 220, y = 390)

        self.btn_busca_todos = Button(self.tela1, text='CONTAS PERSONALIZ.',width = 20,height = 2,bg='yellow', command = self.lista_Personalizada)
        self.btn_busca_todos.place(x = 0, y = 450)

        self.btn_busca_forn = Button(self.tela1, text='CATEGORIAS',width = 20,height = 2,bg='BLUE', command = self.pesquisa_Cat)
        self.btn_busca_forn.place(x = 220, y = 450)

        self.btn_atualiza = Button(self.tela1, text='ALTERAR',width = 20,height = 2,bg='skyblue',command = self.atualiza_Contas, state = 'disable')# command = self.atualiza_Contas)
        self.btn_atualiza.place(x = 440, y = 390)

        self.btn_sair = Button(self.tela1, text='SAIR',width = 20,height = 2,bg='red', command = self.tela1.destroy)
        self.btn_sair.place(x = 440, y = 450)

        self.btn_delete_conta = Button(self.tela1, text='DELETAR', width = 20,height = 6, command = self.deletar_conta, state = 'disable')
        self.btn_delete_conta.place(x = 680, y = 390)
        
        self.tela1.geometry("950x550+250+500")
        self.tela1.title("Cadastro de Contas")
        self.tela1.configure(background='light blue')
        self.tela1.transient(root)
        self.tela1.grab_set()
        if id_conta:
            self.id_contae.insert(0,id_conta)
            self.pesquisar_Contas(None)
            self.consulta_mes.destroy()
        else:
            self.Proximo_Id()
        
    def Proximo_Id(self):
        cnx = connect()
        
        cursor = cnx.cursor()
        
        try:
            cursor.execute("SELECT MAX(IDCONTA) +1 FROM CONTAS_PAGAR")
            dadosbanco = cursor.fetchone()
            #print(cursor.execute)
            if dadosbanco:
               self.id_contae.insert(0,dadosbanco[0])
               #self.desabilitaGravar()
                        
        except mysql.connector.Error as err:
            messagebox.showerror("Erro ao buscar ID",err)

            cnx.close()
            

    def list_pgto(self):
        cnx = connect()
        cursor = cnx.cursor()
        cursor.execute("SELECT DESC_PGTO FROM TIPO_PAGTO")
        result = []
        #cursor = cursor.fetchall()
        for i in cursor.fetchall():
            result.append(i[0])
           
            #print(i)
        return result
        
        cnx.close()
        
            
   
    
    def grav_contas(self):
        self.desabilita_deletar_conta()
        cnx = connect()
        cursor = cnx.cursor()

        idcat = self.id_cat.get()
        if self.id_cat.get() == '':
            messagebox.showwarning("Erro", "CAMPO CÓDIGO DA CATEGORIA VAZIO")
        else:
            #forne = self.forne.get()
            valorcontae = self.valorcontae.get()
            if self.valorcontae.get() == '':
                messagebox.showwarning("Erro", "DIGITE O VALOR",parent=self.tela1)
            else:
                data_compra = self.data_comprae.get()
                vence = self.vence.get()
                pago = self.combo1.get().upper()
                #pago = self.pagoe.get().upper()
                data_pgto = self.data_pgtoe.get()
                tipo_pagto = self.combo.get().upper()
                #tipo_pgto =  self.tipo_pgtoe.get().upper()
                #pago = self.combo.get()
                obs = self.observae.get().upper()
        
        
                       
        cursor.execute("INSERT INTO CONTAS_PAGAR (ID_CAT,VALOR,DATA_COMPRA,DATA_VENCIMENTO,PAGO,DATA_PGTO,TIPO_PGTO,OBS) VALUES('"+idcat+"','"+valorcontae+"','"+data_compra+"','"+vence+"','"+pago+"','"+data_pgto+"','"+tipo_pagto+"','"+obs+"')")

        try:
            cnx.commit()
            #print("Dados gravados com sucesso")
            messagebox.showinfo("Dados Gravados", "Gravação OK! ",parent=self.tela1)
            #self.Limpa_gravar()
            self.Limpa_gravar_Limpa_Id()
            self.Proximo_Id()
            
            
        except mysql.connector.Error as err:
            #print("Não conseguiu gravar",err)
            messagebox.showerror("Não conseguiu gravar",err) 

        cnx.close()

           

    def Limpa_gravar(self):
        self.id_cat.delete(0,END)
        self.valorcontae.delete(0,END)
        self.data_comprae.delete(0,END)
        self.categoria.delete(0,END)
        self.vence.delete(0,END)
        self.combo1.delete(0, END)
        self.data_pgtoe.delete(0, END)
        self.combo.delete(0, END)
        self.observae.delete(0, END)

    def Limpa_gravar_Limpa_Id(self):
        self.desabilita_alterar()
        self.desabilita_deletar_conta()
        self.habilitaGravar()
        self.Proximo_Id()
        self.id_contae.delete(0,END)
        self.categoria.delete(0, END)
        self.id_cat.delete(0,END)
        self.valorcontae.delete(0,END)
        self.data_comprae.delete(0,END)
        self.editcategoria.delete(0,END)
        self.vence.delete(0,END)
        self.combo1.delete(0, END)
        self.data_pgtoe.delete(0, END)
        self.combo.delete(0, END)
        self.observae.delete(0, END)    
        
    def View_Contas(self):
  
        cnx = connect()
        cursor = cnx.cursor()
        cursor.execute("SELECT C.IDCONTA,C.ID_CAT, F.DESC_CAT, C.VALOR,C.DATA_COMPRA,DATA_VENCIMENTO,C.PAGO,C.DATA_PGTO,C.TIPO_PGTO,C.OBS FROM CONTAS_PAGAR \
                        AS C INNER JOIN CATEGORIAS AS F ON C.ID_CAT=F.ID_CAT ORDER BY C.IDCONTA")
        rows=cursor.fetchall()
        for row in rows:
            '''print(row)'''
            self.tree1.insert("",END, values = row)
        cnx.close()    

        
    def pesquisa_Contas(self):
        self.consulta1 = Toplevel()
        self.tree1= ttk.Treeview(self.consulta1, column=("column", "column1","column2",
                                                       "column3","column4","column5",
                                                         "column6","column7","column8",
                                                         "column9","column10"))

        
        self.tree1.column("#0",minwidth=0,width=0)
        self.tree1.heading("#1", text="IDCONTA")
        self.tree1.column("#1", minwidth=0,width=80)
        self.tree1.heading("#2", text="ID_CAT")
        self.tree1.column("#2", minwidth=0,width=80)
        self.tree1.heading("#3", text="CATEG.")
        self.tree1.column("#3", minwidth=0,width=280)        
        self.tree1.heading("#4", text="VALOR")
        self.tree1.column("#4", minwidth=0,width=90)
        self.tree1.heading("#5", text="DATA_COMPRA.")
        self.tree1.column("#5", minwidth=0,width=110)
        self.tree1.heading("#6", text="VENCIMENTO")
        self.tree1.column("#6", minwidth=0,width=110)
        self.tree1.heading("#7", text="PAGO")
        self.tree1.column("#7", minwidth=0,width=80)
        self.tree1.heading("#8", text="DATA_PGTO.")
        self.tree1.column("#8", minwidth=0,width=110)
        self.tree1.heading("#9", text="TIPO_PGTO.")
        self.tree1.column("#9", minwidth=0,width=160)
        self.tree1.heading("#10", text="OBS.")
        self.tree1.column("#10", minwidth=0,width=320)
##        self.tree1.column("#11",minwidth=0,width=0)

        self.tree1.configure(height=28)
        self.tree1.grid()
        self.View_Contas()

        
        self.consulta1.geometry('1580x760')
        self.consulta1.title('CONSULTA TODAS AS CONTAS')
        self.consulta1.transient(root)
        self.consulta1.focus_force()
        self.consulta1.grab_set()

   
        

    def Completar(self, event):#TRAZ A CATEGORIA
        self.id_cat.delete(0,END)
        self.categoria.delete(0,END)
        cnx = connect()
        cursor = cnx.cursor()
        
        try:
            cursor.execute("SELECT ID_CAT, DESC_CAT FROM CATEGORIAS WHERE DESC_CAT  LIKE '%"+ self.editcategoria.get()+"%' ")
            dadosbanco = cursor.fetchone()
            #print(cursor.execute)
            if dadosbanco:
               self.id_cat.insert(0,dadosbanco[0]) 
               self.categoria.insert(0,dadosbanco[1])
               self.valorcontae.focus_force()
            
        except mysql.connector.Error as err:
            messagebox.showerror("Erro ao buscar Categoria",err)

            cnx.close()

    #    PAGAR CONTA
    def atualiza_Contas(self):
      
        cnx = connect()
        cursor = cnx.cursor()
        idconta = self.id_contae.get()
        valorconta = self.valorcontae.get()
        pago = self.combo1.get().upper()
        data_compra = self.data_comprae.get()
        data_vence = self.vence.get()
        data_pagto =  self.data_pgtoe.get()
        tipo_pgto = self.combo.get().upper()
        obs = self.observae.get().upper()
                    
        
        sql = "UPDATE CONTAS_PAGAR SET VALOR ='"+valorconta+"',PAGO = '"+pago+"', DATA_COMPRA = '"+data_compra+"',DATA_VENCIMENTO = '"+data_vence+"',\
                                                    DATA_PGTO = '"+data_pagto+"',TIPO_PGTO = '"+tipo_pgto+"', OBS = '"+obs+"' WHERE IDCONTA = "+idconta
        
        try:                     
            cursor.execute(sql)                
            cnx.commit()
            #print("Dados gravados com sucesso")
            messagebox.showinfo("Dados Gravados", "Gravação OK! ")#,parent=self.tela1)
            self.Limpa_gravar()
            self.desabilita_deletar_conta()
            
        except mysql.connector.Error as err:
            #print("Não conseguiu gravar",err)
            messagebox.showerror("Não conseguiu gravar",err)#,parent=tela1) 

            cnx.close()
    # UPDATE CONTAS
    def pesquisar_Contas(self,event):
        self.desabilitaGravar()
        self.habilita_alterar()
        self.habilita_deletar_conta()
        cnx = connect()
        cursor = cnx.cursor()
        
        cursor.execute("SELECT C.ID_CAT,F.DESC_CAT,C.VALOR, C.DATA_COMPRA,C.DATA_VENCIMENTO,C.PAGO,C.DATA_PGTO,C.TIPO_PGTO, C.OBS FROM \
                        CONTAS_PAGAR AS C INNER JOIN CATEGORIAS AS F ON C.ID_CAT=F.ID_CAT WHERE IDCONTA = '"+self.id_contae.get()+"' ")
        
        dadosbanco = cursor.fetchone()
        if dadosbanco:
            self.Limpa_gravar()
            #print(cursor.execute())
            self.id_cat.insert(0, dadosbanco[0])
            self.categoria.insert(0, dadosbanco[1]) 
            self.valorcontae.insert(0, dadosbanco[2])
            self.data_comprae.insert(0, dadosbanco[3])
            self.vence.insert(0, dadosbanco[4])
            self.combo1.insert(0, dadosbanco[5])
            self.data_pgtoe.insert(0, dadosbanco[6])
            self.combo.insert(0, dadosbanco[7])
            self.observae.insert(0, dadosbanco[8])
        cnx.close()    

    def deletar_conta(self):
        self.desabilitaGravar()
        cnx = connect()
        cursor = cnx.cursor()
        
        sql = "DELETE FROM CONTAS_PAGAR WHERE IDCONTA = '"+self.id_contae.get()+"' "

        try:                     
            cursor.execute(sql)                
            cnx.commit()
            #print("Dados gravados com sucesso")
            messagebox.showinfo("DADOS APAGADOS", "DELETE OK! ",parent=self.tela1)
            self. Limpa_gravar_Limpa_Id()
            
        except mysql.connector.Error as err:
            #print("Não conseguiu gravar",err)
            messagebox.showerror("NÃO CONSEGUIU DELETAR",err,parent=tela1) 
        
        
        cnx.close()    

    def habilita_deletar_conta(self):
        self.btn_delete_conta = Button(self.tela1, text='DELETAR',width = 20,height = 6,bg='red', command = self.deletar_conta, state = 'normal')
        self.btn_delete_conta.place(x = 680, y = 390)

    def desabilita_deletar_conta(self):
        self.btn_delete_conta = Button(self.tela1, text='DELETAR',width = 20,height = 6,bg='red', command = self.deletar_conta, state = 'disable')
        self.btn_delete_conta.place(x = 680, y = 390)

    def habilita_alterar(self):
        self.btn_atualiza = Button(self.tela1, text='ALTERAR',width = 20,height = 2,bg='skyblue',command = self.atualiza_Contas, state = 'normal')# command = self.atualiza_Contas)
        self.btn_atualiza.place(x = 440, y = 390)

    def desabilita_alterar(self):
        self.btn_atualiza = Button(self.tela1, text='ALTERAR',width = 20,height = 2,bg='skyblue',command = self.atualiza_Contas, state = 'disable')
        self.btn_atualiza.place(x = 440, y = 390)

    def desabilitaGravar(self):
        self.btn_gravar = Button(self.tela1, text='Gravar',width = 20,height = 2,bg='green', command = self.grav_contas, state = 'disable')
        self.btn_gravar.place(x = 0, y = 390)
        

    def habilitaGravar(self):
        self.btn_gravar = Button(self.tela1, text='Gravar',width = 20,height = 2,bg='green', command = self.grav_contas, state = 'normal')
        self.btn_gravar.place(x = 0, y = 390)    
                     

   

    # PESQUISA CONTAS DO MÊS ATUAL NA TELA PRINCIPAL

    def View_Contas_Mes(self):
  
        cnx = connect()
        cursor = cnx.cursor()
        #cursor.execute("SELECT * FROM CONTAS_PAGAR ORDER BY IDCONTA ")
        cursor.execute("SELECT C.IDCONTA,C.ID_CAT, F.DESC_CAT, C.VALOR,C.DATA_COMPRA,DATA_VENCIMENTO,C.PAGO,C.DATA_PGTO,C.TIPO_PGTO,C.OBS FROM CONTAS_PAGAR \
                        AS C INNER JOIN CATEGORIAS AS F ON C.ID_CAT=F.ID_CAT WHERE  MONTH(C.DATA_VENCIMENTO) = MONTH(NOW()) ORDER BY C.DATA_VENCIMENTO" )
        rows=cursor.fetchall()
        for row in rows:
            '''print(row)'''
            self.tree5.insert("",END, values = row)
        cnx.close()    

        
    def pesquisa_Contas_mes(self):
        ''' TRAZ TODAS AS CONTAS DO MÊS '''
        self.consulta_mes = Toplevel()
        cnx = connect()
        cursor = cnx.cursor()
        cursor.execute("SELECT SUM(VALOR) FROM CONTAS_PAGAR WHERE  MONTH(DATA_VENCIMENTO) = MONTH(NOW())")
        row=cursor.fetchone()        
         
        if row:
            self.total_mes = Label(self.consulta_mes, text = 'TOTAL R$ ' + str(row[0]),font=('arial 22 bold'),fg='red')
            self.total_mes.grid()
                  
        cnx.close()
        
        self.tree5= ttk.Treeview(self.consulta_mes, column=("column", "column1","column2",
                                                       "column3","column4","column5","column6","column7","column8","column9","column10"))
        self.tree5.column("#0",minwidth=0,width=0)
        self.tree5.heading("#1", text="IDCONTA")
        self.tree5.column("#1", minwidth=0,width=80)
        self.tree5.heading("#2", text="ID_CAT")
        self.tree5.column("#2", minwidth=0,width=80)
        self.tree5.heading("#3", text="CATEG.")
        self.tree5.column("#3", minwidth=0,width=280)        
        self.tree5.heading("#4", text="VALOR")
        self.tree5.column("#4", minwidth=0,width=90)
        self.tree5.heading("#5", text="DATA_COMPRA")
        self.tree5.column("#5", minwidth=0,width=110)
        self.tree5.heading("#6", text="VENCIMENTO")
        self.tree5.column("#6", minwidth=0,width=110)
        self.tree5.heading("#7", text="PAGO")
        self.tree5.column("#7", minwidth=0,width=80)
        self.tree5.heading("#8", text="DATA_PGTO.")
        self.tree5.column("#8", minwidth=0,width=110)
        self.tree5.heading("#9", text="TIPO_PGTO.")
        self.tree5.column("#9", minwidth=0,width=200)
        self.tree5.heading("#10", text="OBS.")
        self.tree5.column("#10", minwidth=0,width=280)
        self.tree5.column("#11",minwidth=0,width=0)

        self.tree5.configure(height=28)
        self.tree5.grid()
        self.tree5.bind("<Double-1>", self.treeDoubleClick)
        #self.tree5.bind("<Double-1>",lambda e:print(self.tree5.selection()[0]))
        self.View_Contas_Mes()
       
        
        self.consulta_mes.geometry('1480x680')
        self.consulta_mes.title('CONSULTA CONTAS DO MES')
        self.consulta_mes.transient(root)
        self.consulta_mes.focus_force()
        self.consulta_mes.grab_set()

    def treeDoubleClick(self, event):
        item = self.tree5.selection()[0]
        id_conta = self.tree5.item(item,"values")[0]
        self.cadastraContas(id_conta=id_conta)
        
        

    

    def View_Contas_Mes_Pagas(self):
        ''' PESQUISA CONTAS DO MÊS ATUAL NA TELA PRINCIPAL PAGAS '''

        cnx = connect()
        cursor = cnx.cursor()
        cursor.execute("SELECT C.IDCONTA,C.ID_CAT, F.DESC_CAT, C.VALOR,C.DATA_COMPRA,DATA_VENCIMENTO,C.PAGO,C.DATA_PGTO,C.TIPO_PGTO,C.OBS FROM CONTAS_PAGAR \
                        AS C INNER JOIN CATEGORIAS AS F ON C.ID_CAT=F.ID_CAT WHERE  MONTH(C.DATA_VENCIMENTO) = MONTH(NOW()) AND C.PAGO ='SIM'")
        rows=cursor.fetchall()
        for row in rows:
            ''' print(row)
            '''
            self.tree6.insert("",END, values = row)
        cnx.close()    

        
    def pesquisa_Contas_mes_pagas(self):
        self.consulta_mes_paga = Toplevel()
        cnx = connect()
        cursor = cnx.cursor()
        #cursor.execute("SELECT * FROM CONTAS_PAGAR ORDER BY IDCONTA ")
        cursor.execute("SELECT SUM(VALOR) FROM CONTAS_PAGAR WHERE  MONTH(DATA_VENCIMENTO) = MONTH(NOW()) AND PAGO ='SIM'")

        row=cursor.fetchone()
             
         
        if row:
            self.total_mes_pago = Label(self.consulta_mes_paga, text = 'TOTAL R$ ' + str(row[0]),font=('arial 22 bold'),fg='red')
            self.total_mes_pago.grid()#(row = 0, column = 1)
                  
        cnx.close()
        
       
        self.tree6= ttk.Treeview(self.consulta_mes_paga, column=("column", "column1","column2",
                                                       "column3","column4","column5","column6","column7","column8","column9","column10"))#,"column11"))
        self.tree6.column("#0",minwidth=0,width=0)
        self.tree6.heading("#1", text="IDCONTA")
        self.tree6.column("#1", minwidth=0,width=60)
        self.tree6.heading("#2", text="ID_CAT")
        self.tree6.column("#2", minwidth=0,width=60)
        self.tree6.heading("#3", text="CATEG.")
        self.tree6.column("#3", minwidth=0,width=260)        
        self.tree6.heading("#4", text="VALOR")
        self.tree6.column("#4", minwidth=0,width=90)
        self.tree6.heading("#5", text="DATA_COMPRA")
        self.tree6.column("#5", minwidth=0,width=110)
        self.tree6.heading("#6", text="VENCIMENTO")
        self.tree6.column("#6", minwidth=0,width=110)
        self.tree6.heading("#7", text="PAGO")
        self.tree6.column("#7", minwidth=0,width=60)
        self.tree6.heading("#8", text="DATA_PGTO.")
        self.tree6.column("#8", minwidth=0,width=110)
        self.tree6.heading("#9", text="TIPO_PGTO.")
        self.tree6.column("#9", minwidth=0,width=200)
        self.tree6.heading("#10", text="OBS.")
        self.tree6.column("#10", minwidth=0,width=280)
        self.tree6.column("#11",minwidth=0,width=0)

        self.tree6.configure(height=28)
        self.tree6.grid()
        self.View_Contas_Mes_Pagas()
        
       
        
        self.consulta_mes_paga.geometry('1450x798+100+50')
        self.consulta_mes_paga.title('CONSULTA CONTAS DO MES PAGAS')
        self.consulta_mes_paga.transient(root)
        self.consulta_mes_paga.focus_force()
        self.consulta_mes_paga.grab_set()


    # PESQUISA CONTAS DO MÊS ATUAL NA TELA PRINCIPAL EM ABERTO

    def View_Contas_Mes_Aberto(self):
  
        cnx = connect()
        cursor = cnx.cursor()
        #cursor.execute("SELECT * FROM CONTAS_PAGAR ORDER BY IDCONTA ")
        cursor.execute("SELECT C.IDCONTA,C.ID_CAT, F.DESC_CAT, C.VALOR,C.DATA_COMPRA,DATA_VENCIMENTO,C.PAGO,C.DATA_PGTO,C.TIPO_PGTO,C.OBS FROM CONTAS_PAGAR \
                        AS C INNER JOIN CATEGORIAS AS F ON C.ID_CAT=F.ID_CAT WHERE  MONTH(C.DATA_VENCIMENTO) = MONTH(NOW()) AND C.PAGO ='NAO' ORDER BY C.DATA_VENCIMENTO")
        rows=cursor.fetchall()
        for row in rows:
            '''print(row)'''
            self.tree7.insert("",END, values = row)
        cnx.close()    

        
    def pesquisa_Contas_mes_Aberto(self):
        self.consulta_mes_aberto = Toplevel()
        cnx = connect()
        cursor = cnx.cursor()
        cursor.execute("SELECT SUM(VALOR) FROM CONTAS_PAGAR WHERE  MONTH(DATA_VENCIMENTO) = MONTH(NOW()) AND PAGO ='NAO'")

        row=cursor.fetchone()             
         
        if row:
            self.total_mes_aberto = Label(self.consulta_mes_aberto, text = 'TOTAL R$ ' + str(row[0]),font=('arial 22 bold'),fg='red')
            self.total_mes_aberto.grid()
                  
        cnx.close()
        self.tree7= ttk.Treeview(self.consulta_mes_aberto , column=("column", "column1","column2",
                                                       "column3","column4","column5","column6","column7","column8","column9","column10"))#,"column11"))
        self.tree7.column("#0",minwidth=0,width=0)
        self.tree7.heading("#1", text="IDCONTA")
        self.tree7.column("#1", minwidth=0,width=80)
        self.tree7.heading("#2", text="ID_CAT")
        self.tree7.column("#2", minwidth=0,width=80)
        self.tree7.heading("#3", text="CATEG.")
        self.tree7.column("#3", minwidth=0,width=280)        
        self.tree7.heading("#4", text="VALOR")
        self.tree7.column("#4", minwidth=0,width=90)
        self.tree7.heading("#5", text="DATA_COMPRA")
        self.tree7.column("#5", minwidth=0,width=110)
        self.tree7.heading("#6", text="VENCIMENTO")
        self.tree7.column("#6", minwidth=0,width=110)
        self.tree7.heading("#7", text="PAGO")
        self.tree7.column("#7", minwidth=0,width=80)
        self.tree7.heading("#8", text="DATA_PGTO.")
        self.tree7.column("#8", minwidth=0,width=110)
        self.tree7.heading("#9", text="TIPO_PGTO.")
        self.tree7.column("#9", minwidth=0,width=200)
        self.tree7.heading("#10", text="OBS.")
        self.tree7.column("#10", minwidth=0,width=280)
        self.tree7.column("#11",minwidth=0,width=0)

        self.tree7.configure(height=28)
        self.tree7.grid()
        self.View_Contas_Mes_Aberto()
       
        
        self.consulta_mes_aberto .geometry('1480x680')
        self.consulta_mes_aberto .title('CONSULTA CONTAS EM ABERTO MES ATUAL')
        self.consulta_mes_aberto .transient(root)
        self.consulta_mes_aberto .focus_force()
        self.consulta_mes_aberto .grab_set()

        
        
    # -----------------------------------------------------------------------#
    #                           CATEGORIAS                                #
    # -----------------------------------------------------------------------#
    
    def cad_Cat(self):
        self.cad_cat = Toplevel()
        self.idcat = Label(self.cad_cat, text ="ID ", fg= 'black',bg='#CCFFCC')
        self.idcat.grid(row = 0, column = 0)
        self.editidcat =Entry(self.cad_cat,width = 10,bg='lemonchiffon',bd=4)
        self.editidcat.grid(row = 0, column = 1,sticky=W)
        self.catB = Button(self.cad_cat, text="BUSCAR CATEG.",width=17,font=('Arial',14, 'bold'))
        self.catB.grid(row = 0, column = 2)
        self.catB.bind("<Return>", self.pesquisar_Cat)
        self.descricao = Label(self.cad_cat, text ="DESCRICAO", fg= 'black',bg='#CCFFCC')
        self.descricao.grid(row = 1, column = 0)
        self.editdescricao = Entry(self.cad_cat,width = 20,bg='lemonchiffon',bd=4)
        self.editdescricao.grid(row = 1, column =1,sticky=W)
        self.editdescricao.focus()
        self.obs_cat = Label(self.cad_cat, text='OBSERVAÇÕES',font=('Arial',16, 'bold'),bg='lightskyblue')
        self.obs_cat.grid(row = 2, column = 1)
        self.obs_e =  Entry(self.cad_cat,width = 30,bg='lemonchiffon',bd=4)
        self.obs_e.grid(row =3, column=1)


        

    # ===========================================================================================================================================
    #                                                   BOTÕES                                                                                  =
    # ===========================================================================================================================================           

        self.grav_cat = Button(self.cad_cat, text ='GRAVAR ',pady=2,bg ='black', padx=1,bd=2, width = 25, height = 2,
                          font = ('Arial', 12,'bold'), fg ='blue',command = self.gravaCat)#, state = 'disable')
        self.grav_cat.grid(row = 7, column = 0)
        
        self.limpa_cat = Button(self.cad_cat, text ='LIMPAR ',pady=1,bg ='black', padx=2,bd=1, width = 25, height = 2,
                          font = ('Arial', 12,'bold'), fg ='green',command = self.limpa_gravaCat)
        self.limpa_cat.grid(row = 7, column = 1)

        self.boficina = Button(self.cad_cat, text ='TODAS CATEGORIAS',pady=1,bg ='black', padx=2,bd=1, width = 25, height = 2,
                          font = ('Arial', 12,'bold'), fg ='yellow',command = self.pesquisa_Cat)
        self.boficina.grid(row = 8, column = 0)
        
        self.sair_categ = Button(self.cad_cat, text ='SAIR ',pady=1,bg ='black', padx=2,bd=1, width = 25, height = 2,
                          font = ('Arial', 12,'bold'), fg ='red', command = self.cad_cat.destroy)
        self.sair_categ.grid(row = 8, column = 1)

        self.btn_editar = Button(self.cad_cat, text='ALTERAR',width = 20,height = 2,bg='black', fg= 'yellow',command = self.atualiza_Cat)
        self.btn_editar.grid(row = 7 , column = 2)

       

        self.cad_cat.geometry('890x350+500+500')
        self.cad_cat.title('CADASTRO DE CATEGORIAS')
        self.cad_cat.transient(root)
        self.cad_cat.focus_force()
        self.cad_cat.grab_set()
        self.cad_cat.configure(background = '#CCFFCC')

    

    def gravaCat(self):
        cnx = connect()
        cursor = cnx.cursor()

        descricao = self.editdescricao.get().upper()
        if self.editdescricao.get() == '':
            messagebox.showwarning("Erro", "DIGITE A DESCRICAO",parent=self.cad_cat)
        else:
              obs = self.obs.get().upper()        

        #data = time.strftime('%d/%m/%y %H:%M:%S')

        cursor.execute("INSERT INTO CATEGORIAS (DESC_CAT, OBS_CAT)\
        VALUES ('"+descricao+"','"+obs+"')")
        
        try:
            cnx.commit()
            #print("Dados gravados com sucesso")
            messagebox.showinfo("SUCESSO","Dados gravados com sucesso!:)",parent=self.cad_cat)
            self.limpa_gravaCat()
            
            
           
        except mysql.connector.Error as err:
            #print("Não conseguiu gravar no banco de dados.:",err)
            messagebox.showrror("Erro ao gravar os dados",err,parent=self.cad_cat)
               
        cnx.close()


        

    def limpa_gravaCat(self):# Mysql
       #self.editlist_ofi.delete(0,END)
       self.editdescricao.delete(0,END)
       self.obs_e.delete(0,END)        
       

    # UPDATE Categorias
    def pesquisar_Cat(self,event):
        self.desabilita_Cat()
        cnx = connect()
        cursor = cnx.cursor()
        
        cursor.execute("SELECT * FROM CATEGORIAS WHERE ID_CAT = '"+self.editidcat.get()+"' ")
        
        dadosbanco = cursor.fetchone()
        self.limpa_gravaCat()
        if dadosbanco:
            #self.Limpa_gravar()
            #print(cursor.execute())
            self.editdescricao.insert(0, dadosbanco[1])
            self.editcnpj.insert(0, dadosbanco[2]) 
                          
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
                      
            
               
            sql = "UPDATE CATEGORIAS SET DESC_CAT = '"+descricao+"' WHERE ID_CAT = "+idcat 
        try:                     
            cursor.execute(sql)                
            cnx.commit()
            #print("Dados gravados com sucesso")
            messagebox.showinfo("Dados Gravados", "Gravação OK! ")
            self.limpa_gravaCat()
            self.habilita_Cat()
            
        except mysql.connector.Error as err:
            #print("Não conseguiu gravar",err)
            messagebox.showerror("Não conseguiu gravar",err) 

        cnx.close()
    def desabilita_Cat(self):
        self.grav_cat = Button(self.cad_cat, text ='GRAVAR ',pady=2,bg ='black', padx=1,bd=2, width = 25, height = 2,
                          font = ('Arial', 12,'bold'), fg ='blue',command = self.gravaForn, state = 'disable')
        self.grav_cat.grid(row = 7, column = 0)

    def habilita_Cat(self):
        self.grav_cat = Button(self.cad_cat, text ='GRAVAR ',pady=2,bg ='black', padx=1,bd=2, width = 25, height = 2,
                          font = ('Arial', 12,'bold'), fg ='blue',command = self.gravaCat, state = 'normal')
        self.grav_cat.grid(row = 7, column = 0)     
       
    # ===========================================================================================================================


    def View_Cat(self):# categorias
        cnx = connect()
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM CATEGORIAS ORDER  BY ID_CAT ")
        rows=cursor.fetchall()
        for row in rows:
            '''print(row)'''
            self.tree2.insert("",END, values = row)
        cnx.close()    

        
    def pesquisa_Cat(self):
        self.consulta2 = Toplevel()
        self.tree2= ttk.Treeview(self.consulta2, column=("column", "column1","column2",
                                                       "column3"))
        self.tree2.column("#0",minwidth=0,width=0)
        self.tree2.heading("#1", text="IDCAT")
        self.tree2.column("#1", minwidth=0,width=78)
        self.tree2.heading("#2", text="DESCRICAO")
        self.tree2.column("#2", minwidth=0,width=280)
        self.tree2.heading("#3", text="OBSERVAÇÕES")
        self.tree2.column("#3", minwidth=0,width=480)
        self.tree2.column("#4", minwidth=0,width=10)

        self.tree2.configure(height=18)
        self.tree2.grid()
        self.View_Cat()
       
        
        self.consulta2.geometry('860x400+50+50')
        self.consulta2.title('CONSULTA CATEGORIAS')
        self.consulta2.transient(root)
        self.consulta2.focus_force()
        self.consulta2.grab_set()        
            
    # ========================================================================================================================#
    #                                           LISTA PERSONALIZADA  (CATEGORIAS)                                           #
    # ========================================================================================================================#

    def lista_PersonaCat(self):#Busca por data
        self.listaCat_perso = Toplevel()
        self.buscadados = Label(self.listaCat_perso, font =('Arial',10,'bold'),
                              text='BUSCA POR DESCRICAO')
        self.buscadados.grid(row = 0, column = 0)
        self.descricao = Label(self.listaCat_perso, text = 'NOME')
        self.descricao.grid(row = 1, column = 0)
        self.editdescricao = Entry(self.listaCat_perso,width =20, bg = 'lemonchiffon', bd = 4) 
        self.editdescricao.grid(row = 2, column = 0, sticky = W)
        self.editdescricao.focus()
   
    # ==========================================================================================================================
    #                                            LINHA DE SEPARAÇÃO                                                            =
    # ==========================================================================================================================        
        
        separa_linha2 =Frame(self.listaCat_perso, height=4, bd=2, relief=SUNKEN)
        separa_linha2.grid(row = 4,stick=W+E+N+S,columnspan=8,pady=10)
       
    

    # ===========================================================================================================================
    #                                                   BOTÕES                                                                  =
    # ===========================================================================================================================

        self.busca_perso = Button(self.listaCat_perso, text ='BUSCAR ',pady=1,bg ='black', padx=1,bd=2, width = 15, height = 2,
                          font = ('Arial', 12,'bold'), fg ='blue', command = self.listaPersonaForn)
        self.busca_perso.grid(row = 10, column = 0)
        
        sair_buscaPerso = Button(self.listaCat_perso, text ='SAIR',pady=1, bg ='red', padx = 1,bd = 2, width = 15, height = 2,
                         font = ('Arial', 12,'bold'), fg ='yellow', command=self.listaCat_perso.destroy)
        sair_buscaPerso.grid(row = 11, column = 0)
       
        


        self.listaCat_perso.geometry('840x270')
        self.listaCat_perso.title('LISTAR POR DESCRICAO')
        self.listaCat_perso.transient(root)
        self.listaCat_perso.focus_force()
        self.listaCat_perso.grab_set()


    def View_Lista_For(self):#Query que traz do banco todas informacoes da lisat personalizada solicitadas

        cnx = connect()
        cursor = cnx.cursor()

        cursor.execute("SELECT * FROM CATEGORIAS WHERE DESCRICAO like '%"+self.editdescricao.get()+"%' ")
        rows=cursor.fetchall()
        for row in rows:
            #print(row)
            self.treecat.insert("",END, values = row)
        cnx.close()


    def listaPersonaCat(self):#Traz todas  já feitas
        #self.limpaCampos()
        self.consulta3 = Toplevel()
        self.treecat= ttk.Treeview(self.consulta3,column=("column", "column1","column2","column3","column4","column5","column6",
                                                          "column7","column8","column9","column10","column11"))
                                                      
        self.treecat.column("#0",minwidth=0,width=10)
        self.treecat.heading("#1", text="ID")
        self.treecat.column("#1", minwidth=0,width=30)
        self.treecat.heading("#2", text="RAZAO")
        self.treecat.column("#2", minwidth=0,width=260)
        self.treecat.heading("#3", text="CNPJ")
        self.treecat.column("#3", minwidth=0,width=140)
        self.treecat.heading("#4", text="IM")
        self.treecat.column("#4", minwidth=0,width=100)
        self.treecat.heading("#5", text="IE")
        self.treecat.column("#5", minwidth=0,width=100)
        self.treecat.heading("#6", text="END.")
        self.treecat.column("#6", minwidth=0,width=240)
        self.treecat.heading("#7", text="BAIRRO")
        self.treecat.column("#7", minwidth=0,width=180)
        self.treecat.heading("#8", text="CIDADE")
        self.treecat.column("#8", minwidth=0,width=180)
        self.treecat.heading("#9", text="UF")
        self.treecat.column("#9", minwidth=0,width=30)
        self.treecat.heading("#10", text="PAIS")
        self.treecat.column("#10", minwidth=0,width=80)
        self.treecat.heading("#11", text="CEP")
        self.treecat.column("#11", minwidth=0,width=90)
        self.treecat.column("#12", minwidth=0,width=0)
        
        self.treecat.configure(height=20)
        self.treecat.grid()
        self.View_Lista_For()
        self.listaCat_perso.destroy()
        
        
        self.consulta3.geometry('1380x200')
        self.consulta3.title('BUSCA PERSONALIZADA')
        self.consulta3.transient(root)
        self.consulta3.focus_force()
        self.consulta3.grab_set()



    #  SELECT TOTAL CONTAS POR TIPO DE PAGAMENTO
    
    def lista_Totais_pgto(self):#Busca por data e total
        self.listaTotal = Toplevel()
        self.lista_tipo = []
        

        self.x_index = 0
        self.y_index = 0
        self.x_counter = 0

        cnx = connect()
        cursor = cnx.cursor()
        cursor.execute("SELECT TIPO_PGTO, SUM(VALOR)  FROM  CONTAS_PAGAR WHERE MONTH(DATA_VENCIMENTO) = MONTH(NOW())  GROUP BY TIPO_PGTO")        
        rows=cursor.fetchall()
        lista_valores = []
        self.lista_tipo.append(rows)
        #print(self.lista_tipo)
        for i in rows:
            #print(i)
            
            lb1 = Label(self.listaTotal, text= '' + str(i[0]),font='arial 18 bold', bg='light blue')#, fg='blue')
            lb1.place(x=0, y=self.y_index)
            lb2 = Label(self.listaTotal, text= ' R$ '+ str(i[1]),font='arial 18 bold', bg='light blue')#, fg='blue')
            lb2.place(x= 350, y=self.y_index)
            lista_valores.append(i[1])
            self.x_counter +=1
            #self.y_index += 0
            self.y_index += 40
            self.x_counter += 1
##        print('Lista de todos os valores',lista_valores)
##        print('Lista de total dos valores  R$ {:.2f} '.format(sum(lista_valores)))
        total_geral = "{:.2f}".format(sum(lista_valores))

        lb3 = Label(self.listaTotal, text=' Total                                   R$ '+ str(total_geral),font='arial 22 bold ',fg='red', bg='SteelBlue1')
        lb3.place(x=0, y=200)
       
        cnx.close()

        self.listaTotal.geometry('640x270')
        self.listaTotal.title('TOTAL FORMA PGTO MES ATUAL')
        self.listaTotal.transient(root)
        self.listaTotal.configure(background='light blue')
        self.listaTotal.focus_force()
        self.listaTotal.grab_set()




    def cad_Faturas(self):
        self.cad_fatura = Toplevel()
        self.idfatura = Label(self.cad_fatura, text ="ID ", fg= 'black',bg='#CCFFCC')
        self.idfatura.grid(row = 0, column = 0)
        self.editidfatura =Entry(self.cad_fatura,width = 10,bg='lemonchiffon',bd=4)
        self.editidfatura.grid(row = 0, column = 1,sticky=W)

        self.desccartao = Label(self.cad_fatura, text ="DESCRICAO", fg= 'black',bg='#CCFFCC')
        self.desccartao.grid(row = 1, column = 0)
        self.combo6 = ttk.Combobox(self.cad_fatura, height= 4,width = 25)
        #self.combo6.current(1)
        self.combo6.grid(row = 1, column = 1,sticky=W)
        self.combo6['values']= self.list_pgto()
        ''' self.editdesccartao = Entry(self.cad_fatura,width = 30,bg='lemonchiffon',bd=4)
            self.editdesccartao.grid(row = 1, column =1,sticky=W)
            self.editdesccartao.focus()
         '''   
        self.valorcartao = Label(self.cad_fatura, text ="VALOR R$", fg= 'black',bg='#CCFFCC')
        self.valorcartao.grid(row = 1, column = 2)
        self.editvalorcartao = Entry(self.cad_fatura,width = 10,bg='lemonchiffon',bd=4)
        self.editvalorcartao.grid(row = 1, column = 3,sticky=W)
        self.venctocartao = Label(self.cad_fatura, text ="VENCIMENTO", fg= 'black',bg='#CCFFCC')
        self.venctocartao.grid(row = 2, column = 0)
        self.editvenctocartao = Entry(self.cad_fatura,width = 20,bg='lemonchiffon',bd=4)
        self.editvenctocartao.grid(row = 2, column =1,sticky=W)
        self.pago_fat = Label(self.cad_fatura, text ="PAGO (SIM/NAO)", fg= 'black',bg='#CCFFCC')
        self.pago_fat.grid(row = 2, column = 2)
        self.combo5 = ttk.Combobox(self.cad_fatura, height= 4,width = 10)
        self.combo5['values']=('SIM','NAO')
        self.combo5.current(1)
        self.combo5.grid(row = 2, column = 3,sticky=W)
        #self.combo5['values']= self.box_list()
        self.data_pgto = Label(self.cad_fatura, text ="DATA PAGAMENTO", fg= 'black',bg='#CCFFCC')
        self.data_pgto.grid(row = 4, column = 0)
        self.editdata_pgto = Entry(self.cad_fatura,width = 20,bg='lemonchiffon',bd=4)
        self.editdata_pgto.grid(row = 4, column =1,sticky=W)
        self.valor_pgto = Label(self.cad_fatura, text ="VALOR PAGO", fg= 'black',bg='#CCFFCC')
        self.valor_pgto.grid(row = 4, column = 2)
        self.editvalor_pgto = Entry(self.cad_fatura,width = 10,bg='lemonchiffon',bd=4)
        self.editvalor_pgto.grid(row = 4, column = 3,sticky=W)
        


    # ===========================================================================================================================================
    #                                                 BOTÕES                                                                                  =
    # ===========================================================================================================================================           

        self.grav_fatura = Button(self.cad_fatura, text ='GRAVAR ',pady=2,bg ='black', padx=1,bd=2, width = 25, height = 2,
                          font = ('Arial', 12,'bold'), fg ='blue',command = self.gravaFatura)#, state = 'disable')
        self.grav_fatura.grid(row = 8, column = 0)

        self.editarfat = Button(self.cad_fatura, text='ALTERAR',width = 25,height = 2,bg='black', fg= 'yellow',command = self.edita_Fatura)
        self.editarfat.grid(row = 8 , column = 1)
        
##        self.limpa_forn = Button(self.cad_fatura, text ='LIMPAR ',pady=1,bg ='black', padx=2,bd=1, width = 25, height = 2,
##                          font = ('Arial', 12,'bold'), fg ='green')#,command = self.limpa_gravaForn)
##        self.limpa_forn.grid(row = 7, column = 1)
##
        self.boficina = Button(self.cad_fatura, text ='TODAS FATURAS ',pady=1,bg ='black', padx=2,bd=1, width = 25, height = 2,
                          font = ('Arial', 12,'bold'), fg ='yellow',command = self.pesq_Faturas_all)
        self.boficina.grid(row = 9, column = 0)
        
        self.sair_fatura = Button(self.cad_fatura, text ='SAIR ',pady=1,bg ='black', padx=2,bd=1, width = 25, height = 2,
                          font = ('Arial', 12,'bold'), fg ='red', command = self.cad_fatura.destroy)
        self.sair_fatura.grid(row = 9, column = 1)

       

        self.cad_fatura.geometry('890x350+500+500')
        self.cad_fatura.title('FATURAS CARTOES')
        self.cad_fatura.transient(root)
        self.cad_fatura.focus_force()
        self.cad_fatura.grab_set()
        self.cad_fatura.configure(background = '#CCFFCC')
        

    def gravaFatura(self):
        cnx = connect()
        cursor = cnx.cursor()
        descfat = self.combo6.get().upper()
        if self.combo6.get() == '':
            messagebox.showwarning("Erro", "DIGITE A DESCRICAO")
        else:
            valor_cartao = self.editvalorcartao.get()        
            data_vencto =  self.editvenctocartao.get()
            pago = self.combo5.get().upper()
            data_pgto = self.editdata_pgto.get()
            valor_pgto = self.editvalor_pgto.get()
            
        #data = time.strftime('%d/%m/%y %H:%M:%S')

        cursor.execute("INSERT INTO FATURAS (DESC_CARTAO, VALOR_CARTAO, DATA_VENCIMENTO,PAGO,DATA_PAGAMENTO,VALOR_PAGAMENTO)\
                        VALUES ('"+descfat+"','"+valor_cartao+"','"+data_vencto+"','"+pago +"','"+data_pgto+"','"+valor_pgto+"')")
        
        try:
            cnx.commit()
            #print("Dados gravados com sucesso")
            messagebox.showinfo("SUCESSO","Dados gravados com sucesso!:)")
            self.limpa_faturas()
            
            
           
        except mysql.connector.Error as err:
            #print("Não conseguiu gravar no banco de dados.:",err)
            messagebox.showrror("Erro ao gravar os dados",err)
               
        cnx.close()

#     EDITAR FATURA PAGA/NÃO PAGO
    def edita_Fatura(self):
        cnx = connect()
        cursor = cnx.cursor()
        idfatura =self.editidfatura.get()
        descfat = self.combo6.get().upper()
        if self.combo6.get() == '':
            messagebox.showwarning("Erro", "DIGITE A DESCRICAO")
        else:
            valor_cartao = self.editvalorcartao.get()        
            data_vencto =  self.editvenctocartao.get()
            pago = self.combo5.get().upper()
            data_pgto = self.editdata_pgto.get()
            valor_pgto = self.editvalor_pgto.get()
            
        #data = time.strftime('%d/%m/%y %H:%M:%S')
            
        sql = "UPDATE FATURAS SET DESC_CARTAO = '"+descfat+"', VALOR_CARTAO = '"+valor_cartao+"',\
                        DATA_VENCIMENTO = '"+data_vencto+"',PAGO = '"+pago +"',DATA_PAGAMENTO = '"+data_pgto+"',\
                        VALOR_PAGAMENTO = '"+valor_pgto+"' WHERE IDFATURA = "+idfatura
                            
        
        try:
            cursor.execute(sql)
            cnx.commit()
            #print("Dados gravados com sucesso")
            messagebox.showinfo("SUCESSO","Dados gravados com sucesso!:)")
            self.limpa_faturas()
            
            
           
        except mysql.connector.Error as err:
            #print("Não conseguiu gravar no banco de dados.:",err)
            messagebox.showrror("Erro ao gravar os dados",err)
               
        cnx.close()


    def limpa_faturas(self):
         self.combo6.delete(0,END)
         self.editvalorcartao.delete(0,END)
         self.editvenctocartao.delete(0,END)
         self.editdata_pgto.delete(0,END)
         self.combo5.delete(0,END)
         self.editvalor_pgto.delete(0,END)



    def box_list(self):
        cnx = connect()
        cursor = cnx.cursor()
        cursor.execute("SELECT DESC_CARTAO FROM FATURAS")
        result = []
        
        for i in cursor.fetchall():
            result.append(i[0])
           
            #print(i)
        return result
        
        cnx.close()
 # TRAZER TODAS AS FATURAS CADSTRADAS

 
    def View_Faturas(self):
        cnx = connect()
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM FATURAS ORDER  BY IDFATURA ")
        rows=cursor.fetchall()
        for row in rows:
            '''print(row)'''
            self.tree3.insert("",END, values = row)
        cnx.close()    

        
    def pesq_Faturas_all(self):
        self.consulta5 = Toplevel()
        self.tree3= ttk.Treeview(self.consulta5, column=("column", "column1","column2",
                                                       "column3","column4","column5","column6",
                                                         "column7"))#,"column8","column9","column10"))
                
        self.tree3.column("#0",minwidth=0,width=0)
        self.tree3.heading("#1", text="IDFAT")
        self.tree3.column("#1", minwidth=0,width=78)
        self.tree3.heading("#2", text="DESCRICAO")
        self.tree3.column("#2", minwidth=0,width=280)
        self.tree3.heading("#3", text="VALOR")
        self.tree3.column("#3", minwidth=0,width=140)
        self.tree3.heading("#4", text="VENCIMENTO")
        self.tree3.column("#4", minwidth=0,width=140)
        self.tree3.heading("#5", text="PAGO")
        self.tree3.column("#5", minwidth=0,width=60)
        self.tree3.heading("#6", text="DATA_PGTO")
        self.tree3.column("#6", minwidth=0,width=140)
        self.tree3.heading("#7", text="VALOR_PGTO")
        self.tree3.column("#7", minwidth=0,width=100)
        self.tree3.column("#8",minwidth=0,width=0)
        

        self.tree3.configure(height=28)
        self.tree3.grid()
        self.View_Faturas()
       
        
        self.consulta5.geometry('1080x610')
        self.consulta5.title('CONSULTA CATEGORIAS')
        self.consulta5.transient(root)
        self.consulta5.focus_force()
        self.consulta5.grab_set()
        
# TIPOS DE PAGAMENTO
    def cad_Tipos_Pgto(self):
        self.cad_tipospgto = Toplevel()
        self.idpgto = Label(self.cad_tipospgto, text ="ID ", fg= 'black',bg='#CCFFCC')
        self.idpgto.grid(row = 0, column = 0,sticky=W)
        self.editidpgto =Entry(self.cad_tipospgto,width = 10,bg='lemonchiffon',bd=4)
        self.editidpgto.grid(row = 0, column = 1,sticky=W)
        self.desc_pgto = Label(self.cad_tipospgto, text ="DESCRICAO ", fg= 'black',bg='#CCFFCC')
        self.desc_pgto.grid(row = 1, column = 0,sticky=W)
        self.editdesc_pgto =Entry(self.cad_tipospgto,width = 20,bg='lemonchiffon',bd=4)
        self.editdesc_pgto.grid(row = 1, column = 1,sticky=W)

        self.obs = Label(self.cad_tipospgto, text='OBSERVAÇÕES (MAXIMO 60 CARACTERES)',font=('Arial',12, 'bold'),bg='lightskyblue')
        self.obs.place(x = 20, y =150)

        self.obspgto = Text(self.cad_tipospgto, height=5)
        self.obspgto.place(x = 5,y = 180)
        self.obspgto.get(1.0,END)

        self.grav_fatura = Button(self.cad_tipospgto, text ='GRAVAR ',pady=2,bg ='black', padx=1,bd=2, width = 25, height = 2,
                          font = ('Arial', 12,'bold'), fg ='blue',command = self.grava_tipopgto)
        self.grav_fatura.place(x = 20, y = 280)


        self.cad_tipospgto.geometry('655x400')
        self.cad_tipospgto.title('CADASTRO TIPOS DE PAGAMENTOS')
        self.cad_tipospgto.transient(root)
        self.cad_tipospgto.focus_force()
        self.cad_tipospgto.grab_set() 

    def grava_tipopgto(self):
        cnx = connect()
        cursor = cnx.cursor()
        desctipo = self.editdesc_pgto.get().upper()
        if self.editdesc_pgto.get() == '':
            messagebox.showwarning("Erro", "DIGITE A DESCRICAO")
        else:
            obs_pgto = self.obspgto.get(1.0, END).upper()
           
            #data = time.strftime('%d/%m/%y %H:%M:%S')

        cursor.execute("INSERT INTO TIPO_PAGTO (DESC_PGTO,OBS)\
                        VALUES ('"+desctipo+"','"+obs_pgto+"')")
        
        try:
            cnx.commit()
            #print("Dados gravados com sucesso")
            messagebox.showinfo("SUCESSO","Dados gravados com sucesso!:)")
            self.limpa_tipopgto()
            
        except mysql.connector.Error as err:
            #print("Não conseguiu gravar no banco de dados.:",err)
            messagebox.showrror("Erro ao gravar os dados",err)
               
        cnx.close()
        
    def limpa_tipopgto(self):
        self.editdesc_pgto.delete(0,END)
        self.obspgto.delete(1.0,END)
        

#   listar todos os tipos de pagamentos
    def list_tipos_pgto(self):
        cnx = connect()
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM TIPO_PAGTO")
        rows=cursor.fetchall()
        for row in rows:
            #print(row)
            self.tree8.insert("",END, values = row)
        cnx.close()


    def lista_tipos_pgto(self):#Traz todos os tipos cadastrados
        #self.limpaCampos()
        self.consulta6 = Toplevel()
        self.tree8 = ttk.Treeview(self.consulta6,column=("column", "column1","column2","column3"))#,"column4","column5","column6",
                                                          #"column7","column8","column9","column10","column11"))
                                                      
        self.tree8.column("#0",minwidth=0,width=10)
        self.tree8.heading("#1", text="ID")
        self.tree8.column("#1", minwidth=0,width=30)
        self.tree8.heading("#2", text="DESCRICAO")
        self.tree8.column("#2", minwidth=0,width=260)
        self.tree8.heading("#3", text="OBS")
        self.tree8.column("#3", minwidth=0,width=200)
        self.tree8.column("#4",minwidth=0,width=10)
        
        self.tree8.configure(height=20)
        self.tree8.grid()
        self.list_tipos_pgto()       
        
        self.consulta6.geometry('550x400')
        self.consulta6.title('LISTA TODAS AS FORMAS DE PAGAMENTO CADASTRADAS')
        self.consulta6.transient(root)
        self.consulta6.focus_force()
        self.consulta6.grab_set()
        

    # Planilhas

    def gera_planilha(self):
        workbook = xlwt.Workbook()
        worksheet = workbook.add_sheet('Contas')
        cnx = connect()
        cursor = cnx.cursor()

        cursor.execute("SELECT C.IDCONTA,C.ID_CAT, F.DESC_CAT, C.VALOR,C.DATA_COMPRA,DATA_VENCIMENTO,C.PAGO,C.DATA_PGTO,C.TIPO_PGTO,C.OBS FROM CONTAS_PAGAR \
                        AS C INNER JOIN CATEGORIAS AS F ON C.ID_CAT=F.ID_CAT AND MONTH(C.DATA_VENCIMENTO) = MONTH(NOW()) ORDER BY C.IDCONTA")
        rows=cursor.fetchall()


        worksheet.write(0,0,'IDCONTA')
        worksheet.write(0,1,'ID_CAT')
        worksheet.write(0,2,'DESC.CAT')
        worksheet.write(0,3,'VALOR')
        worksheet.write(0,4,'DATA COMPRA')
        worksheet.write(0,5,'VENCIMENTO')
        worksheet.write(0,6,'PAGO')
        worksheet.write(0,7,'DAT PGTO')
        worksheet.write(0,8,'TIPO PGTO')
        worksheet.write(0,9,'OBSERVAÇÕES')


        for i, conta in enumerate(rows):
            worksheet.write(i + 1, 0, conta[0])
            worksheet.write(i + 1, 1, conta[1])
            worksheet.write(i + 1, 2, conta[2])
            worksheet.write(i + 1, 3, conta[3], style = xlwt.easyxf(num_format_str='R$#,##0.00'))
            worksheet.write(i + 1, 4, conta[4],
                            style = xlwt.easyxf(num_format_str='dd/mm/yyyy'))
            worksheet.write(i + 1, 5, conta[5],
                            style = xlwt.easyxf(num_format_str='dd/mm/yyyy'))
            worksheet.write(i + 1, 6, conta[6])
            worksheet.write(i + 1, 7, conta[7],
                            style = xlwt.easyxf(num_format_str='dd/mm/yyyy'))
            worksheet.write(i + 1, 8, conta[8])
            worksheet.write(i + 1, 9, conta[9],
                            style = xlwt.easyxf(num_format_str='@'))
            
        workbook.save('/home/julio/Python_Des/FINANCAS/Contas.xls')
        messagebox.showinfo("SUCESSO","Planilha criada em: /home/julio/Python_Des/FINANCAS/Contas.xls)")
        cnx.close()


     # =============================================================================================================#
     #                                           LISTA PERSONALIZADA  selecionar todas as contas por fornecedor     #
     # =============================================================================================================#

    def lista_Personalizada_Cat(self):#Busca por data
        self.lista_perso_Cat = Toplevel()
        self.right1 = Frame(self.lista_perso_Cat, width=700,height=80)#, bg='white')
        self.right1.pack(side=TOP)
        
        self.left1 = Frame(self.lista_perso_Cat, width=700,height=690)#, bg='white')
        self.left1.pack(side=TOP)
        
        self.buscadata_forn = Label(self.lista_perso_Cat, font =('Arial',10,'bold'),
                              text='BUSCA ENTRE DATAS:')
        self.buscadata_forn.place(x = 0 , y= 0)
        self.dataini_forn = Label(self.lista_perso_Cat, text = 'DATA INICIAL')
        self.dataini_forn.place(x = 0 , y= 20)
        self.editdataini_forn = Entry(self.lista_perso_Cat,width =20, bg = '#CCFFCC', bd = 4) 
        self.editdataini_forn.place(x = 0 , y= 40)
        self.editdataini_forn.focus()
        self.datafin_forn = Label(self.lista_perso_Cat, text = 'DATA FINAL')
        self.datafin_forn.place(x = 200 , y= 20)
        self.editdatafin_forn = Entry(self.lista_perso_Cat,width =20, bg = '#CCFFCC', bd = 4) 
        self.editdatafin_forn.place(x = 200 , y= 40)
        self.categoria_conta = Label(self.lista_perso_Cat, text = 'CATEGORIA')
        self.categoria_conta.place(x = 400 , y= 20)
        self.editcategoria_conta = Entry(self.lista_perso_Cat,width =20, bg = '#CCFFCC', bd = 4) 
        self.editcategoria_conta.place(x = 400 , y= 40)
        self.busca_perso_forn = Button(self.lista_perso_Cat, text ='BUSCAR ',pady=1,bg ='yellow', padx=1,bd=2, width = 15, height = 1,
                          font = ('Arial', 10,'bold'), fg ='blue')
        self.busca_perso_forn.place(x = 600 , y= 40)
        self.busca_perso_forn.bind("<Return>", self.View_Lista_perso_Cat)
        
  
    # =================================================================================================================================
    #                                                   BOTÕES                                                                        =
    # =================================================================================================================================           
       
        self.limpa_perso_forn = Button(self.lista_perso_Cat, text ='LIMPAR ',pady=1,bg ='yellow', padx=1,bd=2, width = 15, height = 1,
                          font = ('Arial', 10,'bold'), fg ='blue', command = self.delete_view_labels)
        self.limpa_perso_forn.place(x = 750 , y= 40)
        
        sair_buscaPerso_forn = Button(self.lista_perso_Cat, text ='SAIR',pady=1, bg ='red', padx = 1,bd = 2, width = 15, height = 1,
                         font = ('Arial', 10,'bold'), fg ='blue', command=self.lista_perso_Cat.destroy)
        sair_buscaPerso_forn.place(x = 900 , y= 40)

        self.total_categ = Label(self.lista_perso_Cat, text=' Total R$ ',font='arial 17 bold ',width=15)
        self.total_categ.place(x=800, y=600)
        self.total_categoria = Entry(self.lista_perso_Cat,width=10,font='arial 17 bold', fg='red')
        self.total_categoria.place(x=960, y=600)
              

        self.tree9= ttk.Treeview(self.left1,column=("column", "column1","column2","column3","column4","column5","column6",
                                                     "column7","column8","column9"))
                                                             
        self.tree9.column("#0",minwidth=0,width=10)
        self.tree9.heading("#1", text="IDCONTA")
        self.tree9.column("#1", minwidth=0,width=80)
        self.tree9.heading("#2", text="ID_CAT")
        self.tree9.column("#2", minwidth=0,width=80)
        self.tree9.heading("#3", text="DESCRICAO")
        self.tree9.column("#3", minwidth=0,width=250)
        self.tree9.heading("#4", text="VALOR")
        self.tree9.column("#4", minwidth=0,width=80)
        self.tree9.heading("#5", text="DATA_COMPRA")
        self.tree9.column("#5", minwidth=0,width=110)
        self.tree9.heading("#6", text="VENCIMENTO")
        self.tree9.column("#6", minwidth=0,width=110)
        self.tree9.heading("#7", text="PAGO")
        self.tree9.column("#7", minwidth=0,width=70)
        self.tree9.heading("#8", text="TIPO PAGTO")
        self.tree9.column("#8", minwidth=0,width=200)
        self.tree9.heading("#9", text="OBSERVACAO")
        self.tree9.column("#9", minwidth=0,width=250)
        self.tree9.column("#10", minwidth=0,width=0)
                
        self.tree9.configure(height=20)
        self.tree9.pack()
        
        self.lista_perso_Cat.geometry('1250x700')
        self.lista_perso_Cat.title('Listar Todas as contas por Categorias6')
        self.lista_perso_Cat.transient(root)
        self.lista_perso_Cat.focus_force()
        self.lista_perso_Cat.grab_set()


    def View_Lista_perso_Cat(self,event):#Query que traz do banco todas as Os de pagamentos entre as datas solicitadas por fornecedor(Razao)
        self.tree9.delete(*self.tree9.get_children())
        cnx = connect()
        cursor = cnx.cursor()
        
        cursor.execute("SELECT C.IDCONTA, C.ID_CAT,F.DESC_CAT, C.VALOR,C.DATA_COMPRA, C.DATA_VENCIMENTO,C.PAGO,C.TIPO_PGTO, C.OBS FROM CONTAS_PAGAR AS C INNER JOIN \
                                            CATEGORIAS AS F ON C.ID_CAT = F.ID_CAT AND DATA_VENCIMENTO BETWEEN '"+self.editdataini_forn.get()+"' \
                                            AND '"+self.editdatafin_forn.get()+"'  WHERE F.DESC_CAT  LIKE '%"+  self.editcategoria_conta.get()+"%' ") 
        
        rows=cursor.fetchall()
        for row in rows:
            #print(row)
            self.tree9.insert("",END, values = row)
            
        cnx.close()
        self.soma_total_cat()

    def soma_total_cat(self):
        self.total_categoria.delete(0, END)
        cnx = connect()
        cursor = cnx.cursor()
        
        cursor.execute("SELECT SUM(C.VALOR) FROM CONTAS_PAGAR AS C INNER JOIN  CATEGORIAS AS F ON C.ID_CAT = F.ID_CAT AND DATA_VENCIMENTO BETWEEN '"+self.editdataini_forn.get()+"' \
                                            AND '"+self.editdatafin_forn.get()+"'  WHERE F.DESC_CAT  LIKE '%"+  self.editcategoria_conta.get()+"%' ") 
        
        row=cursor.fetchone()
        if row:
            self.total_categoria.insert(0,float(row[0]))
        cnx.close()    
            
           
    def delete_view_labels(self):
        self.editdataini_forn.delete(0, END)
        self.editdatafin_forn.delete(0, END)
        self.editcategoria_conta.delete(0, END)
        self.total_categoria.delete(0, END)
        self.tree9.delete(*self.tree9.get_children())


 # =============================================================================================================#
    #                                           LISTA PERSONALIZADA  (PAGAMENTOS)                                  #
    # =============================================================================================================#

    def lista_Personalizada(self):#Busca por data
        self.lista_perso = Toplevel()
        self.right2 = Frame(self.lista_perso, width=700,height=80)#, bg='white')
        self.right2.pack(side=TOP)
        
        self.left2 = Frame(self.lista_perso, width=700,height=690)#, bg='white')
        self.left2.pack(side=TOP)
        
        self.buscadata = Label(self.lista_perso, font =('Arial',10,'bold'),
                              text='BUSCA ENTRE DATAS:')
        self.buscadata.place(x = 0, y = 0)
        self.dataini = Label(self.lista_perso, text = 'Data Inicial')
        self.dataini.place(x = 0, y = 20)
        self.editdataini = Entry(self.lista_perso,width =20, bg = '#CCFFCC', bd = 4) 
        self.editdataini.place(x = 0, y = 40)
        self.editdataini.focus()
        self.datafin = Label(self.lista_perso, text = 'Data Final')
        self.datafin.place(x = 200, y = 20)
        self.editdatafin = Entry(self.lista_perso,width =20, bg = '#CCFFCC', bd = 4) 
        self.editdatafin.place(x = 200, y = 40)

      

        self.ofi_desc = Label(self.lista_perso, text = 'STATUS')
        self.ofi_desc.place(x = 400, y = 20)
        self.combo2 = ttk.Combobox(self.lista_perso, height= 4,width = 15)
        self.combo2['values']=('SIM','NAO')
        self.combo2.current(1)
        self.combo2.place(x = 400, y = 40)
        self.form_pgto = Label(self.lista_perso, text = 'FORMA PGTO')
        self.form_pgto.place(x=600, y = 20)
        self.combo3 = ttk.Combobox(self.lista_perso, height= 4,width = 30)
        self.combo3['values']= self.list_pgto()

        self.combo3.current(0)
        self.combo3.place(x = 600, y = 40)
        self.total_lista_personalizada = Label(self.lista_perso, text = 'TOTAL R$ ', font='arial 18 bold')
        self.total_lista_personalizada.place(x = 800, y= 600)
        self.total_lista_personalizada = Entry(self.lista_perso,width =10, bg = '#CCFFCC', bd = 2,fg='red',font='arial 16 bold')
        self.total_lista_personalizada.place(x = 940, y = 600)


    # =================================================================================================================================
    #                                                   BOTÕES                                                                        =
    # =================================================================================================================================           

        self.busca_perso = Button(self.lista_perso, text ='BUSCAR ',pady=1,bg ='black', padx=1,bd=2, width = 15, height = 1,
                          font = ('Arial', 12,'bold'), fg ='blue', command = self.View_Lista_perso)
        self.busca_perso.place(x = 880, y = 40)
        
        sair_buscaPerso = Button(self.lista_perso, text ='SAIR',pady=1, bg ='red', padx = 1,bd = 2, width = 15, height = 1,
                         font = ('Arial', 12,'bold'), fg ='yellow', command=self.lista_perso.destroy)
        sair_buscaPerso.place(x = 1040, y = 40)

        self.treepgto= ttk.Treeview(self.left2,column=("column", "column1","column2","column3","column4","column5","column6",
                                                          "column7","column8","column9"))
                                                              
        self.treepgto.column("#0",minwidth=0,width=10)
        self.treepgto.heading("#1", text="IDCONTA")
        self.treepgto.column("#1", minwidth=0,width=80)
        self.treepgto.heading("#2", text="ID_CAT")
        self.treepgto.column("#2", minwidth=0,width=80)
        self.treepgto.heading("#3", text="DESCRICAO")
        self.treepgto.column("#3", minwidth=0,width=250)
        self.treepgto.heading("#4", text="VALOR")
        self.treepgto.column("#4", minwidth=0,width=80)
        self.treepgto.heading("#5", text="DATA_COMPRA")
        self.treepgto.column("#5", minwidth=0,width=110)
        self.treepgto.heading("#6", text="VENCIMENTO")
        self.treepgto.column("#6", minwidth=0,width=110)
        self.treepgto.heading("#7", text="PAGO")
        self.treepgto.column("#7", minwidth=0,width=70)
        self.treepgto.heading("#8", text="TIPO PAGTO")
        self.treepgto.column("#8", minwidth=0,width=200)
        self.treepgto.heading("#9", text="OBSERVACAO")
        self.treepgto.column("#9", minwidth=0,width=250)
        self.treepgto.column("#10", minwidth=0,width=0)
        
      
        self.treepgto.configure(height=20)
        self.treepgto.pack()

        self.lista_perso.geometry('1300x800')
        self.lista_perso.title('BUSCA PERSONALIZADA')
        self.lista_perso.transient(root)
        self.lista_perso.focus_force()
        self.lista_perso.grab_set()


    def View_Lista_perso(self):#Query que traz do banco todas as Os de pagamentos entre as datas solicitadas
        self.treepgto.delete(*self.treepgto.get_children())
        cnx = connect()
        cursor = cnx.cursor()
        
        cursor.execute("SELECT C.IDCONTA, C.ID_CAT,F.DESC_CAT, C.VALOR,C.DATA_COMPRA, C.DATA_VENCIMENTO,C.PAGO,C.TIPO_PGTO, C.OBS FROM CONTAS_PAGAR AS C INNER JOIN \
                                            CATEGORIAS AS F ON DATA_VENCIMENTO \
                                            BETWEEN '"+self.editdataini.get()+"' AND '"+self.editdatafin.get()+"'  AND \
                                            C.PAGO = '"+(self.combo2.get())+"' AND C.TIPO_PGTO = '"+self.combo3.get()+"' AND C.ID_CAT = F.ID_CAT ORDER BY C.DATA_VENCIMENTO")
        
        rows=cursor.fetchall()
        for row in rows:
            #print(row)
            self.treepgto.insert("",END, values = row)
        cnx.close()
        self.total_Lista_perso()


    def total_Lista_perso(self):
        self.total_lista_personalizada.delete(0, END)
        cnx = connect()
        cursor = cnx.cursor()
        
        cursor.execute("SELECT SUM(C.VALOR) AS TOTAL FROM CONTAS_PAGAR AS C INNER JOIN CATEGORIAS AS F ON DATA_VENCIMENTO \
                                            BETWEEN '"+self.editdataini.get()+"' AND '"+self.editdatafin.get()+"'  AND \
                                            C.PAGO = '"+(self.combo2.get())+"' AND C.TIPO_PGTO = '"+self.combo3.get()+"' AND C.ID_CAT = F.ID_CAT")
        row=cursor.fetchone()
        
        if row:
            self.total_lista_personalizada.insert(0,float(row[0]))
        cnx.close() 

    def add_entradas(self):
        self.entradas = Toplevel()
        self.frame_entradas = Frame(self.entradas, width=700,height=600)#, bg='white')
        self.frame_entradas.pack(side=TOP)
        self.id_entrada = Label(self.entradas, text='COD. ENTRADA ',font =('Arial',14,'bold'))
        self.id_entrada.place(x = 0, y =20)
        self.id_entradae = Entry(self.entradas, width =10)
        self.id_entradae.place(x = 145, y = 20)
        self.fonte_entrada = Label(self.entradas, text='FONTE PAGTO', font =('Arial',14,'bold'))#, fg='blue')
        self.fonte_entrada.place(x = 0, y = 50)
        self.fonte_entradae = Entry(self.entradas,width = 25)
        self.fonte_entradae.place(x = 145, y = 50)
        self.valor_entrada = Label(self.entradas, text='VALOR PAGTO R$', font =('Arial',14,'bold'))
        self.valor_entrada.place(x = 400, y = 50)
        self.valor_entradae = Entry(self.entradas, width = 25,  fg ='green')
        self.valor_entradae.place(x = 570, y = 50)
        self.data_pagto = Label(self.entradas, text='DATA PAGTO', font =('Arial',14,'bold'))
        self.data_pagto.place(x = 0, y = 80)
        self.data_pagtoe = Entry(self.entradas, width = 25)
        self.data_pagtoe.place(x = 145, y = 80)
        self.obs_ent = Label(self.entradas, text='OBSERVAÇÕES', font =('Arial',14,'bold'))
        self.obs_ent.place(x = 400, y = 80)
        self.obs_ent_e = Entry(self.entradas, width = 25)
        self.obs_ent_e.place(x = 570, y = 80)

        self.grav_entradas = Button(self.entradas, text ='GRAVAR ',pady=1,bg ='black', padx=1,bd=1, width = 20, height = 2,
                          font = ('Arial', 12,'bold'), fg ='blue',command = self.gravaEntrada)
        self.grav_entradas.place(x = 0 , y = 250)
        
        self.limpa_entradas = Button(self.entradas, text ='LIMPAR ',pady=1,bg ='black', padx=1,bd=1, width = 20, height = 2,
                          font = ('Arial', 12,'bold'), fg ='green',command = self.limpa_entrada)
        self.limpa_entradas.place(x = 200, y = 250)

        self.sair_entradas = Button(self.entradas, text ='SAIR ',pady=1,bg ='black', padx=1,bd=1, width = 20, height = 2,
                          font = ('Arial', 12,'bold'), fg ='red',command = self.entradas.destroy)
        self.sair_entradas.place(x = 0, y = 300)
        
        self.entradas.geometry("800x480+200+200")
        self.entradas.title("CADASTRO ENTRADAS CRÉDITOS")
##        self.entradas.configure(background='light blue')
        self.entradas.transient(root)
        self.entradas.grab_set()    

    
    def gravaEntrada(self):
        cnx = connect()
        cursor = cnx.cursor()

        fonte_pgto = self.fonte_entradae.get().upper()
        if self.fonte_entradae.get() == '':
            messagebox.showwarning("Erro", "DIGITE A FONTE")
        else:
            valor = self.valor_entradae.get()
            if self.valor_entradae.get() == '':
                messagebox.showwarning("Erro", "VALOR NÃO PODE SER VAZIO")
            else:
                data_entrada = self.data_pagtoe.get()
                if self.data_pagtoe.get() =='':
                    messagebox.showwarning("Erro", "DATA NÃO PODE SER VAZIO")
                else:
                   obs = self.obs_ent_e.get().upper()        

        cursor.execute("INSERT INTO ENTRADAS (FONTE_PGTO,VALOR,DATA_PGTO,OBSERVACOES)\
        VALUES ('"+fonte_pgto+"','"+valor+"','"+data_entrada+"','"+obs+"')")
        
        try:
            cnx.commit()
            #print("Dados gravados com sucesso")
            messagebox.showinfo("SUCESSO","Dados gravados com sucesso!:)")
            self.limpa_entrada()
            
            
           
        except mysql.connector.Error as err:
            #print("Não conseguiu gravar no banco de dados.:",err)
            messagebox.showrror("Erro ao gravar os dados")
               
        cnx.close()



    def limpa_entrada(self):
        self.id_entradae.delete(0, END)
        self.fonte_entradae.delete(0, END)
        self.valor_entradae.delete(0, END)
        self.data_pagtoe.delete(0, END)
        self.obs_ent_e.delete(0, END)
        
        
        
        
        
root = Tk()
Sistema(root)
root.geometry("750x640+540+110")
#root.resizable(0,0)
root.title("JS Financas")
root.configure(background='#004400')
#root.configure(background='pink')
root.configure(highlightbackground='#CC00CC')
root.configure(highlightcolor='black')
root.mainloop()
