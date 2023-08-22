'''
7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una 
persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es 
opcional. Crear los siguientes métodos para la clase:
   Un constructor, donde los datos pueden estar vacíos.
   Los setters y getters para cada uno de los atributos. El atributo no se puede modificar 
directamente, sólo ingresando o retirando dinero.
   mostrar(): Muestra los datos de la cuenta.
   ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es 
negativa, no se hará nada.
   retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números 
  rojos.
  
'''
class Cuenta:
   def __init__(self, titular, edad, cantidad = 0.0):
      self.titular = titular
      self.edad = edad
      self.cantidad = cantidad
    
    #Getter titular
   def get_titular(self):
      return self.titular
    #Getter cantidad
   def get_cantidad(self):
      return self.cantidad
   #Getter Edad
   def get_edad(self):
      return self.edad
    #Setter titular
   def set_titular(self, titular):
      self.titular = titular
    #Setter edad
   def set_edad(self, edad):
      self.edad = edad
    #Setter cantidad
   def set_cantidad(self, cantidad):
      self.cantidad = cantidad
    
   def mostrar(self):
      print("El titular es", self.titular)
      print("Edad:", self.edad)
      print("El saldo en cuenta es de", self.cantidad)
      
   def ingresar(self, cantidad):
      if cantidad >= 0:
         self.cantidad += cantidad
       
      else:
         print("La cantidad ingresada no es válida")

   def retirar(self, cantidad):
      self.cantidad -= cantidad
    

'''
8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase 
CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase, 
además del titular y la cantidad se debe guardar una bonificación que estará expresada en 
tanto por ciento. Crear los siguientes métodos para la clase:
   Un constructor.
   Los setters y getters para el nuevo atributo.
   En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo 
tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es 
mayor de edad pero menor de 25 años y falso en caso contrario.
   Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
   El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la 
cuenta.'''


class CuentaJoven(Cuenta):
   def __init__(self, titular, cantidad, edad, bonificacion):
      super().__init__(titular, cantidad, edad)
      self.bonificacion = bonificacion
      
   #Getter bonificacion
   def get_bonificacion(self):
      return self.bonificacion
   #Setter bonificacion
   def set_bonificacion(self, bonificacion):
      self.bonificacion = bonificacion
   
   def es_titular_valido(self):
      if self.edad >= 18 and self.edad < 25:
         return True
      else:
         return False
      
   def retirar(self, cantidad):
      if (self.es_titular_valido(self)):
         self.cantidad -= cantidad

   def mostrar(self):
      print(f"Cuenta Joven - Bonificacion {self.bonificacion}%")
      print("El titular es", self.titular)
      print("El saldo en cuenta es de", self.cantidad)
    
