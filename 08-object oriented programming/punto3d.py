from punto import Punto

class Punto3d(Punto):
    def __init__(self, x=0, y=0,z=0):
        super().__init__(x, y)
        self.z=z
        
    @property
    def z(self):
        print("Doy z")
        return self.__z
    
    @z.setter
    def z(self,z):
        print("Cambio z")
        self.__z=z
    
    def mostrar(self):
        return super().mostrar()+":"+str(self.z)
    
    def distancia(self, otro):
        dx = self.__x - otro.__x
        dy = self.__y - otro.__y
        dz = self.__z - otro.__z
        return (dx*dx + dy*dy +dz*dz)**0.5