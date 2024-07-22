class ClimaSemanal:
    
    def __init__(self):
        self.temperaturas = []

    #Función para ingresar temperaturas
    def ingresar_temperaturas(self):
        for i in range(7):
            temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
            self.temperaturas.append(temp)

    #Función para calcular promedio
    def calcular_promedio_semanal(self):
        return sum(self.temperaturas) / len(self.temperaturas)

def main():
    # Crear una instancia de ClimaSemanal
    clima = ClimaSemanal()
    
    # Ingresar las temperaturas diarias
    clima.ingresar_temperaturas()
    
    # Calcular el promedio semanal
    promedio = clima.calcular_promedio_semanal()
    
    # Mostrar el promedio semanal
    print(f"El promedio semanal de temperatura es: {promedio:.2f}")

if __name__ == "__main__":
    main()
