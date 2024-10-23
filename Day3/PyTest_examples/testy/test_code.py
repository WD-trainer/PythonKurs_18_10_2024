import pytest  # pip install pytest
import sys

from Day3.PyTest_examples.code_pytest import sumuj, dajCyfry, is_palindrome, calculate_average, calculate_percentage, loadDB, getOne, getData


def test_sumuj():
    assert sumuj(5, 3) == 8


def test_dajCyfryMin():
    tab = dajCyfry()
    assert min(tab) == 1


def test_dajCyfryMax():
    tab = dajCyfry()
    assert max(tab) == 10


def test_dajCyfryLen():
    tab = dajCyfry()
    assert len(tab) == 10


def test_palindrome_true():
    assert is_palindrome("kajak") == True
    assert is_palindrome("kajak           ") == True
    assert is_palindrome("level") == True
    assert is_palindrome("A man a plan a canal Panama") == True
    assert is_palindrome("racecar") == True


def test_palindrome_with_simple_palindromes():
    assert is_palindrome("radar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("deified") == True

def test_palindrome_with_spaces():
    assert is_palindrome("A man a plan a canal Panama") == True
    assert is_palindrome("No lemon no melon") == True

def test_palindrome_with_mixed_case():
    assert is_palindrome("RaceCar") == True
    assert is_palindrome("MadAm") == True

def test_non_palindromes():
    assert is_palindrome("hello") == False
    assert is_palindrome("world") == False
    assert is_palindrome("python") == False

def test_empty_string():
    assert is_palindrome("") == True

def test_single_character():
    assert is_palindrome("a") == True
    assert is_palindrome("z") == True

def test_palindrome_with_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama") == False  # Punctuation makes it not a palindrome in this implementation

def test_palindrome_with_numbers():
    assert is_palindrome("12321") == True
    assert is_palindrome("12345") == False



lista_przypadkow_testowych = ["hello", "python", "123456x"]
@pytest.mark.parametrize('text', lista_przypadkow_testowych)
def test_palindrome_false(text):
    assert is_palindrome(text) == False


lista_przypadkow_testowych2 = [("hello", False), ("python", False), ("123456x", False), ("Kajak", True)]
@pytest.mark.parametrize('text, result', lista_przypadkow_testowych2)
def test_palindrome_false_parametryzacja_z_wynikiem(text, result):
    assert is_palindrome(text) == result


def test_average_empty_list():
    assert calculate_average([]) is None


@pytest.mark.parametrize("numbers, expected_result", [
    ([1, 2, 3], 2.0),
    ([0, 0, 0, 0], 0.0),
    ([10, 20, 30, 40, 50], 30.0),
])
def test_average_parametrized(numbers, expected_result):
    assert calculate_average(numbers) == expected_result


def test_calculate_percentage_invalid_percent():
    with pytest.raises(ValueError) as e:
        calculate_percentage(100, -10)
    assert str(e.value) == "Percent must be between 0 and 100"




# def setup_module():
#     print("\n############## setup ##############")
#     loadDB()
#
# def teardown_module():
#     print("\n############## bye ##############")
#
# def test_getOne():
#     assert getOne(0)[1]=='Marian'
#
# def test_getData():
#     assert len(getData()) > 0



@pytest.fixture(scope="module", autouse=True)
def setup_and_teardown():
    print("\n############## setup ##############")
    loadDB()
    yield
    print("\n############## bye ##############")


def test_getData():
    assert len(getData()) > 0


def test_getOne():
    assert getOne(0)[1] == 'Marian'


@pytest.fixture(scope="function")
def example_fixture():
    print("\nSetup: Przygotowanie zasobów")
    data = {"key": "value"}
    yield data
    print("\nTeardown: Sprzątanie po teście")

# Testy współdzielą tę samą fixture (ponieważ scope='module')
def test_example_1(example_fixture):
    assert example_fixture["key"] == "value"

def test_example_2(example_fixture):
    assert example_fixture["key"] == "value"




@pytest.mark.skipif(sys.platform == "win32", reason="Pomijany na Windows")
def test_not_on_windows():
    assert True

@pytest.mark.skipif(sys.version_info < (3, 9), reason="Wymaga Pythona 3.9 lub wyższej")
def test_requires_python_39():
    assert True