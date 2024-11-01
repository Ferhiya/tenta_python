
class programmerare:
    def __init__(self,smeknamn,programmeringsspråk,kan_hacka):
        self._smeknamn=smeknamn
        self.programmeringsspråk=programmeringsspråk
        self._kan_hacka=kan_hacka
        self._is_hacking=False
        pass 
    
    def  kan_hacka_modell(self,modell):
        if modell in self._kan_hacka:
            return True
        else:
            return False
    
    def hacka(self,laptop):
        self._is_hacking=True
        laptop.get_hacked(self._smeknamn)
        self._is_hacking=False
        

    def is_hacking(self):
        if self._is_hacking == True:
            return True
        else: 
            return False
         
class laptop:
    def __init__(self,laptop,tillverkningsår,skärmstorlek,batteritid):
        self._laptop=laptop
        self._tillverkningsår=tillverkningsår
        self._skärmstorlek=skärmstorlek
        self._batteritid=batteritid
        self._blivit_hackad=False
                 
        
    def är_hacked(self):
        return self._blivit_hackad
                
            
    def get_hacked(self,programerare):
        kan_du_hacka=input(f"Kan du hacka {self._laptop}")
        kan_du_hacka.lower()
        if kan_du_hacka == "ja" and self._is_hacking == True:
            self._blivit_hackad=True
        else:
            return False
            

Programmerare=programmerare("Linda_lzzo","Python",["Router","iphone","Samsung","hp"])  
Laptop=laptop("hp",2012,24,12)

res=Laptop.är_hacked()
print(f"Kan jag hacka {res}")
