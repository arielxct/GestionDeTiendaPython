import time
# ----------------------------------------
# Importo Libreria Colorama
from colorama import init, Fore, Back

# Inicializar colorama
init()

caracter1 = chr(0x2591)
caracter2 = chr(0x2592)

# ------------------------------------------------------------
print(Back.YELLOW+Fore.BLUE+"╔══════════════════════════════════════════╗"+Fore.RESET+Back.RESET)
print(Back.YELLOW+Fore.BLUE+"║                                          ║"+Fore.RESET+Back.RESET)
print(Back.YELLOW+Fore.BLUE+"║          BIENVENIDO A SISTEMA            ║"+Fore.RESET+Back.RESET)
print(Back.YELLOW+Fore.BLUE+"║                  TIENDA                  ║"+Fore.RESET+Back.RESET)
print(Back.YELLOW+Fore.BLUE+"║                                          ║"+Fore.RESET+Back.RESET)
print(Back.YELLOW+Fore.BLUE+"║      Copyrigth ® Ariel Campos Tula       ║"+Fore.RESET+Back.RESET)
print(Back.YELLOW+Fore.BLUE+"║      email:   campostula@gmail.com       ║"+Fore.RESET+Back.RESET)
print(Back.YELLOW+Fore.BLUE+"║                                          ║"+Fore.RESET+Back.RESET)
print(Back.YELLOW+Fore.BLUE+"╚══════════════════════════════════════════╝"+Fore.RESET+Back.RESET)    
    
time.sleep(3)  # Retrasa la ejecución durante 3 segundos
# ----------------------------------------------------------

# Lista principal que contendrá sublistas: [nombre, categoría, precio]
productos = []

while True:
    # ---------------------------------------------------------------
    print("")
    print(caracter1*56)
        
    print(caracter1,"____________________________________________________",caracter1)
    print(caracter1,Fore.RED + "      *** MENU PRINCIPAL DE LA TIENDA ***           " + Fore.RESET, caracter1)
    print(caracter1,"____________________________________________________",caracter1)
    print(caracter1,Fore.BLUE+"1"+Fore.GREEN +" - Agregar Producto:                               "+ Fore.RESET,caracter1)
    print(caracter1,Fore.BLUE+"2"+Fore.GREEN +" - Visualizar productos                            "+ Fore.RESET,caracter1)
    print(caracter1,Fore.BLUE+"3"+Fore.GREEN +" - Buscar productos por nombre                     "+ Fore.RESET,caracter1)
    print(caracter1,Fore.BLUE+"4"+Fore.GREEN +" - Eliminar productos                              "+ Fore.RESET,caracter1)
    print(caracter1,Fore.BLUE+"5"+Fore.GREEN +" - Salir                                           "+ Fore.RESET,caracter1)
    print(caracter1,"                                                    ",caracter1)
    print(caracter1*56)
        
    opcion = input(Fore.LIGHTGREEN_EX+"Ingrese un numero del 1 al 5: "+Fore.RESET).strip()
    # ----------------------------------------------------------------

    if opcion == "1":
        print("")
        print(caracter1*56)
        print("\n--- AGREGAR NUEVO PRODUCTO ---")
        print("")
        print(caracter1*56)
        
        # Validación del nombre
        while True:
            nombre = input("Ingrese el nombre del producto: ").strip().capitalize()
            if nombre:
                break
            print("Error: El nombre no puede estar vacío.")

        # Validación de la categoría (solo letras y espacios)
        while True:
            categoria = input("Ingrese la categoría del producto: ").strip().capitalize()
            if categoria and categoria.replace(" ", "").isalpha():
                break
            print("Error: La categoría solo debe contener letras (sin números ni símbolos).")

        # Validación del precio usando .isdigit() 
        while True:
            precio_str = input("Ingrese el precio del producto (sin centavos): ").strip()
            if precio_str.isdigit():
                precio = int(precio_str)
                if precio > 0:
                    break
                else:
                    print("Error: El precio debe ser mayor a 0.")
            else:
                print("Error: Por favor, ingrese un número entero válido.")

        # Almacenar como sublista
        productos.append([nombre, categoria, precio])
        print("")
        print(f"¡Éxito! El producto '{nombre}' ha sido agregado correctamente.")
        print("")

    elif opcion == "2":
        print("")
        print(caracter1*70)
        print(Fore.CYAN + "                    --- LISTA DE PRODUCTOS ---" + Fore.RESET)
        print("")
        print(caracter1*70)
        
        if not productos:
            print("\nNo hay productos registrados actualmente.\n")
        else:
            # Cabecera de la tabla con colores y anchos definidos
            print(f"\n{Fore.YELLOW}{'N°':<4} | {'NOMBRE':<15} | {'CATEGORÍA':<12} | {'PRECIO':<8}{Fore.RESET}")
            print(caracter1 * 70)
            
            # Filas de productos alineadas
            for i, prod in enumerate(productos, start=1):
                nombre = prod[0]
                categoria = prod[1]
                precio = prod[2]
                print(f"{i:<4} | {nombre:<25} | {categoria:<20} | ${precio:<7}")
                
        print("")
        print(caracter1*70)

    elif opcion == "3":
        print("")
        print(caracter1*56)
        print("\n--- BUSCAR PRODUCTO ---")
        print("")
        print(caracter1*56)        
        
        if not productos:
            print("No hay productos registrados para buscar.")
        else:
            busqueda = input("Ingrese el nombre (o parte del nombre) a buscar: ").strip().lower()
            encontrados = False

            print("\nResultados de la búsqueda:")
            for i, prod in enumerate(productos, start=1):
                if busqueda in prod[0].lower():
                    print(f">>>> [{i}] Nombre: {prod[0]} | Categoría: {prod[1]} | Precio: ${prod[2]}  <<<<")
                    encontrados = True

            if not encontrados:
                print("No se encontraron resultados para esa búsqueda.")

    elif opcion == "4":
        print("")
        print(caracter1*56)
        print("\n--- ELIMINAR PRODUCTO ---")
        print("")
        print(caracter1*56)        
        
        if not productos:
            print("No hay productos registrados para eliminar.")
        else:
            print("Productos actuales:")
            for i, prod in enumerate(productos, start=1):
                print(f"{i}. {prod[0]} (${prod[2]})")

            # Validación de la posición a eliminar usando .isdigit()
            while True:
                posicion_str = input("Ingrese el número de la posición del producto a eliminar: ").strip()
                if posicion_str.isdigit():
                    posicion = int(posicion_str)
                    if 1 <= posicion <= len(productos):
                        eliminado = productos.pop(posicion - 1)
                        print(f"¡Producto '{eliminado[0]}' eliminado con éxito!")
                        break
                    else:
                        print(caracter1*70)
                        print(f"Error: Por favor, ingrese un número entre 1 y {len(productos)}.")
                        print(caracter1*70)
                else:
                    print(caracter1*56)
                    print("Error: Ingrese un número entero válido.")
                    print(caracter1*56)

    elif opcion == "5":
        print("")
        print(caracter1*70)
        print("\n--- Saliendo del programa de gestión de la tienda. ---")
        print("")
        print(caracter1*70)
        
        print("")
        print("Saliendo del sistema...")
        
        print(Back.BLUE+Fore.RED+"┌──────────────────────────────────────────┐"+Fore.RESET+Back.RESET)
        print(Back.BLUE+Fore.RED+"│                                          │"+Fore.RESET+Back.RESET)
        print(Back.BLUE+Fore.RED+"│    GRACIAS POR USAR SISTEMA TIENDA       │"+Fore.RESET+Back.RESET)
        print(Back.BLUE+Fore.RED+"│                                          │"+Fore.RESET+Back.RESET)
        print(Back.BLUE+Fore.RED+"│      Copyrigth ® Ariel Campos Tula       │"+Fore.RESET+Back.RESET)
        print(Back.BLUE+Fore.RED+"│      email:   campostula@gmail.com       │"+Fore.RESET+Back.RESET)
        print(Back.BLUE+Fore.RED+"│                                          │"+Fore.RESET+Back.RESET)
        print(Back.BLUE+Fore.RED+"└──────────────────────────────────────────┘"+Back.RESET+Back.RESET)
        break
       
    else:
        print("")
        print(caracter1*70)
        print("\n--- Opcion no valida. Por favor, elija una opción del 1 al 5. ---")
        print("")
        print(caracter1*70)