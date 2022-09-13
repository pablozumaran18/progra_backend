

class operaciones:

    def suma(a,b):
        return (a + b)

    def resta(a,b):
        return (a - b)

    def multi (a,b):
        return(a * b)

    def div (a,b):
        return (a / b)
    


class perro:

    nombre = ""
    edad = ""

    def __init__(self,nombre,edad) -> None:

        self.nombre = nombre
        self.edad = edad
        

    def ladrar(self):
        print("guau "+self.nombre+" esta ladrando")

    def caminar (self):
        return("caminando")

