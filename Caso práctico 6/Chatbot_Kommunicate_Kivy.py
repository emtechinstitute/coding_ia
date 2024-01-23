from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.webview import WebView  # Asumiendo que existe un widget de WebView


class ChatbotScreen(Widget):

  def __init__(self, **kwargs):
    super(ChatbotScreen, self).__init__(**kwargs)
    self.add_widget(Button(text='Abrir Chatbot', on_press=self.open_chatbot))

  def open_chatbot(self, instance):
    # Abrir la interfaz del chatbot en un WebView o navegador externo
    # Esto requeriría la URL de la interfaz del chatbot proporcionada por Kommunicate
    chatbot_webview = WebView(source='https://tu-chatbot-url.com')
    self.add_widget(chatbot_webview)


class MyApp(App):

  def build(self):
    return ChatbotScreen()


if __name__ == '__main__':
  MyApp().run()
