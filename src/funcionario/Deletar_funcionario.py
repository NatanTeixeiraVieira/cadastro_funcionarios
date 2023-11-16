from utils.Utils import Utils
import json

from solicitar_informacoes.Funcionario import Funcionario

class Deletar_funcionario:
  def __init__(self):
    self.lista_funcionarios = []
    self.arquivo_txt = Utils.pegar_txt()
    self.cpf_funcionario_deletado = Funcionario.cpf("Digite o CPF do funcionário que desja deletar: ")
    self.cpf_encontrado = False

    self.deletar()

  def deletar(self):
    with open(self.arquivo_txt, "r") as file:
      for line in file:
        funcionario = json.loads(line)
        if(funcionario["cpf"] == self.cpf_funcionario_deletado):
          self.cpf_encontrado = True
          continue
        self.lista_funcionarios.append(line)
    
    with open(self.arquivo_txt, "w") as file:
      for line in self.lista_funcionarios:
        file.write(line)

    if self.cpf_encontrado:
      print("Funcionário deletado com sucesso.")
    else:
      print("CPF não encontrado.")
      