
class carro:
  def __init__(self,marca,placa):
    self._placa=placa
    self._marca=marca
  

  @property
  def placa(self):
    return self._placa
  
  @placa.setter
  def placa(self,a):
    self._placa=a
  
  @property
  def marca(self):
    return self._marca
  
  @marca.setter
  def marca(self,b):
    self._marca=b
  
  def __str__ (self):
    return "El carro de la marca "+self._marca+", su numero de placa es "+self._placa