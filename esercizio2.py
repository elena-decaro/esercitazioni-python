import random

n1 = float(input("Inserisci un numero - anche con la virgola - qui: "))
print("Il numero che hai inserito è: ", n1)
n2 = random.randint(1,100)
print("Il numero randomico che è uscito è: ", n2)

if n1 < n2:
    print("Il numero che hai scelto è minore del numero randomico")
elif n1 > n2:
    print("Il numero che hai scelto è maggiore del numero randomic")
else:
    print("I due numeri potrebbero essere uguali!")

#devo capire ancora un po' come funziona questa roba!