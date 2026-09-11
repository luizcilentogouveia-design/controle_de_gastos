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

  def listar_despesas(self, lista_exibicao=None):
    alvo=lista_exibicao if lista_exibicao is not None else self.despesas
    if alvo:
      for index, despesa in enumerate(alvo, start=1):
        print(f"{index}. Descrição: {despesa.descricao}")
        print(f"   Categoria: {despesa.categoria}")
        print(f"   Valor: R$ {despesa.valor:.2f}")
        print("-" * 15)
    else:
      print("Nenhuma despesa cadastrada.")

  def calcular_total(self):
    return sum(despesa.valor for despesa in self.despesas)
  
  def remover_despesa(self, indice):
    posicao=indice-1
    if 0<=posicao<len(self.despesas):
      despesa_removida=self.despesas.pop(posicao)
      print(f"Despesa '{despesa_removida.descricao}' removida")
    else:
      print("Erro. Número de despesa inválido")
    
  def filtrar_categoria(self, busca_categoria):
    filtradas=[d for d in self.despesas
               if d.categoria.lower()==busca_categoria.lower()
               ]
    print(f"\n--- Despesas na categoria '{busca_categoria}'---")
    self,self.listar_despesas(filtradas)

if __name__ == "__main__":
  controle = ControleDespesas()

  while True:
    print("\n--- MENU ---")
    print("1. Adicionar despesa")
    print("2. Listar despesas")
    print("3. Remover despesa")
    print("4. Ver total de gasto")
    print("5. Filtrar por categoria")
    print("6. Sair")
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
     print("\n Despesas cadastradas:")
     controle.listar_despesas()
     if controle.despesas:
       try:
         numero=int(input("Digite o número da despesa: "))
         controle.remover_despesa(numero)
       except ValueError:
         print("Erro. Digite um número válido")
  
    elif opcao == "4":
      total = controle.calcular_total()
      print(f"\nTotal acumulado: R$ {total:.2f}")

    elif opcao=="5":
      busca_categoria=input("Qual a categoria?")
      controle.filtrar_categoria(busca_categoria)

    elif opcao=="6":
      print("Finalizando...")
      break

    else:
      print("Opção inválida.")