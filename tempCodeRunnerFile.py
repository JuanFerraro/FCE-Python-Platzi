def message_creator(text):
   # Escribe tu solución 👇
   if text == 'computadora':
      print('Con mi computadora puedo programar usando Python')
   elif text == 'celular':
      print('En mi celular puedo aprender usando la app de Platzi')
   elif text == 'cable':
      print('¡Hay un cable en mi bota!')
   else:
      print("Artículo no encontrado")
   return ''

text = 'celular'
response = message_creator(text)
print(response)