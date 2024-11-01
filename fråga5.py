lista_med_djur=[]

while True:
        print("skriva in djur information\n")
        djur=input("Skriv in ett djur: ")
        antalet_djur=input("Skriv in antalet djur: ")
        djur_mat=input("Vad äter djuret: ")
        djur_info=[
            { 
            "namn":djur, "antal":antalet_djur, "mat":djur_mat
            }
        ]
        lista_med_djur.append(djur_info)
        val=input("Vill du fortsätta skriva in djur? ja/nej ")
        val=val.lower()
        if val == "ja":
            continue
        elif val == "nej":
            break
for djur in lista_med_djur: 
 print(djur)