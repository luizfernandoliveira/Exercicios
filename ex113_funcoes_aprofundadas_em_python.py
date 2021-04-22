"EX113 Funções aprofundadas em Python"

def leiaInt(num):
    print('-' * 30)
    while True:
        try:
            i = int(input(num))
        except (ValueError, TypeError):
            print('\033[31mErro! Digite um número inteiro válido.\033[m')
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return i



def leiaReal(num):
    while True:
        try:
            r = float(input(num))
        except (ValueError, TypeError):
            print('\033[31mErro! Digite um número real válido.\033[m')
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return r




# Programa Principal
ni = leiaInt('Digite um número inteiro: ')
nr = leiaReal('Digite um número real: ')
print(f'O número inteiro foi {ni} e o número real foi {nr}.')
print('-' * 30)
