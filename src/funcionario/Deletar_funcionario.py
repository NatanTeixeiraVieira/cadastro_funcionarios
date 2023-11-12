from utils.Utils import Utils
import json

class Deletar_funcionario:
  def __init__(self):
    self.lista_funcionarios = []
    self.arquivo_txt = Utils.pegar_txt()
    self.cpf_funcionario_deletado = int(input("Digite o cpf do funcionário que desja deletar: "))

    self.deletar()

  def deletar(self):
    with open(self.arquivo_txt, "r") as file:
      for line in file:
        funcionario = json.loads(line)
        if(funcionario["cpf"] == self.cpf_funcionario_deletado):
          continue
        self.lista_funcionarios.append(line)
    
    with open(self.arquivo_txt, "w") as file:
      for line in self.lista_funcionarios:
        file.write(line)