from utils.Utils import Utils
import json

class Emitir_relatorio:
  def __init__(self):
    self.arquivo_txt = Utils.pegar_txt()
    self.emitir_relatorio()

  def emitir_relatorio(self):
    print("Relatório \n")
    with open(self.arquivo_txt, "r") as file:
      for numero_funcionario, linha in enumerate(file, start=1):
        funcionario = json.loads(linha)
        self.escrever_relatorio(funcionario, numero_funcionario)
  
  def escrever_relatorio(self, funcionario, numero_funcionario):
    print(f'Funcionário {numero_funcionario}')
    print(f'Nome: {funcionario["nome"]}')
    print(f'Tipo de funcioanário: {funcionario["tipo"]}')
    print(f'Endereço: {funcionario["endereco"]}')
    print(f'CPF: {funcionario["cpf"]}')
    print(f'Data de admissão: {funcionario["data_admissao"]}')
    print(f'Salário líquido: {funcionario["salario_liquido"]}')
    print("==========================================================")