from random import randint, shuffle
def truefalse(txt):
    """True/False == 1/0"""
    resp = 2
    while resp not in [0,1]:
        try:
            resp = int(input(f"Tem {txt} na senha:\n1 para True e 0 para False:  "))
            if resp not in [0,1]:
                raise ValueError
        except ValueError:
            print("Digite apenas 0 ou 1")
        
    return resp


def definicoesSenha():
  """Caracteristicas da senha"""
  di = {"maiusculas": truefalse("maiusculas"),
   'minusculas': truefalse('minusculas'),
    'caracteres especiais':truefalse('caracteres especiais'),
    'numeros': truefalse('numeros')}
  return di


def numChrCategoria(d):
 pass


def passWord(tam=16, maiuscula=1, minuscula=1, chrEspeciais=1, numero = 1):
  """Gerador de senhas
  É possível especificar o tamanho da senha, se há números, letras maiúsculas ou minúsculas e caracteres especiais."""
  
  lista = []
  pass

"""print('\n\n\n')
for a in range(32, 128):
  print(a, chr(a))"""

a = definicoesSenha()
print(a)
