# Simulador de caixa eletronico

# Primeira forma de fazer
print('-' * 30)
print('{:^30}'.format('BANCO'))
print('-' * 30)

tot50 = resto = tot20 = tot10 = tot1 = 0
while True:
    print('-' * 30)
    valor = int(input('Qual valor deseja sacar? R$'))
    if valor >= 50:
        tot50 = valor // 50
        resto = valor % 50
    if resto >= 20:
        tot20 = resto // 20
        resto = resto % 20
    if resto >= 10:
        tot10 = resto // 10
        resto = resto % 10
    if resto >= 1:
        tot1 = resto // 1
        resto = resto % 1
    if resto < 1:
        break
if tot50 > 0:
    print(f'{tot50} Cédulas de R$50,00.')
if tot20 > 0:
    print(f'{tot20} Cédulas de R$20,00.')
if tot10 > 0:
    print(f'{tot10} Cédulas de R$10,00.')
if tot1 > 0:
    print(f'{tot1} Cédulas de R$ 1,00.')
print('-' * 30)
print('Operação concluída. Volte sempre ao BANCO!')

# Segunda forma de fazer

print('-' * 30)
print('{:^30}'.format('BANCO'))
print('-' * 30)
valor = int(input('Qual valor deseja sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('-' * 30)
print('Operação concluída. Volte sempre ao BANCO!')
