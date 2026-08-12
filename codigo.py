class Despesa:

  def __init__(self, descricao, categoria, valor):
    self.descricao = descricao
    self.categoria = categoria
    self.valor = valor


class ControleDespesas:

  def __init__(self):
    self.despesas = []

  def add_despesa(self, despesa):
    self.despesas.append(despesa)

  def listar_despesas(self):
    if self.despesas:
      for index, despesa in enumerate(self.despesas, start=1):
        print(f"{index}. Descrição: {despesa.descricao}")
        print(f"   Categoria: {despesa.categoria}")
        print(f"   Valor: R$ {despesa.valor:.2f}")
        print("-" * 15)
    else:
      print("Nenhuma despesa cadastrada.")


if __name__ == "__main__":
  controle = ControleDespesas()

  while True:
    print("\n--- MENU ---")
    print("1. Adicionar despesa")
    print("2. Listar despesas")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
      descricao = input("Qual a descrição da despesa? ")
      categoria = input("Qual a categoria? ")
      try:
        valor = float(input("Qual o valor (R$)? "))
        despesa = Despesa(descricao, categoria, valor)
        controle.add_despesa(despesa)
        print("Adicionado com sucesso!")
      except ValueError:
        print("Erro: Digite um valor numérico válido (ex: 25.50).")

    elif opcao == "2":
      print("\nLista de despesas:")
      controle.listar_despesas()

    elif opcao == "3":
      print("Finalizando...")
      break

    else:
      print("Opção inválida.")
