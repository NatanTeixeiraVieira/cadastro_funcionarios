from utils.Utils import Utils
from solicitar_informacoes.Funcionario import Funcionario
import json

class Cadastrar_funcionario:
  def __init__(self):
    self.nome = Funcionario.nome()
    self.cpf = Funcionario.cpf()
    self.endereco = Funcionario.endereco()
    self.data_admissao = Funcionario.data_admissao()

    self.arquivo_txt = Utils.pegar_txt()

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