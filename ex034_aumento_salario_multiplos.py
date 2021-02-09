#Aumento de salários multíplos

s= float(input('Digite o salário atual: '))
if s > 1250:
	sn = s * 1.1
else:
	sn = s * 1.15
print('O novo salário será de R$ {:.2f}'.format(sn))