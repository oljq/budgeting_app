#2 strana 
#prikaz svih racuna sa mestom i iznos

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView

from dugme import DugmeNazad
from funkcije import Linija, ResponzivniLabel
import funkcije as f 


class Listing(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        f.ucitaj_racune()

        layout = FloatLayout()

        pozadina = Image(source="static/bg123.jpg", size_hint=(1, 1.1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(pozadina)

        layout.add_widget(Linija(height=2, size_hint=(1, None)))

        dugme_nazad = DugmeNazad(
            slika_path="static/2.jpg",  # Putanja do slike
            size_hint=(0.4, 0.2),
            pos_hint={'center_x': 0.5, 'y': 0.8}
        )
        dugme_nazad.bind(on_release=f.vrati_na_pocetni)
        layout.add_widget(dugme_nazad)


        if not f.racuni:
            poruka1=ResponzivniLabel(
                velicina=0.25,
                text="Nemate racune",
                size_hint=(1, 0.08),
                pos_hint={'center_x': 0.5, 'y': 0.7},
                color=(0, 0, 0, 1))
            layout.add_widget(poruka1)

        else:

            poruka2= ResponzivniLabel(
                velicina=0.25,
                text="---RACUNI---", 
                size_hint=(1, 0.08),
                pos_hint={'center_x': 0.5, 'y': 0.7},
                color=(0, 0, 0, 1))
            layout.add_widget(poruka2)
            layout.add_widget(Linija(height=2, size_hint=(1, None)))

        scroll_layout = BoxLayout(orientation='vertical', spacing=0,size_hint_y=None)
        scroll_layout.bind(minimum_height=scroll_layout.setter('height'))
        
        for racun in f.racuni:
            lbl = ResponzivniLabel(
                velicina=0.40,
                text=f"{racun['mesto']}: {racun['iznos']} RSD", 
                size_hint=(1, None), 
                height=60,
                halign="center", valign="middle",
                color=(0, 0, 0, 1),
            )
            scroll_layout.add_widget(lbl)

        scroll_view = ScrollView(size_hint=(1, 0.5), pos_hint={'center_x': 0.5, 'y': 0.2})
        scroll_view.add_widget(scroll_layout)
        layout.add_widget(scroll_view)
        
        layout.add_widget(Linija(height=2, size_hint=(1, None)))

        ukupno=f.saberi_sve()
        poruka=ResponzivniLabel(
            velicina=0.25,
            text=f"Ukupno: {ukupno} RSD", 
            size_hint=(1, 0.08),
            pos_hint={'center_x': 0.5, 'y':0.15 },
            color=(0, 0, 0, 1))
        layout.add_widget(poruka)

        self.add_widget(layout)