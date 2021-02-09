# Estatísticas em produtos

total = maior_mil = menor_preco = 0
mais_barato = ' '
print('-' * 30)
print('Lojas TOP')
print('-' * 30)

while True:
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))
    total += preco
    if preco > 1000:
        maior_mil +=1
    if menor_preco == 0:
        mais_barato = produto
        menor_preco = preco
    if menor_preco > preco:
        mais_barato = produto
        menor_preco = preco
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja cadastrar outro produto? (s / n) ')).strip().upper()
    if opcao in 'Nn':
        break
print('-' * 30)
print(f'O total da compra foi R${total}.')
print(f'Temos {maior_mil} produtos acima de R$1000,00.')
print(f'O produto com o menor preço é o {mais_barato} que custa {menor_preco}')
