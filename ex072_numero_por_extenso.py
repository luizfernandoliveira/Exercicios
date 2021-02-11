# Número por extenso

tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
         'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
opcao = ' '
while True:
    while True:
        n = int(input('Digite um número entre 0 e 20: '))
        c = 0
        for x in range(0, 21):
            if x == n:
                c += 1
        if c != 1:
            print('Número inválido!')
        else:
            print(f'Você digitou o número {tupla[n]}.')
            break
    while opcao not in 'NS':
        opcao = str(input('Deseja digitar outro número? (s / n) ')).strip().upper()
    if opcao in 'Nn':
        break
    n = ' '
    opcao = ' '
print('Fim')
