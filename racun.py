from enum import Enum

class Kategorija(Enum):
    Namirnice=1
    Hrana=2
    Kuca=3
    Kafa=4
    Kozmetika=5
    Odeca=6
    Zabava=7
    Izlaci=8
    Putovanje=9
    Cuvanje=10

class Nacin(Enum):
    Kes=1
    Kartica=2
    Devizni_racun=3


class Racun:

    def __init__(self,mesto,iznos,kategorija,nacin_placanja):
        self.mesto=mesto
        self.iznos=iznos
        self.kategorija = kategorija  
        self.nacin_placanja = nacin_placanja 

    
