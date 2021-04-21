"EX107 Exercitando módulos em Pyton"
from ex107 import moedas

n = float(input('Digite o preço: R$'))
print(f'A metade de R${n:.2f} é R${moedas.metade(n):.2f}')
print(f'O dobro de R${n:.2f} é R${moedas.dobro(n):.2f}')
print(f'Aumentando 10%, temos R${moedas.aumentar(n):.2f}')
