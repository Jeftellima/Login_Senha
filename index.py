# importar bibliotecas.
from tkinter import *            #importar toda a biblioteca
from tkinter import messagebox   #importar mensagem de texto pro usuário
from tkinter import ttk
import DataBaser
# Criar nossa janela
jan = Tk()                                #Criar variável da janela Tk() estamos atribuindo que essa variável é uma janela !
jan.title("Login - Painel de Acesso")     # Agora vamos para os atributos e mensagem do título.
jan.geometry("600x300")                   # Aqui colocamos o tamnho da janela.
jan.configure(background="white")                    # Aqui configuramos a cor.
jan.resizable(width=False, height=False)  # Aqui iremos limitar o tamanho da  janela.
jan.attributes("-alpha", 0.9)
jan.iconbitmap(default="icons/LogoIcon.ico")

#CARREGAR IMAGENS
logo = PhotoImage(file="icons/logo.png")

#------------wIDGETS------------------------------------------------------------------------------------------
LeftFrame = Frame(jan, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise") #Parametros de configuração de cor
LeftFrame. pack(side=LEFT)      #Parametros de definiçao de frame simples

RightFrame = Frame(jan, width=395, height=300, bg="MIDNIGHTBLUE", relief="raise") #Parametros de configuração de cor
RightFrame. pack(side=RIGHT)      #Parametros de definiçao de frame simples

LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE")  #Configurando label para logo ficar na esquerda
LogoLabel.place(x=-50, y=-15)
# Botão de Usuário e suas configurações de altura e posicionamento cor e fonte.
UserLabel = Label(RightFrame, text="Username:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
UserLabel.place(x=1, y=100)   #Configurações visuais do texto Username

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=175, y=113)
# Botão de senha e suas configurações de altura e posicionamento cor e fonte.
PassLabel = Label(RightFrame, text="Password:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
PassLabel.place(x=5, y=150)   #Configurações visuais do texto Username

PassEntry = ttk.Entry(RightFrame, width=30, show="*") 
PassEntry.place(x=150, y=160)


def Login():
    User = UserEntry.get()
    Pass = PassEntry.get()

    DataBaser.cursor.execute("""
    SELECT * FROM Users
    WHERE (User = ? and Password = ?)
    """, (User, Pass))
    print("Selecionou")
    VerifyLogin = DataBaser.cursor.fetchone()
    try:
        if (User in VerifyLogin and Pass in VerifyLogin):
            messagebox.showinfo(title="Login Info", message="Acesso Confirmado - Bem Vindo!")
    except:
        messagebox.showinfo(title="Login Info", message="Acesso Negado - Verifique seu Cadastro no sistema!")  
    
# Botões
LoginButton = ttk.Button(RightFrame, text="Login", width=30, command=Login)
LoginButton.place(x=100, y=225)

def Register():
    #Removendo Widgets de Login
     LoginButton.place(x=5000)
     RegisterButton.place(x=5000)
     #Inserindo Widgets de Cadastro
     NomeLabel = Label(RightFrame, text="Name:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
     NomeLabel.place(x=1, y=10)
    #Posigão geometrica do campo "Name"
     NomeEntry  = ttk.Entry(RightFrame, width=39)
     NomeEntry.place(x=95, y=24)

     EmailLabel = Label(RightFrame, text="Email:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
     EmailLabel.place(x=2, y=50)
     #Criar entry do Email
     EmailEntry = ttk.Entry(RightFrame, width=39)
     EmailEntry.place(x=95, y=66)

     def RegisterToDataBase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User =UserEntry.get()
        Pass = PassEntry.get()
        #colocando condições para os dados completos ser
        if (Name == "" and Email == "" and User == "" and Pass == ""):
            messagebox.showerror(title="Register Error", message="Não deixe de preencher todos os campos")
        else:        
            #import pdb 
            #pdb.set_trace()
            DataBaser.cursor.execute("""
            INSERT INTO Users(Name, Email, User, Password) VALUES(?, ?, ?, ?)
            """,(Name, Email, User, Pass))
            DataBaser.conn.commit()
            messagebox.showinfo(title="Register Info", message="Conta Criada Com Sucesso")

     Register = ttk.Button(RightFrame, text="Register", width=30, command=RegisterToDataBase)
     Register.place(x=100, y=225)
     

     def BackToLogin():
        #Removendo widget de cadastro
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000) 
        #Trazendo de volta os widgets de login
        LoginButton.place(x=5000)
        RegisterButton.place(x=125)


     Back = ttk.Button(RightFrame, text="Back", width=20, command=BackToLogin) 
     Back.place(x=125, y=260)

   




RegisterButton = ttk.Button(RightFrame, text="Register", width=20, command=Register)
RegisterButton.place(x=125, y=260)

 

jan.mainloop() 
#INSERT INTO Users(Name, Email, User, Password) VALUES('Jefte', 'jefte.lima.silva@gmail.com', 'jefinho', '1234');