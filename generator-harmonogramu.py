from datetime import date, timedelta
import csv

# Ustawienia
rok = 2025
przesuniecie_cyklu = 7  # tutaj cykl rozpoczyna sie od drugiej II zmiany
ilosc_osob = 4          # ilosc osob w brygadzie

# Separator dla PL CSV
separator_csv = ";"

# Zapis cyklu dla systemu 16-dniowego, gdzie 4 x III zmiana, 2 x Wolne, 4 x II zmiana, 1 x Wolne, 4 x I zmiana, 1 x Wolne
cykl = ['III', 'III', 'III', 'III', ' ', ' ', 'II', 'II', 'II', 'II', ' ', 'I', 'I', 'I', 'I', ' ']

# Zakres od 1 stycznia do 31 grudnia
start = date(rok, 1, 1)
koniec = date(rok, 12, 31)

# Bufor na dane
dzien_tygodnia = {i: [] for i in range(1, 13)}
symbol_zmiany = {i: [] for i in range(1, 13)}

# Przygotowanie tablic
while start <= koniec:
    symbol = cykl[przesuniecie_cyklu % len(cykl)]
    miesiac = start.month

    dzien_tygodnia[miesiac].append(f"{rok}-{miesiac}-{start.day}")
    symbol_zmiany[miesiac].append(symbol)

    start += timedelta(days=1)
    przesuniecie_cyklu += 1

# Zapis do pliku CSV
with open(f"harmonogram_{rok}.csv", "w", newline="", encoding="utf-8") as plik:
    zapis = csv.writer(plik, delimiter=separator_csv)
    for miesiac in range(1, 13):
        for _ in range(2):
            zapis.writerow(dzien_tygodnia[miesiac])
        for _ in range(ilosc_osob):
            zapis.writerow(symbol_zmiany[miesiac])
        zapis.writerow([])
