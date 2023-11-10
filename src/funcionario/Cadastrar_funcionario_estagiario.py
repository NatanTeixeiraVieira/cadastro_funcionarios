from utils.pegar_db import pegar_txt
import json

class Cadastrar_funcionario_estagiario:
  def __init__(self):
    self.tipo = "Estagiário"
    self.nome = input("Digite o nome: ")
    self.endereco = input("Digite o endereço: ")
    self.cpf = input("Digite o CPF: ")
    self.data_admissao = input("Digite a data de admissão (DD/MM/AAAA): ")
    self.salario_liquido = 1302

    self.arquivo_txt = pegar_txt()

    self.cadastrar_funcionario()

  def cadastrar_funcionario(self):
    cadastro = {
      "tipo": self.tipo,
      "nome": self.nome,
      "endereco": self.endereco,
      "cpf": self.cpf,
      "data_admissao": self.data_admissao,
      "salario_liquido": self.salario_liquido
    }
    with open(self.arquivo_txt, "a") as file:
      file.write(json.dumps(cadastro) + "\n")

    print("\nNovo funcionário efetivo cadastrado com sucesso:")
    for key, value in cadastro.items():
      print(f"{key}: {value}")