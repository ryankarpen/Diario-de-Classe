def menu():
    print('-=-'*20)
    print('{:^50}'.format('DIÁRIO DE CLASSE'))
    print('-=-' * 20)
    print('\033[33m1\033[m - \033[34mCadastrar notas de um aluno\033[m ')
    print('\033[33m2\033[m - \033[34mMostrar notas dos alunos cadastrados\033[m')
    print('\033[33m3\033[m - \033[34mSair do sistema\033[m')
    print('-=-'*20)


def verificadorint(msg):
    while True:
        try:
            texto = int(input(msg))
        except ValueError:
            print('\033[31mERRO! Escolha apenas um valor inteiro nesse campo.\033[m')
            continue
        else:
            return texto


def verificadorfloat(msg):
    while True:
        try:
            texto = float(input(msg))
        except ValueError:
            print('\033[31mERRO! Informe apenas números nesse campo.\033[m')
            continue
        else:
            return texto


cadastro = dict()
lista = list()
while True:
    menu()
    cadastro = {}
    resp = verificadorint('Opção escolhida:')
    if resp == 3:
        break
    elif resp == 1:
        cadastro['aluno'] = str(input('Informe o nome do usuário:'))
        cadastro['nota1'] = verificadorfloat('Informe a nota da primeira avaliação:')
        cadastro['nota2'] = verificadorfloat('Informe a nota da segunda avaliação:')
        cadastro['nota3'] = verificadorfloat('Informe a nota da terceira avaliação:')
        cadastro['média'] = (cadastro['nota1'] + cadastro['nota2'] + cadastro['nota3'])/3
        lista.append(cadastro.copy())
    elif resp == 2:
        print('Aluno      Prova1      Prova2     Prova3      Média final')
        for c in lista:
            print(f'{c["aluno"]}        {c["nota1"]}        {c["nota2"]}        {c["nota3"]}        {c["média"]:.2f}')




