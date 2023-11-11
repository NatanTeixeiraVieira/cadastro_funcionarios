from utils.pegar_db import pegar_txt
import json


class Cadastrar_funcionario:
  def __init__(self):
    self.nome = str(input("Digite o nome do funcionario: "))
    self.tipo = "Temporario"
    self.cpf = input("Digite o CPF: ")
    self.endereco = input("Digite o endereço: ")
    self.data_admissao = input("Data de admissão (dd/mm/aa): ")

    self.arquivo_txt = pegar_txt()

  def cadastrar_funcionario(self, tipo, salario_liquido):
      cadastro = {
        "tipo": tipo,
        "nome": self.nome,
        "endereco": self.endereco,
        "cpf": self.cpf,
        "data_admissao": self.data_admissao,
        "salario_liquido": salario_liquido
      }
      with open(self.arquivo_txt, "a") as file:
        file.write(json.dumps(cadastro) + "\n")

      print("\nFuncionário cadastrado com sucesso!")