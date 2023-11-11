from funcionario.Cadastrar_funcionario import Cadastrar_funcionario

class Cadastrar_funcionario_estagiario(Cadastrar_funcionario):
  def __init__(self):
    self.tipo = "Estagiário"
    self.salario_liquido = 1302

    super().__init__()

    self.cadastrar_funcionario(self.tipo, self.salario_liquido)