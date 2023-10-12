#!/usr/bin/env Python 

class Persona():
   """Esta es una clase generica para almacenar personas"""

   def __init__(self):
      self.items = 0  # "canasta" de items
      self.tlocal = 0 # tiempo total en el super


class Validador(Persona):
   """Esta es una clase para representar personas que validen"""

   def __init__(self, fac=5):
      super().__init__()
      # Este es el factor de conversion items a tiempo de validar
      self.validfactor = fac
      self.validationTime = 0

   # Lo cambie dado que get_* se puede entender como un getter.
   def recibir_items(self, nitems):
      self.items = nitems
      self.validationTime = nitems*self.validfactor 

   def validar(self, dt):
      """Método para validar items en espera durante dt"""
      while(dt > 0 and self.validationTime > 0):
         # Validamos items en este tiempo:
         self.validationTime -= 1
         # Descontamos tiempo transcurrido:
         dt -= 1
         # sumamos nuestro tiempo en el super:
         self.tlocal += 1
      # si sobró tiempo, le avisamos a la clase superior para que 
      # asigne otro cliente y continuemos validando
      return dt


class Cliente(Persona):
   """Esta es una clase para representar clientes en el super"""
   
   def __init__(self, buscfactor=120):
      super().__init__()
      # Esta estructura resultó igual que la de Validador (falló DRY)
      self.buscfactor = buscfactor
      self.searchTime = 0

   def set_target(self, nitems):
      """Método para estimar cuánto tiempo estará buscando nitems"""
      self.items = nitems
      self.searchTime = nitems*self.buscfactor

   def buscar_items(self, dt):
      """Método para contabilizar el tiempo de búsqueda en el super.
         Retorna el tiempo sobrante en caso de terminar la búsqueda."""
      while(dt > 0 and self.searchTime > 0):
         self.searchTime -= 1
         dt -= 1
         # sumamos el tiempo dentro del local:
         self.tlocal += 1
      return dt

   def comprar(self):
      return self.items
   
