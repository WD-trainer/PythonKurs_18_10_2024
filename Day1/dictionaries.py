import operator
import random
import os
import re
from collections import defaultdict


if __name__ == '__main__':
    slownik = {}
    slownik2 = dict()

    info = {
        "LG123": "Telewizor 60' z HD Ready, wejściem na internety ifiltrem reklam",
        "SONY666": "Piekielnie dobry telewizor",
        "SZAJSUNG999": "Telewizor świetnie nadający się do zakrycia dziury w ścianie(i niczego więcej)"
    }

    print(info)
    print(info["LG123"])
    print(info.keys())
    print(info.values())

    # print(info["abc"])

    info["abc"] = "Jakis teskt"

    print(info["abc"])

    for i in info:
        print(f'i = {i}')
        print(f'info[i] = {info[i]}')

    for key in info.keys():
        print(info[key])

    if "LG123" in info:
        print("Mamy LG")
    else:
        print("niet :(")

    people = {}

    with open("dane.txt", "r") as file:
        for line in file:
            line_splited = line.rstrip().split(';')
            people[line_splited[0]] = (line_splited[1], line_splited[2])

    for key, value in people.items():
        print(f"Key: {key}: value: {value}")

    # wczytaj dane do słownika w ten sposób by pierwsza kolumna stanowila klucze a
    # druga przypisane do nich wartości. Przeiteruj po słowniku i wypisz klucze oraz przypisane do nich wartości
    ustawienia = {}

    with open("ustawienia.txt", "r") as file:
        for line in file:
            line = line.strip().split(';')
            if len(line) == 2:
                key, value = line
                ustawienia[key] = value

    for key, value in ustawienia.items():
        print(f'Klucz: {key}, wartosc: {value}')

    # Dlaczego tak?
    # def search_dict_by_value(dictionary: dict, searched_value: str) -> list[str]:
    #     found_elements = [value for k, v in dictionary.items() if v == searched_value]
    #     return found_elements

    studenci = {
        1001: {'imie': 'Jan', 'nazwisko': 'Kowalski', 'wiek': 21, 'oceny': [4, 3, 5, 4]},
        1002: {'imie': 'Anna', 'nazwisko': 'Nowak', 'wiek': 22, 'oceny': [5, 5, 4, 5]},
        1003: {'imie': 'Marek', 'nazwisko': 'Zielinski', 'wiek': 23, 'oceny': [3, 4, 2, 3]},
        1004: {'imie': 'Zofia', 'nazwisko': 'Wiśniewska', 'wiek': 20, 'oceny': [4, 4, 4, 4]},
        1005: {'imie': 'Krzysztof', 'nazwisko': 'Wojcik', 'wiek': 24, 'oceny': [2, 3, 2, 3]}
    }

    studenci[1006] = {'imie': 'Krzysztof2', 'nazwisko': 'Wojcik', 'wiek': 26, 'oceny': [2, 3, 2, 3]}

    list_of_names = [studenci[id]['imie'] for id in studenci]
    print(list_of_names)

    #  Oblicz średnią ocenę dla każdego studenta i dodaj ją do ich słownika
    for id in studenci:
        oceny = studenci[id]['oceny']
        srednia = sum(oceny) / len(oceny)
        studenci[id]['srednia_ocen'] = srednia

    print(studenci)

    nazwiska = ['Kowalski', 'Nowak', 'Zielinski', 'Wiśniewska', 'Wojcik']
    dlugosci_nazwisk = {nazwisko : len(nazwisko) for nazwisko in nazwiska if len(nazwisko) > 6}
    print(dlugosci_nazwisk)

    #  Znajdź studentów, którzy mają średnią ocenę powyżej 4.0, stworz słownik id: słownik 