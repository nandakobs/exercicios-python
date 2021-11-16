import response
dicio = response.response
estados = response.estados1


def check_email(email=''):
    """
    Retira todos os acentos e espaços do email, e deixa todas as letras em minusculo.
    """
    a = email.lower().replace(' ', '')
    a = a.replace('á', 'a').replace('ã', 'a').replace('é', 'e').replace('ê', 'e').replace('í', 'i')
    return a


print(f'Input: {dicio}')
for lista in dicio['usuarios']:

    lista['Estado'] = estados[lista['Estado']]

    for k, v in enumerate(lista):
        if lista[v] == 'desconhecido':
            lista[v] = None

    if lista['email'] is None:
        nome = lista['nome completo'].split()
        lista['email'] = check_email(f'{nome[0]}.{nome[-1]}@gmail.com')
    else:
        lista['email'] = check_email(lista['email'])

    for k, lang in enumerate(lista['cursos']):
        if lang == 'A melhor linguagem do mundo':
            lista['cursos'][k] = 'Python'

    if lista['CEP'] is not None:
        lista['CEP'] = int(f'{lista["CEP"]}0')

    cursos = lista['cursos'].copy()
    lista['cursos'] = {'Quantidade de cursos': len(cursos),
                       'Aluno Aplicado': len(cursos) > 2,
                       'Aluno da melhor professora': 'Python' in cursos,
                       'cursos do aluno': 0 if len(cursos) == 0 else cursos}
print('=' * 30)
print(f'Output: {dicio}')