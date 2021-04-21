"Ex112 Entrada de dados monetários"

from ex112.utilidadescev import moeda, dado

n = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(n, 35, 22)
