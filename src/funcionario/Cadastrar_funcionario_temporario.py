from utils.pegar_db import pegar_txt
import json

class Cadastrar_funcionario_temporario:
    def __init__(self):
      self.nome = str(input("Digite o nome do funcionario: "))
      self.tipo = "Temporario"
      self.cpf = input("Digite o CPF: ")
      self.endereco = input("Digite o endereço: ")
      self.data_admissao = input("Data de admissão (dd/mm/aa): ")
      self.salario_liquido = 1800

      self.arquivo_txt = pegar_txt()

      self.mostrar_informacoes()

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
        
    def mostrar_informacoes(self):
      print("Nome do funcionário:", self.nome)
      print("Tipo de funcionário:", self.tipo)
      print("CPF: ", self.cpf)
      print("Endereço: ", self.endereco)
      print("Data de admissão: ", self.data_admissao)
      print("Salário base: R$",self.salario_liquido)