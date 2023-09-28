class Dog:

   """Esta es una clase inutil para instanciar perros"""
   def __init__(self, name):
      """Constructor de Perros"""
      self.name = name
      self.tricks = []

   def aprender(self, truco):
      """Metodo para aprender cosas"""
      self.tricks = truco

