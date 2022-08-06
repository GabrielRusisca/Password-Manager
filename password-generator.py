#! python3
import secrets as sc, pyperclip
from sys import exit
from random import shuffle

def true_false(txt: str) -> int:
    """Representa True e False como 1 e 0"""
    resposta = 2
    while resposta not in [0,1]:
        try:
            print('---')
            resposta = int(input(f"Tem {txt} na senha:\n1 para True e 0 para False:  "))
            if resposta not in [0,1]:
                raise ValueError
        except ValueError:
            print('---')
            print("!!!Digite apenas 0 ou 1!!!")
    return resposta

def definicoes_senha() -> dict:
  """Caracteristicas da senha"""
  caracteristicas_senha_inexistente = {"maiusculas": 0, 'minusculas': 0, 'numeros': 0, 'caracteres especiais':0}
  try:
    dS = {"maiusculas": true_false("maiusculas"),
    'minusculas': true_false('minusculas'), 'numeros': true_false('numeros'),
      'caracteres especiais':true_false('caracteres especiais')}
    if dS == caracteristicas_senha_inexistente:
      raise ValueError
  except ValueError:
    print('Impossível haver uma senha com todas as características nulas!\nDevido a isso o programa será encerrado.\nAté mais ver (`>°)!!!')
    exit()
  return dS

def num_chr_categoria(dictInfo : dict = {}) -> tuple:
  """Define o tamanho e quantidade de itens por categoria, se desejado"""
  numCategoriasSenha: int = 0
  tam : int = 0
  if dictInfo == {}: 
    dictInfo = definicoes_senha()
    for v in dictInfo.values():
      if v == 1: numCategoriasSenha += 1
    print('---')
    while not tam > 0:
      try:
        tam = int(input('Quantos dígitos quer na senha (recomendado: mais que 16): ')) 
      except ValueError:
        print('Erro! Digite um número inteiro!')
    if tam < numCategoriasSenha:
      tam = numCategoriasSenha
    return dictInfo, tam  
  for v in dictInfo.values():
    try:
      numCategoriasSenha += int(v)
      if v < 0:
        raise ValueError
    except ValueError:
      print('ERRO! Dados dispon_sbilizados incorretos.\nUma senha nova senha será gerada aleatoriamente.\nDefina os itens da senha:')
      dictInfo = definicoes_senha()
  return dictInfo, 0

def rd_caractere(listaAscii : list) -> str:
  '''Escolhe um caractere aleatoriamente de acordo com seu valor decimal na tabela ASCII'''
  lista : list = []
  if len(listaAscii) == 2:
    lista += list(range(listaAscii[0], listaAscii[1]))
  else:
    for a in listaAscii:
      lista += list(range(a[0], a[1]))
  val =  sc.choice(lista)
  return chr(val)

def password(dictinfo : dict = {}) -> str:
  """Gerador de senhas
  É possível especificar a quantidade de itens de cada tipo e os tipos presentes na senha: números (48 a 57), letras maiúsculas (65 a 90) ou minúsculas (97 a 122) e caracteres especiais (33 a 47, 58 a 64, 91 a 96 e 123 a 126).
  Valores entre parênteses são os intervalos (inicio, final+1) em que se encontram os caracters na tabela ASCII."""
  dados : tuple = num_chr_categoria(dictinfo)
  d : dict = dados[0]
  tamanho = dados[1]
  dAscii : dict = {'maiusculas': (65, 91), 'minusculas': (97, 123), 'numeros': (48, 58), 'caracteres especiais': [(33, 48),(58, 65), (91, 97), (123, 127)]}
  senha : list = []
  listaASCII : list
  for v in d.values():
    if v > 1:
      dictDisponibilizado : bool = True
      break
    dictDisponibilizado = False

  if dictDisponibilizado:
    for k,v in d.items():
      listaASCII = []
      if k == 'caracteres especiais':
        for i in dAscii[k]:
          listaASCII.append(i)
      else:
        listaASCII = dAscii[k]
      for i in range(v):
        senha.append(rd_caractere(listaASCII))
        
  else:
    listaASCII = []
    for k,v in d.items():
      listaAsciiAdicaoMinima : list = []
      if v == 1:
        if k == 'caracteres especiais':
          for i in dAscii[k]:
            listaASCII.append(i)
            listaAsciiAdicaoMinima.append(i)
        else:
          listaAsciiAdicaoMinima.append(dAscii[k])
          listaASCII.append(dAscii[k])
        senha.append(rd_caractere(listaAsciiAdicaoMinima)) 
    while len(senha) != tamanho:
      senha.append(rd_caractere(listaASCII))

  shuffle(senha)
  return ''.join(senha)

def main():
  senha = password()
  pyperclip.copy(senha)
  print('Sua senha é:', senha, '\nE ela foi copiada para a área de transferência (Use o Ctrl+v, para acessá-la)!')


if __name__ == '__main__':
  main()
