from random import choices
import json

# Leitura de palavras do banco de dados
arquivoDePalavras = open('palavras.json')
palavras = json.load(arquivoDePalavras)
arquivoDePalavras.close()

palavraEscolhida = choices(palavras, k=1)[0]

acertos = []
erros = []

quantErros = 0

def inicio():
  print('=========================')
  print('===== Jogo da Forca =====')
  print('=========================')

  print('Digite: ')
  print('[1] Jogar ')
  print('[0] Sair')

  escolha = input()

  if escolha == '1':
    return jogo()

  return sair()

def desenhaForca():
  global quantErros
  cabeca = 'O' if quantErros > 0 else ' '
  
  corpo = '|' if quantErros > 1 else ' '
  bracoE = '/' if quantErros > 2 else ' '
  bracoD = '\\' if quantErros > 3 else ' '

  pernaE = '/' if quantErros > 4 else ' '
  pernaD = '\\' if quantErros > 5 else ' '
  
  print(' ______')
  print('|      |')
  print('|      {}'.format(cabeca))
  print('|     {}{}{}'.format(bracoE, corpo, bracoD))
  print('|     {} {}'.format(pernaE, pernaD))
  print('|')

def desenhaPalavra():
  ganhou = True
  print('\n')
  for letra in palavraEscolhida:
    if letra in acertos:
      print(f' {letra}', end='')
    else:
      print(' _', end='')
      ganhou = False

  return ganhou
    
def jogo():
  global quantErros
  desenhaForca()
  
  if desenhaPalavra():
    return ganhou()  

  if quantErros > 5:
    return perdeu()

  # Mostra letras que o usuario errou
  print('\n')
  for i in erros:
    print(i, ' ', end='')
  
  palpite = input('\n\nChute uma letra: ').upper()

  if palpite in erros or palpite in acertos:
    print('Você já testou essa letra')
    return jogo()

  if palpite in palavraEscolhida:
    acertos.append(palpite)
  else:
    erros.append(palpite)
    quantErros += 1

  return jogo()

def jogarNovamente():
  global palavraEscolhida
  global acertos
  global erros
  global quantErros
  
  escolha = input('Deseja jogar denovo? (S/N) ').upper()
  
  if escolha == 'S':
    palavraEscolhida = choices(palavras, k=1)[0]

    acertos = []
    erros = []
    
    quantErros = 0
    return jogo()
  
  return sair()

def perdeu():
  print('\n\nDeu forca!\n')
  return jogarNovamente()

def ganhou():
  print('\n\nParabéns você ganhou!')
  return jogarNovamente()

def sair():
  print('\n\nObrigado por jogar!')
  return

inicio()