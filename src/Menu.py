from funcionario.Deletar_funcionario import Deletar_funcionario
from funcionario.Emitir_relatorio import Emitir_relatorio
from Menu_funcionario import Menu_funcionario

from utils.Utils import Utils

class Menu:
  def __init__(self):
    self.opcao = "0"
    self.voltar_para_menu = "s"
    self.opca_invalida = False

    while self.voltar_para_menu == "s":
      Utils.limpar_tela()
      if self.opca_invalida:
        Utils.mensagem_opcao_invalida()

      self.mostrar_opcoes()
  
  def mostrar_opcoes(self):
    self.opca_invalida = False
    print("Bem vindo, o que deseja fazer?")
    print("1 - Cadastrar novo funcionario")
    print("2 - Emitir relatorio")
    print("3 - Deletar funcionário")
    print("4 - Sair")
    self.opcao = input("--> ")
    self.chamar_opcao()

  def chamar_opcao(self):
    if self.opcao == "1":
      cadastrar_funcionario = "s"
      Utils.limpar_tela()

      while cadastrar_funcionario == "s":
        menu_funcionario = Menu_funcionario()
        if not menu_funcionario.opcao_invalida:
          Utils.limpar_tela()
          
        menu_funcionario.mostrar_menu()

        if menu_funcionario.opcao_invalida:
          Utils.limpar_tela()
          Utils.mensagem_opcao_invalida()
        else:
          cadastrar_funcionario = Utils.repetir_acao("Deseja cadastrar um novo funcionário?")
        

    elif self.opcao == "2":
      emitir_relatorio = "s"

      while emitir_relatorio == "s":
        Utils.limpar_tela()
        Emitir_relatorio()
        emitir_relatorio = Utils.repetir_acao("Deseja emitir um novo relatório?")

    elif self.opcao == "3":
      deletar_funcionario = "s"

      while deletar_funcionario == "s":
        Utils.limpar_tela()
        Deletar_funcionario()
        deletar_funcionario = Utils.repetir_acao("Deseja deletar outro funcionário?")

    elif self.opcao == "4":
      self.voltar_para_menu = "n"

    else:
      self.opca_invalida = True