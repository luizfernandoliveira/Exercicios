"EX105 Analisando e gerando Dicionários"

def notas(*n, sit=False):

    """
    - Função para analisar a(s) nota(s) e situações do(s) aluno(s).
    :param n: Digite a(s) nota(s) dos aluno(s).
    :param sit: valor opcional, indica ou não a situção do aluno.
    :return: Dicionário com as informações da turma.
    """
    dicionario = {}
    dicionario['total'] = len(n)
    maior = menor = soma = 0
    for x in n:
        if maior == 0:
            maior = x
        else:
            if x > maior:
                maior = x
        if menor == 0:
            menor = x
        else:
            if x < menor:
                menor = x
        soma += x
    media = soma/len(n)
    dicionario['maior'] = maior
    dicionario['menor'] = menor
    dicionario['media'] = media
    if sit == True:
        if media < 5:
            dicionario['situação'] = 'Ruim'
        elif media < 7:
            dicionario['situação'] = 'Razoável'
        else:
            dicionario['situação'] = 'Boa'
        return dicionario
    else:
        return dicionario


# Programa Principal
resp = notas(10, 5.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)
