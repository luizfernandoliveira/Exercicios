# Cadastro de trabalhador em python

from datetime import datetime
cadastro = {'nome': str(input('Nome: '))}
ano_nascimento = int(input('Ano de nascimento: '))
ano_atual = datetime.today().year
cadastro['idade'] = ano_atual - ano_nascimento
cadastro['ctps'] = int(input('Carteira de trabalho (0 não possui): '))
if cadastro['ctps'] != 0:
    cadastro['contratacao'] = int(input('Ano de contratação: '))
    cadastro['salario'] = float(input('Salário R$'))
    cadastro['aposentadoria'] = cadastro['contratacao'] + 35 - ano_nascimento
print('-' * 30)
for k, v in cadastro.items():
    print(f'   - {k.title()} tem o valor de {v}.')
print('-' * 30)
