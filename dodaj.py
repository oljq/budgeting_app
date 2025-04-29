#1. strana
#Dodavanje racuna

from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.image import Image
import funkcije as f 
from funkcije import ResponzivniLabel
from funkcije import Linija
from dugme import DugmeNazad
from racun import Kategorija,Nacin

class Dodaj(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = FloatLayout()

        pozadina = Image(source="static/bg123.jpg", size_hint=(1, 1.1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(pozadina)

        layout.add_widget(Linija(height=2, size_hint=(1, None)))

        dugme_nazad = DugmeNazad(
            slika_path="static/1.jpg",  
            size_hint=(0.4, 0.2),
            pos_hint={'center_x': 0.5, 'y': 0.8}
        )
        dugme_nazad.bind(on_release=f.vrati_na_pocetni)
        layout.add_widget(dugme_nazad)

        # Unos mesta
        self.mesto_input = TextInput(hint_text="Unesi mesto", size_hint=(0.8, None), height=50, pos_hint={'center_x': 0.5, 'y': 0.7})
        layout.add_widget(self.mesto_input)

        # Unos iznosa
        self.iznos_input = TextInput(hint_text="Unesi iznos", size_hint=(0.8, None), height=50, pos_hint={'center_x': 0.5, 'y': 0.6})
        layout.add_widget(self.iznos_input)

        kategorija_dropdown = DropDown()
        for k in Kategorija:
            btn = Button(text=str(k.name), size_hint_y=None, height=44)
            btn.background_normal = ''  
            btn.background_color =( 0.9, 0.7, 0.8, 0.3)
            btn.color = (0, 0, 0, 1)  
            btn.bind(on_release=lambda btn, k=k, dropdown=kategorija_dropdown: self.kategorija_selected(btn, k, dropdown))
            kategorija_dropdown.add_widget(btn)
                
        self.kategorija_button = Button(text="Izaberite kategoriju", size_hint=(0.8, None), height=50, pos_hint={'center_x': 0.5, 'y': 0.5})
        self.kategorija_button.bind(on_release=kategorija_dropdown.open)
        layout.add_widget(self.kategorija_button)

        # Nacin placanja (Dropdown)
        nacin_dropdown = DropDown()
        for n in Nacin:
            btn = Button(text=n.name, size_hint_y=None, height=44) 
            btn.background_normal = ''  
            btn.background_color =( 0.9, 0.7, 0.8, 0.3)
            btn.color = (0, 0, 0, 1)  
            btn.bind(on_release=lambda btn, n=n,dropdown=nacin_dropdown: self.nacin_selected(btn,n,dropdown))
            nacin_dropdown.add_widget(btn)

        self.nacin_button = Button(text="Izaberite način plačanja", size_hint=(0.8, None), height=50, pos_hint={'center_x': 0.5, 'y': 0.4})
        layout.add_widget(self.nacin_button)

        def open_dropdown(instance):
            nacin_dropdown.open(self.nacin_button)

        self.nacin_button.bind(on_release=open_dropdown)

        # Dugme za dodavanje računa
        dugme_dodaj = Button(
            text="Dodaj račun", 
            size_hint=(0.8, None), 
            height=44, 
            pos_hint={'center_x': 0.5, 'y': 0.3},
            background_normal='',
            background_down='',
            background_color=(0, 0, 0, 0),
            color=(0, 0, 0, 1)
            )
        dugme_dodaj.bind(on_release=self.dodaj_racun)
        layout.add_widget(dugme_dodaj)

        self.mesto_input.text = ""
        self.iznos_input.text = ""
        self.selected_kategorija = None
        self.selected_nacin_placanja = None
        self.kategorija_button.text = "Izaberite kategoriju"  
        self.nacin_button.text = "Izaberite način plačanja" 

        self.current_message = None

        self.add_widget(layout)


    def kategorija_selected(self, btn, k, dropdown):
        self.selected_kategorija = k
        self.kategorija_button.text = str(k.name) 
        dropdown.dismiss()

    def nacin_selected(self, btn, n, dropdown):
        self.selected_nacin_placanja = n
        self.nacin_button.text = str(n.name)
        dropdown.dismiss()

    def dodaj_racun(self, instance):
        mesto = self.mesto_input.text
        iznos = self.iznos_input.text

        # Provera da li su polja prazna
        if not mesto or not iznos:
            self.prikazi_poruku("Unesite mesto i iznos")
            return

        try:
            iznos = float(iznos)
        except ValueError:
            self.prikazi_poruku("Greška u unosu iznosa. Molimo unesite validan broj.")
            return
        
        kategorija = self.selected_kategorija
        nacin = self.selected_nacin_placanja

        if not kategorija or not nacin:
            self.prikazi_poruku("Unesite kategoriju i nacin")
            return

        # Dodavanje računa
        f.dodaj_racun(mesto, iznos, kategorija, nacin)

        # Očisti polja nakon uspešnog dodavanja
        self.mesto_input.text = ""
        self.iznos_input.text = ""
        self.selected_kategorija = None
        self.selected_nacin_placanja = None

        self.prikazi_poruku("Račun je uspešno dodat")

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



