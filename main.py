from BancoDeDados import ControleDespesas
from Despesa import Despesa

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
     if controle.buscar_todas():
        try:
          id_remover = int(
              input("Digite o ID da despesa que deseja remover: ")
          )
          controle.remover_despesa(id_remover)
        except ValueError:
          print("Erro: Digite um ID numérico inteiro válido.")
     else:
        print("Nenhuma despesa para remover.")
  
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