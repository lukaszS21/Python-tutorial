import random
class Moneta:
    def __init__(self, value,waluta): 
        wartosc = [0.01, 0.02, 0.05, 0.1, 0.2, 0.50, 1, 2, 5]
        waluta_=["PLN","EUR","USD"]
        if value not in wartosc:
            self._value = 0
        else:
            self._value = value
            
        if waluta not in waluta_:
            self._waluta = "nienzana moneta"
        else:
            self._waluta = waluta
       
            
    def get_value(self) -> int:
        return self._value 
    def get_waluta(self) -> str:
        return self._waluta
    def wypisz(self):
        print(str(self._value)+"-----"+str(self._waluta))


  
class Skarbonka:
    mon=[]
    def __init__(self):
        self.mon = []
        self.wal=[]
    def dodaj(self, moneta): 
        if type(moneta) is Moneta:
            if moneta._waluta=="PLN":
                self.mon.append(moneta._value)
            else:
                print("nieznana moneta")
        else:
            raise Exception("obiekt nie jest moneta")
    def suma(self):
        value = 0
        for moneta in self.mon:
            value += moneta.get_value()
        return value
    def wypisz(self):
        print(str(self.mon))
        
class Prze(Skarbonka):
    def __init__(self):
        self.mon = []
        
    
    def zwroc(self,moneta):
        if type(moneta) is Moneta:
            self.mon.remove(moneta)
        else:
            raise Exception("obiekt nie jest moneta")
class Złota(Skarbonka,Moneta):
        def __init__(self):
            self.mon = []
        def dodaj(self,moneta):
            if type(moneta) is Moneta:
                moneta._value=9000
                moneta._waluta ="PLN"
                self.mon.append(moneta._value)
            else:
                raise Exception("obiekt nie jest moneta")
        def wypisz(self):
            print(str(self.mon))
class Moneta2:
    zidentyfikowany = False
    war = 0
class Numizmatyk:
    __lista=[]
    def inedtyfikuj(self,moneta):
        if hasattr(moneta,'zidentyfikowany'):
            moneta.zidentyfikowany=True
            d=random.triangular(1900,2017,2000)
            if d <=1939 and d>=1914:
                moneta.war=1000
            elif d <=1914 :
                moneta.war=2000
            else:
                moneta.war=0
    def sprzedaj(self,moneta):
        self.inedtyfikuj(moneta)
        self.__lista.append(moneta.war)
        moneta.war=0
        return self.__lista
    def trans(self,moneta):
        moneta.zidentyfikowany=False
        del moneta.war


d1=Numizmatyk()
for i in range(0,100,1):
    g1=Moneta2()
    d1.inedtyfikuj(g1)
    d1.sprzedaj(g1)
print(sum(d1.sprzedaj(g1)))
