class Circulo():
    def __init__(self,centro, radio):
        self.centro=centro
        self.radio=radio
        
    def mostrar(self):
        return "Centro:{0}-Radio:{1}".format(self.centro.mostrar(),self.radio)