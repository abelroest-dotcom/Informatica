# Pythagoras calculator

# Functies declareren
def bereken_c(a, b):
    c = (a**2 + b**2) ** 0.5
    return c

def bereken_a(b, c):
    a = (c**2 - b**2) ** 0.5
    return a

def bereken_b(a, c):
    b = (c**2 - a**2) ** 0.5
    return b

# Keuze menu
print("Wat wil je berekenen?")
print("1. Schuine zijde c")
print("2. Zijde a")
print("3. Zijde b")

keuze = input("Kies 1, 2 of 3: ")

# Berekening op basis van keuze
if keuze == "1":
    a = float(input("Hoeveel is zijde a? "))
    b = float(input("Hoeveel is zijde b? "))
    uitkomst = bereken_c(a, b)
    print("De schuine zijde c is:", round(uitkomst, 2))

elif keuze == "2":
    b = float(input("Hoeveel is zijde b? "))
    c = float(input("Hoeveel is de schuine zijde c? "))
    uitkomst = bereken_a(b, c)
    print("Zijde a is:", round(uitkomst, 2))

elif keuze == "3":
    a = float(input("Hoeveel is zijde a? "))
    c = float(input("Hoeveel is de schuine zijde c? "))
    uitkomst = bereken_b(a, c)
    print("Zijde b is:", round(uitkomst, 2))

else:
    print("Ongeldige keuze!")
