"Ex096 Função que calcula área"

def calculo_area():
    area = largura * comprimento
    print(f'A área de um terreno com a lagura de {largura} metros e o comprimento de {comprimento} metros é '
          f'{area:.2f} metros quadrados.')
def espaçador():
    print('-' * 120)


espaçador()
print('Controle de terrenos')
espaçador()
largura = float(input('Lagura (em metros): '))
comprimento = float(input('Comprimento (em metros): '))
calculo_area()
espaçador()