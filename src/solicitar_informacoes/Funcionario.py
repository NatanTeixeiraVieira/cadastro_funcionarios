import re

from datetime import datetime 

class Funcionario:
  @staticmethod
  def nome():
    mostrar_nome = True
    while mostrar_nome:
      nome = input("Digite o nome completo do funcionário: ").strip()

      if len(nome) <= 0:
        print("Este campo é obrigatório.\n")
        continue

      if len(nome) < 3:
        print("O nome precisa conter pelo menos 3 letras.\n")
        continue

      regex = r"^[A-Za-zà-úÀ-Ú]+\s[A-Za-zà-úÀ-Ú\s]+$"
      nome_validado = re.match(regex, nome)

      if nome_validado:
        nome_dividido_por_espacos = nome.split()
        nome_formatado = " ".join(nome_dividido_por_espacos)
        return nome_formatado.title()
      
      else:
        print("Nome inválido.\n")
        continue
      
  @staticmethod
  def cpf(mensagem = "Digite o CPF (somente números): "):
    mostrar_cpf = True
    while mostrar_cpf:
      cpf = input(mensagem).strip()

      if len(cpf) <= 0:
        print("Este campo é obrigatório.\n")
        continue

      regex = r"^\d{11}$"
      cpf_validado = re.match(regex, cpf)

      if cpf_validado:
        if len(cpf) == 11:
          return str(cpf)
        else:
          print("O CPF precisa ter 11 dígitos.\n")
          continue
      
      else:
        print("CPF inválido.\n")
        continue

  @staticmethod
  def endereco():
    mostrar_endereco = True
    while mostrar_endereco:
      endereco = input("Digite o endereço (Ex.: Rua Exemplo, 999 - Nome do Bairro, Nome da Cidade): ").strip()

      if len(endereco) <= 0:
        print("Este campo é obrigatório.\n")
        continue
      
      caracteres_com_espacos = r"[A-Za-zà-úÀ-Ú][A-Za-zà-úÀ-Ú\s]+"
      espaco = r"\s"
      regex = re.compile(fr"^(Rua|Avenida){espaco}{caracteres_com_espacos},{espaco}\d+{espaco}-{espaco}{caracteres_com_espacos},{espaco}{caracteres_com_espacos}$")

      endereco_validado = re.match(regex, endereco)

      if endereco_validado:
        return endereco.title()
      else:
        print("Endereço inválido.\n")
    
  @staticmethod
  def data_admissao():
    mostrar_data_admissao = True
    while mostrar_data_admissao:
      data_admissao = input("Digite a data de admissão (DD/MM/AAAA): ").strip()

      if len(data_admissao) <= 0:
        print("Este campo é obrigatório.\n")
        continue

      regex = r"^\d{2}/\d{2}/\d{4}$"
      data_admissao_validada = re.match(regex, data_admissao)
    
      if data_admissao_validada:
        DATA_ATUAL = datetime.now()
        try:
          DIAS_DIFERECA_PARA_DATA_ATUAL = DATA_ATUAL - datetime.strptime(data_admissao, "%d/%m/%Y")
          if(DIAS_DIFERECA_PARA_DATA_ATUAL.days >= 0):
            return data_admissao
          else:
            print("Data de admissão inválida.\n")
            continue
        except:
          print("Data de admissão inválida.\n")
          continue

      else:
        print("Data de admissão inválida.\n")
        continue
    
  @staticmethod
  def salario(mensagem):
    mostrar_salario = True
    while mostrar_salario:
      salario = input(f"{mensagem} (Ex.: 1500.00)").strip()

      if len(salario) <= 0:
        print("Este campo é obrigatório.\n")
        continue

      regex = r"^\d+.\d{2}$"
      salario_validado = re.match(regex, salario)
    
      if salario_validado:
        return float(salario)
      else:
        print("Salário inválido.\n")
        continue