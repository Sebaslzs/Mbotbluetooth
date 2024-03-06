import tkinter as tk
from tkinter import ttk
import serial

puerto = serial.Serial('COM4',9600)

def mover_arriba():
    puerto.write(b'w')
    print("Arriba")

def mover_abajo():
    puerto.write(b's')
    print("Arriba")

def mover_izquierda():
    puerto.write(b'd')
    print("Izquierda")

def mover_derecha():
    puerto.write(b'a')
    print("Derecha")

def detener():
    print("Detener")



ventana = tk.Tk()
ventana.title("Movimiento de flechas")
ventana.geometry("400x200")

estilo = ttk.Style()
estilo.configure("TButton", font=("Arial", 12))
estilo.configure("TLabel", font=("Arial", 12))

btn_arriba = ttk.Button(ventana, text="↑", command=mover_arriba, width=5)
btn_abajo = ttk.Button(ventana, text="↓", command=mover_abajo, width=5)
btn_izquierda = ttk.Button(ventana, text="←", command=mover_izquierda, width=5)
btn_derecha = ttk.Button(ventana, text="→", command=mover_derecha, width=5)
btn_detener = ttk.Button(ventana, text="Detener", command=detener, width=10)



btn_arriba.grid(row=0, column=1, pady=10)
btn_abajo.grid(row=2, column=1, pady=10)
btn_izquierda.grid(row=1, column=0, padx=20)
btn_derecha.grid(row=1, column=2, padx=20)
btn_detener.grid(row=1, column=1, pady=10)



ventana.mainloop()