#!/usr/bin/env python
# coding: utf-8

# In[2]:


import json

login=[]
senha=[]

def cadastro():
    login_novo = input("Crie seu login")
    senha_novo = input("Crie sua senha")
    res = input("Repita a senha")
    if senha_novo == res and senha_novo != "" and login_novo != "":
        print("Cadastro feito com sucesso")
        login.append(login_novo)
        senha.append(senha_novo)
        with open('cadastro.json', 'w') as dados:
            json.dump({"login": login_novo, "senha": senha_novo}, dados)

    else:
        print("As informações não estão corretas")
    
    

def iniciar():
    log = input("digite o login")
    sen = input("digite a senha")
    with open('cadastro.json', 'r') as dados:
        cadastros = json.load(dados)
    if log == cadastros["login"] and sen == cadastros["senha"]:
        print(f"Login realizado. Bem vindo {log}")
    else:
        print("Login ou senha inválida")

print("Bem vindo, o que deseja?")
entrar = int(input("Pressione 1 para cadastrar e 2 para fazer login"))


if entrar == 1:
    cadastro()
elif entrar == 2:
    iniciar()
else:
    print("Escolha uma opção válida")


# In[ ]:




