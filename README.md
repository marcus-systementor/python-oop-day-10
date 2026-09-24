# Labb: Från funktioner till object – två TV-apparater

Bygg om ett fungerande procedurellt TV-program till en `class`. Två TV-apparater är självständiga: när du ändrar volymen på den ena ändras inte den andra. Arbeta i små steg och kör programmet ofta.

## Mål

Du ska kunna skilja mellan `class` och `object`, förstå vilket object `self` syftar på och skapa två object med eget `state`.

## Kom igång

1. Gör den ograderade avstämningen i `diagnostic.md` tillsammans med klassen.
2. Öppna lärarens publika template på GitHub, välj **Use this template → Create a new repository** och döp ditt repo till exempelvis `oop-tv-ditt-namn`. Välj **Private** för ditt eget repo.
3. Klona **ditt eget repo** och öppna det i VS Code.
4. Förutsäg vad programmet skriver ut. Kör `python student/procedural_tv.py` (på Windows eventuellt `py`, på vissa datorer `python3`). Jämför med din förutsägelse.

Inga externa Python-paket behövs.

## Uppgift 1: Läs startkoden

Peka ut vilka värden som beskriver en TV och vilka funktioner som ändrar eller läser dem. Skriv dina svar i `REFLECTION.md`. Kör gärna programmet en gång till med andra anrop.

## Uppgift 2: Skapa en class

Skapa `student/tv.py` med `class TV`:

- `__init__(self, brand)` sparar märket och ger varje ny TV `is_on = False` och `volume = 10`.
- `turn_on(self)` sätter `is_on` till `True`.
- `increase_volume(self)` ökar volymen med 1 **bara om TV:n är på**.
- `get_status(self)` returnerar samma slags text som funktionen i startkoden.

Skriv först `__init__` och skapa ett object. Lägg till en `method` i taget och testa den innan du fortsätter.

## Uppgift 3: Två object

Skapa `student/main.py`. Skapa `first = TV("Nord")` och `second = TV("Syd")`. Slå på `first`, höj dess volym två gånger och försök höja volymen på `second` när den är av. Skriv ut status för båda. Förutsäg resultatet innan du kör.

Förväntad output från både startkoden och din färdiga lösning:

```text
Nord: on=True, volume=12
Syd: on=False, volume=10
```

## Uppgift 4: Reflektera och dela

Fyll i `REFLECTION.md`. Gör minst en `commit` och `push`. För att läraren ska kunna öppna ditt privata repo: bjud in lärarens arbetskonto via **Settings → Collaborators → Add people**, och dela sedan repo-länken till marcus@systementor.se.

## Extra uppgift

Lägg till `turn_off(self)` och `change_channel(self, channel)` med ett nytt `channel` som startar på 1. Bestäm vad som ska hända om TV:n är avstängd. Testa att en ändring på `first` inte påverkar `second`. Frågor om giltiga kanaler och volymgränser sparar vi till senare.

Förslag på commit messages: `Add TV class` och `Use two independent TVs`.
