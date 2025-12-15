"""
Aplicación de saludo personalizado
Autor: Tonny
Fecha: 15/12/2025
"""


def obtener_nombre():
    """Solicita el nombre al usuario"""
    nombre = input("¿Cómo te llamas? ")
    return nombre


def obtener_edad():
    """Solicita la edad al usuario"""
    while True:
        try:
            edad = int(input("¿Cuántos años tienes? "))
            if edad > 0 and edad < 120:
                return edad
            else:
                print("Por favor, introduce una edad válida.")
        except ValueError:
            print("Por favor, introduce un número.")


def generar_saludo(nombre, edad):
    """Genera un mensaje de saludo personalizado"""
    print("\n" + "=" * 50)
    print(f"¡Hola, {nombre}!")
    print(f"Tienes {edad} años.")

    if edad < 18:
        print("Eres menor de edad.")
    elif edad < 65:
        print("Eres adulto.")
    else:
        print("Eres adulto mayor.")

    print("=" * 50)
    print("\nEste programa fue creado con PyCharm")
    print("y será convertido en ejecutable.")


def main():
    """Función principal del programa"""
    print("=" * 50)
    print("PROGRAMA DE SALUDO PERSONALIZADO")
    print("=" * 50)

    nombre = obtener_nombre()
    edad = obtener_edad()
    generar_saludo(nombre, edad)

    input("\nPresiona ENTER para salir...")


if __name__ == "__main__":
    main()