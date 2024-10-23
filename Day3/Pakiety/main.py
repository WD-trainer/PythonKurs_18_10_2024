import os

import pandas as pd
from numpy import zeros # import numpy as np



from PodPakiet import functions
# from PodPakiet.functions import times3

# from PodPakiet import times3




# PYTHONPATH jest istotny
# from Day1.functions import times2


#Nazwy modułów
#Importy cykliczne
#Importy relatywne - relative paths

if __name__ == "__main__":
    print(os.getenv("PYTHONPATH"))

    print(zeros((3,3)))

    print(f'3x3={functions.times3(3)}')

    # print(f'3x3={times3(3)}')
    # print(_times4(4))
