import funcoes
import json
import os
from funcoes import verifica_usuario

print('Bem vindo ao projeto Health-me')
print('Estamos desenvolvendo um app para auxiliar as pessoas montando uma dieta')
print('temos 2 opções, você pode ler um pouco sobre como nosso projeto funciona, ou ver o aplicativo na pratica, com a coleta de dados e exibindo os seus resultados')
print('Faça sua escolha,  explicação do projeto(1) ou Aplicativo funcionando(2)')
escolha = int(input(':'))
# explicação do app

# Explicação do projeto
while escolha == 1:
    print('Aqui está a explicação do projeto')
    print('Faça Sua Escolha:')
    print('Problema (1)')
    print('Introdução (2)')
    print('Projeto (3)')
    print('Objetivo do Projeto (4)')
    escolhadentro1 = input(':').lower()

    if escolhadentro1 == "1" or escolhadentro1 == "problema":
        print('Problema:')
        print('As doenças cardiovasculares, principal causa de morte global, estão fortemente ligadas a uma alimentação inadequada, especialmente o consumo excessivo de gorduras saturadas e trans. Promover hábitos alimentares saudáveis, com uma dieta equilibrada, é crucial para prevenir essas doenças. Além disso, dados recentes da Pesquisa Vigitel apontam um aumento alarmante no excesso de peso no Brasil, atingindo 55,7% da população em 2019, comparado a 42,6% em 2006. O excesso de peso é mais prevalente entre os jovens de 18 a 24 anos, exigindo abordagens educativas e preventivas desde cedo. Essas tendências destacam a urgência de ações para reduzir fatores de risco e promover a saúde cardiovascular e o controle do peso.')
        input('\n<aperte enter para continuar>')
        puxei = "decisão"

    if escolhadentro1 == "2" or escolhadentro1 == "introdução" or escolhadentro1 == "introducao":
        print('Introdução:')
        print('Identificamos que muitos brasileiros desejam melhorar seus hábitos alimentares, mas enfrentam dificuldades na criação de uma dieta equilibrada. Para abordar esse desafio, concebemos um inovador aplicativo focado em orientar usuários a alcançar uma alimentação saudável, considerando objetivos específicos. O aplicativo oferecerá opções personalizadas para ganho de massa muscular, perda de gordura ou manutenção da saúde, indo além de simples recomendações ao incluir sugestões de refeições práticas e deliciosas, adaptadas às preferências e situação financeira de cada usuário. A abordagem prática e econômica visa tornar a adoção de hábitos alimentares saudáveis mais acessível e sustentável, contribuindo para a promoção da saúde e bem-estar em larga escala.')
        input('\n<aperte enter para continuar>')
        puxei = "decisão"

    if escolhadentro1 == "3" or escolhadentro1 == "projeto":
        print('Projeto:')
        print('O aplicativo proporcionará uma experiência personalizada desde o início, com um cadastro detalhado que inclui informações como altura, peso, idade, gênero biológico e objetivos de saúde. Utilizando a bioimpedância para uma avaliação precisa, o aplicativo calcula o gasto calórico individualizado, estabelecendo uma base sólida para criar uma dieta personalizada. A extensa biblioteca de alimentos abrange dados nutricionais, permitindo recomendações balanceadas de macronutrientes e calorias, com orientações sobre o timing de consumo. Os usuários podem personalizar o plano alimentar indicando preferências, restrições e exceções, garantindo sustentabilidade a longo prazo. A integração com dispositivos como smartwatches, via Wi-Fi, possibilita monitoramento contínuo do gasto calórico e adaptação dinâmica do plano alimentar. O aplicativo também analisa a região do usuário para oferecer recomendações fundamentadas de produtos, propondo alternativas com base em parcerias estratégicas com empresas de entrega, visando otimizar a eficiência no processo de compras. Essa abordagem holística visa não apenas atender às necessidades nutricionais, mas também aprimorar a saúde geral do usuário, considerando fatores como pressão arterial e condições ambientais.')
        input('\n<aperte enter para continuar>')
        puxei = "decisão"

    if escolhadentro1 == "4" or escolhadentro1 == "objetivo do projeto" or escolhadentro1 == "objetivo":
        print('Objetivo do Produto')
        print('Nosso objetivo central é desenvolver um aplicativo funcional, intuitivo e personalizado, com a missão primordial de capacitar os usuários na adoção de hábitos alimentares saudáveis. Buscamos não apenas reduzir significativamente os riscos de doenças cardiovasculares, mas também criar uma plataforma que promova de maneira sustentável a melhoria na qualidade de vida. Através de recursos interativos e adaptáveis, nosso foco vai além de fornecer orientações nutricionais personalizadas; almejamos promover uma educação alimentar abrangente, capacitando os usuários a fazerem escolhas informadas que impactem positivamente sua saúde. Acreditamos que ao atingir esses objetivos, nosso aplicativo se destacará como uma ferramenta indispensável para a promoção de hábitos alimentares saudáveis, contribuindo não apenas para a prevenção de doenças cardiovasculares, mas também para uma mudança positiva e duradoura nos padrões alimentares, resultando em uma população mais saudável e consciente.')
        input('\n<aperte enter para continuar>')
        puxei = "decisão"

        
    if puxei == "decisão":
        print('Deseja continuar? (s/n)')
        esco = input(':').lower()
        while esco != 's' and esco != 'n':
            print('Insira uma resposta válida => (s/n)')
            esco = input(':').lower()

    if esco == 's':
        continue
    elif esco == 'n':
        print('Escolha: explicação do projeto (1) ou Aplicativo funcionando (2)')
        escolha = int(input(':'))

    
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
        
        print('Agora vamos coletar alguns dados atualizados para montar a sua dieta.')
        print('')
        print('Quantos anos você tem?')
        idade_usuario = int(input(':'))
        print('Qual a sua altura? (em cm)')
        altura_usuario = int(input(':'))
        print('Qual a seu peso? (em kg)')
        peso_usuario = float(input(':'))
        print('Qual o seu sexo biologico? (masculino/feminino)')
        sexo_usuario = input(':').lower()
        while sexo_usuario != 'masculino' and sexo_usuario != 'feminino':
            print('Por favor insira um dos seguintes tipos de genero: Masculino ou Feminino ')
            print('Qual o seu sexo biologico? (masculino/feminino)')
            sexo_usuario = input(':').lower()
        
        print('\nQual o seu nivel de exercicio?')
        print('sedentario/nenhuma vez na semana(1)')
        print('levemente ativo/1 ou 2 vezes na semana(2)')
        print('moderadamente ativo/3 ou 4 vezes na semana(3)')
        print('altamente ativo/5 até 7 vezes na semana(4) ')
        print('intensamente ativo/ atividades muito instensas ou 2x por dia(5)')
        quantidade_exercicios_usuario = int(input(':'))
        
        usuario_dados = {"email":email_logar,"idade": idade_usuario, "peso": peso_usuario, "altura": altura_usuario, "sexo": sexo_usuario, "quantidade_exercicios": quantidade_exercicios_usuario}
        funcoes.adiciona_dados_usuario(usuario_dados)
        
        if sexo_usuario == 'masculino':
            tx_basal = 66 + (13.8*peso_usuario) + (5*altura_usuario) - (6.8*idade_usuario)
        if sexo_usuario == 'feminino':
            tx_basal = 655 + (9.6 * peso_usuario) + (1.8*altura_usuario) - (4.7*idade_usuario)
        print(f'\nCom os dados, calculasmos a sua taxa metabolica basal, e o resultado foi de {tx_basal}')
        print('A taxa metabolica basal refere-se à quantidade mínima de energia que o corpo humano necessita em repouso absoluto para manter funções vitais, como a respiração, circulação sanguínea, manutenção da temperatura corporal e funcionamento de órgãos vitais, como o coração, fígado e cérebro. Em outras palavras, é a quantidade de calorias que o corpo queima quando está em completo repouso.')
        print('\nPorém a taxa metabolica basal, deve ser multiplicada pela quantidade de vezes que a pessoa faz exercicio, pois ja aumenta o gasto calorico da pessoa')
        
        if quantidade_exercicios_usuario == 1:
            tx_basal = tx_basal*1.2
        elif quantidade_exercicios_usuario == 2:
            tx_basal = tx_basal*1.375
        elif quantidade_exercicios_usuario == 3:
            tx_basal = tx_basal*1.55
        elif quantidade_exercicios_usuario == 4:
            tx_basal = tx_basal*1.725
        elif quantidade_exercicios_usuario == 5:
            tx_basal = tx_basal*1.9
        print(f'Diariamente você tem um gasto calorico de {tx_basal}')    
        print('\nAgora, vamos montar a sua dieta')
        print('Qual é o seu objetivo')
        print('Emagrecer(1)')
        print('Ganho de massa(2)')
        print('manter opeso(3)')       
        objetivo_usuario = int(input(':'))
        if objetivo_usuario == 1:
            calorias_da_dieta = tx_basal - 500
        if objetivo_usuario == 2:
            calorias_da_dieta = tx_basal 
        if objetivo_usuario == 3:
            calorias_da_dieta = tx_basal + 500
        print(f'você recebera uma dieta de {calorias_da_dieta} calorias por dia')
       
        print(f'\nvocê deve distribuir sua alimentação em 5 refeições')
        print('1 - café da manhã')
        print('2 - lanche da manhã') 
        print('3 - almoço')
        print('4 - lanche da tarde')
        print('5 - janta')
        
        print('\nPodemos também reduzir a quantidade de alimento nas refeições e adicionar outras duas refeições, o pré-treino e o pós-treino')
        if quantidade_exercicios_usuario != 1:
            print('No seu caso, como você não pratica exercicio, pode manter apenas as 5 refeições')
        else:
            print('\nDevido a sua pratica de exercícios, você vai adicionar o pré-treino e o pós-treino')
            print('O pré-treino, deve ser composto principalmente por carboidrato, como fonte de energia')
            print('O pós-treino, deve ser composto principalmente pro proteina para a recuperação muscular')

        print('\nPara calcular o consumo diário nescessário de proteina, fazemos 1.2g x o peso da pessoa')
        print('Quando já se tem uma quatidade de exercícios razoável, pode ter uma dieta hipercalorica, sendo 1.6 x o seu peso ')
        print('Porém Fisiculturistas devem ter um consumo maior para sua recuperação muscular, então deve ser de 2.2 x o seu peso')
        if quantidade_exercicios_usuario == 5:
            proteina = 2.2*peso_usuario
            print(f'\nPortanto, o seu consumo de proteina deve ser de {proteina}g diariamente')
        if quantidade_exercicios_usuario < 5 and quantidade_exercicios_usuario > 2:
            proteina = 1.6*peso_usuario
            print(f'\nPortanto, o seu consumo de proteina deve ser de {proteina}g diariamente')
        if quantidade_exercicios_usuario < 3:
            proteina = 1.2*peso_usuario
            print(f'\nPortanto, o seu consumo de proteina deve ser de {proteina}g diariamente')
        
        print('\nO Carboidrato equivale a 50% da sua alimentação')
        print(f'Sendo assim você deve consumir {calorias_da_dieta/2} calorias em carboidratos')
        

        carboidratos = (calorias_da_dieta/2)/4
        lipideos = (calorias_da_dieta/2)/9 - proteina
        print(f'\nsua dieta é composta por:')
        print(f'{proteina} gramas de proteina')
        print(f'{carboidratos} gramas de carboidratos')
        print(f'{lipideos} gramas de lipideos')
        print(f'\n distribuindo ao longo do dia fica:')
        if quantidade_exercicios_usuario == 1:
            print(f'No café da manhã:')
            print(f'{proteina/4} gramas de proteina\n {carboidratos/4} gramas de carboidratos\n {lipideos/4} gramas de lipideos')
            print(f'No lanche da manhã:')
            print(f'{proteina/10} gramas de proteina\n {carboidratos/10} gramas de carboidratos\n {lipideos/10} gramas de lipideos')
            print(f'No almoço:')
            print(f'{proteina/3.3} gramas de proteina\n {carboidratos/3.3} gramas de carboidratos\n {lipideos/3.3} gramas de lipideos')
            print(f'No lanche da tarde:')
            print(f'{proteina/10} gramas de proteina\n {carboidratos/10} gramas de carboidratos\n {lipideos/10} gramas de lipideos')
            print(f'Na janta:')
            print(f'{proteina/4} gramas de proteina\n {carboidratos/4} gramas de carboidratos\n {lipideos/4} gramas de lipideos')
        else:
            print(f'No café da manhã:')
            print(f'{proteina/5} gramas de proteina\n {carboidratos/5} gramas de carboidratos\n {lipideos/5} gramas de lipideos')
            print(f'No lanche da manhã:')
            print(f'{proteina/10} gramas de proteina\n {carboidratos/10} gramas de carboidratos\n {lipideos/10} gramas de lipideos')
            print(f'No almoço:')
            print(f'{proteina/4} gramas de proteina\n {carboidratos/4} gramas de carboidratos\n {lipideos/4} gramas de lipideos')
            print(f'No lanche da tarde:')
            print(f'{proteina/10} gramas de proteina\n {carboidratos/10} gramas de carboidratos\n {lipideos/10} gramas de lipideos')
            print(f'Na janta:')
            print(f'{proteina/5} gramas de proteina\n {carboidratos/5} gramas de carboidratos\n {lipideos/5} gramas de lipideos')
            print(f'No pré-treino:')
            print(f'{proteina/13.4} gramas de proteina\n {carboidratos/13.4} gramas de carboidratos\n {lipideos/13.4} gramas de lipideos')
            print(f'No pó-treino:')
            print(f'{proteina/13.4} gramas de proteina\n {carboidratos/13.4} gramas de carboidratos\n {lipideos/13.4} gramas de lipideos')
            
        print(f'Agora vamos calcular o quanto de agua, você de beber')
        agua = 35 * peso_usuario
        print(f'Devido ao seu peso, você deve tomar {agua}ml de agua')
        if quantidade_exercicios_usuario != 1:
            print(f'Como você pratica exercicios deve se aumentar 500ml, sendo assim {agua + 500}ml')
        print('em dias quentes deve se adicionar mais 700ml')
        print('para avisa-lo diariamente se deve ou não aumentar a quantidade de agua nosso aplicatvo se conectou com seu smart watch')
        import random
        print('****criando situação hipotetica****')
        clima = random.randint(5,35)
        print(f'Hoje a temperatura está em {clima} graus')
        if clima > 19:
            print('Como o clima está quente, você deve tomar mais 700ml')
        else:
            print('como o clima está mais frio não é preciso tomar mais agua')
                    
        print('muito obrigado pelo uso do aplicativo, esperamos ter ajudado a montar a sua dieta')
        print('atualise os seus dados e monte uma nova para atingir o seu peso ideal')
        break