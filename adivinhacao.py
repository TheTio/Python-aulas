import random

def jogar():

  print("---------------------------------")
  print("Bem Vindo ao jogo de Adivinhação!")
  print("---------------------------------")

  numero_secreto = random.randrange(1,101)
  total_de_tentativas = 0
  pontos = 1000

  print("Qual nível de dificuldade?")
  print(" (1) Fácil | (2) Médio | (3) Difícil ")

  nivel = int(input("Define o Nível: "))

  if (nivel == 1):
    total_de_tentativas = 20
  elif (nivel == 2):
    total_de_tentativas = 10
  elif (nivel == 3):
    total_de_tentativas = 5
  else:
    print("ERRO! Opção Invalida!")

  for rodada in range(1, total_de_tentativas + 1):
    print(f"Tentativa {rodada} de {total_de_tentativas}")
    chute = int(input("Digite um Número entre 1 e 100: "))
    print("Você Digitou: ", chute)

    if (chute < 1 or chute > 100):
      print("Você deve digitar um número entre 1 e 100!")
      continue

    acertou = chute == numero_secreto
    maior   = chute >  numero_secreto
    menor   = chute <  numero_secreto 

    if (acertou):
      print("Parabéns, Você Acertou!")
      print(f"E Você fez {pontos} Pontos!")
      break
    else :
      pontos_perdidos = abs(numero_secreto - chute)
      pontos = pontos - pontos_perdidos
      if ( maior ):
        print("Você Errou! O seu chute foi maior do que o Número Secreto")
        if(rodada == total_de_tentativas):
          print(f"O Número secreto era {numero_secreto}. Você fez {pontos}")
      elif( menor ):
        print("Você Errou! O seu chute foi menor do que o Número Secreto")
        if(rodada == total_de_tentativas):
          print(f"O Número secreto era {numero_secreto}. Você fez {pontos}")

  print("Fim de Jogo")

if (__name__ == "__main__"):
  jogar()