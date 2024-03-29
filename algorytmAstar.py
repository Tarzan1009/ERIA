import math

rozmiarx = 19
rozmiary = 19
startx = 0
starty = 0
koniecx = rozmiarx
koniecy = rozmiary

class kratka:
    def __init__(self, x, y, g, rodzic):
        self.x = x
        self.y = y
        self.g = g
        self.rodzic = rodzic
        self.h = math.sqrt(pow(x-koniecx, 2) + pow(y-koniecy, 2))
        self.f = self.g + self.h

def generujMape():
    plik = open("grid.txt", "r")
    lista = []
    for i in range(rozmiarx+1):
        wiersz = []
        linia = plik.readline()
        for j in range(0, (rozmiary+1)*2, 2):
            wiersz.append(int(linia[j]))
        lista.append(wiersz)
    lista.reverse()
    return lista

def wypiszMape(mapa):
    for wiersz in reversed(mapa):
        for kratka in wiersz:
            print(str(kratka), end = ' ')
        print('')

def czyJest(lista,kratka):
    for a in lista:
        if kratka.x == a.x and kratka.y == a.y:
            return True
    return False

def kierunki(rodzic):
    wynik = []
    for (i,j) in [(0,1),(1,0),(0,-1),(-1,0)]:
        xy = []
        xy.append(rodzic.x + i)
        xy.append(rodzic.y + j)
        if rozmiarx >= xy[0] >=0 and rozmiary >= xy[1] >=0:
            wynik.append(xy)
    return wynik

def dodajKratke(kratka):
    flaga = 0
    for a in otwarta:
        if kratka.x == a.x and kratka.y == a.y:
            if kratka.f <= a.f:
                a = kratka
                print("dodano do otwartej (" + str(kratka.x) + ',' + str(kratka.y) + ')')
            flaga = 1
    if not flaga:
        otwarta.append(kratka)
        print("dodano do otwartej (" + str(kratka.x) + ',' + str(kratka.y) + ')')

def stworzDzieci(rodzic):
    print("rodzic: (" + str(rodzic.x) + ',' + str(rodzic.y) + ')')
    for kierunek in kierunki(rodzic):
        if mapa[kierunek[0]][kierunek[1]] == 0:
            nowa = kratka(kierunek[0], kierunek[1], rodzic.g + 1, rodzic)
            if not czyJest(zamknieta, nowa):
                print("stworzono (" + str(nowa.x) + ',' + str(nowa.y) + ')')
                dodajKratke(nowa)

def znajdzMinF():
    wynik = otwarta[0]
    for a in otwarta:
        if a.f <= wynik.f:
            wynik = a
    otwarta.remove(wynik)
    print("usunieto z otwartej (" + str(wynik.x) + ', ' + str(wynik.y) + ')')
    zamknieta.append(wynik)
    print("dodano do zamknietej (" + str(wynik.x) + ',' + str(wynik.y) + ')')

def wypiszWsp(kratka):
    print('(' + str(kratka.x) + ', ' + str(kratka.y) + ')')


mapa = generujMape()
otwarta = []
start = kratka(startx,starty,0,None)
zamknieta = []
zamknieta.append(start)

while True:
    if zamknieta[-1].x == koniecx and zamknieta[-1].y == koniecy:
        print("ZNALEZIONO")
        wypiszMape(mapa)
        iterator = zamknieta[-1]
        while iterator:
            mapa[iterator.x][iterator.y] = 1
            wypiszWsp(iterator)
            iterator = iterator.rodzic
        wypiszMape(mapa)
        break
    stworzDzieci(zamknieta[-1])
    znajdzMinF()
    if not otwarta:
        print("koniec")
        break
    print("w otwartej jest " + str(len(otwarta)))
    print("w zamknietej jest " + str(len(zamknieta)))