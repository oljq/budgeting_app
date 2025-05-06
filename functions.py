from receipts import *

from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle

import json
import os

#File paths to data base

file_path = "base/receipts.json"
initial_state = "base/initial_state.json"

receipts = []
start_cash = 0.0
start_card = 0.0


class Line(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(0, 0., 0., 1) 
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect = self.size


class ResponsiveLabel(Label):
    def __init__(self, size_factor, **kwargs):
        super().__init__(**kwargs)
        self.size_factor = size_factor
        self.bind(size=self.update_font)  
        self.update_font()  

    def update_font(self, *args):
        """Updates font size based on widget height and desired factor"""
        self.font_size = self.height * self.size_factor


#Functions for working with base/initial_state.json


def load_state():
    global start_cash, start_card
    if os.path.exists(initial_state):
        with open(initial_state, "r", encoding="utf-8") as f:
            data = json.load(f)
            start_cash = data.get("start_cash", 0)
            start_card = data.get("start_card", 0)
    else:
        save_state(0, 0)

def save_state(cash, card):
    global start_cash, start_card
    start_cash = cash
    start_card = card
    with open(initial_state, "w", encoding="utf-8") as f:
        json.dump({
            "start_cash": cash,
            "start_card": card
        }, f, indent=4)

#Functions for working with base/receipts.json

def load_receipts():
    global receipts
    if not os.path.exists('base'):
        os.makedirs('base')

    # If the file exists, load it, otherwise create a file with empty lists
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                receipts = json.load(f)
                return receipts
            except json.JSONDecodeError:
                return []
    else:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=4)
        return []
    
    return receipts 


def save_receipts(receipts):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(receipts, f, ensure_ascii=False, indent=4)

def add_receipt(location, amount, category, payment_method):
    receipts = load_receipts()
    new_receipt = {
        "location": location,
        "amount": amount,
        "category": category.name if hasattr(category, 'name') else category,
        "payment_method": payment_method.name if hasattr(payment_method, 'name') else payment_method
    }
    receipts.append(new_receipt)
    save_receipts(receipts)

#sum functions

def sum_all():
    receipts = load_receipts() 
    sum = 0
    for receipt in receipts:
        sum += receipt['amount']
    return sum

def sum_category():
    receipts = load_receipts()  
    sum = {category: 0 for category in Category}  
    
    for receipt in receipts:
        if receipt['category'] in Category.__members__:
            sum[Category[receipt['category']]] += receipt['amount']
    
    return sum

def sum_payment_method():
    receipts = load_receipts()  
    sum = {payment_method: 0 for payment_method in Payment_method}  
    
    for receipt in receipts:
        if receipt['payment_method'] in Payment_method.__members__:
            sum[Payment_method[receipt['payment_method']]] += receipt['amount']  
    
    return sum

#display functions


def display_remaining_cash():
    global start_cash
    sum = sum_payment_method()
    remaining = start_cash - sum.get(Payment_method.Cash, 0)
    return round(remaining, 2)

def display_remaining_card():
    global start_card
    sum = sum_payment_method()
    remaining= start_card - sum.get(Payment_method.Card, 0)
    return round(remaining, 2)

def display_remaining_money():
    sum =start_card + start_cash
    sum_buy_payment_methodu = sum_payment_method()
    total_payment = sum_buy_payment_methodu.get(Payment_method.Card, 0) + sum_buy_payment_methodu.get(Payment_method.Cash, 0)
    return round(sum - total_payment, 2)



def delete(instance=None):
    global receipts
    receipts.clear() 

    if os.path.exists('base/receipts.json'):
        os.remove('base/receipts.json')

def return_to_home_screen(instance):
    from kivy.app import App
    load_receipts() 
    root = App.get_running_app().root
    root.current = 'home_scr' 



