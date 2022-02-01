with open('exe.txt', 'a+') as file:
    while True:
        print('1 - Ver pessoas cadastradas')
        print('2 - cadastrar nova pessoa')
        print('3 - Sair do sistema')
        op = str(input('Digite sua opção: '))
        if op == '1':
            file.seek(0)
            print(file.read())
        if op == '2':
            nome = str(input('Digite o nome: '))
            idade = str(input('Digite a idade: '))
            if idade.isnumeric() != True:
                while True:
                    print('Digite uma idade valida')
                    idade = str(input('Digite a idade: '))
                    if idade.isnumeric():
                        break
            file.write(f'\n\t{nome:<15} \t{idade:>3} anos')
            print('Pessoa cadastrada com sucesso')
        if op == '3':
            print('Tenha um otimo dia')
            break
        if op not in '1 2 3':
            print('\033[31m Digite um numero valido \033[m')
            continue


