
times = ('Internacional', 'Flamengo', 'Atlético-MG', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras', 'Corinthians',
         'Bragantino', 'Santos', 'Athletico-PR', 'Atlético-go', 'Ceará', 'Sport', 'Fortaleza', 'Bahia', 'Vasco',
         'Goiás', 'Coritiba', 'Botafogo')

print('-' * 100)
print(f'Todos os times do campeonato Brasileiro: \n{times}')
print('-' * 100)
print(f'Os cinco primeiros colocados do campeonato: \n{times[0:5]}')
print('-' * 100)
print(f'Os quatro últimos colocados: \n{times[16:]}')
print('-' * 100)
print(f'Times por ordem alfabética: \n{sorted(times)}: ')
print('-' * 100)
print(f'O Corinthians está na {times.index("Corinthians") + 1}ª posição.')
print('-' * 100)
