from time import sleep
perguntas = ['telefonou para a vitima?', 'esteve no local do crime?',
             'mora perto da vítima?', 'tinha dívidas com a vítima?',
             'já trabalhou com a vítima?']
print('-='*40)
print(f'{"INTERROGANDO AS TESTEMUNHAS":^80}')
print('-='*40)
testemunhas = []
continua = ''
while continua != 'N':
    pontos = 0
    nome = input('Qual é o nome da testemunha a ser interrogada?').strip()
    print('\nPara que a analise possa ser realizada responda SIM ou NÃO\n')
    for pergunta in perguntas:
        resposta = input(f'{nome.split()[0]} {pergunta}').upper().strip()[0]
        if 'S' in resposta:
            pontos += 1
        sleep(0.2)
    print('\nAnalisando...\n')
    sleep(1)
    if pontos < 2:
        print('\033[1;32mTestemunha inocente.\033[m')
        analise = '\033[1;32mTestemunha inocente.\033[m'
    elif pontos == 2:
        print('\033[33mTestemunha suspeita.\033[m')
        analise = '\033[33mTestemunha suspeita.\033[m'
    elif pontos <= 4:
        print('\033[31mPossível cúmplice do Assassino.\033[m')
        analise = '\033[31mPossível cúmplice do Assassino.\033[m'
    elif pontos == 5:
        print('\033[1;31mAssassino\033[m')
        analise = '\033[1;31mAssassino\033[m'
    testemunhas.append([nome, pontos, analise])
    continua = input('\nAnalisar mais uma testemunha? [S/N]').strip().upper()[0]
    print()
print('-='*40)
print(f'{"RELATÓRIO DO INTERROGATÓRIO":^80}')
print('-='*40)
print(f'{"Nome":<25}{"Pontos":^5}{"Análise":^60}')
for p in testemunhas:
    print(f'{p[0]:<25}{p[1]:^5}{p[2]:^60}')