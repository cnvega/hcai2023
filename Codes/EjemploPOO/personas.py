
class Persona():
   """Esta es una clase generica para almacenar personas"""

   def __init__(self):
      self.items = 0
      self.tlocal = 0 # tiempo total en el super


class Validador(Persona):
   """Esta es una clase para representar personas que validen"""

   def __init__(self, fac=5):
      # Este es el factor de conversion items a tiempo de validar
      self.validfactor = fac
      self.validationTime = 0

   def get_items(self, nitems):
      self.items = nitems
      self.validationTime = nitems*self.validfactor 

   def validar(self, dt):
      while(dt > 0 and self.validationTime > 0):
         self.validationTime -= 1
         dt -= 1
      return dt

class Cliente(Persona):
   """Esta es una clase para representar clientes en el super"""
   def __init__(self, buscfactor=120):
      self.buscfactor = buscfactor
      self.searchTime = 0

   def set_target(self, nitems):
      self.items = nitems
      self.searchTime = nitems*self.buscfactor

   def buscar_items(self, dt):
      while(dt > 0 and self.searchTime > 0):
         self.searchTime -= 1
         dt -= 1
      return dt

   def comprar(self):
      return self.items

