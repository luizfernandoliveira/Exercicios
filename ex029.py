# Radar eletrônico

# Primeira forma de fazer

v = float(input('Digite a velocidade do carro: '))
if v <= 80:
    pass
else:
    print('MULTADO!!! Você excedeu o limite permitido que é 80 km/h.\nVocê deve pagar R${:.2f}.'.format((v-80)*7))
print('Bom dia! Dirija com segurança')

# Segunda forma de fazer
v = float(input('Digite a velocidade do carro: '))
if v >80:
    print('MULTADO!!! Você excedeu o limite permitido que é 80 km/h.')
    multa = (v-80)*7
    print('Você deve pagar R${:.2f}.'.format(multa))
print('Bom dia! Dirija com segurança')

