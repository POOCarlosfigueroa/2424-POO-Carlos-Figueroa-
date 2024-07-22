# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio_semanal(temperaturas):
    return sum(temperaturas) / len(temperaturas)

def main():
    # Ingresar las temperaturas diarias
    temperaturas = ingresar_temperaturas()
    
    # Calcular el promedio semanal
    promedio = calcular_promedio_semanal(temperaturas)
    
    # Mostrar el promedio semanal
    print(f"El promedio semanal de temperatura es: {promedio:.2f}")

if __name__ == "__main__":
    main()
