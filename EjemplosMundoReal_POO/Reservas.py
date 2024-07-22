# Clase cliente
class Cliente:
    def __init__(self, nombre, email, telefono):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def __str__(self):
        return f"Cliente: {self.nombre}, Email: {self.email}, Telefono: {self.telefono}"

# clase reserva que utiliza un objeto cliente
class Reserva:
    def __init__(self, cliente, fecha_ingreso, fecha_salida, habitacion):
        self.cliente = cliente
        self.fecha_ingreso = fecha_ingreso
        self.fecha_salida = fecha_salida
        self.habitacion = habitacion

    def __str__(self):
        return (f"Reserva de {self.cliente.nombre}\n"
                f"Fecha de ingreso: {self.fecha_ingreso}\n"
                f"Fecha de salida: {self.fecha_salida}\n"
                f"Habitación: {self.habitacion}")

def main():
    # Crear un cliente
    cliente1 = Cliente("Juan Pérez", "juan.perez@example.com", "0987568790" )
    
    # Crear una reserva para el cliente
    reserva1 = Reserva(cliente1, "2024-07-10", "2024-07-15", "110")
    
    # Mostrar la información de la reserva
    print(reserva1)

if __name__ == "__main__":
    main()
