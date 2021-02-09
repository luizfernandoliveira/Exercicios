# Indice de massa corporal:

peso = float(input('Digite o seu peso (em kg): '))
altura = float(input('Digite sua altura (em metros): '))
imc = peso/(altura*altura)
print('O seu índice de massa corporal é {:.2f} kg/m^2'.format(imc))
if imc < 18.5:
	print('Você esta ABAIXO DO PESO!')
elif imc <= 25:
	print('Você esta com PESO IDEAL!')
elif imc <= 30:
	print('Você esta com SOBREPESO!')
elif imc <= 40:
	print('Você esta com OBESIDADE!')
else:
	print('Você esta com OBESIDADE MÓRBIDA')