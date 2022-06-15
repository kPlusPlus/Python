#book page 22

import kivy.app
import kivy.uix.textinput

class TestApp(kivy.app.App):
    def build(self):
        return kivy.uix.textinput.TextInput(text="Hello World")
    
app = TestApp()
app.run()
    