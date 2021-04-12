"EX103 Ficha de jogador"


def ficha(jogador='<desconhecido>', gols=0):
    return f'O jogador {jogador} fez {gols} gols(s) no campeonato.'


j = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
ver_gols = g.isnumeric()
if ver_gols == False:
    g = 0
else:
    g = int(g)
if j.strip() == '':
    print(ficha(gols=g))
else:
    print(ficha(j, g))


