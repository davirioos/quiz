perguntas = {
    'Pegunta 1':
        {
            'peguntapc': 'Quanto é 2 + 2 ?',
            'alternativas': {'A': '1', 'B': '2', 'C': '3', 'D': '4'},
            'resposta_correta': 'D'
        },
    'Pegunta 2':
        {
            'peguntapc': 'Quanto é 2 + 2 ?',
            'alternativas': {'A': '1', 'B': '2', 'C': '3', 'D': '4'},
            'resposta_correta': 'D'
        },
    'Pegunta 3':
        {
            'peguntapc': 'Quanto é 2 + 2 ?',
            'alternativas': {'A': '1', 'B': '2', 'C': '3', 'D': '4'},
            'resposta_correta': 'D'
        },
    'Pegunta 4':
        {
            'peguntapc': 'Quanto é 2 + 2 ?',
            'alternativas': {'A': '1', 'B': '2', 'C': '3', 'D': '4'},
            'resposta_correta': 'D'
        },
    'Pegunta 5':
        {
            'peguntapc': 'Quanto é 2 + 2 ?',
            'alternativas': {'A': '1', 'B': '2', 'C': '3', 'D': '4'},
            'resposta_correta': 'D'
        }
}

vida = 3

for perguntando, valor in perguntas.items():
    print(f'{perguntando}\n{valor["peguntapc"]}')

    for alt, resp in valor['alternativas'].items():
        print(alt, resp)

    usuarioResponde = input('Qual Alternativa esta Correta ?').upper()

    if usuarioResponde == valor['resposta_correta']:
        print('Parabens Vamos para Proxima \n')

    else:
        vida -= 1
        print(f'Errado Acabou de Perde 1 Vida, restam : {vida} \n')
        if vida == 0:
            print('Você perdeu')
            break