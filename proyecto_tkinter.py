import tkinter as tk
from tkinter import messagebox, ttk, simpledialog
import random

# ====== MENÚ PRINCIPAL ======

def lanzar_calculadora_imc():
    ventana_imc = tk.Toplevel()
    ventana_imc.title("Calculadora de IMC")
    ventana_imc.geometry("300x300")
    ventana_imc.config(bg="#1c1c1c")

    def calcular_imc():
        try:
            peso = float(entry_peso.get())
            altura = float(entry_altura.get()) / 100
            imc = peso / (altura ** 2)
            resultado = f"Tu IMC es: {imc:.2f}\n"
            if imc < 18.5:
                resultado += "Estás bajo de peso."
            elif 18.5 <= imc < 24.9:
                resultado += "Peso normal."
            elif 25 <= imc < 29.9:
                resultado += "Sobrepeso."
            else:
                resultado += "Obesidad."
            label_resultado.config(text=resultado)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos.")

    tk.Label(ventana_imc, text="Calculadora de IMC", font=("Arial", 16, "bold"), bg="#1c1c1c", fg="white").pack(pady=10)
    tk.Label(ventana_imc, text="Peso (kg):", bg="#1c1c1c", fg="white").pack()
    entry_peso = tk.Entry(ventana_imc)
    entry_peso.pack()
    tk.Label(ventana_imc, text="Altura (cm):", bg="#1c1c1c", fg="white").pack()
    entry_altura = tk.Entry(ventana_imc)
    entry_altura.pack()
    tk.Button(ventana_imc, text="Calcular IMC", command=calcular_imc).pack(pady=10)
    label_resultado = tk.Label(ventana_imc, text="", bg="#1c1c1c", fg="lightgreen", font=("Arial", 12))
    label_resultado.pack()


def lanzar_pedidos():
    ventana_pedidos = tk.Toplevel()
    ventana_pedidos.title("Sistema de Pedidos")
    ventana_pedidos.geometry("500x500")

    votantes = set()
    comidas = set()
    comida_y_montos = {}

    def registrar_votante():
        nombre = simpledialog.askstring("Registro", "Nombre del votante:")
        if nombre:
            nombre = nombre.strip().lower()
            if nombre in votantes:
                messagebox.showinfo("Info", "Ya estás registrado.")
            else:
                votantes.add(nombre)
                messagebox.showinfo("Registrado", f"{nombre} fue agregado.")

    def agregar_comida():
        comida = simpledialog.askstring("Comida", "Nombre de la comida:")
        if comida:
            comida = comida.strip().lower()
            if comida in comidas:
                messagebox.showwarning("Duplicado", "Comida ya registrada.")
                return
            try:
                precio = float(simpledialog.askstring("Precio", f"Precio de {comida}:"))
                comidas.add(comida)
                comida_y_montos[comida] = precio
                actualizar_lista()
            except:
                messagebox.showerror("Error", "Precio inválido")

    def actualizar_lista():
        text_comidas.delete("1.0", tk.END)
        for c, p in comida_y_montos.items():
            text_comidas.insert(tk.END, f"{c}: ${p:.2f}\n")

    def calcular_total():
        if not votantes:
            messagebox.showwarning("Sin votantes", "No hay votantes registrados.")
            return
        total = sum(comida_y_montos.values())
        por_persona = round(total / len(votantes), 2)
        messagebox.showinfo("Total", f"Total: ${total:.2f}\nCada uno paga: ${por_persona:.2f}")

    tk.Button
