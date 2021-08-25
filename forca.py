import random


def jogar():

  mensagem_de_abertura()
  palavra_secreta = carregar_palavra_secreta()
 
  letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

  enforcou = False
  acertou = False
  erros = 0

  print(letras_acertadas)

  while(not enforcou and not acertou):
    
    chute = pede_chute()
   
    if(chute in palavra_secreta):
      marca_chute_correto(chute,letras_acertadas,palavra_secreta)
    else:
      erros += 1

    enforcou = erros == 6
    acertou = "_" not in letras_acertadas

    print(letras_acertadas)
    print("---------------------------------")

  if(acertou):
    mensagem_vencedor()
  else:
    mensagem_perdedor(palavra_secreta)

def mensagem_vencedor():
    print("Você Ganhou!")

def mensagem_perdedor(palavras_secreta):
    print("Você Perdeu!")
    print(f"A palavra era {palavras_secreta}")

  

def marca_chute_correto(chute,letras_acertadas,palavra_secreta):
  index = 0
  for letra in palavra_secreta:
    if(chute == letra):
      letras_acertadas[index] = letra
    index +=  1

def pede_chute():
  chute = input("Escolha uma letra: ")
  chute= chute.strip().upper()
  print("---------------------------------")
  return chute 

def mensagem_de_abertura():
  print("---------------------------------")
  print("---Bem Vindo ao jogo da Forca!---")
  print("---------------------------------")

def carregar_palavra_secreta():

  arquivo = open("palavras.txt", "r")
  palavras = []

  for linha in arquivo:
    linha = linha.strip()
    palavras.append(linha)

  arquivo.close()

  numeros = random.randrange(0,len(palavras))
 

  palavra_secreta = palavras[numeros].upper()
  return palavra_secreta

def inicializa_letras_acertadas(palavra):
  lista = ['_' for letra in palavra]
  return lista

if(__name__ == "__main__"):
  jogar()