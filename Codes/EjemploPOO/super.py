#!/usr/bin/env Python 

# Importaremos nuestras Clases de Personas:
from personas import Cliente, Validador

# Utilizaremos deque para las colas de clientes:
from collections import deque

class Caja():
   """Esta clase administra proceso: cola de clientes -> validación -> checkout"""
   
   def __init__(self):
      """Constructor de Caja"""
      
      # Persona que atiende:
      self.cajero = Validador() 
      
      # Clientes en espera
      self.cola = deque([])
      # Este objeto es similar a una lista pero permite eliminar los 
      # elementos agregados al principio de una manera eficiente.
      # Pueden utilizar deque([]) cada vez que necesiten un objeto 
      # con funcionalidad first-in-first-out (FIFO), como una cola o
      # lista de espera.

      # Persona a la que se está atendiendo:
      self.comprador = 0


   def add_cliente(self, cliente):
      """Método para agregar clientes a la cola de espera"""
      self.cola.append(cliente)
   
   def kick_client(self):
      """Rutina para guardar un cliente en archivo"""
      #TODO: Completar!

      self.comprador = 0


   def trabajar(self, dt):
      """Rutina que avanza el proceso de validación, checkout y cola"""
      
      # Iteramos para cada unidad de tiempo mientras dt>0:
      while(dt > 0):
         # Avanzamos la cola si no está atendiendo a nadie:
         if not self.comprador:
            self.comprador = self.cola.popleft()
            self.cajero.recibir_items(self.comprador.comprar())
         
         # Validamos items:
         tleft = self.cajero.validar(dt)
         # Agregamos este tiempo de compra al comprador:
         # (Esto no cumple OCP: deberíamos modificar tlocal con un método.
         self.comprador.tlocal += (dt - tleft)

         # En caso de terminar de validar, llamamos a kick_client y
         # continuamos:
         if (self.cajero.validationTime <= 0):
            kick_client()
         
         dt = tleft

   def get_cola(self):
      """Método que retorna el número de items que hay en cola"""
      itot = self.cajero.items
      for c in self.cola:
         itot += c.items
      return itot
       

class Supermarket():
   """Clase que contiene/simula las diferentes componentes de un super"""

   def __init__(self, ncajas=1):
      """Constructor de Supermarket."""
      # Cajas disponibles:
      self.cajas = [Caja()  for _ in range(ncajas)]
      # Clientes en tienda buscando productos:
      self.clientes_buscando = []
      # Todos los clientes:
      self.clientes_total = []
      # Hora actual
      self.tnow = 0
   
   def set_flujo(self):
      """Método para cargar la lista de clientes a recibir en la
      simulacion."""
      #TODO: Completar!

   def _clientes_nuevos(self, dt):
      """Método para verificar si llegan clientes nuevos en este dt"""
      #TODO: Completar forma de agregar clientes entre tnow y tnow+dt
      #      -> clientes a buscar items.

   def buscar_caja(self):
      """Método que retorna la caja más vacía en el momento."""
      minitems = self.cajas[0].get_cola()
      mincaja = self.cajas[0]
      for caja in self.cajas:
         tmp = caja.get_cola()
         if (tmp < minitems):
            minitems = tmp
            mincaja = caja
      return mincaja


   def _asignar_caja(self, cind=-1):
      """Método para asignar una caja disponible a un cliente"""
      # Si no se ingresa el cliente, selecciona todos lo que terminaron
      # su búsqueda:
      if (-1 == cind):
         cterm = []
         for i, c in enumerate(self.clientes_buscando):
            if (c.searchTime <= 0):
               cterm.append(c)
      else:
         if not type(cind) == list:
            cind = [cind]
         for i in cind:
            cterm.append(self.clientes_buscando[i])

      for c in cterm:
         # sacamos de la lista los que terminaron:
         self.clientes_buscando.remove(c)
         # asignamos cajas:
         self.buscar_caja().add_cliente(c)


   def run(self, dt):
      """Método que avanza en el proceso de búsqueda y compra por dt"""
      
      while (dt > 0):
         # Recorremos todos los clientes para que busquen sus items en dt=1:
         for cliente in self.clientes_buscando:
            cliente.buscar_items(1)
         # En el mismo tiempo, las cajas procesan items:
         for caja in self.cajas:
            caja.trabajar(1)
         # Si alguno terminó, asignamos caja:
         self._asignar_caja()
         dt -= 1

