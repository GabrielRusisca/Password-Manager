import os, random as rd

try: # Teste para implementar randomizações mais protegidas
  d = {}
  for i in range(1000):
    a = os.urandom(1)
    c = int.from_bytes(a, 'big')
    d.setdefault(c,0)
    d[c] += 1
  cont = 0
  for k,v in d.items():
    if v > 2:
      cont += 1
      #print(k,v)
    if k < 20:
      print(k, v)
  print('cont = ', cont)
  print('len =', len(d))
  
except:
  print('caca')

def truefalse(txt: str) -> int:
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

def definicoesSenha() -> dict:
  """Caracteristicas da senha"""
  dS = {"maiusculas": truefalse("maiusculas"),
   'minusculas': truefalse('minusculas'), 'numeros': truefalse('numeros'),
    'caracteres especiais':truefalse('caracteres especiais'),
    }
  return dS

def numChrCategoria() -> dict:
  """Separa a quantos caractéres cada categoria da senha possuirá"""
  d: dict = definicoesSenha()
  numCategSenha: int = 0   
  for v in d.values():
    numCategSenha += v
  print('---')
  tam :int = int(input('Quantos dígitos quer na senha: ')) - numCategSenha
  lista: list = []
  for i in range(1,numCategSenha + 1):
    limite: int = tam // numCategSenha * i
    if i == numCategSenha:
      lista.append(tam-sum(lista))
      break
    elif i == 1:
      lista.append(rd.randint(1, limite))
    else:
      lista.append(rd.randint(lista[-1],limite)-sum(lista)+1)
  rd.shuffle(lista)
  for i in lista:
    for k in d.keys():
      if d.get(k,'erro') == 1:
        d[k] += i
        break
  return d

def rdCaractere(start : int, stop : int) -> str:
  '''Escolhe um caractere aleatoriamente de acordo com seu valor decimal na tabela ASCII'''
  return chr(rd.randint(start, stop))

def passWord() -> str:
  """Gerador de senhas
  É possível especificar o tamanho da senha, se há números (48 a 57), letras maiúsculas (65 a 90) ou minúsculas (97 a 122) e caracteres especiais (33 a 47, 58 a 64, 91 a 96 e 123 a 126).
  Valores entre parênteses são os intervalos em que se encontram os caracters na tabela ASCII."""
  d : dict = numChrCategoria()
  dAscii: dict = {'maiusculas': (65, 90), 'minusculas': (97, 122), 'numeros': (48, 57), 'caracteres especiais': [(33, 47),(58, 64), (91, 96), (123, 126)]}
  texto: str = ''
  for k,v in d.items():
    for i in range(v):
      if k != 'caracteres especiais':
        texto += ' '+ rdCaractere(dAscii[k][0], dAscii[k][1])
      else:
        escolha : tuple = rd.choice(dAscii[k])
        texto += ' ' + rdCaractere(escolha[0], escolha[1])
  lista : list = texto.split(' ')
  rd.shuffle(lista)
  return ''.join(lista)

# a = passWord()
# print(a)