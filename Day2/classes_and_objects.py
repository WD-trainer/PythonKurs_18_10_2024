from timeit import default_timer as timer
import time

from abc import ABC, abstractmethod
from dataclasses import dataclass

import pandas as pd

class Osoba(object):

    def __init__(self, imie:str, nazwisko:str, wiek:int):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def wypiszMnie(self):
        print(self.imie, self.nazwisko, self.wiek)

    def __str__(self):
        return f'Cześć jestem: {self.imie}, {self.nazwisko}, {self.wiek}'

    def __repr__(self):
        return f"Osoba({self.imie, self.nazwisko, self.wiek})"



o = Osoba("Wojtek", "Dudzik", 31)
o2 = Osoba("Jan", "Nowak", 23)
print(o.imie, o.nazwisko, o.wiek)

o.wypiszMnie()
o2.wypiszMnie()

#o.imie = "Kamil"
#print(o.imie)

o3 = Osoba(imie="Krzysztof", nazwisko="Nowak", wiek=32)

lista_osob = [o, o2, o3]

for osoba in lista_osob:
    osoba.wypiszMnie()

print("*" * 45)


#     Stwórz klasę "Samochod" posiadającą pola "marka", "model", "rejestracja".
#     Klasa ta powinna zawierać też metodę "wyswietl" wypisującą dane z obiektu na konsoli
#     Stwórz dwa obiekty tej klasy i korzystajac  z metody "wyświetl" wyswietl na konsoli ich zawartość.
class Samochod:

    def __init__(self, marka: str, model: str, kierowca: Osoba, rejestracja:str = "DOMYSLNA"):
        self.marka = marka
        self.model = model
        self.rejestracja = rejestracja
        self.kierowca = kierowca

    def wyswietl(self):
        print(f"Samochod: {self.marka}, {self.model}, {self.rejestracja}")

    def __repr__(self):
        return f'Samochod("{self.marka}", "{self.model}", "{self.rejestracja}")'

    def __str__(self):
        return f'Samochod: {self.marka}, {self.model}, {self.rejestracja}, {self.kierowca}'

    def _funckje_dla_mechanika(self):
        print("Naprawiam")


s1 = Samochod("Opel", "Astra", rejestracja="KK 88023", kierowca=o)
s2 = Samochod("Audi", "R8", rejestracja="WW DR346", kierowca=o2)

# s1.wyswietl()
# s2.wyswietl()

s2._funckje_dla_mechanika()

print(s1)
napis_z_samochod = str(s1)
napis_z_osoby = str(o)

print(f'Napis z samochodu {napis_z_samochod}')
print(f'Napis z osoby {napis_z_osoby}')


class Circle:
    def __init__(self, radius):
        self.__radius = radius


    def _get_radius(self):
        print("Get radius")
        return self.__radius

    def _set_radius(self, value):
        print("Set radius")
        self.__radius = value

    radius = property(fget=_get_radius,
                      # fset=_set_radius,
                      doc="Radius property of circle")


kolo = Circle(5)

print(kolo.radius)
try:
    kolo.radius = 30
except Exception as err:
    print(err)


class Rectangle:
    def __init__(self, a:int, b:int):
        self._a = a
        self.b = b

    @property
    def dlugosc_a(self):
        print("Get a")
        return self._a

    # @dlugosc_a.setter
    # def a(self, value):
    #     print("Set a")
    #     self._a = value


r = Rectangle(4,2)
r.b = 8
# r.dlugosc_a = 30
print(f'Rectangle {r.dlugosc_a}, {r.b}')


# Stwórz klasę Zawodnik posiadającą pola wzrost i masa, imie. Pola te mają być uzupełniane przy tworzeniu obiektu.
# stworz atrybut BMI który będzie tylko do odczytu
# Powołaj do życia obiekt tej klasy i wyświetl na konsoli obliczone BMI.
# Wzrost jest atrybutem chronionym (__wzrost)
# Waga może być zmieniana ale też jako atrybut z wykorzystaniem dekoratora @property
# wzor na bmi = masa / (wzrost ** 2)   wzrost podany w metrach 1.84
# dodac metode __str__
class Zawodnik:
    def __init__(self, wzrost: float, masa: float, imie: str):
        self.__wzrost = wzrost
        self._masa = masa
        self._imie = imie

    @property
    def BMI(self) -> float:
        return self._masa / (self.__wzrost ** 2)

    @property
    def waga(self) -> float:
        return self._masa

    @waga.setter
    def waga(self, value: float):
        self._masa = value

    def __str__(self):
        return f'Zawodnik: {self._imie}, o BMI={self.BMI:.3f}'

    @staticmethod
    def nie_uzywam_atrybutow(info:str):
        print(info)

    @classmethod
    def create_from_string(cls, text: str):
        dane = text.strip().split(';')
        if len(dane) == 3:
            wzrost_cm, waga_lbs, imie = dane
            z = cls(wzrost=int(wzrost_cm) / 100, masa=int(waga_lbs) * 0.454, imie=imie)
            return z


    # odczytali dane z pliku dane.txt
    # zbudowali sobie liste zawodnikow (jako obietky klasy) przy uzyciu  @classmethod
    



    # Bardzo zła praktyka
    # def dodaj_atrybut_nazwisko(self, nazwisko:str):
    #     self.nazwisko = nazwisko



z = Zawodnik(1.8, 80, "Jan")
# z.dodaj_atrybut_nazwisko("Nowak")
print(z)
z.waga = 75
print(z)

Zawodnik.nie_uzywam_atrybutow("Hello")
z.nie_uzywam_atrybutow("Hello world")


z2 = Zawodnik.create_from_string("176;150;Paweł")
print(z2)




class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y


MathUtils.add(2,2)