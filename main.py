from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
import functions as f 

from kivy.core.window import Window
Window.size = (360, 720) 
# #best if looking on pc

class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.title = "Budgeting"
        self.icon = "static/4.jpg"

        self.receipts = f.receipts
        f.load_receipts()
        f.load_state()

    def build(self):
        from settings import Settings
        from home_scr import Home_scr
        from history import History
        from add import Add
        from list import List

        sm = ScreenManager()  

        sm.add_widget(Home_scr(name='home_scr'))
        sm.add_widget(Add(name='add'))
        sm.add_widget(List(name='list'))
        sm.add_widget(History(name='category'))
        sm.add_widget(Settings(name='settings'))
  

        return sm



if __name__ == '__main__':
    MyApp().run()
