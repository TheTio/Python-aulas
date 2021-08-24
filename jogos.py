
import forca
import adivinhacao

def jogar():
  print("---------------------------------")
  print("--------Bem Vindo ao jogo--------")
  print("---------------------------------")  
  print("---------Escolha um jogo---------")
  print("---------------------------------")  

  print(" (1) Forca || (2) Adivinhação ")

  jogo =  int(input("Qual jogo? "))

  if(jogo == 1):
    forca.jogar()
  elif(jogo == 2): 
    adivinhacao.jogar()

if(__name__ == "__main__"):
  jogar()