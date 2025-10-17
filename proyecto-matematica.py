import math
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

# --- Funciones de cálculo ---

def calcular_combinaciones():
    try:
        n = int(entry_n.get())
        r = int(entry_r.get())
        if r > n or n < 0 or r < 0:
            messagebox.showerror("Error", "Verifica los valores de n y r (r ≤ n)")
            return
        resultado = math.comb(n, r)
        label_resultado_cr.config(text=f"Combinaciones (C): {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Ingresa valores válidos para n y r")

def calcular_permutaciones():
    try:
        n = int(entry_n.get())
        r = int(entry_r.get())
        if r > n or n < 0 or r < 0:
            messagebox.showerror("Error", "Verifica los valores de n y r (r ≤ n)")
            return
        resultado = math.perm(n, r)
        label_resultado_cr.config(text=f"Permutaciones (P): {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Ingresa valores válidos para n y r")

def calcular_conjuntos(op):
    try:
        A = set(entry_A.get().replace(" ", "").split(","))
        B = set(entry_B.get().replace(" ", "").split(","))
        if op == "union":
            resultado = A | B
            label_resultado_conj.config(text=f"Unión: {resultado}")
        elif op == "interseccion":
            resultado = A & B
            label_resultado_conj.config(text=f"Intersección: {resultado}")
        elif op == "diferencia":
            resultado = A - B
            label_resultado_conj.config(text=f"Diferencia (A - B): {resultado}")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

def calcular_mcd():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        resultado = math.gcd(a, b)
        label_resultado_mcd.config(text=f"MCD: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Ingresa números válidos")

# --- Ventana principal ---

root = ttk.Window(themename="darkly")  # Puedes probar: 'flatly', 'cyborg', 'morph', 'darkly', 'superhero'
root.title("Herramienta Matemática")
root.geometry("500x400")
root.resizable(False, False)

notebook = ttk.Notebook(root, bootstyle="dark")
notebook.pack(expand=True, fill="both", padx=10, pady=10)

# --- Pestaña 1: Combinaciones y Permutaciones ---
frame_cr = ttk.Frame(notebook)
notebook.add(frame_cr, text="Combinaciones / Permutaciones")

ttk.Label(frame_cr, text="Valor de n:", bootstyle="inverse").pack(pady=5)
entry_n = ttk.Entry(frame_cr, width=10)
entry_n.pack()

ttk.Label(frame_cr, text="Valor de r:", bootstyle="inverse").pack(pady=5)
entry_r = ttk.Entry(frame_cr, width=10)
entry_r.pack()

ttk.Button(frame_cr, text="Calcular Combinaciones (C)", bootstyle="info", command=calcular_combinaciones).pack(pady=8)
ttk.Button(frame_cr, text="Calcular Permutaciones (P)", bootstyle="warning", command=calcular_permutaciones).pack(pady=8)

label_resultado_cr = ttk.Label(frame_cr, text="Resultado aparecerá aquí", bootstyle="success")
label_resultado_cr.pack(pady=15)

# --- Pestaña 2: Conjuntos ---
frame_conj = ttk.Frame(notebook)
notebook.add(frame_conj, text="Conjuntos")

ttk.Label(frame_conj, text="Conjunto A (usa comas):", bootstyle="inverse").pack(pady=5)
entry_A = ttk.Entry(frame_conj, width=40)
entry_A.pack()

ttk.Label(frame_conj, text="Conjunto B (usa comas):", bootstyle="inverse").pack(pady=5)
entry_B = ttk.Entry(frame_conj, width=40)
entry_B.pack()

botones_frame = ttk.Frame(frame_conj)
botones_frame.pack(pady=10)
ttk.Button(botones_frame, text="Unión", bootstyle="primary", command=lambda: calcular_conjuntos("union")).grid(row=0, column=0, padx=5)
ttk.Button(botones_frame, text="Intersección", bootstyle="success", command=lambda: calcular_conjuntos("interseccion")).grid(row=0, column=1, padx=5)
ttk.Button(botones_frame, text="Diferencia (A - B)", bootstyle="danger", command=lambda: calcular_conjuntos("diferencia")).grid(row=0, column=2, padx=5)

label_resultado_conj = ttk.Label(frame_conj, text="Resultado aparecerá aquí", bootstyle="success")
label_resultado_conj.pack(pady=15)

# --- Pestaña 3: MCD ---
frame_mcd = ttk.Frame(notebook)
notebook.add(frame_mcd, text="MCD")

ttk.Label(frame_mcd, text="Número a:", bootstyle="inverse").pack(pady=5)
entry_a = ttk.Entry(frame_mcd)
entry_a.pack()

ttk.Label(frame_mcd, text="Número b:", bootstyle="inverse").pack(pady=5)
entry_b = ttk.Entry(frame_mcd)
entry_b.pack()

ttk.Button(frame_mcd, text="Calcular MCD", bootstyle="primary-outline", command=calcular_mcd).pack(pady=10)
label_resultado_mcd = ttk.Label(frame_mcd, text="Resultado aparecerá aquí", bootstyle="success")
label_resultado_mcd.pack(pady=15)

# --- Ejecutar interfaz ---
root.mainloop()

