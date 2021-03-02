# Matriz em Python

# Primeira forma de fazer

# matriz = [[], [], []]

# for a in range(0,3):
#	n1 = int(input(f'Digite os valor para [0, {a}]: ' ))
#	matriz[0].append(n1)

# for b in range(0, 3):
#	n2 = int(input(f'Digite os valor para [1, {b}]: ' ))
#	matriz[1].append(n2)

# for c in range(0, 3):
#	n3 = int(input(f'Digite os valor para [1, {c}]: ' ))
#	matriz[2].append(n3)
# print('-' * 30)
# for d in matriz[0]:
#	print(f'[ {d:^5} ]', end='')
# print()
# for e in matriz[1]:
#	print(f'[ {e:^5} ]', end='')
# print()
# for f in matriz[2]:
#	print(f'[ {f:^5} ]', end='')
# print()
# print('-' * 30)

# Segunda forma de fazer

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [ {l}, {c} ]: '))
print('-' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
