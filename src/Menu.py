from funcionario.Deletar_funcionario import Deletar_funcionario
from funcionario.Cadastrar_funcionario_estagiario import Cadastrar_funcionario_estagiario
from funcionario.Emitir_relatorio import Emitir_relatorio
from funcionario.Cadastrar_funcionario_efetivo import Cadastrar_funcionario_efetivo
from funcionario.Cadastrar_funcionario_temporario import Cadastrar_funcionario_temporario

from utils.Utils import Utils

class Menu:
  def __init__(self):
    self.opcao = 0
    self.voltar_para_menu = "s"

    while self.voltar_para_menu == "s":
      Utils.limpar_tela()
      self.mostrar_opcoes()
  
  def mostrar_opcoes(self):
    print("Bem vindo, o que deseja fazer?")
    print("1 - Cadastrar novo funcionario")
    print("2 - Emitir relatorio")
    print("3 - Deletar funcionário")
    print("4 - Sair")
    self.opcao = int(input("--> "))
    self.chamar_opcao()

  def chamar_opcao(self):
    if self.opcao == 1:
      cadastrar_funcionario = "s"

      while cadastrar_funcionario == "s":
        Utils.limpar_tela()
        self.escolher_tipo_funcionario()
        cadastrar_funcionario = Utils.repetir_acao("Deseja cadastrar um novo funcionário?")

    elif self.opcao == 2:
      emitir_relatorio = "s"

      while emitir_relatorio == "s":
        Utils.limpar_tela()
        Emitir_relatorio()
        emitir_relatorio = Utils.repetir_acao("Deseja emitir um novo relatório?")

    elif self.opcao == 3:
      deletar_funcionario = "s"

      while deletar_funcionario == "s":
        Utils.limpar_tela()
        Deletar_funcionario()
        deletar_funcionario = Utils.repetir_acao("Deseja emitir um novo relatório?")

    elif self.opcao == 4:
      self.voltar_para_menu = "n"
    else:
      print("Opção inválida.")
  
  def escolher_tipo_funcionario(self):
    print("Qual tipo de funcionário deseja cadastrar?")
    print("1 - Efetivo")
    print("2 - Temporário")
    print("3 - Estagiário")
    
    TIPO_FUNCIONARIO = int(input("--> "))

    if(TIPO_FUNCIONARIO == 1):
      Utils.limpar_tela()
      Cadastrar_funcionario_efetivo()
    elif(TIPO_FUNCIONARIO == 2):
      Utils.limpar_tela()
      Cadastrar_funcionario_temporario()
    elif(TIPO_FUNCIONARIO == 3):
      Utils.limpar_tela()
      Cadastrar_funcionario_estagiario()
      