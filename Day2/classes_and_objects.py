from timeit import default_timer as timer
import time

from abc import ABC, abstractmethod
from dataclasses import dataclass


class Osoba:

    def __init__(self, imie:str, nazwisko:str, wiek:int):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def wypiszMnie(self):
        print(self.imie, self.nazwisko, self.wiek)



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

    def __init__(self, marka: str, model: str, rejestracja:str):
        self.marka = marka
        self.model = model
        self.rejestracja = rejestracja

    def wyswietl(self):
        print(f"Samochod: {self.marka}, {self.model}, {self.rejestracja}")


s1 = Samochod("Opel", "Astra", "KK 88023")
s2 = Samochod("Audi", "R8", "WW DR346")

s1.wyswietl()
s2.wyswietl()