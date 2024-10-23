import os

import pandas as pd
from numpy import zeros # import numpy as np

# import numpy as pd
# from numpy import * # raczej zła praktyka

from PodPakiet import functions

#from PodPakiet.functions import times3

from PodPakiet import times3


# Stwórz pakiet zawierający moduł który bedzie zawierał funkcję przyjmującą wzrost i masę a zwracającą bmi.
# Zaimportuj i wywołaj tę funkcję w taki sposób by przy jej wywołaniu nie trzeba było  podawać nazwy pakietu ani modułu.
# W tym module dopisz funkcje walidacji danych dla funkcji BMI - czy waga < 200 i 1.00 < wzrost < 2.50. Jesli warunek nie jest spelniony
# rzuc wyjatkiem Value error. # raise ValueError("wiadomosc bledu")
# W pliku __init__.py ustaw zmienna __all__ tak aby tylko funkcja liczac BMI byla widoczna po imporcie pakietu
# dodajcie print do pliku __init__.py
#import BodyMassIndex as bmi
from BodyMassIndex import calculate_bmi




# PYTHONPATH jest istotny
# from Day1.functions import times2

# from Day2.classes_and_objects import Zawodnik


#Nazwy modułów
#Importy cykliczne
#Importy relatywne - relative paths

if __name__ == "__main__":
    df = pd.DataFrame()

    print(os.getenv("PYTHONPATH"))

    print(zeros((3,3)))

    #print(f'3x3={functions.times3(3)}')

    # print(f'3x3={times3(3)}')
    print(functions._times4(4))

    try:
        height = [2.11, 1.80]
        weight = [100, 400]
        for h, w in zip(height, weight):
            bmi_result = calculate_bmi(h, w)
            print("Your BMI is:", bmi_result)
    except ValueError as e:
        print("Error:", e)

    #dokumentacja i sprawdzanie infomracji
    help(calculate_bmi)

    import BodyMassIndex

    # Wywołanie docstringa pakietu
    print(BodyMassIndex.__doc__)

    # Sprawdzanie wersji pakietu
    print("Package version:", BodyMassIndex.__version__)  # scipy==1.0
