#3 page
#display category and amount


from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from functions import Line
import functions as f 
from functions import ResponsiveLabel
from button import Button_back


class History(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = FloatLayout()

        background = Image(source="static/bg123.jpg", size_hint=(1, 1.1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(background)

        layout.add_widget(Line(height=2, size_hint=(1, None)))

        button_back = Button_back(
            picture_path="static/3.jpg",  
            size_hint=(0.4, 0.2),
            pos_hint={'center_x': 0.5, 'y': 0.8}
        )
        button_back.bind(on_release=f.return_to_home_screen)
        layout.add_widget(button_back)

        sume = f.sum_category()

        y_pos = 0.75

        for category, amount in sume.items():
            y_pos -= 0.05
            lbl = ResponsiveLabel(
                size_factor=0.13,
                text=f"{category.name}: {amount} RSD",
                size_hint=(1, 0.15), 
                pos_hint={'center_x': 0.5, 'y': y_pos},  
                halign="center", valign="middle",
                color=(0, 0, 0, 1)
            )
            layout.add_widget(lbl)

        sum_all=f.sum_all()
        message=ResponsiveLabel(
            size_factor=0.25,
            text=f"Sum: {sum_all} EUR",
            size_hint=(1, 0.08),
            pos_hint={'center_x': 0.5, 'y':0.15 },
            color=(0, 0, 0, 1))
        layout.add_widget(message)

        self.add_widget(layout)


        


            