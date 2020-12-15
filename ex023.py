#Separando digítos de um número

num = int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('O número {} possui {} unidades.'.format(num, u))
print('O número {} possui {} dezenas.'.format(num, d))
print('O número {} possui {} centenas.'.format(num, c))
print('O número {} possui {} milhares.'.format(num, m))
