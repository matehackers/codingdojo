import unittest
from caixa import CaixaEletronico

"""
Desenvolva um programa que simule a entrega de notas quando um cliente efetuar um saque em um caixa eletrônico. 
Os requisitos básicos são os seguintes:

Entregar o menor número de notas;
É possível sacar o valor solicitado com as notas disponíveis;
Saldo do cliente infinito;
Quantidade de notas infinito (pode-se colocar um valor finito de cédulas para aumentar a dificuldade do problema);
Notas disponíveis de R$ 200,00; R$ 100,00; R$ 50,00; R$ 20,00; R$ 10,00; R$ 5,00 e R$ 2,00

Exemplos:

Valor do Saque: R$ 30,00 – Resultado Esperado: Entregar 1 nota de R$20,00 e 1 nota de R$ 10,00.
Valor do Saque: R$ 80,00 – Resultado Esperado: Entregar 1 nota de R$50,00 1 nota de R$ 20,00 e 1 nota de R$ 10,00. 
"""
class CaixaEletronicoTest(unittest.TestCase):

  def setUp(self):
    self.caixa = CaixaEletronico()

  def teste_saque_10(self):
    self.assertEqual(self.caixa.saque(10), [10])

  def teste_saque_20(self):
    self.assertEqual(self.caixa.saque(20), [20])

  def teste_saque_50(self):
    self.assertEqual(self.caixa.saque(50), [50])

  def teste_saque_100(self):
    self.assertEqual(self.caixa.saque(100), [100])

  def test_saque_30(self):
    self.assertEqual(self.caixa.saque(30), [20, 10])

  def test_saque_110(self):
    self.assertEqual(self.caixa.saque(110), [100, 10])

  def test_saque_80(self):
    self.assertEqual(self.caixa.saque(80), [50, 20, 10])

  def test_saque_40(self):
    self.assertEqual(self.caixa.saque(40), [20, 20])

  def test_saque_60(self):
    self.assertEqual(self.caixa.saque(60), [50, 10])
  
  def test_saque_300(self):
    self.assertEqual(self.caixa.saque(300), [200, 100])

  def test_saque_340(self):
    self.assertEqual(self.caixa.saque(340), [200, 100, 20, 20])

  def test_saque_342(self):
    self.assertEqual(self.caixa.saque(342), [200, 100, 20, 20, 2])

  def test_saque_1(self):
    self.assertEqual(self.caixa.saque(1), [])

unittest.main()