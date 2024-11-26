#esercizio ciclo while 

#faccio la prima domanda e faccio inserire la risposta
print("Qual è la risposta alla domanda fondamentale sulla vita, l'universo e tutto quanto?")
risposta = int(input("Scrivi la tua risposta qui:"))

#inizio il ciclo:
while True:

    #questa è la condizione fondamentale (!)
    if risposta == 42:
        print("Bravo! Hai risposto alla domanda!")
        #stoppo il programma non appena viene inserito il valore giusto
        break
    #altrimenti stampo l'avviso di errore...
    else:
        print("Nah-ah. Rileggi il libro - o almeno guarda il film!")
        #...e faccio inserire nuovamente il valore
        risposta=int(input("Riproviamo: qual è la risposta giusta?"))

#finisco il programma
print(" ") #(spazietto tattico)
print("Ora il programma è finito.")