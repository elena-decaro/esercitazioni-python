#intanto creo il menù che l'utente può utilizzare per scegliere ciò che vuole fare.
from libro import visualizza, aggiungere, prestito, restituizione, libriprestati, disponibilita, uscita
from libro import listaLibri
from libro import libriPrestati

while (True):
    print("Ciao! Benvenuto nella libreria, cosa vuoi fare oggi?")
    print(" ")
    print(" 1. Voglio vedere il catalogo dei libri")
    print(" 2. Voglio aggiungere un libro nel catalogo")
    print(" 3. Voglio sapere se un libro è disponibile")
    print(" 4. Voglio prendere in prestito un libro")
    print(" 5. Voglio restituire un libro")
    print(" 6. Voglio vedere la lista di libri prestati")
    print(" 7. Voglio uscire dalla libreria")
    print(" ")
    scelta = int(input("Inserisci il numero corrispondente alla funzione scelta: "))

    if scelta == 1: 
        visualizza()
    elif scelta == 2:
        aggiungere()
    elif scelta == 3:
        disponibilita()
    elif scelta == 4:
        prestito()
    elif scelta == 5: 
        restituizione() 
    elif scelta == 6:
        libriprestati()
    elif scelta == 7:
        uscita()
        break
    else: 
        print(" ")
        print("Questa opzione non è disponibile.")
        print("Per favore, scegli un'opzione presente nel menù.")
        print("Fai ripartire il programma per tornare al menù principale.")
        print(" ")

