
class Coche:
    def __init__(self, num_puertas, color):
        self.num_puertas = num_puertas
        self.color = color
        
    def incrementarPuertas(self, incremento):
        self.num_puertas += incremento
        
    def cambiarColor(self, nuevoColor):
        self.color = "Verde"

def main():
    coche1= Coche(3, "rojo")
    coche1.incrementarPuertas(4)
    print("Número de puertas:", coche1.num_puertas)
    print("Color actual del coche", coche1.color)
    coche1.cambiarColor("verde")
    print("El nuevo color del coche es:", coche1.color)

if __name__ == "__main__":
    main()