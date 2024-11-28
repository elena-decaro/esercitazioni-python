listaLibri = []  #creo una lista di libri vuota, ovvero il "catalogo"
libriPrestati = [] #creo il mio 'carrello' di libri

#Funzione 1: ti fa visualizzare quali libri sono nel catalogo
def visualizza():  
    print(" ") #spazio tattico. nd: non chiedetemi perché è qui e non in libreria. 
    print(listaLibri)
    print("") #spazio tattico

#Funzione 2: ti fa aggiungere un libro al catalogo
def aggiungere():
    print(" ")#spazio tattico
    libro = input("Che libro vuoi aggiungere?\n")
    listaLibri.append(libro)
    print(" ")#spazio tattico
    print("Il libro <", libro, "> è stato aggiunto alla libreria")  #rivedere questa funzione!!!! 
    print("")#spazio tattico

#Funzione 3: visualizza se un libro desiderato è disponibile nel catalogo. 
def disponibilita():
    print(" ")#spazio tattico
    desiderio = input("Inserisci il nome del libro del quale vuoi verificare la disponibilità:\n")
    if desiderio in listaLibri:
        print(" ")#spazio tattico
        print(desiderio, "è disponibile. Premi 4 per prendere in prestito questo libro.")
        print(" ")#spazio tattico
    elif desiderio in libriPrestati:
        print(" ")#spazio tattico
        print(desiderio, "è già nella tua lista di libri presi in prestito.")
        print("Premi <6> per vedere la lista dei libri che ti sono stati prestati.")
        print("Altrimenti, premi <1> per visualizzare la lista dei libri che sono disponibili.")
        print(" ")#spazio tattico
    else:
        print(" ")#spazio tattico
        print(desiderio, "non è presente né nel catalogo né nella tua lista di libri prestati.")
        print(" ")#spazio tattico

#Funzione 4: ti fa prendere in prestito un libro. Ovvero, sposta un libro dal catalogo al tuo carrello
def prestito():
    print(" ")#spazio tattico
    prestito = input("Inserisci il nome del libro che vuoi prendere in prestito:\n")
    if prestito in listaLibri:
        listaLibri.remove(prestito)
        libriPrestati.append(prestito)
        print(" ")#spazio tattico
        print("Hai preso in prestito il libro <", prestito, ">.")
        print(" ")#spazio tattico
    else:
        print(" ")#spazio tattico
        print("Il libro che hai selezionato non è nel catalogo.") 
        print("Premi 1 per visualizzare il catalogo e, poi, ripeti la procedura.")
        print(" ")#spazio tattico

#Funzione 5: ti fa restituire un libro. Ovvero, sposta un libro dal tuo carrello al catalogo
def restituizione():
    print(" ")#spazio tattico
    restituire = input("Inserisci il nome del libro che vuoi restituire:\n")
    if restituire in libriPrestati:
        libriPrestati.remove(restituire)
        listaLibri.append(restituire)
        print(" ")#spazio tattico
        print("Hai restituito il libro <", restituire, ">.")
        print(" ")#spazio tattico
    else:
        print(" ")#spazio tattico
        print("Il libro che stai cercando di restituire non è nel tuo catalogo")
        print("Premi <6>  per visualizzare la lista dei libri in tuo possesso, poi ripeti il processo.")
        print(" ")#spazio tattico

#Funzione 6: ti fa visualizzare quali libri ti sono stati prestati. Ovvero, visualizza la lista di libri nel tuo carrello
def libriprestati():
    print(" ")#spazio tattico
    print("Questa è la lista dei libri che ti sono stati prestati:")
    print(libriPrestati)
    print(" ")#spazio tattico