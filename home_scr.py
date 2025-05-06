#0. page
#4 battons for navigating to new windows

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
import settings as p
import functions as f

from functions import *

class Home_scr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.receipts=f.receipts

        layout = FloatLayout()

        background = Image(source="static/start_bg.jpg", size_hint=(1, 1.1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(background)

        message = ResponsiveLabel(
            size_factor=0.4,
            text="Hello!",
            size_hint=(1, 0.08),
            pos_hint={'center_x': 0.5, 'y': 0.9},
            halign="center", valign="middle"
            )
        message.bind(size=lambda inst, val: setattr(inst, 'text_size', inst.size))
        layout.add_widget(message)

        sum_all_r=float(f.display_remaining_money())

        sum_all = ResponsiveLabel(
            size_factor=0.5,
            text=f"{sum_all_r}EUR",
            bold=True, 
            size_hint=(1, 0.09), 
            pos_hint={'center_x': 0.5, 'y': 0.83},
            halign="center", valign="middle"
            )
        message.bind(size=lambda inst, val: setattr(inst, 'text_size', inst.size))
        layout.add_widget(sum_all)

        cash=str(f.display_remaining_cash())

        money_layout = BoxLayout(orientation='horizontal', spacing=20, size_hint=(1, 0.06), pos_hint={'center_x': 0.5, 'y': 0.75})
        cash = ResponsiveLabel(
            size_factor=0.3,  
            text=f"Cash: {cash}RSD" ,
            halign="center", valign="middle"
        )
        cash.bind(size=lambda inst, val: setattr(inst, 'text_size', inst.size))

        card=str(f.display_remaining_card())

        card = ResponsiveLabel( 
            size_factor=0.3, 
            text=f"Card: {card} RSD", 
            halign="center", valign="middle"
        )
        card.bind(size=lambda inst, val: setattr(inst, 'text_size', inst.size))
        

        money_layout.add_widget(cash)
        money_layout.add_widget(card)
        layout.add_widget(money_layout)

        button1 = Button(
            text="Add cost",  
            size_hint=(1, 0.15), 
            pos_hint={'center_x': 0.5, 'y': 0.5},
            background_normal='',
            background_down='',
            background_color=(0, 0, 0, 0),
            color=(0, 0, 0, 1)
            )
        button1.bind(on_release=self.open_add)

        button2 = Button(
            text="All receipts",  
            size_hint=(1, 0.15), 
            pos_hint={'center_x': 0.5, 'y': 0.35},
            background_normal='',
            background_down='',
            background_color=(0, 0, 0, 0),
            color=(0, 0, 0, 1)
            )
        button2.bind(on_release=self.open_list)

        button3 = Button(
            text="Category",
            size_hint=(1, 0.15),
            pos_hint={'center_x': 0.5, 'y': 0.2},
            background_normal='',
            background_down='',
            background_color=(0, 0, 0, 0),
            color=(0, 0, 0, 1)
            )
        button3.bind(on_release=self.open_category)

        button4 = Button(
            text="Settings",
            size_hint=(1, 0.15),
            pos_hint={'center_x': 0.5, 'y': 0.05},
            background_normal='',
            background_down='',
            background_color=(0, 0, 0, 0),
            color=(0, 0, 0, 1)
            )
        button4.bind(on_release=self.open_settings)

        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(button3)
        layout.add_widget(button4)

        self.add_widget(layout)

    def open_add(self, instance):
        self.manager.current = 'add'

    def open_list(self, instance):
        self.manager.current = 'list'

    def open_category(self, instance):
        self.manager.current = 'category'

    def open_settings(self, instance):
        self.manager.current = 'settings'




