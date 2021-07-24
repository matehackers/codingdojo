

class CaixaEletronico():

  def __init__(self):
    self.notas = [200, 100, 50, 20, 10, 5, 2]

  def saque(self, valor):
    valor_atual = valor
    lista_saque = []
    nota_atual = 0

    while nota_atual < len(self.notas):
      n = self.notas[nota_atual]

      if valor_atual < n:
        nota_atual += 1
      else:
        lista_saque.append(n)
        valor_atual -= n

    return lista_saque