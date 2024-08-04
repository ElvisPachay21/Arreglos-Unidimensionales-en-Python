def main():
    cantidad = int(input("¿Cuántas temperaturas desea ingresar? "))

    temperaturas = []

    for i in range(cantidad):
        temp = float(input(f"Ingrese la temperatura {i+1}: "))
        temperaturas.append(temp)

    media = sum(temperaturas) / len(temperaturas)

    count_superiores_iguales = sum(1 for temp in temperaturas if temp >= media)

    print(f"La media de las temperaturas es: {media:.2f}")
    print(f"Cantidad de temperaturas mayores o iguales a la media: {count_superiores_iguales}")

if __name__ == "__main__":
    main()