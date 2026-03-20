# Variabelen
naam = "Temperatuur Omrekentool"
print(naam)

# Functies
def celsius_naar_fahrenheit(celsius):
    resultaat = celsius * 9 / 5 + 32
    return resultaat

def celsius_naar_kelvin(celsius):
    resultaat = celsius + 273.15
    return resultaat

def celsius_naar_rankine(celsius):
    resultaat = (celsius + 273.15) * 9 / 5
    return resultaat

def fahrenheit_naar_celsius(fahrenheit):
    resultaat = (fahrenheit - 32) * 5 / 9
    return resultaat

def kelvin_naar_celsius(kelvin):
    resultaat = kelvin - 273.15
    return resultaat

def rankine_naar_celsius(rankine):
    resultaat = (rankine - 491.67) * 5 / 9
    return resultaat

# Keuzemenu - def berekenen 
print("Wat wil je omrekenen?")
print("1 - Celsius naar Fahrenheit")
print("2 - Celsius naar Kelvin")
print("3 - Celsius naar Rankine")
print("4 - Fahrenheit naar Celsius")
print("5 - Kelvin naar Celsius")
print("6 - Rankine naar Celsius")

keuze = input("Kies een nummer: ")
getal = float(input("Voer de temperatuur in: "))

# Berekening uitvoeren
if keuze == "1":
    uitkomst = celsius_naar_fahrenheit(getal)
    print(getal, "Celsius =", uitkomst, "Fahrenheit")

elif keuze == "2":
    uitkomst = celsius_naar_kelvin(getal)
    print(getal, "Celsius =", uitkomst, "Kelvin")

elif keuze == "3":
    uitkomst = celsius_naar_rankine(getal)
    print(getal, "Celsius =", uitkomst, "Rankine")

elif keuze == "4":
    uitkomst = fahrenheit_naar_celsius(getal)
    print(getal, "Fahrenheit =", uitkomst, "Celsius")

elif keuze == "5":
    uitkomst = kelvin_naar_celsius(getal)
    print(getal, "Kelvin =", uitkomst, "Celsius")

elif keuze == "6":
    uitkomst = rankine_naar_celsius(getal)
    print(getal, "Rankine =", uitkomst, "Celsius")

else:
    print("Ongeldige keuze!")
