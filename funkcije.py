from racun import *

from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle

import json
import os

PUTANJA_FAJLA = "baza/racuni.json"
putanja_stanja = "baza/pocetno_stanje.json"

racuni = []
pocetak_kes = 0
pocetak_kartica = 0


class Linija(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(0, 0., 0., 1) 
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect = self.size


class ResponzivniLabel(Label):
    def __init__(self, velicina, **kwargs):
        super().__init__(**kwargs)
        self.velicina = velicina
        self.bind(size=self.azuriraj_font)  # Povezivanje promene veličine sa funkcijom
        self.azuriraj_font()  # Ažuriranje odmah pri inicijalizaciji

    def azuriraj_font(self, *args):
        """Ažurira veličinu fonta na osnovu visine widgeta i željenog faktora"""
        self.font_size = self.height * self.velicina


#Funkcije za rad sa baza/pocetno_stanje.json


def ucitaj_stanje():
    global pocetak_kes, pocetak_kartica
    if os.path.exists(putanja_stanja):
        with open(putanja_stanja, "r", encoding="utf-8") as f:
            podaci = json.load(f)
            pocetak_kes = podaci.get("pocetak_kes", 0)
            pocetak_kartica = podaci.get("pocetak_kartica", 0)
    else:
        sacuvaj_stanje(0, 0)

def sacuvaj_stanje(kes, kartica):
    global pocetak_kes, pocetak_kartica
    pocetak_kes = kes
    pocetak_kartica = kartica
    with open(putanja_stanja, "w", encoding="utf-8") as f:
        json.dump({
            "pocetak_kes": kes,
            "pocetak_kartica": kartica
        }, f, indent=4)

#Funkcije za rad sa baza/racuni.json

def ucitaj_racune():
    global racuni
    if not os.path.exists('baza'):
        os.makedirs('baza')

    # Ako fajl postoji, učitaj ga, u suprotnom kreiraj fajl sa praznim listama
    if os.path.exists(PUTANJA_FAJLA):
        with open(PUTANJA_FAJLA, "r", encoding="utf-8") as f:
            try:
                #return json.load(f)
                racuni = json.load(f)
                return racuni
            except json.JSONDecodeError:
                return []
    else:
        # Ako fajl ne postoji, kreiramo ga sa praznim listama računa
        with open(PUTANJA_FAJLA, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=4)
        return []
    
    return racuni 


def sacuvaj_racune(racuni):
    with open(PUTANJA_FAJLA, "w", encoding="utf-8") as f:
        json.dump(racuni, f, ensure_ascii=False, indent=4)

def dodaj_racun(mesto, iznos, kategorija, nacin):
    racuni = ucitaj_racune()
    novi_racun = {
        "mesto": mesto,
        "iznos": iznos,
        "kategorija": kategorija.name if hasattr(kategorija, 'name') else kategorija,
        "nacin": nacin.name if hasattr(nacin, 'name') else nacin
    }
    racuni.append(novi_racun)
    sacuvaj_racune(racuni)

#FUNKCIJE ZA SIBARANJE

def saberi_sve():
    racuni = ucitaj_racune() 
    suma = 0
    for racun in racuni:
        suma += racun['iznos']
    return suma

def saberi_kategorije():
    racuni = ucitaj_racune()  
    suma = {kategorija: 0 for kategorija in Kategorija}  
    
    for racun in racuni:
        # Pretpostavljamo da 'kategorija' sadrži naziv kategorije kao string
        if racun['kategorija'] in Kategorija.__members__:
            suma[Kategorija[racun['kategorija']]] += racun['iznos']
    
    return suma

def saberi_nacin_placanja():
    racuni = ucitaj_racune()  # Učitajte račune iz fajla
    suma = {nac_pla: 0 for nac_pla in Nacin}  # Pretpostavljamo da Nacin sadrži sve moguće načine plačanja
    
    for racun in racuni:
        # Pretpostavljamo da 'nacin' sadrži naziv načina plačanja kao string
        if racun['nacin'] in Nacin.__members__:
            suma[Nacin[racun['nacin']]] += racun['iznos']  # Dodajte iznos u odgovarajući način plačanja
    
    return suma

#FUNKCIJE ZA PRIKAZ


def prikaz_ostalog_kesa():
    suma = saberi_nacin_placanja()
    ostalo = pocetak_kes - suma.get(Nacin.Kes, 0)
    return round(ostalo, 2)

def prikaz_ostale_kartice():
    suma = saberi_nacin_placanja()
    return pocetak_kartica - suma[Nacin.Kartica]

def prikaz_ostalog_novca():
    zbir = pocetak_kartica + pocetak_kes
    suma_po_nacinu = saberi_nacin_placanja()
    suma = suma_po_nacinu[Nacin.Kartica] + suma_po_nacinu[Nacin.Kes]
    return zbir - suma

#Funkcije

def brisi(instance=None):
    global racuni
    racuni.clear() 

    if os.path.exists('baza/racuni.json'):
        os.remove('baza/racuni.json')

def vrati_na_pocetni(instance):
    from kivy.app import App
    ucitaj_racune() 
    root = App.get_running_app().root
    root.current = 'pocetni' 



