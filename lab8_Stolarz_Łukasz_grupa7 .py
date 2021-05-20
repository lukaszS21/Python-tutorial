import random
class Wspak:
    def __init__(self,slowo):
        self.slowo=slowo
        self.index=len(slowo)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index ==0:
            raise StopIteration
        self.index =self.index -1
        return self.slowo[self.index]
r=Wspak('Zadanie1')
iter(r)
for i in r:
    print(i)
class Unikalne:
    def __init__(self, lista: list):

        self.lista = lista
        self.ile = {}
        for e in self.lista:
            if e in self.ile.keys():
                self.ile[e] = self.ile[e]+1
            else:
                self.ile[e] = 1
        self.new_list = [x for x in self.lista if self.ile[x] == 1]
        self.indeks = -1

    def __iter__(self):

        return self

    def __next__(self):

        if self.indeks == len(self.new_list) - 1:
            raise StopIteration

        self.indeks = self.indeks + 1
        return self.new_list[self.indeks]
print("zad 2")
l=[1,1,1,2,3,3,3,3,5,5,5,6,7,7,8]
print('lista = ',l)
u = Unikalne(l)
for x in u:
    print(x)

print("zad 3")
def zakres(x: int):

    i = -1

    while i < x -1:

        i = i + 1
        yield i

for x in zakres(10):
    print(x)
print("zad 4")

class Moneta:
    def __init__(self, ilosc: int):
        if ilosc not in [1,2]:
            raise Exception(str(ilosc)+" - zly nominal")
        self.__ilosc = ilosc
    def __str__(self):
        return str(self.__ilosc)+" groszy"

def jednoreki_bandyta(ilosc: int):
    suma = 0
    while suma < ilosc:
        nominal = random.randint(1,2)
        if suma + nominal > ilosc:
            pass
        else:
            suma = suma + nominal
            yield Moneta(nominal)
print('mam 6 gr')
for x in jednoreki_bandyta(6):
    print(x)
print("zad 6")
def list_(l1: list, l2: list):
    return sum(x*y for x,y in zip(l1, l2))
l1 = [1,3,1]
l2 = [2,3,4]
print('L1: ',l1,' L2: ',l2)
print(list_(l1,l2))
print("zad 7")
def sumowanie():
     suma=0
    
     while True:
         a=(yield)
         print("Otrzymano:", a)
         suma+=a
         yield suma
generator=sumowanie()
ile=0
suma=0
suma_ary=0
for i in [1, 2, 3, 5, 7, 11]:
 ile=ile+1
 print(ile)
 next(generator)
 
 print("Generator zwrócił:", generator.send(i)/ile)
 
print("zad specjalne")
x=0

def bla():
    global x
    x+=1
print(x)
bla()
print(x)
