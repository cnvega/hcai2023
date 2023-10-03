# Esta es la implementacion del ejemplo de clases:

class Complex:
   """Otra clase de numeros complejos"""

   def __init__(self, r, i):
      """Constructor"""
      self.r = r
      self.i = i

   def __str__(self):
      return str(self.r)+"+i"+str(self.i)

   def __add__(self, c):
      print(self)
      return Complex(self.r+c.r, self.i+c.i)

   def mostrar_lindo(self):
      rep = self.__str__()
      print ("Este es mi numero: "+rep)


