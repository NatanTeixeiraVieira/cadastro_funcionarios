from utils.pegar_db import pegar_txt
import json

class Cadastrar_funcionario_efetivo:
    def __init__(self):
        self.tipo = "Efetivo"
        self.nome = ""
        self.endereco = ""
        self.cpf = ""
        self.data_admissao = ""
        self.salario_base = 0

        self.arquivo_txt = pegar_txt()

        self.cadastrar_funcionario_efetivo()

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

    def cadastrar_funcionario_efetivo(self):
        self.nome = input("Digite o nome: ")
        self.endereco = input("Digite o endereço: ")
        self.cpf = input("Digite o CPF: ")
        self.data_admissao = input("Digite a data de admissão (DD/MM/AAAA): ")
        self.salario_base = float(input("Digite o salário base do funcionário: "))

        salario_liquido = self.calcular_salario_liquido()

        cadastro = {
            "tipo": self.tipo,
            "nome": self.nome,
            "endereco": self.endereco,
            "cpf": self.cpf,
            "data_admissao": self.data_admissao,
            "salario_liquido": salario_liquido
        }

        with open(self.arquivo_txt, "a") as file:
            file.write(json.dumps(cadastro) + "\n")

        print("\nNovo funcionário efetivo cadastrado com sucesso:")
        for key, value in cadastro.items():
            print(f"{key}: {value}")

