# Startavstämning i Python

Detta är en övning, inte ett betygsgrundande prov. Arbeta självständigt i cirka 20 minuter. Skriv först vad du tror att koden gör; kör sedan exemplen och jämför. Det går bra att lämna en fråga ofärdig.

## 1. Variabler och värden

Vad skrivs ut? Vilka värden har `first` och `second` efteråt?

```python
first = 10
second = first
first = first + 5
print(second)
```

## 2. Villkor och loop

Vad skrivs ut, och vilka värden läggs till i `total`?

```python
total = 0
for value in [10, 20, 30]:
    if value > 10:
        total += value
print(total)
```

## 3. Function och return

Vad skrivs ut? Vad gör `return`, och vad gör `print`?

```python
def add_tax(price):
    return price + 5

total = add_tax(20)
print(total)
```

## 4. Dictionary som ändras av en function

Vad skrivs ut? Vilken TV ändras, och varför?

```python
def increase_volume(tv):
    tv["volume"] += 1

first = {"brand": "Nord", "volume": 10}
second = {"brand": "Syd", "volume": 10}
increase_volume(first)
print(first["volume"], second["volume"])
```

## 5. Om du får tid över

Skriv `turn_on(tv)` som ändrar värdet för `is_on` till `True` i en dictionary för en TV. Testa funktionen på två TV-apparater. Skriv också en sak du vill att vi förklarar tillsammans.
