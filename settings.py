# 4. page
# Initial cash, card
# Spent cash, card
# Delete all receipts

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image

from functions import Line, ResponsiveLabel
from button import Button_back
import functions as f 
from receipts import *


class Settings(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.receipts=f.receipts
        self.start_cash=f.start_cash
        self.start_card=f.start_card

        layout = FloatLayout()

        background = Image(source="static/bg123.jpg", size_hint=(1, 1.1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(background)

        layout.add_widget(Line(height=2, size_hint=(1, None)))

        button_back = Button_back(
            picture_path="static/4.jpg",  
            size_hint=(0.4, 0.2),
            pos_hint={'center_x': 0.5, 'y': 0.8}
        )
        button_back.bind(on_release=f.return_to_home_screen)
        layout.add_widget(button_back)

        self.cash_input = TextInput(hint_text="Enter initial cash", size_hint=(0.8, None), height=50, pos_hint={'center_x': 0.5, 'y': 0.75})
        layout.add_widget(self.cash_input)

        self.card_input = TextInput(hint_text="Enter initial card", size_hint=(0.8, None), height=50, pos_hint={'center_x': 0.5, 'y': 0.65})
        layout.add_widget(self.card_input)

        self.sacuvaj_button=Button(
            text="Save changes", 
            size_hint=(0.8, None), 
            height=50, 
            pos_hint={'center_x': 0.5, 'y': 0.3},
            background_normal='',
            background_down='',
            background_color=(0, 0, 0, 0),
            color=(0, 0, 0, 1)
        )
        self.sacuvaj_button.bind(on_release=self.change)
        layout.add_widget(self.sacuvaj_button)
        

        layout.add_widget(Line(height=2, size_hint=(1, None)))

        spent_layout = BoxLayout(orientation='horizontal', spacing=20, size_hint=(1, 0.06), pos_hint={'center_x': 0.5, 'y': 0.5})
        sume = f.sum_payment_method()
        spent_cash = round(sume.get(Payment_method.Cash, 0), 2)
        spent_card = round(sume.get(Payment_method.Card, 0), 2)

        spent_cash_label=ResponsiveLabel(            
            size_factor=0.3, 
            text=f"Spent cash: {spent_cash}",
            halign="center", valign="middle",
            color=(0, 0, 0, 1)
        )
        spent_cash_label.bind(size=lambda inst, val: setattr(inst, 'text_size', inst.size))

        spent_card_label=ResponsiveLabel(            
            size_factor=0.3, 
            text=f"Spent cash: {spent_cash}",
            halign="center", valign="middle",
            color=(0, 0, 0, 1)
        )
        spent_card_label.bind(size=lambda inst, val: setattr(inst, 'text_size', inst.size))

        spent_layout.add_widget(spent_cash_label)
        spent_layout.add_widget(spent_card_label)
        layout.add_widget(spent_layout)

        layout.add_widget(Line(height=2, size_hint=(1, None)))

        home_scr_layout=BoxLayout(orientation='horizontal', spacing=20, size_hint=(1, 0.06), pos_hint={'center_x': 0.5, 'y': 0.4})
        home_scr_cash=ResponsiveLabel(
            size_factor=0.3,
            text=f"Initial cash: {f.start_cash}",
            halign="center", valign="middle",
            color=(0, 0, 0, 1)
        )
        home_scr_cash.bind(size=lambda inst, val:setattr(inst,'text_size', inst.size ))

        home_scr_card=ResponsiveLabel(
            size_factor=0.3,
            text=f"Initial card: {f.start_card}",
            halign="center", valign="middle",
            color=(0, 0, 0, 1)
        )
        home_scr_card.bind(size=lambda inst, val:setattr(inst,'text_size', inst.size ))

        home_scr_layout.add_widget(home_scr_cash)
        home_scr_layout.add_widget(home_scr_card)
        layout.add_widget(home_scr_layout)


        sum_all=f.sum_all()
        message=ResponsiveLabel(
            size_factor=0.25,
            text=f"Sum: {sum_all} EUR",
            size_hint=(1, 0.08),
            pos_hint={'center_x': 0.5, 'y':0.55 },
            color=(0, 0, 0, 1))
        layout.add_widget(message)

        layout.add_widget(Line(height=2, size_hint=(1, None)))

        self.delete_button=Button(
            text="Delete all", 
            size_hint=(0.8, None), 
            height=44, 
            pos_hint={'center_x': 0.5, 'y': 0.2},
            background_normal='',
            background_down='',
            background_color=(0, 0, 0, 0),
            color=(0, 0, 0, 1))
        self.delete_button.bind(on_release=lambda _: (f.delete(), self.display_message("All deleted!")))


        layout.add_widget(self.delete_button)


        self.current_message = None

    
        self.add_widget(layout)
    

    def change(self, instance):
        cash = self.cash_input.text 
        card = self.card_input.text  
        try:
            cash = float(cash)
            self.cash_input.text=" "
            self.display_message("Saved!")
        except ValueError:
            self.display_message("Invalid cash input. Please try again ")

        try:
            card = float(card)
            self.card_input.text=" "
            self.display_message("Saved!")
        except ValueError:
            self.display_message("Invalid card input. Please try again")

        f.save_state(cash, card)




    def display_message(self, tekst):
        # Ako postoji prethodna message, ukloni je
        if self.current_message:
            self.remove_widget(self.current_message)

        # Prikazi novu poruku
        message = ResponsiveLabel(
            size_factor=0.25,
            text=tekst,
            size_hint=(1, 0.08),
            pos_hint={'center_x': 0.5, 'y': 0.1},
            halign="center", valign="middle",
            color=(0,0,0,1)
        )
        message.bind(size=lambda inst, val: setattr(inst, 'text_size', inst.size))
        self.add_widget(message)

        # Čuvaj referencu na trenutnu poruku
        self.current_message = message

        