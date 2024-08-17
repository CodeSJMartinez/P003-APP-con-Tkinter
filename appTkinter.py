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
