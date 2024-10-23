from timeit import default_timer as timer
import time

from abc import ABC, abstractmethod
from dataclasses import dataclass

import pandas as pd
from functools import total_ordering   # fills in missing comparison methods (<, <=, >, >=) based on just two: either __eq__ and one other comparison method like __lt__ or __gt__.


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

@total_ordering
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
    @classmethod
    def create_from_file(cls, path_to_file: str) -> list:
        """

        Parameters
        ----------
        path_to_file

        Returns
        -------

        """
        zawodnicy = []
        with open(path_to_file, "r") as plik:
            for linia in plik:
                dane = linia.strip().split(";")
                if len(dane) == 3:
                    imie, waga, wzrost = dane
                    zawodnicy.append(cls(masa=float(waga), wzrost=float(wzrost), imie=imie))
        return zawodnicy


    def __lt__(self, other):
        return self.BMI < other.BMI

    def __eq__(self, other):
        return True

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


list_zawodnikow = Zawodnik.create_from_file("dane.txt")
print(list_zawodnikow[0])

print("*" * 50)

nowa_lista_posortowana = sorted(list_zawodnikow, key= lambda zawodnik: zawodnik.BMI)
for z in nowa_lista_posortowana:
    print(z)

print("*" * 50)

list_zawodnikow.sort()
for z in list_zawodnikow:
    print(z)

print("*" * 50)


if list_zawodnikow[0] >= list_zawodnikow[1]:
    print("Wiekszy")
else:
    print("mniejszy")

print("*" * 50)


class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y


MathUtils.add(2,2)



# https://realpython.com/python-magic-methods/
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)

    def __len__(self):
        return 2

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Index out of range")

    def __setitem__(self, index, value):
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        else:
            raise IndexError("Index out of range")

    def __iter__(self):
        yield self.x
        yield self.y

    def __contains__(self, value):
        return value == self.x or value == self.y

    def __hash__(self):
        return hash((self.x, self.y))


v1 = Vector2D(3, 4)
v2 = Vector2D(5, 6)

print(repr(v1))
print(str(v2))

print(v1 == v2)  # __eq__
print(v1 + v2)  # __add__: Vector(8, 10)
print(v2 - v1)
print(v1 * 2)

print(len(v1))  # __len__: 2
print(v1[0], v1[1])  # __getitem__: 3 4

for coordinate in v2:  # __iter__
    print(coordinate)

print(5 in v2)  # __contains__

hash_value = hash(v1)  # __hash__
print(hash_value)

v1[0] = 15  # __setitem__
print(v1)


# Napisz klase Timer która będzie mierzyła czas wykonania funkcji jako context menager.
# klasa ta w zaleznosci od zmiennej verbose bedzie wypisywała na ekran czas wykonania przy wyjsciu z contextu
# from timeit import default_timer as timer
#timer_obj = timer
#start = timer_obj()
# cos co mierzymy
#end = timer_obj()

#def __enter__(self):
#def __exit__(self, *args):

#https://www.geeksforgeeks.org/context-manager-in-python/
class Timer:
    """
    Tu generalny opis do czego jest klasa
    """
    def __init__(self, verbose: bool):
        """

        Parameters
        ----------
        verbose
        """
        self.timer = timer
        self.elapsed = 0
        self.verbose = verbose
        self.start = 0

    def __enter__(self):
        """

        Returns
        -------

        """
        print("Zaczynam pomiar")
        self.start = self.timer()
        return self

    def __exit__(self, *args):
        print("Koncze pomiar")
        end = self.timer()
        self.elapsed = end - self.start
        self.elapsed *= 1000 # convert to miliseconds
        if self.verbose:
            print(f"Measured time: {self.elapsed}")





with Timer(verbose=True) as t:
    #time.sleep(3)
    print("Moja bardzo długa funkcja")


print(f'Ta funkcja trwała {t.elapsed}')

# Dokumentowanie klas
from pandas import DataFrame
#####################

class BankAccount:
    # Class variable to store interest rate
    interest_rate = 0.05

    def __init__(self, owner, balance):
        self.owner = owner  # Instance variable
        self.balance = balance

    def calculate_interest(self):
        self.balance += self.balance * BankAccount.interest_rate

    def __str__(self):
        return f'Account {self.owner} has {self.balance}'


account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 2000)

account1.calculate_interest()
print(account1)
print(BankAccount.interest_rate)  # Output: 0.05
BankAccount.interest_rate = 0.1
account2.calculate_interest()
account1.calculate_interest()
print(account1)
print(account2)
#
#
@dataclass   # https://docs.python.org/3/library/dataclasses.html
class Point:
    x: int
    y: int

point = Point(x=10, y=20)
print(point)


@dataclass
class Person:
    first_name: str
    last_name: str
    age: int


person1 = Person('Jan', 'Kowalski', 30)
person2 = Person('Anna', 'Nowak', 25)

print(person1)
print(person2)

print(person1 == person2)



#################################################### CWICZENIE DODATKOWE

# Stwórz klasę Ustawienia która będzie w momencie tworzenia obiektu czytac plik ustawienia.csv o treści:
# encoding;utf-8
# language;pl
# timezone;-2
# Dane te mają zostać wczytane do wewnętrznego słownika tak, by pierwsza kolumna stanowila klucze a druga wartosci.
# Obiekt ma umożliwiać sprawdzanie ustawień w ten sposób:
# u=Ustawienia()
# print( u['encoding'] )
# Obiekt ma umożliwiać też ustawienie wartości na zasadzie u[‘nazwa’]=’wartosc’.
# W przypadku zmiany powinna ona dotyczyć również zawartości pliku.

#################################################### CWICZENIE DODATKOWE


class IDraw(ABC):
    @abstractmethod
    def drawing(self):
        pass

class Figure(ABC):
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def give_name(self):
        print(f"Figure {self.name}, {self.color}")

    @abstractmethod
    def area(self):
        pass


class Squre(Figure, IDraw):
    def __init__(self, lenght:float):
        super().__init__("Squer", "red")
        self.lenght = lenght

    def area(self):
        return self.lenght ** 2

    def drawing(self):
        print("**")
        print("**")


class Rectangle(Figure, IDraw):
    def __init__(self, a:float, b:float, *args, **kwargs):
        super().__init__("Rectangle", "green", *args, **kwargs)
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def drawing(self):
        print("****")
        print("****")


class SpecialRectangle(Rectangle):
    def __init__(self, a: float, b: float, *args, **kwargs):
        super().__init__(a,b, *args, **kwargs)

    def area(self):
        return self.a * self.b * 2

    def drawing(self):
        print("****" * 2)
        print("****" * 2)

figury =  [Rectangle(2,3), Squre(50), Rectangle(6,8)]  # Figure("Nazwa") --- nie dozwolne tworzenie instancji klasy abstrakcyjnej
for f in figury:
    f.give_name()
    print(f.area())
    f.drawing()




# zmien klase animal na klase abstrakcyjna
# zmien metode speak na metode abstrakcyjna
# dodaj interfejs ILiveOn ktore bedzie posiadał funkcje where_I_live()
# dodac interfejs do klas pochodnych klasy animal

class ILiveOn(ABC):
    @abstractmethod
    def where_I_live(self):
        pass


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        pass

    def eat(self):
        print("eating")

    def __str__(self):
        return f'My name is {self.name}'


class Dog(Animal, ILiveOn):
    def speak(self):
        print(f"{self.name} barks")

    def where_I_live(self):
        print("In dog house outside")


class Cat(Animal, ILiveOn):
    def speak(self):
        print(f"{self.name} meows")

    def where_I_live(self):
        print("In my owner bed")


#animal = Animal("Generic Animal") # !!!!
dog = Dog("Buddy")
cat = Cat("Whiskers")

# animal.speak() # !!!!
dog.speak()
cat.speak()
cat.eat()

lista_zwierzat = [cat, dog]

for zwierze in lista_zwierzat:
    zwierze.speak()
    zwierze.where_I_live()
    zwierze.eat()
    print(zwierze)

if isinstance(cat, Cat):
    print("meow")

from sklearn.svm import SVC




################################## Example of mixin

class BorrowableMixin:
    def __init__(self):
        self._borrowed = False

    def borrow(self):
        if self._borrowed:
            raise Exception("Item already borrowed")
        self._borrowed = True

    def return_item(self):
        if not self._borrowed:
            raise Exception("Item not borrowed")
        self._borrowed = False

    def is_borrowed(self):
        return self._borrowed


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def info(self):
        return f"Book: {self.title} by {self.author}"


class DVD:
    def __init__(self, title, director):
        self.title = title
        self.director = director

    def info(self):
        return f"DVD: {self.title}, directed by {self.director}"


class BorrowableBook(Book, BorrowableMixin):
    def __init__(self, title, author):
        Book.__init__(self, title, author)
        BorrowableMixin.__init__(self)

class BorrowableDVD(DVD, BorrowableMixin):
    def __init__(self, title, director):
        DVD.__init__(self, title, director)
        BorrowableMixin.__init__(self)


book = BorrowableBook("1984", "George Orwell")
dvd = BorrowableDVD("Inception", "Christopher Nolan")

print(book.info())
book.borrow()
print(f"Czy jest wypozyczona {book.is_borrowed()}")
book.return_item()
print(f"Czy jest wypozyczona {book.is_borrowed()}")




# Python używa algorytmu C3 linearization (MRO - Method Resolution Order) do ustalania kolejności przeszukiwania klas bazowych.
class A:
    def do_something(self):
        print("A")

class B(A):
    def do_something(self):
        print("B")
        super().do_something()

class C(A):
    def do_something(self):
        print("C")
        super().do_something()

class D(B, C):
    def do_something(self):
        print("D")
        super().do_something()


d = D()
d.do_something()