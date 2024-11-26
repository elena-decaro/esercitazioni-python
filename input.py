#esercizio input

#istruzione
print("Ora ti chiederò di inserire dei numeri.")

#creo delle variabili con i numeri inseriti in input e le stampo
a = (input("Inserisci un numero: "))
print ("Hai inserito il numero ",a)
b = (input("Inserisci un secondo numero: "))
print("Hai inserito il numero ",b)

#cambio istruzione
print("Ora passiamo ad un altro gioco")

#creo qualcosa di un pochino (pochissimo!) più complicato
import random
c = int(input("Inserisci un numero (intero!) qui: "))
print("Il numero che hai inserito è questo: ", c)
d = random.randint(1,100)
print("Il numero randomico che ti è uscito è questo: ", d)

#fine del programma
print("Fine del programma.")