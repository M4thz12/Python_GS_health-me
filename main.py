import funcoes
import json
import os
print('Bem vindo ao projeto Health-me')
print('Estamos desenvolvendo um app para auxiliar as pessoas montando uma dieta')
print('temos 2 opções, você pode ler um pouco sobre como nosso projeto funciona, ou ver o aplicativo na pratica, com a coleta de dados e exibindo os seus resultados')
print('Faça sua escolha,  explicação do projeto(1) ou Aplicativo funcionando(2)')
escolha = int(input(':'))
# explicação do app

# pedir o cadastro 
while escolha == 2:
    print('Já tem cadastro no app? (s/n)')
    resposta_cadastro = input(':').lower()
    while resposta_cadastro != 's' and resposta_cadastro != 'n':
        print('insira uma resposta valida => (s/n)')
        resposta_cadastro = input(':').lower()
    if resposta_cadastro == 'n':
        print('Vamos fazer o seu cadastro.')
        print('Digite seu nome:')
        nome_usuario = input(':')
        if  funcoes.verifica_numero(nome_usuario) == True:
            print('O nome não pode conter numeros')
            break
        print('Digite seu email')
        email_usario = input(':')
        if funcoes.verifica_email(email_usario) == True:
            break


        print('A senha deve ter pelo menos um numero e uma letra maiuscula')
        print('Digite sua senha')
        senha_usuario = input(':')
        
        
        if funcoes.verifica_maiuscula(senha_usuario) == False:
            print('Senha precisa de pelo menos 1 letra maiuscula')
            break
        if  funcoes.verifica_numero(senha_usuario) == False:
            print('A senha precisa ter pelo menos 1 numero')
            break
        usuario_dados = {"nome": nome_usuario, "email": email_usario, "senha": senha_usuario}
        funcoes.salvar_em_json(usuario_dados)
    resposta_cadastro = 's'
    
    while resposta_cadastro != 's' and resposta_cadastro != 'n':
        print('insira uma resposta valida => (s/n)')
        resposta_cadastro = input(':').lower()
    if resposta_cadastro == 's':

        print('Você já realizou o cadastro, agora vamos logar')
        print('Digite o seu email, para logar')
        email_logar = input(':')
        
        print('Digite a sua senha, para logar')
        senha_logar = input(':')

        if funcoes.verifica_usuario(email_logar, senha_logar):
            print('Login incorreto!')
            break
        
        # print(f'Bem vindo {nomeusuario}')
        # print('Agora vamos colher alguns dados para achar sua melhor opção de dieta.')
        # print('Qual a sua altura? (em cm)')
        # altura_usuario = int(input(':'))
        # print('Qual a seu peso? (em kg)')
        # peso_usuario = float(input(':'))
        # print('Qual o seu sexo?')
        # sexo_usuario = input(':')
        # print('Pratica algum exercício?')
        # exercicio_usuario = input(':')
        # if exercicio_usuario == sim or ss or s or si:
        #     print('Qual a frequência dos exercícios')
        # print('Qual o seu objetivo com este app?')
    