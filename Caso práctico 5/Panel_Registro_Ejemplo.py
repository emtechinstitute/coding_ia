class ProductRegistrationScreen(BoxLayout):

  def __init__(self, **kwargs):
    super(ProductRegistrationScreen, self).__init__(**kwargs)
    self.orientation = 'vertical'
    self.add_widget(TextInput(hint_text='Nombre del Producto'))
    self.add_widget(TextInput(hint_text='Descripción'))
    self.add_widget(TextInput(hint_text='Precio'))
    self.add_widget(
        Button(text='Registrar Producto', on_press=self.register_product))

  def register_product(self, instance):
    # Lógica para registrar el producto en la base de datos
    # Aquí se puede utilizar Copilot para generar el código de conexión y envío de datos
    pass
