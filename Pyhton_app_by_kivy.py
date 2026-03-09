from kivy.app import App
from kivy.uix.label import Label

class my_app(App):
    def build(self):
        return Label(text="Welcome To My App",halign="center")
    
    
my_app().run()