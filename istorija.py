#3 strana
#prikaz kategorija i potrosene sume za kategoriju


from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from funkcije import Linija
import funkcije as f 
from funkcije import ResponzivniLabel
from dugme import DugmeNazad


class Istorija(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = FloatLayout()

        pozadina = Image(source="static/bg123.jpg", size_hint=(1, 1.1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(pozadina)

        layout.add_widget(Linija(height=2, size_hint=(1, None)))

        dugme_nazad = DugmeNazad(
            slika_path="static/3.jpg",  # Putanja do slike
            size_hint=(0.4, 0.2),
            pos_hint={'center_x': 0.5, 'y': 0.8}
        )
        dugme_nazad.bind(on_release=f.vrati_na_pocetni)
        layout.add_widget(dugme_nazad)

        sume = f.saberi_kategorije()

        y_pos = 0.75

        for kategorija, iznos in sume.items():
            y_pos -= 0.05
            lbl = ResponzivniLabel(
                velicina=0.13,
                text=f"{kategorija.name}: {iznos} RSD",
                size_hint=(1, 0.15), 
                pos_hint={'center_x': 0.5, 'y': y_pos},  
                halign="center", valign="middle",
                color=(0, 0, 0, 1)
            )
            layout.add_widget(lbl)

        ukupno=f.saberi_sve()
        poruka=ResponzivniLabel(
            velicina=0.25,
            text=f"Ukupno: {ukupno} RSD",
            size_hint=(1, 0.08),
            pos_hint={'center_x': 0.5, 'y':0.15 },
            color=(0, 0, 0, 1))
        layout.add_widget(poruka)

        self.add_widget(layout)


        


            