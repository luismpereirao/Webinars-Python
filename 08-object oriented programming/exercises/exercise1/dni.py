class Dni():
    
    def __init__(self,numero):
        self.numero=numero
    
    def __calcular_letra(self):
        letras="TRWAGMYFPDXBNJZSQVHLCKE"
        return letras[int(self.numero)%23]
    
    @property
    def numero(self):
        return self.__numero
    
    @property
    def letra(self):
        return self.__letra
    
    @numero.setter
    def numero(self, numero):
        if len(numero)==8 and numero.isdigit():
            self.__numero = numero
            self.__numero = self.__calcular_letra()
        else:
            self.__numero=0
            self.__letra=""
            print("DNI incorrecto.")
            
    def mostrar(self):
        return self.numero+self.letra