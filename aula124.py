# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

#Resolução

for pergunta in perguntas:
    print(pergunta['Pergunta'])

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(pergunta['Opções']):
        print(f'{i})',opcao)
        
    escolha = input('Escolha a opção: ')
    escolha = int(escolha)

    if opcoes[escolha] == pergunta['Resposta']:
        print('Voce acertou!')
    else:
        print("Você errou.")