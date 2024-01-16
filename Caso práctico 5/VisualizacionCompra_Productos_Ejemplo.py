class ProductPurchaseScreen(BoxLayout):
  def __init__(self, **kwargs):
      super(ProductPurchaseScreen, self).__init__(**kwargs)
      self.orientation = 'vertical'
      # Esta lista podría poblarse dinámicamente con los productos disponibles
      self.product_list = self.create_product_list()
      for product_widget in self.product_list:
      self.add_widget(product_widget)


  def create_product_list(self):
    # Aquí se debería recuperar la lista de productos de la base de datos
    # Por ahora, usamos una lista estática para el ejemplo
    products = [
        {"name": "Producto 1", "description": "Descripción 1", "price": "10.00"},
        {"name": "Producto 2", "description": "Descripción 2", "price": "20.00"}
    ]
    product_widgets = []
    for product in products:
        product_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=30)
        product_layout.add_widget(Label(text=product['name']))
        product_layout.add_widget(Label(text=product['description']))
        product_layout.add_widget(Label(text=product['price']))
        product_layout.add_widget(Button(text='Añadir al carrito', on_press=self.add_to_cart))

        product_widgets.append(product_layout)
    return product_widgets

def add_to_cart(self, instance):
    # Lógica para añadir el producto seleccionado al carrito de compras

