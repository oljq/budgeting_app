#4. strana
#Pocetak kes, kartica
#potrsoeno kes, kartica
#brisanje svih racuna

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image

from funkcije import Linija, ResponzivniLabel
from dugme import DugmeNazad
import funkcije as f 
from racun import *


class Podesavanja(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.racuni=f.racuni
        self.pocetak_kes=f.pocetak_kes
        self.pocetak_kartica=f.pocetak_kartica

        layout = FloatLayout()

        pozadina = Image(source="static/bg123.jpg", size_hint=(1, 1.1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(pozadina)

        layout.add_widget(Linija(height=2, size_hint=(1, None)))

        dugme_nazad = DugmeNazad(
            slika_path="static/4.jpg",  # Putanja do slike
            size_hint=(0.4, 0.2),
            pos_hint={'center_x': 0.5, 'y': 0.8}
        )
        dugme_nazad.bind(on_release=f.vrati_na_pocetni)
        layout.add_widget(dugme_nazad)

        self.kes_input = TextInput(hint_text="Unesi pocetak kes", size_hint=(0.8, None), height=50, pos_hint={'center_x': 0.5, 'y': 0.75})
        layout.add_widget(self.kes_input)

        self.kartica_input = TextInput(hint_text="Unesi pocetak kartica", size_hint=(0.8, None), height=50, pos_hint={'center_x': 0.5, 'y': 0.65})
        layout.add_widget(self.kartica_input)

        self.sacuvaj_dugme=Button(
            text="Sacuvaj promene", 
            size_hint=(0.8, None), 
            height=50, 
            pos_hint={'center_x': 0.5, 'y': 0.3},
            background_normal='',
            background_down='',
            background_color=(0, 0, 0, 0),
            color=(0, 0, 0, 1)
        )
        self.sacuvaj_dugme.bind(on_release=self.uredi)
        layout.add_widget(self.sacuvaj_dugme)
        

        layout.add_widget(Linija(height=2, size_hint=(1, None)))

        potrosen_layout = BoxLayout(orientation='horizontal', spacing=20, size_hint=(1, 0.06), pos_hint={'center_x': 0.5, 'y': 0.5})
        sume = f.saberi_nacin_placanja()
        potrosen_kes=ResponzivniLabel(            
            velicina=0.3, 
            text=f"Potrosen kes: {sume[Nacin.Kes]}",
            halign="center", valign="middle",
            color=(0, 0, 0, 1)
        )
        potrosen_kes.bind(size=lambda inst, val: setattr(inst, 'text_size', inst.size))

        potrosen_kartica=ResponzivniLabel(            
            velicina=0.3, 
            text=f"Potrosen kartica:  {sume[Nacin.Kartica]}",
            halign="center", valign="middle",
            color=(0, 0, 0, 1)
        )
        potrosen_kartica.bind(size=lambda inst, val: setattr(inst, 'text_size', inst.size))

        potrosen_layout.add_widget(potrosen_kes)
        potrosen_layout.add_widget(potrosen_kartica)
        layout.add_widget(potrosen_layout)

        layout.add_widget(Linija(height=2, size_hint=(1, None)))

        pocetni_layout=BoxLayout(orientation='horizontal', spacing=20, size_hint=(1, 0.06), pos_hint={'center_x': 0.5, 'y': 0.4})
        pocetni_kes=ResponzivniLabel(
            velicina=0.3,
            text=f"Pocetak kes: {f.pocetak_kes}",
            halign="center", valign="middle",
            color=(0, 0, 0, 1)
        )
        pocetni_kes.bind(size=lambda inst, val:setattr(inst,'text_size', inst.size ))

        pocetni_kartica=ResponzivniLabel(
            velicina=0.3,
            text=f"Pocetak kartica: {f.pocetak_kartica}",
            halign="center", valign="middle",
            color=(0, 0, 0, 1)
        )
        pocetni_kartica.bind(size=lambda inst, val:setattr(inst,'text_size', inst.size ))

        pocetni_layout.add_widget(pocetni_kes)
        pocetni_layout.add_widget(pocetni_kartica)
        layout.add_widget(pocetni_layout)


        ukupno=f.saberi_sve()
        poruka=ResponzivniLabel(
            velicina=0.25,
            text=f"Ukupno: {ukupno} RSD",
            size_hint=(1, 0.08),
            pos_hint={'center_x': 0.5, 'y':0.55 },
            color=(0, 0, 0, 1))
        layout.add_widget(poruka)

        layout.add_widget(Linija(height=2, size_hint=(1, None)))

        self.brisi_dugme=Button(
            text="Brisi", 
            size_hint=(0.8, None), 
            height=44, 
            pos_hint={'center_x': 0.5, 'y': 0.2},
            background_normal='',
            background_down='',
            background_color=(0, 0, 0, 0),
            color=(0, 0, 0, 1))
        #self.brisi_dugme.bind(on_release=f.brisi)
        self.brisi_dugme.bind(on_release=lambda _: (f.brisi(), self.prikazi_poruku("Racuni su obrisani!")))


        layout.add_widget(self.brisi_dugme)


        self.current_message = None

    
        self.add_widget(layout)
    

    def uredi(self, instance):
        kes = self.kes_input.text 
        kartica = self.kartica_input.text  
        try:
            kes = float(kes)
            self.kes_input.text=" "
            self.prikazi_poruku("Uneto!")
        except ValueError:
            self.prikazi_poruku("unesite kes pravilno")

        try:
            kartica = float(kartica)
            self.kartica_input.text=" "
            self.prikazi_poruku("Uneto!")
        except ValueError:
            self.prikazi_poruku("unesi karticu pravilno")

        f.sacuvaj_stanje(kes, kartica)




    def prikazi_poruku(self, tekst):
        # Ako postoji prethodna poruka, ukloni je
        if self.current_message:
            self.remove_widget(self.current_message)

        # Prikazi novu poruku
        poruka = ResponzivniLabel(
            velicina=0.25,
            text=tekst,
            size_hint=(1, 0.08),
            pos_hint={'center_x': 0.5, 'y': 0.1},
            halign="center", valign="middle",
            color=(0,0,0,1)
        )
        poruka.bind(size=lambda inst, val: setattr(inst, 'text_size', inst.size))
        self.add_widget(poruka)

        # Čuvaj referencu na trenutnu poruku
        self.current_message = poruka

        