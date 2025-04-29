#0. strana

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
import podesavanja as p
import funkcije as f

from funkcije import *

class PocetniEkran(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.racuni=f.racuni

        layout = FloatLayout()

        pozadina = Image(source="static/poc_ekr.jpg", size_hint=(1, 1.1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(pozadina)

        poruka = ResponzivniLabel(
            velicina=0.4,
            text="Zdravo!",
            size_hint=(1, 0.08),
            pos_hint={'center_x': 0.5, 'y': 0.9},
            halign="center", valign="middle"
            )
        poruka.bind(size=lambda inst, val: setattr(inst, 'text_size', inst.size))
        layout.add_widget(poruka)

        zbir=str(f.prikaz_ostalog_novca())

        ukupno = ResponzivniLabel(
            velicina=0.5,
            text=f"{zbir}RSD",
            bold=True, 
            size_hint=(1, 0.09), 
            pos_hint={'center_x': 0.5, 'y': 0.83},
            halign="center", valign="middle"
            )
        poruka.bind(size=lambda inst, val: setattr(inst, 'text_size', inst.size))
        layout.add_widget(ukupno)

        kes=str(f.prikaz_ostalog_kesa())

        novac_layout = BoxLayout(orientation='horizontal', spacing=20, size_hint=(1, 0.06), pos_hint={'center_x': 0.5, 'y': 0.75})
        kes = ResponzivniLabel(
            velicina=0.3,  
            text=f"Keš: {kes}RSD" ,
            halign="center", valign="middle"
        )
        kes.bind(size=lambda inst, val: setattr(inst, 'text_size', inst.size))

        kartica=str(f.prikaz_ostale_kartice())

        kartica = ResponzivniLabel( 
            velicina=0.3, 
            text=f"Kartica: {kartica} RSD", 
            halign="center", valign="middle"
        )
        kartica.bind(size=lambda inst, val: setattr(inst, 'text_size', inst.size))
        

        novac_layout.add_widget(kes)
        novac_layout.add_widget(kartica)
        layout.add_widget(novac_layout)

        dugme1 = Button(
            text="Dodaj trošak",  
            size_hint=(1, 0.15), 
            pos_hint={'center_x': 0.5, 'y': 0.5},
            background_normal='',
            background_down='',
            background_color=(0, 0, 0, 0),
            color=(0, 0, 0, 1)
            )
        dugme1.bind(on_release=self.otvori_dodaj)

        dugme2 = Button(
            text="Svi racuni",  
            size_hint=(1, 0.15), 
            pos_hint={'center_x': 0.5, 'y': 0.35},
            background_normal='',
            background_down='',
            background_color=(0, 0, 0, 0),
            color=(0, 0, 0, 1)
            )
        dugme2.bind(on_release=self.otvori_listing)

        dugme3 = Button(
            text="Kategorije",
            size_hint=(1, 0.15),
            pos_hint={'center_x': 0.5, 'y': 0.2},
            background_normal='',
            background_down='',
            background_color=(0, 0, 0, 0),
            color=(0, 0, 0, 1)
            )
        dugme3.bind(on_release=self.otvori_kategorija)

        dugme4 = Button(
            text="Podešavanja",
            size_hint=(1, 0.15),
            pos_hint={'center_x': 0.5, 'y': 0.05},
            background_normal='',
            background_down='',
            background_color=(0, 0, 0, 0),
            color=(0, 0, 0, 1)
            )
        dugme4.bind(on_release=self.otvori_podesavanja)

        layout.add_widget(dugme1)
        layout.add_widget(dugme2)
        layout.add_widget(dugme3)
        layout.add_widget(dugme4)

        self.add_widget(layout)

    def otvori_dodaj(self, instance):
        self.manager.current = 'dodaj'

    def otvori_listing(self, instance):
        self.manager.current = 'listing'

    def otvori_kategorija(self, instance):
        self.manager.current = 'kategorija'

    def otvori_podesavanja(self, instance):
        self.manager.current = 'podesavanja'




