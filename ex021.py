import pygame
print('Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.')
# para iniciar o pygame
pygame.init()
# primeiro fazer o download de um arquivo de musica e dps colocar o nome do arquivo aqui
pygame.mixer.music.load('ex021.mp3')
# vai esperar a musica acabar para acabar de rodar o programa
pygame.mixer.music.play()
pygame.event.wait()
