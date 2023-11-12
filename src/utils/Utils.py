import os

class Utils:
  @staticmethod
  def pegar_txt():
    cwd = os.getcwd()
    arquivo_txt = os.path.join(cwd, 'db/funcionarios.txt')
    return arquivo_txt
  
  @staticmethod
  def limpar_tela():
    if os.name == 'nt': 
      os.system('cls')
    else:
      os.system('clear')

  @staticmethod
  def repetir_acao(mensagem):
    print(mensagem)
    print("Sim - s")
    print("Não - Qualquer caractere exceto 's'")
    resposta = input("--> ")
    return resposta