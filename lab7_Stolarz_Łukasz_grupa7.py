import random
#zad 1
class Moneta:
    def __init__(self, value: float, waluta: str):
        tab = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5]
        self.__waluta = waluta
        if value in tab:
            self.__value = value
        else:
            raise ZlyNominalException

    def get_value(self):
        return self.__value

    def get_currency(self):
        return self.__waluta
    
class ZlyNominalException(Exception):
    print("1")


class NieznanaWalutaException(Exception):
    print("2")


class UderzylesSieWPalecException(Exception):
    print("3")
class PrzechowywaczMonet:
    def __init__(self, tym: list):
        self._tym = tym
        self._monety = []

    def add_monet(self, moneta: Moneta):
        if moneta.get_value() in self._tym:
            self._monety.append(moneta)
        else:
            print("Nie obługujemy tej monety")

    def pull_monet(self, value: float):
        for monet in self._monety:
            if monet.get_value() == value:
                self._monety.remove(monet)
                return monet

    def get_total(self):
        return sum(moneta.get_value() for moneta in self._monety)
    
class Skarbonka(PrzechowywaczMonet):
    def __init__(self, tym: list, waluta: str):
        super().__init__(tym)
        self.__waluta = waluta
        self.__rozbita = False

    def add_monet(self, moneta: Moneta):
        if self.__rozbita:
            return

        if moneta.get_value() in self._tym:
            if self.__waluta== moneta.get_waluta():
                self._monets.append(moneta)
            else:
                raise NieznanaWalutaException
        else:
            raise ZlyNominalException

    def pull_monet(self, value: float):
        print("Nie można wyciągnąć pojedynczej monety")

    def rozbij(self):
        if (self.__rozbita):
            print("Nie mozną rozbić rozbitej skarbonki")
            return
        if random.randint(1, 10) == 1:
            raise UderzylesSieWPalecException
        self.__rozbita = True
        tmp = self._monets
        self._monets = []
        return tmp
#zad2
class Moneta2:
        def __init__(self, value: float):
            tab = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5]
            
            if value in tab:
                self.__value = value
            else:
                raise ZlyNominalException

        def get_value(self):
            return self.__value

       
        def __str__(self):
            return {'value': self.__value}

        def __repr__(self):
            return 'Moneta(value={})'.format(self.__value)
#zad3
import csv
class ListaMonetException(Exception):
    def __init__(self, monety):
        self.__monety = monety

    def get_monety(self):
        return self.__monety


class ZlyFormatPlikuException(ListaMonetException):
    def __init__(self, monety):
        super().__init__(monety)


class ZlyNominalException(ListaMonetException):
    def __init__(self, monety):
        super().__init__(monety)
def wczytaj():
    monety=[]
    nom=[0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5]
    try:
        plik=open('plik.csv')
        r=csv.reader(plik)
    
        for i in r:
            x=float(i[0])
            ilosc=int(i[1])
            if not x in nom:
                raise ZlyNominalException(monety)
            for c in range(ilosc):
                monety.append(Moneta2(x))
        plik.close()
        return monety
    except IOError:
        print("blad")
print(wczytaj())
#zad 4
class Skarbonka(PrzechowywaczMonet):

    __waluta='pln'

    def __init__(self,nominaly):

        super().__init__(nominaly)
        self.rozbita=False
        self.__listaMonet = []

    def dodajMonete(self, moneta: Moneta):
        if self.rozbita:
            print('Nie można wrzucać monet do rozbitej skarbonki!')
        else:

            if isinstance(moneta, Moneta):

                if (moneta.zwrocLiczbeZlotych(), moneta.zwrocLiczbeGroszy()) in self._nominaly:

                    if moneta.zwrocWalute().lower()==self.__waluta:

                        self._przechowywacz.append(moneta)
                    else:

                        raise NieznanaWalutaException(moneta.zwrocWalute(),"Zła waluta")
                else:
                    raise ZlyNominalException(str((moneta.zwrocLiczbeZlotych(),moneta.zwrocLiczbeGroszy())),"Zły nominał")
            else:
                raise Exception('Przesłany obiekt nie jest monetą!')



    def zwrocWartoscPieniedzy(self):

        sumaZlotych = 0
        sumaGroszy = 0

        for x in self._przechowywacz:

            sumaZlotych = sumaZlotych+x.zwrocLiczbeZlotych()
            sumaGroszy = sumaGroszy+x.zwrocLiczbeGroszy()

        reszta = int(sumaGroszy/100)

        return (sumaZlotych+reszta,sumaGroszy%100)

    def rozbij(self):
        szczescie=random.randint(0,10)
        print(szczescie)
        if(szczescie==1):

            raise UderzylesSieWPalecException(' ','Uderzyłeś się w palec')

        else:
            self.rozbita=True

            monety = self._przechowywacz.copy()

            indeks = len(self._przechowywacz)-1
            while indeks>=0:
                self._przechowywacz.remove(self._przechowywacz[indeks])
                indeks = indeks-1

            return monety
def Re(fileName:str):
    l = []

    with open(fileName) as csvf:
        reader = csv.reader(csvf)

        for row in reader:
            if len(str(row[0]).split('\t'))==3:

                if (int(str(row[0]).split('\t')[0]),int(str(row[0]).split('\t')[1])) in Moneta.nominaly:

                    for x in range(int(str(row[0]).split('\t')[2])):
                        l.append(Moneta(int(str(row[0]).split('\t')[0]),int(str(row[0]).split('\t')[1]),'pln'))
                else:
                    raise ZlyNominalException(str((int(str(row[0]).split('\t')[0]),int(str(row[0]).split('\t')[1]))),"Nieobsługiwany nominał",l)
            else:
                raise ZlyFormatPlikuException(fileName,"blad")

        else:
            csvf.close()
        l.sort(key=lambda x:x.zwrocLiczbeZlotych()+x.zwrocLiczbeGroszy()/100)
        return l

try:

    print('Tworzę nową skarbonkę: ',Moneta.nominaly)
    skarbonka = Skarbonka(Moneta.nominaly)

    l = csvReader("plik1.csv")
    for x in l:
        skarbonka.dodajMonete(x)

    print("W skarbonce jest: "+str(skarbonka.zwrocWartoscPieniedzy()).strip('()')+" złotych")

    pieniadze = skarbonka.rozbij()

    print('Po rozbiciu : ',pieniadze)

except UderzylesSieWPalecException as e:

    with open('Pamietnik.txt','a+') as f:

        print('Uderzyłem się')
        f.write(str(datetime.today().date()))
        f.write(' Drogi pamiętniczku, mój palec znowu napotkał młotek na swej drodze. Bolało.\n')
        f.close()
except:
    print('Problem ze wczytaniem listy monet')
