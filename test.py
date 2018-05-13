import pygame
import time
import random
pygame.mixer.init()
helid = [
    pygame.mixer.Sound('clash 01.wav'),
    pygame.mixer.Sound(file = 'fx4.wav'),
    pygame.mixer.Sound(file = 'fx5.wav'),
    pygame.mixer.Sound(file = 'lasrhit1.wav'),
    pygame.mixer.Sound(file = 'lasrhit2.wav'),
    pygame.mixer.Sound(file = 'lasrhit3.wav'),
    pygame.mixer.Sound(file = 'lasrhit4.wav'),
    pygame.mixer.Sound(file = 'Saberblk.wav'),
    pygame.mixer.Sound(file = 'SlowSabr.wav'),
    pygame.mixer.Sound(file = 'sthswng1.wav'),
    pygame.mixer.Sound(file = 'sthswng2.wav'),
    pygame.mixer.Sound(file = 'sthswng3.wav'),
    pygame.mixer.Sound(file = 'sthtwrl1.wav'),
    pygame.mixer.Sound(file = 'sthtwrl2.wav'),
    pygame.mixer.Sound(file = 'Swing01.wav'),
    pygame.mixer.Sound(file = 'Swing02.wav'),
    ]
"""
for i in range(len(helid)):
    pygame.mixer.Sound.play(helid[i])
    time.sleep(1)
"""
def mangi_muusikat():
    pygame.mixer.Sound.play(helid[random.randint(0, len(helid)-1)])

