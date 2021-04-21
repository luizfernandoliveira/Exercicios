"EX109 Exercitando módulos em Pyton"
from ex109 import moedas

n = float(input('Digite o preço: R$'))
print(f'A metade de R${moedas.moeda(n)} é R${moedas.metade(n, True)}')
print(f'O dobro de R${moedas.moeda(n)} é R${moedas.dobro(n, True)}')
print(f'Aumentando 10%, temos R${moedas.aumentar(n, True)}')
print(f'Reduzindo 13%, temos {moedas.diminuir(n, True)}')
