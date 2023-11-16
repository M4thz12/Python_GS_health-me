
# explicação do app

# pedir o cadastro 
print('Já tem cadastro no app? (sim/não)')
resp = input(':')
if resp == sim:
    print('Vamos fazer o seu cadastro.')
    print('Digite seu nome:')
    nome_usuario = input(':')
    

    print('Digite seu email')
    email_usario = input(':')
    if "@" not in email_usario:
        print("Email inválido")
    print('A senha deve ter pelo menos 1 numero e uma letra maiuscula')
    print('Digite sua senha')
    senha_usuario = input(':')



    
    print(f'Bem vindo {nomeusuario}')
    print('Agora vamos colher alguns dados para achar sua melhor opção de dieta.')
    print('Qual a sua altura? (em cm)')
    altura_usuario = int(input(':'))
    print('Qual a seu peso? (em kg)')
    peso_usuario = float(input(':'))
    print('Qual o seu sexo?')
    sexo_usuario = input(':')
    print('Pratica algum exercício?')
    exercicio_usuario = input(':')
    if exercicio_usuario == sim or ss or s or si:
        print('Qual a frequência dos exercícios')
    print('Qual o seu objetivo com este app?')
    