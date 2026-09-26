class Despesa:

  def __init__(self, descricao, categoria, valor, id=None):
    self.id=id
    self.descricao = descricao
    self.categoria = categoria
    self.valor = valor
