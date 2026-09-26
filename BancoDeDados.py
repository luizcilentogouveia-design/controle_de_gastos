from Despesa import Despesa
import sqlite3

class ControleDespesas:

  def __init__(self, banco_nome="despesas.db"):
    self.banco_nome=banco_nome
    self.criar_tabela()

  def conectar(self):
      return sqlite3.connect(self.banco_nome)
    
  def criar_tabela(self):
      with self.conectar() as conectar:
        cursor=conectar.cursor()
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS despesas(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       descricao TEXT NOT NULL,
                       categoria TEXT NOT NULL,
                       valor REAL NOT NULL
                       )
                       """)
        conectar.commit()

  def add_despesa(self, despesa):
    with self.conectar() as conectar:
      cursor = conectar.cursor()
      cursor.execute(
          """
                INSERT INTO despesas (descricao, categoria, valor)
                VALUES (?, ?, ?)
            """,
          (despesa.descricao, despesa.categoria, despesa.valor),
      )
      conectar.commit()

  def buscar_todas(self):
    with self.conectar() as conectar:
      cursor=conectar.cursor()
      cursor.execute("SELECT id, descricao, categoria, valor FROM despesas")
      linhas=cursor.fetchall()
      return[
        Despesa(id=row[0],descricao=row[1], categoria=row[2], valor=row[3])
        for row in linhas
      ]

  def listar_despesas(self, lista_exibicao=None):
    despesas=(lista_exibicao if lista_exibicao is not None else self.buscar_todas())
    if despesas:
      for despesa in despesas:
        print(f"ID [{despesa.id}]- Descrição: {despesa.descricao}")
        print(f" Categoria: {despesa.categoria}")
        print(f"Valor: R$ {despesa.valor:.2f}")
        print("-"*25)
    else:
      print("Nenhuma despesa cadastrada.")

  def calcular_total(self):
    with self.conectar() as conectar:
      cursor=conectar.cursor()
      cursor.execute("SELECT SUM(valor) FROM despesas")
      total=cursor.fetchone()[0]
      return total if total>0.0 else 0.0
    
  def remover_despesa(self, id_despesa):
    with self.conectar() as conectar:
      cursor=conectar.cursor()
      cursor.execute("DELETE FROM despesas WHERE id=?", (id_despesa,))
      conectar.commit()
    if cursor.rowcount>0:
      print(f"Despesa de ID {id_despesa} removida")
    else:
      print("Erro. ID de despesa não encontrado")
    
  def filtrar_categoria(self, busca_categoria):
    with self.conectar() as conectar:
      cursor=conectar.cursor()
      cursor.execute("""
                     SELECT id, descricao, categoria, valor
                     FROM despesas
                     WHERE LOWER(categoria)=LOWER(?)
                     """,(busca_categoria,),)
      linhas=cursor.fetchall()
      filtradas=[Despesa(id=row[0], descricao=row[1], categoria=row[2],valor=row[3])
                 for row in linhas]
      print(f"\n--- Despesas na categoria {busca_categoria}---")
      self.listar_despesas(filtradas)
