# Kacper Karabinowski ETI II rok IV semestr
# Zadanie 1

import numpy as np

# Tworzenie tablicy liczby z losowymi liczbami rzeczywistymi z zakresu [-10, 10]
liczby = np.random.uniform(-10, 10, 10)
liczby = np.round(liczby, 2)

# Tworzenie tablicy waga z losowymi liczbami rzeczywistymi z zakresu (0, 1)
waga = np.random.uniform(0, 1, 3)
waga = np.round(waga, 2)


# Dokonanie splotu elementów obu tablic
def splot_tablicy(liczby, waga):
    wynik = np.zeros_like(liczby)
    n = len(liczby)
    m = len(waga)

    for i in range(n):
        suma_wazona = 0
        suma_wag = 0
        for j in range(m):
            index = i + j - (m // 2)
            if 0 <= index < n:
                suma_wazona += liczby[index] * waga[j]
                suma_wag += waga[j]
        wynik[i] = suma_wazona / suma_wag
    return wynik


wynik_splotu = splot_tablicy(liczby, waga)

print("Tablica liczby:", liczby)
print("Tablica waga:", waga)
print("Wynik splotu:", wynik_splotu)
