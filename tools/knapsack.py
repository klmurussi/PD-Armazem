def knapsack(capacidade, objetos, size):
    capacidade = int(capacidade)
    K = [[0 for x in range(capacidade + 1)] for x in range(size + 1)]
    for i in range(size + 1):
        for w in range(capacidade + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif objetos[i-1].volume <= w:
                K[i][w] = max(objetos[i-1].valor
                              + K[i-1][w-objetos[i-1].volume],
                              K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    return K[size][capacidade]
