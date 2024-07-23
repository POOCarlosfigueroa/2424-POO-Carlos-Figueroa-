#calcular la masa corporaL de una persona
def calcular_imc(peso, altura):

  if altura <= 0:
    raise ValueError("La altura no puede ser 0 o menor.")
  imc = peso / (altura * altura)
  return imc

def mostrar_resultado(imc):

  # Mostrar respuestas de los calculos
  if imc < 18.5:
    clasificacion = "Peso minimo"
  elif imc < 25:
    clasificacion = "peso correcto"
  elif imc < 30:
    clasificacion = "peso maximo"
  else:
    clasificacion = "sobrepeso"

  print(f"Su IMC es de {imc:.2f}, lo que se clasifica como {clasificacion}.")

# Ejemplo de uso al ingresar peso en kilos
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

try:
  imc = calcular_imc(peso, altura)
  mostrar_resultado(imc)
except ValueError as error:
  print(error)