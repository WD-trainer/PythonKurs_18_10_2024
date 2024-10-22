from collections.abc import Iterator

from classes_and_objects import Zawodnik

print("*" * 50)
print("*" * 50)
print("*" * 50)
print("*" * 50)
print("*" * 50)

class IncrementIterator:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == self.i:
            raise StopIteration
        self.i += 1
        return self.i


for e in IncrementIterator(10):
    print(e)

print("*" * 50)


class MiesiaceIterator:
    def __init__(self):
        self.miesiace = [
            "Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec",
            "Lipiec", "Sierpień", "Wrzesień", "Październik", "Listopad", "Grudzień"
        ]
        self.indeks = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.indeks < len(self.miesiace):
            miesiac = self.miesiace[self.indeks]
            self.indeks += 1
            return miesiac
        else:
            raise StopIteration

    def restart(self):
        self.indeks = 0


# Użycie iteratora
miesiace_iterator = MiesiaceIterator()

print("Miesiące:")
for i in range(12):
    print(next(miesiace_iterator))

miesiace_iterator.restart()
next(miesiace_iterator)

for i in range(11):
    print(next(miesiace_iterator))


print("*" * 50)

# uzupełnic klase lista zwodnikow o metody __iter__ oraz __next__
class ListaZawodnikow(Iterator):
    def __init__(self, path:str):
        self.zawodnicy = []
        with open(path, "r") as plik:
            for linia in plik:
                dane = linia.strip().split(";")
                if len(dane) == 3:
                    imie, waga, wzrost = dane
                    self.zawodnicy.append(Zawodnik(masa=float(waga), wzrost=float(wzrost), imie=imie))
        self.index = 0


    def __next__(self):
        if self.index == len(self.zawodnicy):
            raise StopIteration
        self.index += 1
        return self.zawodnicy[self.index - 1]




nasza_lista = ListaZawodnikow("dane.txt")
zawodnik = next(nasza_lista)

for z in nasza_lista:
    print(z)


print("*" * 50)

########################## Kiedy __iter__ nie zwraca self
class MyCollection:
    def __init__(self, items):
        self.items = items

    def __iter__(self):
        return MyCollectionIterator(self.items)


class MyCollectionIterator:
    def __init__(self, items):
        self.items = items
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.items):
            raise StopIteration
        item = self.items[self.index]
        self.index += 1
        return item


# Tworzymy kolekcję
collection = MyCollection([1, 2, 3])

# Iterujemy po kolekcji
for item in collection:
    print(item)

# Iterujemy po kolekcji kolejny raz
for item in collection:
    print(item)


print("*" * 50)



import torch
from torch.utils.data import DataLoader, Dataset


# Definiujemy niestandardowy dataset
class MyDataset(Dataset):
    def __init__(self):
        self.data = torch.arange(10)  # Tworzymy proste dane od 0 do 9

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]

# Tworzymy dataset
dataset = MyDataset()

# Używamy DataLoader, który tworzy iterator
dataloader = DataLoader(dataset, batch_size=2, shuffle=True)

# Iterujemy po DataLoader (wykorzystując iterator wbudowany w DataLoader)
for batch in dataloader:
    print(batch)