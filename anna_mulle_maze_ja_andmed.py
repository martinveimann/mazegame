#toodab valmis maze koos andmetega
import random
from kasulikud_funktsioonid import leia_naabrid2
from kasulikud_funktsioonid import naabrite_hulgas_seinad

def tee_massiiv(laius, pikkus):#teeb antud mõõtmetega massiivi
    massiiv = []
    for i in range (laius):
        massiiv.append([])
        for j in range (pikkus):
            massiiv[i].append(1)
    return massiiv

def palju_listis_seinu(kordinaadid, massiiv):#leiab mitu antud kordinaatidest annab massiivist väärtuse "1"
    n = 0
    a = kordinaadid.pop()
    while kordinaadid != []:
        if massiiv[a[0]][a[1]] == 1:
            n = n + 1
    return n


def kulgede_arv(start, massiiv):#leiab mitu seina on algkordinaadi kõrval
    n = 0
    if start[0] - 1 >= 0:#kontrollib kas kordinaat on massiivi ulatuses
        if massiiv[start[0] - 1][start[1]] == 1:#kontrollib kas on sein
            n = n + 1
    if start[0] + 1 < len(massiiv):
        if massiiv[start[0] + 1][start[1]] == 1:
            n = n + 1
    if start[1] - 1 >= 0:
        if massiiv[start[0]][start[1] - 1] == 1:
            n = n + 1
    if start[1] + 1 < len(massiiv[0]):
        if massiiv[start[0]][start[1] + 1] == 1:
            n = n + 1

    return n

def leia_naabrid(start, massiiv, visited):#tagastab algkordinaadi kõrval olevad kordinaadid
    naabrid = []
    if start[0] + 1 < len(massiiv) and [start[0]+1, start[1]] not in visited: #kontrollib kas kordinaadid on massiivi ulatuses
        naabrid.append([start[0]+1, start[1]])

    if start[1] + 1 < len(massiiv[0])and [start[0], start[1] + 1] not in visited:
        naabrid.append([start[0], start[1] + 1])

    if start[0] -1 > 0 and [start[0] - 1, start[1]] not in visited:
        naabrid.append([start[0] - 1, start[1]])
        
    if start[0] -1 > 0 and [start[0], start[1]-1] not in visited:
        naabrid.append([start[0], start[1]-1])

    return naabrid

def tee_maze(start, massiiv, n):#laburinti genereeriv algoritm
    massiiv[start[0]][start[1]] = n#muudab kordinaadil väärtuse
    visited = []
    visited.append(start)
    naabrid = leia_naabrid(start, massiiv, visited)
    random.shuffle(naabrid)
    while naabrid != []:
        naaber = naabrid.pop()
        if kulgede_arv(naaber, massiiv) == 3:
            tee_maze(naaber, massiiv, n+1)
    
def tee_algandmed():
    maze_andmed = {
        'start': [1, 1],
        'end': [],
        'dead_ends': [],
        'ristumised': [],
        'maze': [],
        'koridorid': [],
        'porand': [],
        'uksed': [],
        'votmed': [],
        'ringid': []
        }
    return maze_andmed

def tagasta_maze_ja_andmed(mootmed):
    start = [1, 1]
    maze_andmed = tee_algandmed()
    suurim = 0
    massiiv = tee_massiiv(mootmed[0], mootmed[1])
    maze = massiiv
    tee_maze(start, massiiv, 2)
    maze_andmed['maze'] = maze
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] > suurim:
                maze_andmed['end'] = [i, j]
                suurim = maze[i][j]
            if maze[i][j] != 1:
                n = naabrite_hulgas_seinad(leia_naabrid2([i, j], maze), maze)
                if n == 3:
                    maze_andmed['dead_ends'].append([i, j])
                elif n <= 1:
                    maze_andmed['ristumised'].append([i, j])
                elif n == 2 and maze_andmed['maze'][i][j] > 4:
                    maze_andmed['koridorid'].append([i, j])
                maze_andmed['porand'].append([i, j])
    random.shuffle(maze_andmed['ristumised'])
    random.shuffle(maze_andmed['dead_ends'])
    random.shuffle(maze_andmed['koridorid'])
    random.shuffle(maze_andmed['porand'])
    maze_andmed['dead_ends'].remove(maze_andmed['end'])
    if maze_andmed['start'] in maze_andmed['dead_ends']:
        maze_andmed['dead_ends'].remove(maze_andmed['start'])
    a = maze_andmed['koridorid'][:]
    for i in range(3):
        maze_andmed['uksed'].append(a.pop())
    a = maze_andmed['porand'][:]
    b = len(maze_andmed['uksed'])
    a.remove(maze_andmed['start'])
    c = [1, 1]
    for i in range(b):
        while c !=[]:
            
            c = a.pop()
            if maze_andmed['maze'][c[0]][c[1]] < maze_andmed['maze'][maze_andmed['uksed'][i][0]][maze_andmed['uksed'][i][1]] and c not in maze_andmed['votmed'] and c not in maze_andmed['uksed']:
                maze_andmed['votmed'].append(c)
                a = maze_andmed['porand']
                break
    a = maze_andmed['porand'][:]
    for i in range(3):
        b = a.pop()
        while b in maze_andmed['votmed'] or b in maze_andmed['uksed'] or b == [1, 1] or b == maze_andmed['end']:
            b = a.pop()
        maze_andmed['ringid'].append(b)
    print(maze_andmed['ringid'])
    return maze_andmed

    

tagasta_maze_ja_andmed([10, 10])
