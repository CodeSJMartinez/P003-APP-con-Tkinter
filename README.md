Para crear una aplicación en Python con una página de inicio que tenga 4 botones, cada uno de los cuales lleva a una página diferente, puedes utilizar un framework como **Tkinter**. Tkinter es una biblioteca estándar para crear interfaces gráficas de usuario (GUI) en Python. A continuación, te mostraré cómo puedes hacerlo paso a paso.

### Paso 1: Instalar Tkinter (si no lo tienes instalado)
Tkinter viene preinstalado con Python en la mayoría de las distribuciones, pero si no lo tienes, puedes instalarlo usando pip:
```bash
pip install tk
```

### Paso 2: Crear la estructura básica de la aplicación

Vamos a crear una aplicación simple que tiene una página de inicio con 4 botones. Cada botón llevará a una nueva ventana que representará una categoría diferente.

### Código en Python

```python
import tkinter as tk
from tkinter import messagebox

# Función para crear una nueva ventana según la categoría seleccionada
def abrir_categoria(categoria):
    nueva_ventana = tk.Toplevel()
    nueva_ventana.title(f"Categoría: {categoria}")
    tk.Label(nueva_ventana, text=f"Esta es la página de la categoría {categoria}").pack(pady=20)
    tk.Button(nueva_ventana, text="Volver", command=nueva_ventana.destroy).pack(pady=10)

# Función para cerrar la aplicación
def salir_app():
    if messagebox.askokcancel("Salir", "¿Deseas salir de la aplicación?"):
        root.destroy()

# Crear la ventana principal
root = tk.Tk()
root.title("Aplicación con Categorías")

# Crear el título en la página principal
tk.Label(root, text="Bienvenido a la Aplicación", font=("Helvetica", 16)).pack(pady=20)

# Crear los botones para las categorías
categorias = ["Categoría 1", "Categoría 2", "Categoría 3", "Categoría 4"]
for categoria in categorias:
    tk.Button(root, text=categoria, width=20, command=lambda c=categoria: abrir_categoria(c)).pack(pady=10)

# Botón para salir de la aplicación
tk.Button(root, text="Salir", command=salir_app, bg='red', fg='white').pack(pady=20)

# Iniciar el loop principal de la aplicación
root.mainloop()
```

### Explicación del código

1. **Ventana principal**:
   - `root = tk.Tk()` crea la ventana principal de la aplicación.
   - `root.title("Aplicación con Categorías")` define el título de la ventana.
   
2. **Título en la página principal**:
   - `tk.Label(root, text="Bienvenido a la Aplicación", font=("Helvetica", 16)).pack(pady=20)` crea un texto de bienvenida en la ventana principal.

3. **Botones de categorías**:
   - Se crean 4 botones, uno para cada categoría. Cuando se hace clic en un botón, se llama a la función `abrir_categoria(categoria)`, que crea una nueva ventana mostrando el contenido correspondiente.

4. **Función `abrir_categoria`**:
   - Esta función abre una nueva ventana (`Toplevel`) con el título y el contenido correspondientes a la categoría seleccionada.

5. **Función para salir de la aplicación**:
   - `salir_app` muestra un mensaje de confirmación antes de cerrar la aplicación.

6. **Loop principal**:
   - `root.mainloop()` mantiene la aplicación abierta y responde a las interacciones del usuario.

### Personalización

- Puedes personalizar las páginas de cada categoría añadiendo más elementos en la función `abrir_categoria`.
- Si prefieres una navegación más avanzada, puedes explorar el uso de `Frames` en lugar de nuevas ventanas para cada categoría.

Este código es un punto de partida simple. En otro proyecto se puede agregar más complejidad, como conectar a bases de datos, o realizar acciones más avanzadas dentro de cada categoría, podemos ir expandiendo la aplicación según las necesidades.
