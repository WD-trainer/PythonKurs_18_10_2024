import random
import requests  # pip install requests

# pip install pytest-cov


def sumuj(a: float, b: float) -> float:
    return a + b


def dajCyfry() -> list[int]:
    return list(range(1, 11))


# "kajak" true
# ""
# "kajak    " true
# "to nie jest palindromem" false
def is_palindrome(text: str) -> bool:
    """
    Sprawdza, czy dany ciąg znaków jest palindromem.

    Parameters:
        text (str): Ciąg znaków do sprawdzenia.

    Returns:
        bool: True, jeśli ciąg jest palindromem, False w przeciwnym razie.
    """
    text = text.lower().replace(" ", "")
    return (
        text == text[::-1]
    )


# napiszcie testy z parametryzacja (pytest) ktory sprawdzi czy potrafimy wyliczyc srednia
# osobny test dla pustej listy (dla None porownanie operatorem is)
def calculate_average(numbers: list[float]) -> float | None:
    if not numbers:
        return None
    return sum(numbers) / len(numbers)



def nieprzetestowana_funckja(a):
    if a > 10:
        print(f"Hahahahaha a mnie nie przetestowałeś! {a}")
    print(f"Testing")


def fetch_data():
    response = requests.get("https://example.com/api/data")
    return response.text



def calculate_percentage(value: float, percent: float) -> float:
    if percent < 0 or percent > 100:
        raise ValueError("Percent must be between 0 and 100")
    return value * (percent / 100)









# Dopisz testy do ponizszej funkcji
# upewnij sie ze funckja dziala jak nalezy z porpawnymi argumentami oraz przetestuj wyjątki przez podanie niepoprawnych danych
def integer_division(a, b):
    """
    Dzieli liczbę a przez b, tylko dla liczb całkowitych.
    Rzuca ValueError, jeśli a lub b nie są liczbami całkowitymi.
    Rzuca ZeroDivisionError, jeśli b == 0.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Obie liczby muszą być liczbami całkowitymi.")
    if b == 0:
        raise ZeroDivisionError("Dzielenie przez zero jest niedozwolone.")
    return a // b




#
baza = []

def loadDB():
    print("############## ŁADOWANIE BAZY ##############")
    global baza
    baza = [(1, "Marian"), (2, "Czesław"), (3, "Zenon"), (4, "Florian")]


def getData():
    global baza
    return baza


def getOne(index: int):
    global baza
    return baza[index]
