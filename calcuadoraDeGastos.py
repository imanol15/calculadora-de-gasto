
gastos = {
    'Comida': 0,
    'Luz': 0,
    'Hipoteca': 0,
    'Varios': 0
}

def mostrar_menu():
    print("\nSelecciona una categoría:")
    print("1. Comida")
    print("2. Luz")
    print("3. Hipoteca")
    print("4. Varios")
    print("5. Ver gastos mensuales")
    print("6. Salir")

def añadir_gasto(categoria, dinero):
    if categoria in gastos:
        gastos[categoria] += dinero
        print(f"Se ha añadido un gasto de {dinero} a {categoria}.")
    else:
        print("Categoría no válida.")

def ver_gastos():
    print("\nGastos mensuales por categoría:")
    for categoria, dinero in gastos.items():
        print(f"{categoria}: {dinero}")

def seleccionar_categoria(opcion):
    categorias = {
        1: 'Comida',
        2: 'Luz',
        3: 'Hipoteca',
        4: 'Varios'
    }

    if opcion in categorias:
        dinero = float(input(f"Introduce el gasto en {categorias[opcion]}: "))
        añadir_gasto(categorias[opcion], dinero)
    elif opcion == 5:
        ver_gastos()
    elif opcion == 6:
        print("Saliendo del programa...")
        exit()
    else:
        print("Opción no válida.")

def main():
    while True:
        mostrar_menu()
        opcion = int(input("Introduce el número de tu selección: "))
        seleccionar_categoria(opcion)

if __name__ == "__main__":
    main()
