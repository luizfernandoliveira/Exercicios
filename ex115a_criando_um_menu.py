"EX115a Criando um menu"
from ex115.lib.interface import *
from ex115.lib.arquivo import  *
from time import sleep

arq = 'cursoemvideo.txt'

if arquivoExiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado!')

# Program Principal
while True:
    resposta = menu(['Ver pessoas cadstradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        cabecalho('Opção 1')
    elif resposta == 2:
        cabecalho('Opção 2')
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        cabecalho('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
