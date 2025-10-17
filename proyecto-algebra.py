import numpy as np
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import simpledialog, messagebox

# ---------------- FUNCIONES MATEMÁTICAS ---------------- #

def inversa_matriz():
    try:
        n = int(simpledialog.askstring("Tamaño", "Ingrese el tamaño de la matriz (n x n):"))
        matriz = []
        for i in range(n):
            fila = simpledialog.askstring("Fila", f"Ingrese los {n} elementos de la fila {i+1}, separados por espacios:")
            matriz.append(list(map(float, fila.split())))
        matriz = np.array(matriz)
        inv = np.linalg.inv(matriz)
        messagebox.showinfo("Resultado", f"Inversa de la matriz:\n{inv}")
    except np.linalg.LinAlgError:
        messagebox.showerror("Error", "La matriz no tiene inversa (determinante = 0)")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

def multiplicar_matrices():
    try:
        n = int(simpledialog.askstring("Tamaño", "Filas de la primera matriz:"))
        m = int(simpledialog.askstring("Tamaño", "Columnas de la primera matriz:"))
        p = int(simpledialog.askstring("Tamaño", "Columnas de la segunda matriz:"))

        A = []
        B = []

        for i in range(n):
            fila = simpledialog.askstring("Matriz A", f"Fila {i+1} ({m} elementos):")
            A.append(list(map(float, fila.split())))
        for i in range(m):
            fila = simpledialog.askstring("Matriz B", f"Fila {i+1} ({p} elementos):")
            B.append(list(map(float, fila.split())))

        A = np.array(A)
        B = np.array(B)
        C = np.dot(A, B)
        messagebox.showinfo("Resultado", f"Resultado de A x B:\n{C}")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

def resolver_sistema():
    try:
        n = int(simpledialog.askstring("Tamaño", "Ingrese el número de incógnitas (2, 3 o 4):"))
        metodo = simpledialog.askstring("Método", "Elija método: 'gauss' o 'cramer'").lower()
        A = []
        B = []

        for i in range(n):
            fila = simpledialog.askstring("Ecuación", f"Ingrese los {n} coeficientes de la ecuación {i+1}, separados por espacios:")
            A.append(list(map(float, fila.split())))
            b = simpledialog.askstring("Constante", f"Ingrese el valor independiente de la ecuación {i+1}:")
            B.append(float(b))

        A = np.array(A)
        B = np.array(B)

        if metodo == "gauss":
            solucion = np.linalg.solve(A, B)
        elif metodo == "cramer":
            detA = np.linalg.det(A)
            if detA == 0:
                messagebox.showinfo("Resultado", "Sistema sin solución o con infinitas soluciones (det = 0)")
                return
            solucion = []
            for i in range(n):
                Ai = np.copy(A)
                Ai[:, i] = B
                solucion.append(np.linalg.det(Ai) / detA)
        else:
            messagebox.showerror("Error", "Método no válido. Use 'gauss' o 'cramer'.")
            return

        det = np.linalg.det(A)
        if det != 0:
            messagebox.showinfo("Resultado", f"Solución única:\n{solucion}")
        else:
            messagebox.showinfo("Resultado", "El sistema no tiene solución o tiene infinitas soluciones.")
    except np.linalg.LinAlgError:
        messagebox.showinfo("Resultado", "El sistema no tiene solución o tiene infinitas soluciones.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

# ---------------- INTERFAZ MODERNA ---------------- #

root = ttk.Window(themename="darkly")
root.title("Álgebra Lineal - Herramienta Interactiva")
root.geometry("500x360")
root.resizable(False, False)

notebook = ttk.Notebook(root, bootstyle="dark")
notebook.pack(expand=True, fill="both", padx=10, pady=10)

# --- Pestaña: Matrices ---
frame_matriz = ttk.Frame(notebook)
notebook.add(frame_matriz, text="Matrices")

ttk.Label(frame_matriz, text="Operaciones con Matrices", font=("Segoe UI", 14, "bold")).pack(pady=15)

ttk.Button(frame_matriz, text="Inversa de una matriz", bootstyle="info", width=35, command=inversa_matriz).pack(pady=10)
ttk.Button(frame_matriz, text="Multiplicación de matrices", bootstyle="warning", width=35, command=multiplicar_matrices).pack(pady=10)

# --- Pestaña: Sistemas ---
frame_sistema = ttk.Frame(notebook)
notebook.add(frame_sistema, text="Sistemas de Ecuaciones")

ttk.Label(frame_sistema, text="Resolver Sistemas Lineales", font=("Segoe UI", 14, "bold")).pack(pady=15)
ttk.Button(frame_sistema, text="Resolver (Gauss o Cramer)", bootstyle="success", width=35, command=resolver_sistema).pack(pady=15)

# --- Botón de salida ---
ttk.Button(root, text="Salir", bootstyle="danger-outline", command=root.destroy).pack(pady=10)

# --- Ejecutar interfaz ---
root.mainloop()


