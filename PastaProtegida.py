import customtkinter as ctk
import os 
import subprocess

#pastas protegidas
PASTA_PROTEGIDA = "CAMINHO DA PASTA"
USUARIO_PADRAO = 'USUARIO'
SENHA_PADRAO = 'SENHA'
#configuração da tela
ctk.set_appearance_mode('dark')

#criação das funções de funcionalidades
def abrir_pasta():
    if os.path.exists(PASTA_PROTEGIDA):
        if os.name == 'nt':  # Windows
            os.startfile(PASTA_PROTEGIDA)
        elif os.name == 'posix':  # macOS e Linux
            subprocess.run(['open', PASTA_PROTEGIDA])
    else:
        resultadoLogin.configure(text='Pasta não encontrada!', text_color='red')

#----------------------#

def validarLogin():
    usuario = campoEntryUsuario.get()
    senha = campoEntrySenha.get()
    #verificar o usuario
    if usuario == 'USUARIO' and senha == 'SENHA':
        resultadoLogin.configure(text='login feito com sucesso',text_color='green')
        app.after(1000, app.destroy)
        abrir_pasta()
    else:
        resultadoLogin.configure(text='login não realizado', text_color='red')
                                 

#criação da janela principal
app = ctk.CTk()
app.title('Acesso Protegido')
app.geometry('300x300')

#criação dos campos
#label usuario
campoLabelUsuario = ctk.CTkLabel(app, text='Usuario')
campoLabelUsuario.pack(pady=10)

#entry usuario
campoEntryUsuario = ctk.CTkEntry(app, placeholder_text='digite seu usuario')
campoEntryUsuario.pack(pady=10)

#label senha
campoLabelSenha = ctk.CTkLabel(app, text='Senha')
campoLabelSenha.pack(pady=10)

#entry senha
campoEntrySenha = ctk.CTkEntry(app, placeholder_text='digite sua senha', show='*')
campoEntrySenha.pack(pady=10)

#button
botaoLogin = ctk.CTkButton(app, text='login', command=validarLogin)
botaoLogin.pack(pady=10)
                
#campo feedback de login
resultadoLogin = ctk.CTkLabel(app, text='')
resultadoLogin.pack(pady=10)

#iniciar aplicação
app.mainloop()