# # Tocando mp3

# #Primeira forma de fazer
import pygame
a = 1
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
volume = int(a/100)
mixer.music.set_volume(volume)


# #Segunda forma de fazer
# from playsound import playsound
#
# playsound('ex021.mp3')


import pygame
radio_status = False
volume = 3
musica = 0
lista_musica = ['Engenheiros_do_hawaii-3_x_4.mp3', 'legiao_urbana-hoje_a_noite_nao_tem_luar.mp3', 'Creed-One_Last_Breath.mp3', 'raul_seixas-ouro_de_tolo.mp3', 'jack_johnson.mp3']
while True:
    if radio_status == False:
        f = input('Rádio Desligado: ')
        if f == 'l':  # liga/desliga
            if radio_status == False:
                radio_status = True
                print('Rádio ligado')
    else:
        while True:
            f = input('Funções: ')
            if f == 'l':  # liga/desliga
                if radio_status == True:
                    radio_status = False
                    print('Rádio desligado2')
                    break
                else:
                    radio_status = False
                    print(radio_status)

            elif f == '+':  # aumenta volume
                if volume < 5:
                    volume += 1
                    print('Volume está em {}'.format(volume))
                else:
                    print('Volume máximo!')
            elif f == '-':
                if volume > 1:
                    volume -= 1
                    print('Volume está em {}'.format(volume))
                else:
                    print('Volume mínimo!')
            elif f == 'p':
                print('Música: {}'.format(musica + 1))
                print(lista_musica[musica])
                pygame.init()
                pygame.mixer.music.load(lista_musica[musica])
                pygame.mixer.music.play()


            elif f == 's':
                pygame.mixer.music.stop()
            elif f == '<':
                if musica > 0:
                    musica -= 1
                    print('Música: {}'.format(musica + 1))
                    print(lista_musica[musica])
                    pygame.init()
                    pygame.mixer.music.load(lista_musica[musica])
                    pygame.mixer.music.play()

                else:
                    total_lista = len(lista_musica)
                    musica = total_lista - 1
                    print('Música: {}'.format(musica + 1))
                    print(lista_musica[musica])
                    pygame.init()
                    pygame.mixer.music.load(lista_musica[musica])
                    pygame.mixer.music.play()

            elif f == '>':
                total_lista = len(lista_musica)
                if musica < (total_lista - 1):
                    musica += 1
                    print('Música: {}'.format(musica + 1))
                    print(lista_musica[musica])
                    pygame.init()
                    pygame.mixer.music.load(lista_musica[musica])
                    pygame.mixer.music.play()

                else:
                    musica = 0
                    print('Música: {}'.format(musica + 1))
                    print(lista_musica[musica])
                    pygame.init()
                    pygame.mixer.music.load(lista_musica[musica])
                    pygame.mixer.music.play()