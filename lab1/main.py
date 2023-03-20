###     Mateusz Godlewski    ###

"""
Zadanie 3

Utworzyć nowe środowisko wirtualne zainstalować moduł do odtwarzania dźwięku i odtworzyć mp3 – w skrypcie.

"""

import pygame

pygame.init()
file = "C:\\Users\\M A T E U S Z\\Desktop\\file_example_MP3_1MG.mg3"
pygame.mixer.music.load(file)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy(): continue
pygame.quit()