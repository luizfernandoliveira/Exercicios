"EX108 Exercitando módulos em Pyton"
from ex108 import moedas

n = float(input('Digite o preço: R$'))
print(f'A metade de R${moedas.moeda(n)} é R${moedas.moeda(moedas.metade(n))}')
print(f'O dobro de R${moedas.moeda(n)} é R${moedas.moeda(moedas.dobro(n))}')
print(f'Aumentando 10%, temos R${moedas.moeda(moedas.aumentar(n))}')
