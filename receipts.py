from enum import Enum

class Category(Enum):
    Groceries=1
    Food=2
    House=3
    Coffee=4
    Cosmetics=5
    Clothes=6
    Entertainment=7
    Going_out=8
    Travel=9
    Saving=10

class Payment_method(Enum):
    Cash=1
    Card=2


class Receipt:

    def __init__(self,location,amount,category,payment_method):
        self.location=location
        self.amount=amount
        self.category = category  
        self.payment_method = payment_method 

    
