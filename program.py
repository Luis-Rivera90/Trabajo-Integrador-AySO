
nombres = []
apellidos = []

print("=== Registro de usuarios ===")


while True:
    nombre = input("Ingrese el nombre: ").strip().capitalize()
    apellido = input("Ingrese el apellido: ").strip().capitalize()

    
    if not nombre.isalpha() or not apellido.isalpha():
        print("Error: solo se permiten letras en el nombre y apellido.")
        continue

    nombres.append(nombre)
    apellidos.append(apellido)

    continuar = input("¿Desea ingresar otro usuario? (s/n): ").lower()
    if continuar != "s":
        break

print("\n=== Lista de usuarios registrados ===")
for i in range(len(nombres)):
    print(f"{i}: {nombres[i]} {apellidos[i]}")


while True:
    indice = input("\nIngrese el número de índice para saludar: ")

    if not indice.isdigit():
        print("Error: Debe ingresar un número entero.")
        continue

    indice = int(indice)

    if 0 <= indice < len(nombres):
        print(f"\n¡Hola {nombres[indice]} {apellidos[indice]}!")
        break
    else:
        print("Error: índice fuera de rango. Intente de nuevo.")

