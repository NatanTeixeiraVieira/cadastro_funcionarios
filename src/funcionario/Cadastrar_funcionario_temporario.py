
from funcionario.Cadastrar_funcionario import Cadastrar_funcionario
class Cadastrar_funcionario_temporario(Cadastrar_funcionario):
  def __init__(self):
    self.tipo = "Temporário"

    super().__init__()

    self.salario_liquido = float(input("Digite o salário líquido do funcionário: "))

    self.cadastrar_funcionario(self.tipo, self.salario_liquido)