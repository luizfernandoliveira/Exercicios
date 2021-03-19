"Ex093 Cadastro de jogador de futebol"

# Primeira forma de fazer
'''
soma_gols = 0
nome_jogador = {'nome': str(input('Digite o nome do jogador: ')), 'gols': [], 'total': 0}
partidas = int(input(f'Quantas partidas {nome_jogador["nome"]} jogou?  '))
for x in range(1, partidas + 1):
    partida = int(input(f'Quantos gols na partida {x}? '))
    nome_jogador['gols'].append(partida)
for k, v in enumerate(nome_jogador['gols']):
    soma_gols += v

nome_jogador['total'] = soma_gols
print('-' * 30)
print(nome_jogador)
print('-' * 30)
for a, b in nome_jogador.items():
    print(f'O campo {a.title()} tem o valor {b}.')
print('-' * 30)
print(f'O jogador {nome_jogador["nome"]} jogou {partidas} partidas.')
for k, v in enumerate(nome_jogador['gols']):
    print(f'    => Na partida {k+1}, fez {nome_jogador["gols"][k]}.')
print(f'Total de {nome_jogador["total"]} gols.')
print('-' * 30)
'''
# Segunda forma de fazer

jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0,tot):
    partidas.append(int(input(f'    Quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-' * 30)
print(jogador)
print('-' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')










