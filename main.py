from classes import objetos

while True:
  print("Digite a capacidade de volume do armazém: ")
  capacidade = input()
  try:
    capacidade = float(capacidade)
    break;
  except:
    print("Valor inválido, digite apenas números.\n")

while True:
  obj = objetos.Objetos()
  print("\n1- Adicionar objeto\n2- Calcular quais deles vão para o armazem\n3- Encerrar o programa")
  escolha = input()

  try: 
    escolha = int(escolha)
  except:
    print ("Valor inválido, digite apenas números.\n")

  if escolha == 1:
    print ("\nNome do objeto: ")
    nome = input ()
    print ("\nVolume de " + nome + ":")
    while True:
      volume = input ()
      try: 
        volume = float(volume)
        break;
      except:
        print ("Valor inválido, digite apenas números.\n")
    print("\nValor de " + nome + ":")
    while True:
      valor = input ()
      try: 
        valor = float(valor)
        break;
      except:
        print ("Valor inválido, digite apenas números.\n")
    obj.addObjeto(nome, volume, valor)

  elif escolha == 2:
    obj.printar()
  elif escolha == 3:
    break;
  else:
    print ("Digite 1 ou 2.\n")
