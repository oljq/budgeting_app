from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
import funkcije as f 

from kivy.core.window import Window
Window.size = (360, 720)

class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.title = "sili"
        self.icon = "static/4.jpg"

        self.racuni = f.racuni
        f.ucitaj_racune()
        f.ucitaj_stanje()

    def build(self):
        from podesavanja import Podesavanja
        from pocetni_ekran import PocetniEkran
        from istorija import Istorija
        from dodaj import Dodaj
        from listing import Listing

        sm = ScreenManager()  

        sm.add_widget(PocetniEkran(name='pocetni'))
        sm.add_widget(Dodaj(name='dodaj'))
        sm.add_widget(Listing(name='listing'))
        sm.add_widget(Istorija(name='kategorija'))
        sm.add_widget(Podesavanja(name='podesavanja'))
  

        return sm



if __name__ == '__main__':
    MyApp().run()
