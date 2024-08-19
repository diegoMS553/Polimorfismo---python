# Clase base (superclase) 
class Automovil: 
    def __init__(self, marca, año): 
        self.marca = marca 
        self.año = año 
    def hacer_sonido(self): 
        return "Sonido genérico" 

# Subclase que hereda de Animal 
class Electrico(Automovil): 
    def hacer_sonido(self): 
        return "........." 

# Otra subclase que hereda de Animal 
class Combustion(Automovil): 
    def hacer_sonido(self): 
        return "Run run run" 

# Función que demuestra polimorfismo 
def imprimir_sonido(animal): 
    print(animal.hacer_sonido()) 
    
# Ejemplo de uso 
model_3 = Electrico("Tesla", 2020) 
chevi = Combustion("Chevrolet", 2002) 

imprimir_sonido(model_3)  # Imprime: .........
imprimir_sonido(chevi)  # Imprime: Run run run
