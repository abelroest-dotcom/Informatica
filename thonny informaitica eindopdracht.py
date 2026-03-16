from browser import document
import math

def bereken(ev):
getalA = int(input("Geef de A: "))
getalB = int(input("Geef de B: "))
getalC = int(input("Geef de C: "))

discriminant = (getalB * getalB) - (4 * getalA * getalC)

if discriminant < 0:
    print("Er is geen oplossing")

elif discriminant == 0:
    X = (-getalB) / (2 * getalA)
    print("Er is 1 oplossing:")
    print(X)

else:
    X1 = ((-getalB) + (discriminant ** 0.5)) / (2 * getalA)
    X2 = ((-getalB) - (discriminant ** 0.5)) / (2 * getalA)
    print("Er zijn 2 oplossingen:")
    print("X1 =", X1)
    print("X2 =", X2)
