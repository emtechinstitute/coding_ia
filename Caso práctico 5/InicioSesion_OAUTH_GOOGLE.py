from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class LoginScreen(BoxLayout):

  def __init__(self, **kwargs):
    super(LoginScreen, self).__init__(**kwargs)
    self.orientation = 'vertical'
    self.add_widget(TextInput(hint_text='Correo electrónico'))
    self.add_widget(TextInput(hint_text='Contraseña', password=True))
    self.add_widget(
        Button(text='Iniciar sesión con Google',
               on_press=self.login_with_google))

  def login_with_google(self, instance):
    # Aquí se implementaría la lógica para iniciar sesión con Google OAuth
    pass


class MyApp(App):

  def build(self):
    return LoginScreen()


if __name__ == '__main__':
  MyApp().run()
