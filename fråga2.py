Konsonanter=['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

Vokaler=['a', 'e', 'i', 'o', 'u', 'å', 'ä', 'ö']

hittad_Vokaler=[]

hittade_Konsonanter=[]



def konsonanter_och_vokaler(min_mening):
    min_mening=min_mening.lower()
    for char in min_mening:  
        if char in 'aeiouåäö':
            hittad_Vokaler.append(char)
            vokstr="".join(hittad_Vokaler)
        elif char in 'bcdfghjklmnpqrstvwyz':
            hittade_Konsonanter.append(char)
            Konsonanterstr="".join(hittade_Konsonanter)
    return vokstr,Konsonanterstr

        
min_mening = "Pythonutvecklare med inriktning AI"
vokaler,Konsonanter=konsonanter_och_vokaler(min_mening) 
print(Konsonanter,vokaler)