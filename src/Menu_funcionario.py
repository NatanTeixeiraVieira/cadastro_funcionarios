from funcionario.Cadastrar_funcionario_efetivo import Cadastrar_funcionario_efetivo
from funcionario.Cadastrar_funcionario_temporario import Cadastrar_funcionario_temporario
from funcionario.Cadastrar_funcionario_estagiario import Cadastrar_funcionario_estagiario

from utils.Utils import Utils

class Menu_funcionario:
  def __init__(self):
    self._opca_invalida = False
   
  def mostrar_menu(self):
    print("Qual tipo de funcionário deseja cadastrar?")
    print("1 - Efetivo")
    print("2 - Temporário")
    print("3 - Estagiário")
    
    TIPO_FUNCIONARIO = input("--> ")

    if(TIPO_FUNCIONARIO == "1"):
      Utils.limpar_tela()
      Cadastrar_funcionario_efetivo()
    elif(TIPO_FUNCIONARIO == "2"):
      Utils.limpar_tela()
      Cadastrar_funcionario_temporario()
    elif(TIPO_FUNCIONARIO == "3"):
      Utils.limpar_tela()
      Cadastrar_funcionario_estagiario()
    else:
      self._opca_invalida = True

  @property
  def opcao_invalida(self):
    return self._opca_invalida