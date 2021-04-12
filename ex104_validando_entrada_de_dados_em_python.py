"EX104 Validando entrada de dados em Python"

def leiaInt(num):
    print('-' * 30)
    val_num = ''
    while True:
        n = str(input('Digite um número: '))
        val_num = n.isnumeric()
        if val_num == True:
            return int(n)
        else:
            print('\033[31mErro! Digite um número inteiro válido.\033[m')

# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
