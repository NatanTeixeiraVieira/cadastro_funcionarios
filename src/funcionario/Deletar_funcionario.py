from utils.pegar_db import pegar_txt
import json

class Deletar_funcionario:
  def __init__(self):
    self.lista_funcionarios = []
    self.arquivo_txt = pegar_txt()

  def deletar(self, cpf):
    with open(self.arquivo_txt, "r") as file:
      for line in file:
        funcionario = json.loads(line)
        if(funcionario["cpf"] == cpf):
          continue
        self.lista_funcionarios.append(line)
    
    with open(self.arquivo_txt, "w") as file:
      for line in self.lista_funcionarios:
        file.write(line)