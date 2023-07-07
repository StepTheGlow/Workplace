import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.config import Config

# Set up Kivy configuration
Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '640')
Config.set('graphics', 'resizable', '0')

class AlonzeGame(FloatLayout):
    def __init__(self, **kwargs):
        super(AlonzeGame, self).__init__(**kwargs)

        self.background = Image(source='background.png', size_hint=(1, 1), allow_stretch=True)
        self.add_widget(self.background)

        self.intro_label = Label(text="Hello, my name is Rafael. Nice to meet you.",
                                 size_hint=(0.8, 0.2),
                                 pos_hint={'center_x': 0.5, 'center_y': 0.75})
        self.add_widget(self.intro_label)

        self.name_input = TextInput(text="",
                                    multiline=False,
                                    size_hint=(0.6, 0.1),
                                    pos_hint={'center_x': 0.5, 'center_y': 0.6})
        self.add_widget(self.name_input)

        self.name_button = Button(text="Enter",
                                  size_hint=(0.2, 0.1),
                                  pos_hint={'center_x': 0.5, 'center_y': 0.45})
        self.name_button.bind(on_release=self.get_name)
        self.add_widget(self.name_button)

        self.gender_label = Label(text="",
                                  size_hint=(0.8, 0.2),
                                  pos_hint={'center_x': 0.5, 'center_y': 0.75})

    def get_name(self, instance):
        name = self.name_input.text
        if name:
            self.intro_label.text = f"Oh, you are {name}. My 3rd wife's 9th, ummm...\nWere you a boy or girl?"
            self.remove_widget(self.name_input)
            self.remove_widget(self.name_button)
            self.add_widget(self.gender_label)

            self.male_button = Button(text="Male",
                                      size_hint=(0.2, 0.1),
                                      pos_hint={'center_x': 0.4, 'center_y': 0.45})
            self.male_button.bind(on_release=self.get_gender)
            self.add_widget(self.male_button)

            self.female_button = Button(text="Female",
                                        size_hint=(0.2, 0.1),
                                        pos_hint={'center_x': 0.6, 'center_y': 0.45})
            self.female_button.bind(on_release=self.get_gender)
            self.add_widget(self.female_button)

    def get_gender(self, instance):
        if instance.text == "Male":
            self.gender_label.text = "Just kidding, I know you are a boy. So this is your assistant."
            self.assistant_name = "Carla"
            self.assistant_dialogue = f"Hello {name}, nice to meet you. I'm Carla, your personal assistant. " \
                                      f"I'm here to help you with anything you need. " \
                                      f"Feel free to ask me questions or give me commands."
        elif instance.text == "Female":
            self.gender_label.text = "Just kidding, I know you are a girl. So this is your assistant."
            self.assistant_name = "Joe"
            self.assistant_dialogue = f"Hello {name}, nice to meet you. I'm Joe, your personal assistant. " \
                                      f"I'm here to assist you and make your life easier. " \
                                      f"Let me know if there's anything I can do for you."

        self.remove_widget(self.gender_label)
        self.remove_widget(self.male_button)
        self.remove_widget(self.female_button)

        self.assistant_label = Label(text=self.assistant_dialogue,
                                     size_hint=(0.8, 0.2),
                                     pos_hint={'center_x': 0.5, 'center_y': 0.75})
        self.add_widget(self.assistant_label)

class AlonzeApp(App):
    def build(self):
        Window.clearcolor = (0, 0, 0, 1)
        return AlonzeGame()

if __name__ == '__main__':
    AlonzeApp().run()
