class wielblad:
    def __init__(self,ilosc,wysokosc):
        self.ilosc=ilosc
        self.wysokosc=wysokosc
    def __eq__(self,wielblad2):
        if self.wysokosc == wielblad2.wysokosc and self.ilosc ==wielblad2.ilosc:
           return True
        else:
            return False
    def __bool__(self):
        if self.ilosc >1:
            return True
        else:
            return False
    def __lt__(self,other):
        if self.wysokosc == other.wysokosc:
            if self.ilosc < other.ilosc:
                return "Pierwszy wielblad jest mniejszy"
            else:
                return "Drugi wielblad jest mniejszy"
        else:
            if self.wysokosc < other.wysokosc:
                return "Pierwszy wielblad jest mniejszy"
            else:
                return "Drugi wielblad jest mniejszy"
    def __gt__(self,other):
        if self.wysokosc == other.wysokosc:
            if self.ilosc > other.ilosc:
                return "Pierwszy wielblad jest wiekszy"
            else:
                return "Drugi wielblad jest wiekszy"
        else:
            if self.wysokosc > other.wysokosc:
                return "Pierwszy wielblad jest wiekszy"
            else:
                return "Drugi wielblad jest wiekszy"
            
        
w1=wielblad(1,300)
w2=wielblad(2,200)
print("Zad 1")
print(w1==w2)
print(w1<w2)
print(w1>w2)
print("zad 2")
print("w1")
print(bool(w1))
print("w2")
print(bool(w2))
class Sluzacy:
    def __init__(self,imie):
        self.imie=imie
    def __call__(self):
        return "Tak Panie?"
print("zad 3")
p1=Sluzacy("Michal")
print(p1())
print("zad 4")
class OgraniczonaLiczba:
    def __init__(self,liczba):
            if liczba >= -128 and liczba <=127:
                self.liczba=liczba
            else:
                print("-----Zla liczba-------")
        
    def __add__(self,other):
        wynik=0
        wynik=self.liczba+other.liczba
        if wynik >=-128 and wynik <=127:
            return wynik
        else:
            return "wynik wyszedl poza zakres"
    def __sub__(self,other):
        wynik=0
        wynik=self.liczba-other.liczba
        if wynik >=-128 and wynik <=127:
            return wynik
        else:
            return "wynik wyszedl poza zakres"
    def __mul__(self,other):
        wynik=0
        wynik=self.liczba*other.liczba
        if wynik >=-128 and wynik <=127:
            return wynik
        else:
            return "wynik wyszedl poza zakres"
    def wypisz(self):
        print(self.liczba)
        
liczba1=OgraniczonaLiczba(-2)
liczba1.wypisz()
liczba2=OgraniczonaLiczba(40)
liczba2.wypisz()
print("dodawanie")
print(liczba1+liczba2)
print("odejmowanie")
print(liczba1-liczba2)
print("mnozenie")
print(liczba1*liczba2)

print("zad 5")
import timeit
import time
def my_decorator(func):
    
    def wrapper(*args,**kwargs):
        print('funckja {}'.format(func.__name__))
        t1=time.time()
        result=func(*args,**kwargs)
        t2=time.time()-t1
        
        return result
    return wrapper
@my_decorator
def fib2(n): 
    a = 0
    b = 1
    if n < 0: 
        print("Incorrect input") 
    elif n == 0: 
        return a 
    elif n == 1: 
        return b 
    else: 
        for i in range(2,n): 
            c = a + b 
            a = b 
            b = c 
        return b 


def fib1(n): 
    if n < 2:
        return n
    else:
        return fib1(n-1) + fib1(n-2)
print("czas fib1")
t1=timeit.Timer("fib1(4)","from __main__ import fib1")
print (t1.timeit(1))
t2=timeit.Timer("fib2(35)","from __main__ import fib2")
print (t2.timeit(1))

