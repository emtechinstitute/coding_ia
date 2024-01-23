def test_chatbot_interaction():
  # Simular el envío de un mensaje al chatbot
  message = "Hola, necesito ayuda"
  # Enviar el mensaje y recibir la respuesta del chatbot
  response = send_message_to_chatbot(message)
  assert "Cómo puedo ayudarte" in response
