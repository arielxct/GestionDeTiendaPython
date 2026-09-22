# GestionDeTiendaPython
Gestion de una Tienda basica realizada en Python. Se maneja por consola. 2026
# 🛒 Sistema de Gestión de Productos (Tienda)

Programa desarrollado en Python para la gestión y control de inventario de una tienda de forma interactiva desde la terminal.

## 🚀 Características Principales
* **Menú Interactivo:** Navegación intuitiva basada en opciones numéricas del 1 al 5.
* **Estructura de Datos:** Almacenamiento eficiente utilizando listas principales y sublistas (`[nombre, categoría, precio]`).
* **Validación de Entradas:** Control robusto de datos ingresados por el usuario mediante bucles `while` y métodos de cadena (como `.isdigit()` y `.isalpha()`) sin utilizar bloques `try-except` ni funciones (`def`).
* **Búsqueda Flexible:** Permite buscar productos por coincidencia parcial en el nombre.
* **Interfaz Visual:** Uso de la librería `colorama` para ofrecer una estética colorida y organizada en formato tabular.

## 📋 Funcionalidades del Menú
1. **Agregar Producto:** Permite ingresar nombre, categoría (validando solo texto) y precio entero positivo.
2. **Visualizar Productos:** Muestra un listado en formato de tabla ordenada con todos los productos registrados y su numeración.
3. **Buscar Productos:** Filtra y muestra coincidencias por nombre.
4. **Eliminar Productos:** Permite dar de baja un producto indicando su número de posición en la lista.
5. **Salir:** Cierra el sistema con un mensaje de despedida personalizado.

## 🛠️ Requisitos Técnicos y Dependencias
* **Python 3.x**
* Librería **Colorama** para los estilos en la terminal.

Para instalar la dependencia necesaria, puedes ejecutar el siguiente comando en tu terminal:
```bash
pip install colorama
