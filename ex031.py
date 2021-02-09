# Custo da viagem

# Primeira forma de fazer
d = float(input('Digite a distância da viagem (em quilômetros): '))
if d <= 200:
    pn = d * 0.50
    print('A sua viagem custará R${:.2f}.'.format(pn))
else:
    pp = d * 0.45
    print('A sua viagem com desconto promocional custará R${:.2f}.'.format(pp))
print('Boa viagem!')

# Segunda forma de fazer
d = float(input('Digite a distância da viagem (em quilômetros): '))
if d <= 200:
    p = d * 0.50

else:
    p = d * 0.45

print('A sua viagem custará R${:.2f}.'.format(p))
print('Boa viagem!')

# Terceira forma de fazer

d = float(input('Digite a distância da viagem (em quilômetros): '))
p = d * 0.50 if d <= 200 else d * 0.45
print('A sua viagem custará R${:.2f}.'.format(p))
print('Boa viagem!')
