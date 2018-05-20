#pygame
import anna_mulle_maze_ja_andmed
from pprint import *
from kasulikud_funktsioonid import *
import twobuttonjoust
import pygame
maze_andmed = anna_mulle_maze_ja_andmed.tagasta_maze_ja_andmed([15, 15])
massiiv = maze_andmed['maze']

#pildid
porand_pilt = pygame.image.load("sein.png")
mangija_pilt = pygame.image.load("uus_kast.png")
sein_pilt = pygame.image.load("porand.png")
uks_pilt = pygame.image.load("uks.png")
voti_pilt = pygame.image.load("voti.png")
redel_alla_pilt = pygame.image.load("redel_alla_pilt.png")
redel_ules_pilt = pygame.image.load("redel_ules_pilt.png")
ring_pilt = pygame.image.load("kuri_ring.png")

#helid
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



def mangi_muusikat():
    pygame.mixer.Sound.play(helid[random.randint(0, len(helid)-1)])

    
pygame.init()
ekraan = pygame.display.set_mode((800, 600))

player_information = {
    'location': maze_andmed['start'],
    'sight_range': 1,
    'nahtud_kordinaadid': maze_andmed['start'],
    'votmed': 0,
    'skoor': 0
    }

def maagia(a, suund, massiiv):
    mangi_muusikat()
    player_information['location'] = [a[0] + suund[0], a[1] + suund[1]]
    b = []
    b = leia_naabrid2(player_information['location'], massiiv)
    if player_information['location'] in maze_andmed['votmed']:
        player_information['votmed'] = player_information['votmed'] + 1
        maze_andmed['votmed'].remove(player_information['location'])
    while b != []:
        c = b.pop()
        if c not in player_information['nahtud_kordinaadid']:#lisab uue kordinaadi kõrval olevad kordinaadid näntud kordinaatite listi, kui neid seal veel ei ole
            player_information['nahtud_kordinaadid'].append(c)
    joonista_maze_mida_naha_on(massiiv)
    ekraan.blit(mangija_pilt, (20*(a[0] + suund[0]), 20*(a[1] + suund[1])))
    pygame.display.flip()

def liiguta_mangijat(suund, massiiv):#joonistab mängija uuel kordinaadil ja kordinaadi, kust mängija lahkus
    a = player_information['location']
    if massiiv[a[0] + suund[0]][a[1] + suund[1]] != 1:#kui ei ole sein
        if [a[0] + suund[0], a[1] + suund[1]] in maze_andmed['uksed']:
            if player_information['votmed'] > 0:
                maze_andmed['uksed'].remove([a[0] + suund[0], a[1] + suund[1]])
                player_information['votmed'] = player_information['votmed'] - 1
                maagia(a, suund, massiiv)
        elif [a[0] + suund[0], a[1] + suund[1]] in maze_andmed['ringid']:
            """
            maze_andmed['ringid'].remove([a[0] + suund[0], a[1] + suund[1]])
            player_information['skoor'] = player_information['skoor'] + 1
            print(player_information['skoor'])
            """

            tekst = twobuttonjoust.startTheGame()
            maze_andmed['ringid'].remove([a[0] + suund[0], a[1] + suund[1]])
            pygame.draw.rect(ekraan, [40, 40, 40], [0, 0, 800, 600], 0)
            if tekst == ("w"):
                player_information['skoor'] += 1
                print(player_information['skoor'])
            maagia(a, suund, massiiv)
            
        else:
            maagia(a, suund, massiiv)
            """
            player_information['location'] = [a[0] + suund[0], a[1] + suund[1]]
            b = []
            b = leia_naabrid2(player_information['location'], massiiv)
            if player_information['location'] in maze_andmed['votmed']:
                player_information['votmed'] = player_information['votmed'] + 1
                player_information['votmed'].remove(player_information['location'])
            while b != []:
                c = b.pop()
                if c not in player_information['nahtud_kordinaadid']:#lisab uue kordinaadi kõrval olevad kordinaadid näntud kordinaatite listi, kui neid seal veel ei ole
                    player_information['nahtud_kordinaadid'].append(c)
            joonista_maze_mida_naha_on(massiiv)
            ekraan.blit(mangija_pilt, (20*(a[0] + suund[0]), 20*(a[1] + suund[1])))
            pygame.display.flip()"""

def joonista_maze_mida_naha_on(massiiv):#joonistab kõik kordinaadid mis on listis "nahtud_kordinaadid"
    for i in range(len(massiiv)):
        for j in range(len(massiiv[i])):
            if [i, j] in player_information['nahtud_kordinaadid']:#kui massiivi indeks on listis 'nahtud_kordinaadid'
                
                if massiiv[i][j] == 1:#kui on sein
                    ekraan.blit(sein_pilt, (20*(i), 20*(j)))#joonistab seina
                    
                elif [i, j] in maze_andmed['uksed']:#jne
                    ekraan.blit(uks_pilt, (20*(i), 20*(j)))
                    
                elif [i, j] in maze_andmed['votmed']:
                    ekraan.blit(porand_pilt, (20*(i), 20*(j)))
                    ekraan.blit(voti_pilt, (20*(i), 20*(j)))
                    
                elif [i, j] == maze_andmed['end']:
                    ekraan.blit(porand_pilt, (20*(i), 20*(j)))
                    ekraan.blit(redel_alla_pilt, (20*(i), 20*(j)))
                elif [i, j] in maze_andmed['ringid']:
                    ekraan.blit(ring_pilt, (20*(i), 20*(j)))
                elif [i, j] == [1, 1]:
                    ekraan.blit(porand_pilt, (20*(i), 20*(j)))
                    ekraan.blit(redel_ules_pilt, (20*(i), 20*(j)))
                else:
                    ekraan.blit(porand_pilt, (20*(i), 20*(j)))
    if maze_andmed['end'] in player_information['nahtud_kordinaadid']:
        ekraan.blit(redel_alla_pilt, [20*maze_andmed['end'][0], 20*maze_andmed['end'][1]])
    pygame.display.flip()
"""        
    a = maze_andmed['ristumised'][:]
    while a != []:
        b = a.pop()
        if b in player_information['nahtud_kordinaadid']:
            ekraan.blit((pygame.font.Font(None, 20)).render("111", 1, [204, 0, 0]), [20*b[0], 20*b[1]])

    a = maze_andmed['dead_ends'][:]
    while a != []:
        b = a.pop()
        if b in player_information['nahtud_kordinaadid']:
            ekraan.blit((pygame.font.Font(None, 20)).render("222", 1, [204, 0, 0]), [20*b[0], 20*b[1]])
    
    a = maze_andmed['koridorid'][:]
    for i in range(10):
        b = a.pop()
        if b in player_information['nahtud_kordinaadid']:
            ekraan.blit(uks_pilt, (20*b[0], 20*b[1]))
            #ekraan.blit((pygame.font.Font(None, 20)).render("333", 1, [204, 0, 0]), [20*b[0], 20*b[1]])
    a = maze_andmed['koridorid'][:]
    b = maze_andmed['porand'][:]
    while a != []:
        c = a.pop()
        while True:
            d = b.pop()
            if maze_andmed['maze'][d[0]][d[1]] < maze_andmed['maze'][c[0]][c[1]] and d not in player_information['votmed']:
                if d in player_information['nahtud_kordinaadid']:
                    ekraan.blit(voti_pilt, (20*d[0], 20*d[1]))
                    break
        b = maze_andmed['porand'][:]
"""


while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            liiguta_mangijat([0, -1], massiiv)

        elif event.key == pygame.K_DOWN:
            liiguta_mangijat([0, 1], massiiv)

        elif event.key == pygame.K_LEFT:
            liiguta_mangijat([-1, 0], massiiv)

        elif event.key == pygame.K_RIGHT:
            liiguta_mangijat([1, 0], massiiv)
    """
    if player_information['location'] == maze_andmed['end']:
        massiiv = tee_massiiv(10, 10)
        pygame.draw.rect(ekraan, [0, 0, 0], [0, 0, 800, 600], 0)
        tee_maze([1, 1], massiiv, 2)
        player_information['nahtud_kordinaadid'] = [1, 1]
        end = joonista_maze_mida_naha_on(massiiv)
        player_information['location'] = [1, 1]

        """
    pygame.display.flip()
    if player_information['location'] == maze_andmed['end']:
        pygame.draw.rect(ekraan, [40, 40, 40], [0, 0, 800, 600], 0)
        maze_andmed = anna_mulle_maze_ja_andmed.tagasta_maze_ja_andmed([18, 18])
        massiiv = maze_andmed['maze']
        player_information['location'] = [1, 1]
        player_information['nahtud_kordinaadid'] = [1, 1]
        a = leia_naabrid2([1, 1], maze_andmed['maze'])
        while a != []:
            b = a.pop()
            player_information['nahtud_kordinaadid'].append(b)
        joonista_maze_mida_naha_on(maze_andmed['maze'])
        ekraan.blit(mangija_pilt, (20, 20))
        pygame.display.flip()
        
