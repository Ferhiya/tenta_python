personer = {
  "19591011-2323": 
    {
    "namn": "Eva Hauser",
    "adress": "Hittepågatan 23B",
    "favoriträtt": "MumsMums" 
    },
  "18550903-1234": 
    {
    "namn": "Kalle Anka",
    "adress": "Ankeborgsgatan 44",
    "favoriträtt": "Hamburgare" 
    },
  "18901022-9877": 
    {
    "namn": "Jon Doe",
    "adress": "Hemlighetsgata 1A",
    "favoriträtt": "Pizza" 
    }
}

while True:
  print("1. Lägg till person")
  print("2. Skriv ut personinformation")
  print("3. Avsluta")
  
  meny_val = input("Ange önskat val: ")

  if meny_val == "1":
    personnummer=input("Ange personnummer: ")
    
    if personnummer in personer:
        print("Personen i fråga finns redan i vårat system! Det går tyvärr ej att lägga till personen!")
    else:
        namn=input("Ange namn: ")
        adress=input("Ange adress: ")
        favortiträtt=input("Ange favoriträtt: ")
        personer[personnummer]={"namn":namn,
                               "adress":adress, 
                               "favortiträtt":favortiträtt}

  elif meny_val == "2":
      personnummer=input("Ange personnummer: ")
    
      if personnummer in personer:
            personer= personer[personnummer]
            namn=personer.get("namn")
            adress=personer.get("adress")
            favoriträtt=personer.get("favoriträtt")
            print(f"namn:{namn}\n")
            print(f"adress:{adress}\n")
            print(f"Favoriträtt:{favortiträtt}\n")
      else:
              print("Den sökta personen finns inte!")
  elif meny_val == "3":
      break
  else:

    print("Ogiltligt val!")