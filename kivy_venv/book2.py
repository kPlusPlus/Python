#book page 24

import kivy.app
import kivy.uix.textinput
import kivy.uix.button
import kivy.uix.boxlayout

class TestApp(kivy.app.App):
    
    def build(self):
        my_button = kivy.uix.button.Button(text="Click me")
        text_input = kivy.uix.textinput.TextInput(text="Data inside TextInput")
        
        box_layout = kivy.uix.boxlayout.BoxLayout(orientation="vertical")
        #box_layout.add_widget(widget=button)
        box_layout.add_widget(my_button)
        #box_layout.add_widget(widget=textInput)
        box_layout.add_widget(text_input)
        
        return box_layout

app = TestApp()
app.run()