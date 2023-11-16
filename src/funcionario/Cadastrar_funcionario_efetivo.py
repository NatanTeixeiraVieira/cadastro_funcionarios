from funcionario.Cadastrar_funcionario import Cadastrar_funcionario
from solicitar_informacoes.Funcionario import Funcionario

class Cadastrar_funcionario_efetivo(Cadastrar_funcionario):
	def __init__(self):
		self.tipo = "Efetivo"
		
		super().__init__()

		self.salario_base = Funcionario.salario("Digite o salário base do funcionário")
		self.salario_liquido = self.calcular_salario_liquido()

		self.cadastrar_funcionario(self.tipo, self.salario_liquido)

	def calcular_salario_liquido(self):
		desconto_previdenciario = self.salario_base * 0.1
		if self.salario_base <= 2000.0:
			imposto_de_renda = 0.0
		elif self.salario_base <= 3000.0:
			imposto_de_renda = self.salario_base * 0.1
		elif self.salario_base <= 4500.0:
			imposto_de_renda = self.salario_base * 0.2
		else:
			imposto_de_renda = self.salario_base * 0.3

		salario_liquido = self.salario_base - desconto_previdenciario - imposto_de_renda
		return salario_liquido

