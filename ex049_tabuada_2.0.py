 # tabuada 2.0
 
n = int(input('Digite o número que deseja a tabuada: '))
 
for x in range(1, 11):
 	print('{} X {:2} = {}'.format(n, x, n * x))