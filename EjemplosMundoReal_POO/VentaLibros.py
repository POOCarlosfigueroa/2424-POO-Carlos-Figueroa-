class Libro:
    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio

    def __str__(self):
        return f"'{self.titulo}' por {self.autor} - ${self.precio:.2f}"

class Venta:
    def __init__(self, libro, cantidad):
        self.libro = libro
        self.cantidad = cantidad

    def calcular_total(self):
        return self.libro.precio * self.cantidad

    def __str__(self):
        return (f"Venta: {self.cantidad} x {self.libro.titulo}\n"
                f"Total: ${self.calcular_total():.2f}")

def main():
    # Crear un libro
    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 19.99)
    
    # Crear una venta del libro
    venta1 = Venta(libro1, 3)
    
    # Mostrar la información de la venta
    print(venta1)

if __name__ == "__main__":
    main()
