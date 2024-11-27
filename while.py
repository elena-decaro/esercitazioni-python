#esercizio ciclo while 

#faccio la prima domanda e faccio inserire la risposta
print("Qual è la risposta alla domanda fondamentale sulla vita, l'universo e tutto quanto?")


#inizio il ciclo:
while True:

    try:
        risposta = int(input("Scrivi la tua risposta qui:"))
        
        #Questa è la condizione fondamentale
        if risposta == 42:
            print("Bravo! Hai risposto alla domanda!")
            #stoppo il programma non appena viene inserito il valore giusto
            break
     #altrimenti stampo l'avviso di errore...
        else:
            print("Nah-ah. Rileggi il libro - o almeno guarda il film!")
            #...e faccio inserire nuovamente il valore
            risposta=int(input("Riproviamo: qual è la risposta giusta?"))
            
    #in questo modo il programma non crasha se inserisco un valore di un tipo diverso da quello dichiarato in "try"
    except ValueError:
            print("Ti do un suggerimento: la risposta è un numero - riprova!")

#finisco il programma
print(" ") #(spazietto tattico)
print("Ora il programma è finito.")