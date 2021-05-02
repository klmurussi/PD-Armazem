from classes import objetos
from tools.knapsack import knapsack

objs = objetos.Objetos()

while True:
    print("Digite a capacidade de volume do armazém: ")
    capacidade = input()
    try:
        capacidade = float(capacidade)
        break
    except:
        print("Valor inválido, digite apenas números.\n")

while True:
    print("\n1- Adicionar objeto\n2- Calcular quais deles vão para o armazem\n3- Encerrar o programa")
    escolha = input()

    try:
        escolha = int(escolha)
    except:
        print("Valor inválido, digite apenas números.\n")

    if escolha == 1:
        print("\nNome do objeto: ")
        nome = input()
        print("\nVolume de " + nome + ":")
        while True:
            volume = input()
            try:
                volume = int(volume)
                break
            except:
                print("Valor inválido, digite apenas números.\n")
        print("\nValor de " + nome + ":")
        while True:
            valor = input()
            try:
                valor = int(valor)
                break
            except:
                print("Valor inválido, digite apenas números.\n")
        objs.addObjeto(nome, volume, valor)

    elif escolha == 2:
        res = knapsack(capacidade, objs.objetos, len(objs.objetos))
        print('\nMaior valor possível:')
        print(res)
        print('Objetos adicionados:')
        res[1].print()
        print('Volume restante: ')
        print(res[2])
    elif escolha == 3:
        break
    else:
        print("Digite 1 ou 2.\n")
