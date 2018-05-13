#siin on kasulikud funktsioonid

def leia_naabrid2(start, massiiv):
    naabrid = []
    if start[0] + 1 <= len(massiiv):
        naabrid.append([start[0]+1, start[1]])

    if start[1] + 1 <= len(massiiv[0]):
        naabrid.append([start[0], start[1] + 1])

    if start[0] -1 >= 0:
        naabrid.append([start[0] - 1, start[1]])
        
    if start[0] -1 >= 0:
        naabrid.append([start[0], start[1]-1])
    return naabrid


def naabrite_hulgas_seinad(naabrid, massiiv):
    n = 0
    while naabrid != []:
        a = naabrid.pop()
        if massiiv[a[0]][a[1]] == 1:
            n = n + 1

    return n
