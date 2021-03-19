"Fernando"
#Meus Desafios
#Liste e imprima na tela de 0 a 100 todos os números primos.
#Obs: Um número primo é classificado como primo se ele é divisível apenas por um e por ele mesmo.


for x in range(0, 101):
    if x == 0 or x == 1:
        print(x)
    else:
        contagem_numeros_nao_primos = 0
        for y in range(1, x):
            d = x % y
            if d == 0:
                contagem_numeros_nao_primos += 1
        if contagem_numeros_nao_primos == 1:
            print('primo')
        else:
            print(x)
