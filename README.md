# WYPRAWA W KOSMOS

## Autor
Adam Kurbiel

---

## Opis projektu

Projekt jest symulacją wyprawy statku kosmicznego w dwuwymiarowym świecie.

Statek porusza się po mapie za pomocą kąta (0–359°), zużywa energię i może zostać uszkodzony w trakcie wyprawy. W świecie występują różne pola oraz losowe zdarzenia, które wpływają na przebieg symulacji.

Celem jest odnalezienie rdzenia energetycznego i przetrwanie jak największej liczby kroków.

---

## Świat

Świat jest planszą 2D ograniczoną współrzędnymi zależnymi od poziomu trudności:

- easy  
- normal  
- hard  

W świecie znajdują się:

- strefy energii (odzyskanie energii)
- strefy niebezpieczne (utrata integralności)
- stacje naprawcze (odzyskanie integralności)
- rdzeń energetyczny (cel wyprawy)

---

## Sterowanie

W każdej turze gracz wybiera jedną akcję:

1. ruch do przodu  
2. obrót w lewo  
3. obrót w prawo  
4. skanowanie terenu  
5. tryb turbo  

---

## Zasoby

Statek posiada dwa podstawowe zasoby:

- energia – zużywana przy ruchu i akcjach
- integralność – wytrzymałość statku

---

## Zdarzenia losowe

W trakcie symulacji mogą wystąpić losowe zdarzenia:

- deszcz meteorytów (utrata integralności)
- wiatr słoneczny (zysk energii)
- grawitacyjna anomalia (utrata energii i przesunięcie)
- złom kosmiczny (odzyskanie integralności)

---

## Ruch

Ruch statku oparty jest o kąt:

- użytkownik ustawia kierunek startowy
- ruch przeliczany jest na współrzędne x, y
- możliwy jest obrót o 45 stopni
- tryb turbo zwiększa dystans ruchu kosztem zasobów

---

## Warunki zakończenia

Symulacja kończy się, gdy:

- energia spadnie do 0
- integralność spadnie do 0
- zostanie przekroczony limit kroków
- zostanie odnaleziony rdzeń

---

## Raport końcowy

Po zakończeniu programu wyświetlany jest raport zawierający:

- nazwę wyprawy i statku
- pozycję końcową
- liczbę wykonanych kroków
- pozostałą energię i integralność
- powód zakończenia
- końcowy wynik punktowy
- listę ważniejszych zdarzeń

---

## Wizualizacja (turtle)

Program wykorzystuje moduł turtle do rysowania trasy wyprawy.

Na ekranie widoczne są:

- granice świata
- trasa statku
- punkty startowe
- obiekty świata (strefy i rdzeń)
- ruch w czasie rzeczywistym

---

## Uruchomienie

Wymagania:
- Python 3.11

Uruchomienie:
```bash
python main.py
```
## Uwagi

Program nie wymaga dodatkowych bibliotek i działa w standardowej instalacji Pythona.
