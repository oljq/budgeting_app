#2 pagee
#display all bills with place and amount

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView

from button import Button_back
from functions import Line, ResponsiveLabel
import functions as f 


class List(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        f.load_receipts()

        layout = FloatLayout()

        background = Image(source="static/bg123.jpg", size_hint=(1, 1.1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(background)

        layout.add_widget(Line(height=2, size_hint=(1, None)))

        button_back = Button_back(
            picture_path="static/2.jpg",  # Putanja do slike
            size_hint=(0.4, 0.2),
            pos_hint={'center_x': 0.5, 'y': 0.8}
        )
        button_back.bind(on_release=f.return_to_home_screen)
        layout.add_widget(button_back)


        if not f.receipts:
            message1=ResponsiveLabel(
                size_factor=0.25,
                text="No receipte",
                size_hint=(1, 0.08),
                pos_hint={'center_x': 0.5, 'y': 0.7},
                color=(0, 0, 0, 1))
            layout.add_widget(message1)

        else:

            message2= ResponsiveLabel(
                size_factor=0.25,
                text="---RECEIPTS---", 
                size_hint=(1, 0.08),
                pos_hint={'center_x': 0.5, 'y': 0.7},
                color=(0, 0, 0, 1))
            layout.add_widget(message2)
            layout.add_widget(Line(height=2, size_hint=(1, None)))

        scroll_layout = BoxLayout(orientation='vertical', spacing=0,size_hint_y=None)
        scroll_layout.bind(minimum_height=scroll_layout.setter('height'))
        
        for receipt in f.receipts:
            lbl = ResponsiveLabel(
                size_factor=0.40,
                text=f"{receipt['location']}: {receipt['amount']} RSD", 
                size_hint=(1, None), 
                height=60,
                halign="center", valign="middle",
                color=(0, 0, 0, 1),
            )
            scroll_layout.add_widget(lbl)

        scroll_view = ScrollView(size_hint=(1, 0.5), pos_hint={'center_x': 0.5, 'y': 0.2})
        scroll_view.add_widget(scroll_layout)
        layout.add_widget(scroll_view)
        
        layout.add_widget(Line(height=2, size_hint=(1, None)))

        sum_all=f.sum_all()
        message=ResponsiveLabel(
            size_factor=0.25,
            text=f"Sum: {sum_all} EUR", 
            size_hint=(1, 0.08),
            pos_hint={'center_x': 0.5, 'y':0.15 },
            color=(0, 0, 0, 1))
        layout.add_widget(message)

        self.add_widget(layout)