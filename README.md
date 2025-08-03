# [Generator Harmonogramu](https://github.com/badquacker/generator-harmonogramu)

## Opis
Prosty skrypt w Pythonie, który generuje harmonogram pracy na cały rok w cyklu 16-dniowym ciągłym.
Skrypt napisałem dla siebie, by móc szybko wygenerować grafik na cały rok dla mojej brygady. Harmonogram zapisywany jest do pliku CSV, skąd przekopiowuję dane do swojego harmonogramu przygotowanego w Excel.

## Format zapisu

![CSV](img/harm_csv.jpg)

## Harmonogram w Excel
Dane przekopiowuję jako wartości do przygotowanego wcześniej harmonogramu w Excel:

![Excel](img/harm_excel.jpg)

[Harmonogram EXCEL](harmonogram_github.xlsx)  
Przygotowany arkusz jest kompatypilny z LibreOffice.  

[Harmonogram LibreOffice](harmonogram_github.ods)
Tutaj wersja dla LibreOffice.

## Konfiguracja
Skrypt nie jest interaktywny i zmiana parametrów związana jest edycją samego skryptu. Zmienne są dość czytelnie rozpisane.

```
rok = 2025
przesuniecie_cyklu = 7 # 0 bez przesunięcia, X - o ile dni cykl będzie przesunięty
ilosc_osob = 4 # ile osob na zmianie

cykl = ['III', 'III', 'III', 'III', ' ', ' ', 'II', 'II', 'II', 'II', ' ', 'I', 'I', 'I', 'I', ' '] # można edytować, tutaj cykl 16-dniowy
```

## Wymagania
Python 3.X

## Uruchomienie
Dla Linux
```bash
python3 generator-harmonogramu.py
```
Dla Windows (jeżeli zainstalowany)
```cmd
py generator-harmonogramu.py
```
W katalogu ze skryptem pojawi się plik `harmonogram_2025.csv`

## Autor
badquacker

## Licencja
MIT
