#frutta = ["mela", "pera", "banana", "arancia", "mandarino", "mango", "ciliegia", "lampone", "ribes", "kiwi"]
#nomeFrutto = str(input("Inserisci il frutto che ti serve qui"))
#if nomeFrutto in frutta:
#    print("Il kiwi è disponibile!")
#else:
#    print("Spiase")


#password = int,str(input("Inserisci la tua password qui"))
#passwordInserita = ["PasswordGiusta1", "passwordGiusta2"]
#if password in passwordInserita:
#    print("Puoi accedere!")
#else:
#    print("La password è sbagliata.")

#i = 1 
#while i <= 5:
#    print(i)
#    i +=1 #i++ non funzionaaaaaa


#parola = ""
#while parola != "stop":
#    parola = input("Inserisci una parola")


#for i in range (10): #in questa maniera incrementa da solo senza necessità del i += 1 
#    print("ciao!")

#for i in range (5,10):
#    print(i)


#nomi = ["Mario", "Luigi", "Peach"]
#for nome in nomi:
#    print(nome)

#parola = "ciao"
#for carattere in parola:    
#    print(carattere)

#for i in range (2,11 ,2): #il ,2 serve a fargli capire ogni quanto deve contare nel range di numeeri tra 2 e 11
#    print(i)

#import random

#numero = random.randint(1,100) #se metto il %numero significa import random



#import random
#numerouno = random.randint(1, 20)
#numerodue = random.randint(1,20)
#print("Il primo numero scelto è: ", numerouno)
#print("Il secondo numero scelto è: " ,numerodue)
#if numerouno > numerodue:
#    print("Il primo numero che hai scelto è maggiore del secondo")
#elif numerouno < numerodue: 
#    print("Il primo numero che hai scelto è minore del secondo")
#else:
#    print("Hai inserito due numeri uguali, fava")


import random
numeroScelto = int(input("Scegli un numero compreso tra 1 e 20: "))
print("Hai scelto il numero: ", numeroScelto)
numeroRandom = random.randint(1,20)
print("Il numero randomico è ", numeroRandom)
if numeroScelto > numeroRandom:
    print("Il numero che hai scelto è maggiore del numero random")
elif numeroScelto < numeroRandom:
    print("Il numero che hai scelto è minore del numero random")
else: 
    print("Hai scelto lo stesso numero del numero random!")

    #commento