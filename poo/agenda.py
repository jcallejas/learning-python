#Creando la clase agenda
class agenda:
    def __init__(self,nombre,apellido,ci,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.ci = ci
        self.edad = edad

    def setNombre(self,nom):
        self.nombre = nom

    def getNombre(self):
        return self.nombre