#1. pagee
#Add expenses

from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.image import Image

import functions as f 
from functions import ResponsiveLabel
from functions import Line
from button import Button_back
from receipts import Category,Payment_method

class Add(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = FloatLayout()

        background = Image(source="static/bg123.jpg", size_hint=(1, 1.1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(background)

        layout.add_widget(Line(height=2, size_hint=(1, None)))

        button_back = Button_back(
            picture_path="static/1.jpg",  
            size_hint=(0.4, 0.2),
            pos_hint={'center_x': 0.5, 'y': 0.8}
        )
        button_back.bind(on_release=f.return_to_home_screen)
        layout.add_widget(button_back)

        
        self.location_input = TextInput(hint_text="Enter location", size_hint=(0.8, None), height=50, pos_hint={'center_x': 0.5, 'y': 0.7})
        layout.add_widget(self.location_input)

        
        self.amount_input = TextInput(hint_text="Enter amount", size_hint=(0.8, None), height=50, pos_hint={'center_x': 0.5, 'y': 0.6})
        layout.add_widget(self.amount_input)

#Dropdown meny

        category_dropdown = DropDown()
        for k in Category:
            btn = Button(text=str(k.name), size_hint_y=None, height=44)
            btn.background_normal = ''  
            btn.background_color =( 0.9, 0.7, 0.8, 0.3)
            btn.color = (0, 0, 0, 1)  
            btn.bind(on_release=lambda btn, k=k, dropdown=category_dropdown: self.category_selected(btn, k, dropdown))
            category_dropdown.add_widget(btn)
                
        self.category_button = Button(text="Select category", size_hint=(0.8, None), height=50, pos_hint={'center_x': 0.5, 'y': 0.5})
        self.category_button.bind(on_release=category_dropdown.open)
        layout.add_widget(self.category_button)

        
        payment_method_dropdown = DropDown()
        for n in Payment_method:
            btn = Button(text=n.name, size_hint_y=None, height=44) 
            btn.background_normal = ''  
            btn.background_color =( 0.9, 0.7, 0.8, 0.3)
            btn.color = (0, 0, 0, 1)  
            btn.bind(on_release=lambda btn, n=n,dropdown=payment_method_dropdown: self.payment_method_selected(btn,n,dropdown))
            payment_method_dropdown.add_widget(btn)

        self.payment_method_button = Button(text="Select payment metod", size_hint=(0.8, None), height=50, pos_hint={'center_x': 0.5, 'y': 0.4})
        layout.add_widget(self.payment_method_button)

        def open_dropdown(instance):
            payment_method_dropdown.open(self.payment_method_button)

        self.payment_method_button.bind(on_release=open_dropdown)

        button_add = Button(
            text="Add receipt", 
            size_hint=(0.8, None), 
            height=44, 
            pos_hint={'center_x': 0.5, 'y': 0.3},
            background_normal='',
            background_down='',
            background_color=(0, 0, 0, 0),
            color=(0, 0, 0, 1)
            )
        button_add.bind(on_release=self.add_receipt)
        layout.add_widget(button_add)

        self.location_input.text = ""
        self.amount_input.text = ""
        self.selected_category = None
        self.selected_payment_method = None
        self.category_button.text = "Select category"  
        self.payment_method_button.text = "Select payment metod" 

        self.current_message = None

        self.add_widget(layout)


    def category_selected(self, btn, k, dropdown):
        self.selected_category = k
        self.category_button.text = str(k.name) 
        dropdown.dismiss()

    def payment_method_selected(self, btn, n, dropdown):
        self.selected_payment_method = n
        self.payment_method_button.text = str(n.name)
        dropdown.dismiss()

    def add_receipt(self, instance):
        location = self.location_input.text
        amount = self.amount_input.text


        if not location or not amount:
            self.display_message("Enter location and amount")
            return

        try:
            amount = float(amount)
        except ValueError:
            self.display_message("Error entering amount. Please enter a valid number.")
            return
        
        category = self.selected_category
        payment_method = self.selected_payment_method

        if not category or not payment_method:
            self.display_message("Please enter category and payment method.")
            return

        f.add_receipt(location, amount, category, payment_method)


        self.location_input.text = ""
        self.amount_input.text = ""
        self.selected_category = None
        self.selected_payment_method = None

        self.display_message("Receipt successfully added")

    def display_message(self, tekst):
        
        if self.current_message:
            self.remove_widget(self.current_message)

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

        # Keep a reference to the current message
        self.current_message = message



