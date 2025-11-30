from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics import Rectangle

#Button back is picture 

class Button_back(Button):
    def __init__(self, picture_path, **kwargs):
        super().__init__(**kwargs)
        
        self.image = Image(source=picture_path, allow_stretch=True, keep_ratio=True)
        self.background_normal = ''  
        self.background_down = '' 
        self.background_color = (0, 0, 0, 0)  
        
        with self.canvas.before:
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.add_widget(self.image)
        
        self.bind(size=self.update_rect, pos=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
        self.image.pos = self.pos
        self.image.size = self.size