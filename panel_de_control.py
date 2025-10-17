import tkinter as tk
from tkinter import messagebox
import webbrowser # Módulo clave para abrir URLs

# --- Función para manejar la selección de la asignatura ---
def seleccionar_asignatura(asignatura):
    """
    Abre una URL asociada a la asignatura en el navegador predeterminado.
    """
    
    # Define las URLs específicas para cada asignatura
    urls = {
        "Algoritmos": "https://es.wikipedia.org/wiki/Algoritmo",
        "Álgebra Lineal": "https://es.wikipedia.org/wiki/%C3%81lgebra_lineal",
        "Matemática Discreta": "https://es.wikipedia.org/wiki/Matem%C3%A1tica_discreta"
    }
    
    url_destino = urls.get(asignatura)
    
    if url_destino:
        # Usar webbrowser.open() para abrir la URL
        webbrowser.open(url_destino)
        
        # Mensaje informativo
        messagebox.showinfo(
            "Abriendo Navegador 🌐",
            f"Abriendo la página para '{asignatura}' en tu navegador predeterminado."
        )
    else:
        messagebox.showerror("Error", "URL no definida para esta opción.")


# --- Configuración de la Interfaz Gráfica (GUI) ---

root = tk.Tk()
root.title("Proyectos II Ciclo Sección 'B'")
root.geometry("450x300") 
root.resizable(False, False)

title_label = tk.Label(
    root, 
    text="Proyectos II Ciclo Sección 'B'", 
    font=("Arial", 16, "bold"), 
    pady=15,
    fg="#003366"
)
title_label.pack()

button_frame = tk.Frame(root, padx=20, pady=10)
button_frame.pack(pady=10)

# Botón 1: Algoritmos
btn_algoritmos = tk.Button(
    button_frame, 
    text="1. Algoritmos", 
    command=lambda: seleccionar_asignatura("Algoritmos"), 
    width=30, 
    height=2, 
    bg="#4CAF50", fg="white", font=("Arial", 10, "bold")
)
btn_algoritmos.pack(pady=8)

# Botón 2: Álgebra Lineal
btn_algebra = tk.Button(
    button_frame, 
    text="2. Álgebra Lineal", 
    command=lambda: seleccionar_asignatura("Álgebra Lineal"), 
    width=30, 
    height=2, 
    bg="#FF9800", fg="white", font=("Arial", 10, "bold")
)
btn_algebra.pack(pady=8)

# Botón 3: Matemática Discreta
btn_discreta = tk.Button(
    button_frame, 
    text="3. Matemática Discreta", 
    command=lambda: seleccionar_asignatura("Matemática Discreta"), 
    width=30, 
    height=2, 
    bg="#2196F3", fg="white", font=("Arial", 10, "bold")
)
btn_discreta.pack(pady=8)

# Iniciar el bucle principal
root.mainloop()