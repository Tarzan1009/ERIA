rozmiarx = 19
rozmiary = 19
koniecx = 19
koniecy = 19

# -1: przeszkoda
# -5: koniec

def generujMape():
    plik = open("grid.txt", "r")
    lista = []
    for i in range(rozmiarx+1):
        wiersz = []
        linia = plik.readline()
        for j in range(0, (rozmiary+1)*2, 2):
            numer = int(linia[j])
            if numer == 5:
                wiersz.append(-1)
            else:
                wiersz.append(0)
        lista.append(wiersz)
    lista.reverse()
    return lista

def wypiszMape(mapa):
    for wiersz in reversed(mapa):
        for kratka in wiersz:
            if kratka == -1:
                print('xx', end=' ')
            else:
                if kratka < 10 and kratka >=0:
                    print('0' + str(kratka), end = ' ')
                else:
                    print(str(kratka), end = ' ')
        print('')

def rozszerz(x,y,koszt):
    if koszt > 0:
        mapa[x][y]=koszt
    for k in [[0,1],[-1,0],[0,-1],[1,0]]:
        if 0 <= x+k[0] <= 19 and 0 <= y+k[1] <= 19 and (mapa[x+k[0]][y+k[1]]==0 or mapa[x+k[0]][y+k[1]]>koszt+1):
            rozszerz(x+k[0],y+k[1],koszt+1)

mapa = []
mapa = generujMape()
mapa[koniecx][koniecy] = -5
wypiszMape(mapa)
print('\n')
rozszerz(koniecx,koniecy,0)
wypiszMape(mapa)