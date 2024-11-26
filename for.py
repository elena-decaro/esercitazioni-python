#esercizio con for

#ho creato una lista vuota
lista = []

#ti chiedo di inserire una parola...
parola = input("inserisci una parola qui: ")
#...e la aggiungo alla lista
lista.append(parola)

#ripetiamo per una seconda parola
altraParola = input("inserisci una nuova parola qui: ")
lista.append(altraParola)

#stampo la lista di parole che hai inserito
print("Queste sono le parole che hai inserito:", lista)

#stampo le parole che hai inserito, ma singolarmente
for parola in lista:
    print("Ho stampato le tue parole: ", parola)


#termino il programma
print(" ") #spazietto tattico
print("Fine programma!")