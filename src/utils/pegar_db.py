import os

def pegar_txt():
  cwd = os.getcwd()
  arquivo_txt = os.path.join(cwd, 'db/funcionarios.txt')
  return arquivo_txt