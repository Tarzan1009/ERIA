import math
import sys

class kratka:
    def __init__(self,x,y,czyZajete):
        self.x = x
        self.y = y
        self.czyZajete = czyZajete
        self.g = sys.maxsize
    def h(self):
        return dystans(self,koniec)

def dystans(kratka1,kratka2):
    wynik = math.sqrt(pow(kratka1.x-kratka2.x,2)+pow(kratka1.y-kratka2.y,2))
    return wynik

def generujMape():
    plik = open("grid.txt","r")
    lista = []
    for i in range(20):
        wiersz = []
        linia = plik.readline()
        for j in range(0,40,2):
            wiersz.append(kratka(i,int(j/2),linia[j]))
        lista.append(wiersz)
    return lista

def wypiszMape(mapa):
    for wiersz in mapa:
        for kratka in wiersz:
            print(str(kratka.czyZajete), end = ' ')
        print('')

mapa = generujMape()
global koniec
koniec = mapa[19][19]
#wypiszMape(mapa)
print(str(mapa[1][1].g))

