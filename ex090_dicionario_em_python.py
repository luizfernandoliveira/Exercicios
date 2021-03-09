# Dicionário em python

# Primeira foram de fazer

dicio = {}
dicio['nome'] = str(input('Nome: '))
dicio['media'] = float(input(f'Média de {dicio["nome"]}: '))
if dicio['media'] >= 7:
    dicio['situacao'] = str('Aprovado')
elif 5 <= dicio['media'] < 7:
    dicio['situacao'] = str('Recuperação')
else:
    dicio['situacao'] = str('Reprovado')
print('-' * 30)
print(f'- O nome do aluno é {dicio["nome"]}.')
print(f'- A média do aluno é {dicio["media"]}.')
print(f'- A situação do aluno é {dicio["situacao"]}.')
print('-' * 30)

# Segunda forma de fazer

aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {dicio["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
print('-' * 30)
for k, v in aluno.items():
    print(f'  - {k} é igual a {v}')
print('-' * 30)

