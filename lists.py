# ==========================================
# Voorbeeld Opdracht
# Maak een lijst aan met daarin de volgende getallen: 10, 20 en 30
#
# Voer de volgende opdrachten uit:
# - Voeg het getal 40 toe aan (het einde van) de lijst
#
# Aan het einde print je de lijst 'getallen'.
# ==========================================


# list met getallen
getallen = [10, 20, 30]

# Voeg het getal 40 toe aan (het einde van) de lijst
getallen.append(40)
print('list na toevoeging 40 aan het einde van de lijst: ', getallen)  # Het resultaat is: [10, 20, 30, 40]


# ==========================================
# Opdracht 1:
# Maak een lijst met daarin de volgende getallen: 2, 4, 7, 11 en 19
# Voer de volgende opdrachten uit:
# - Voeg het getal 22 toe aan (het einde van) de lijst
# - Voeg het getal 6 toe tussen 4 en 7
# - Vervang het getal 4 door het getal 5
# - Print de lijst 'getallen'
#
# Verwachte uitkomst: [2, 5, 6, 7, 11, 19, 22]
# ==========================================

getallen = [2,4,7,11,19]
getallen.append(22)
print(getallen)
getallen.insert(2,6)
print(getallen)
getallen[1] = 5
print(getallen)

# ==========================================
# Opdracht 2:
# In de Fibonacci rij bestaat elk getal uit de som van de twee voorgaande getallen: 1, 1, 2, 3, 5, 8 enzovoorts
# De som van 1 en 1 is 2, de som van 1 en 2 is 3, enzovoorts. Implementeer de functie ‘fibonacci’ die een lijst als parameter meekrijgt.
# Voer de volgende opdrachten uit:
# - Maak een variabele aan genaamd 'fibonacci_start_reeks' en geef  die de eerste twee elementen van de Fibonacci reeks.
# - Maak een functie genaamd fibonacci die de fibonacci_reeks uitbreidt met een nieuw element.
# - Roep de functie 5 keer aan (Bijvoorbeeld met een for-loop).
# - Print de waarde van de fibonacci_reeks
#
# Verwachte uitkomst:   [1, 1, 2, 3, 5, 8, 13]
# ==========================================

# === VERSIE 1 ===
# De regel: 'return fibonacci' klopt niet, in dit geval return je de functie en niet de waarde.
# Waarom werkt de code wel? Omdat de append wel werkt en dat wordt in de for loop aangeroepen, maar er wordt niets gedaan met de functie
# De functie doet niets
print('=== VERSIE 1 ===')
fibonacci_start_reeks = [1,1]

def fibonacci(fibonacci_start_reeks):
    fibonacci_start_reeks.append(fibonacci_start_reeks[-1] + fibonacci_start_reeks[-2])
    return  fibonacci

for i in range(1,6):
    fibonacci(fibonacci_start_reeks)
print(fibonacci_start_reeks)


# === VERSIE 2 ===
# In de functie geef je de waarde van de lijst terug, dit is goed
# In de for loop geef je aan hoe vaak dat moet gebeuren
# return van de functie is overbodig. Het is correct geschreven, maar je doet er niets mee
print('=== VERSIE 2 ===')
fibonacci_start_reeks = [1,1]

def fibonacci(fibonacci_start_reeks):
    fibonacci_start_reeks.append(fibonacci_start_reeks[-1] + fibonacci_start_reeks[-2])
    return  fibonacci_start_reeks

for i in range(1,6):
    fibonacci(fibonacci_start_reeks)
print(fibonacci_start_reeks)


# === VERSIE 3 ===
# In de functie geef je de waarde van de lijst terug
# In de for loop geef je aan hoe vaak dat moet gebeuren
# return heb je niet nodig in de functie
print('=== VERSIE 3 ===')
fibonacci_start_reeks = [1,1]

def fibonacci(fibonacci_start_reeks):
    fibonacci_start_reeks.append(fibonacci_start_reeks[-1] + fibonacci_start_reeks[-2])


for i in range(1,6):
    fibonacci(fibonacci_start_reeks)
print(fibonacci_start_reeks)

# === VERSIE 4 ===
# Als je print statement buiten de for loop plaatst dan krijg je de lijst in zijn geheel te zien
# Als je de print statement in de for loop plaatst dan print het elke iteratie van de for loop
print('=== VERSIE 4 ===')
fibonacci_start_reeks = [1,1]

def fibonacci(fibonacci_start_reeks):
    fibonacci_start_reeks.append(fibonacci_start_reeks[-1] + fibonacci_start_reeks[-2])


for i in range(1,6):
    fibonacci(fibonacci_start_reeks)
    print(fibonacci_start_reeks)


# ==========================================
# Opdracht 3:
# Maak een lijst ‘kwadraten’ die de kwadraten bevat van de getallen 1 tot en met 10. Gebruik een for loop.
#
# Verwachte uitkomst:  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# ==========================================
# === VERSIE 1 ===
# Ik dacht dat het zo moest maar x kan niet omdat het niet gedefinieërd is
#kwadraten = [x**2 for i in range(1,11)]
#print(kwadraten)

# === VERSIE 2 ===
# De 'i' is datgene wat je wil kwadrateren
kwadraten = [i**2 for i in range(1,11)]
print(kwadraten)

# === VERSIE 3 ===
# Dit werd in de opdracht gevraagd
# Je kunt range ook invullen met een len() functie
kwadraten = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(kwadraten)):
    kwadraten[i] = kwadraten[i]**2
print(kwadraten)



