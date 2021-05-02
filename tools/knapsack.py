from classes.objetos import Objetos


def knapsack(capacidade, objetos, qtdObjetos):
    capacidade = int(capacidade)
    K = [[0 for x in range(capacidade+1)] for x in range(qtdObjetos+1)]
    for objetoAtual in range(1, qtdObjetos+1):
        for volumeAtual in range(1, capacidade+1):
            if volumeAtual >= objetos[objetoAtual-1].volume:
                """ caso o volume atual da iteração seja maior do que o volume do objeto atual """
                """ realiza o calculo da equação de Bellman, selecionando o maior entre o """
                """ o valor para o objeto anterior naquele volume, ou a adição do novo objeto """
                """ removendo o seu volume do volume atual """
                K[objetoAtual][volumeAtual] = max(objetos[objetoAtual-1].valor
                                                  + K[objetoAtual-1][volumeAtual -
                                                                     objetos[objetoAtual-1].volume],
                                                  K[objetoAtual-1][volumeAtual])
            else:
                """ caso o volume atual da iteração seja menor do que o volume do objeto atual """
                """ seleciona o valor do objeto anterior para aquele volume pois não é """
                """ possível adicionar outro objeto"""
                K[objetoAtual][volumeAtual] = K[objetoAtual-1][volumeAtual]
    res = findSolution(objetos, K, qtdObjetos, capacidade)
    return (K[qtdObjetos][capacidade], res[0], res[1])


def findSolution(objetos, matrizRes, qtdObj, capacidade):
    res = matrizRes[qtdObj][capacidade]
    resObjs = Objetos()
    qtdObs = qtdObj
    cap = capacidade
    while ((cap != 0) and (qtdObs-1 > 0)):
        if res == matrizRes[qtdObs-1][cap]:
            qtdObs -= 1
        else:
            if(cap - objetos[qtdObs-1].volume > 0):
                resObjs.add(objetos[qtdObs-1])
                cap -= objetos[qtdObs-1].volume
                qtdObs -= 1
            else:
                return (resObjs, cap)
    return (resObjs, cap)
