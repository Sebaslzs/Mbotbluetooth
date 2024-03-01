import tkinter as tk
from tkinter import ttk
import threading
import time
import serial
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Supongamos que MbotControl y Graficador ya están definidos
class MbotControl:
    def __init__(self, puerto='COM5'):
        self.puerto = serial.Serial(puerto, 9600)

    def mover_arriba(self):
        self.puerto.write(b'w')

# Sustituye esta implementación por la real
class Graficador:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set_title('Gráfica de Posición vs. Tiempo')

    def actualizar_grafica(self, nuevo_tiempo, nueva_posicion):
        # Actualizar gráfica aquí
        pass

def tarea_fondo():
    while True:
        print("Tarea en el fondo ejecutándose...")
        time.sleep(2)

def iniciar_tarea_fondo():
    tarea_thread = threading.Thread(target=tarea_fondo)
    tarea_thread.daemon = True
    tarea_thread.start()

def main():
    ventana = tk.Tk()
    ventana.title("Control mBot y Gráfica")
    ventana.geometry("400x200")

    mbot = MbotControl('COM5')
    graficador = Graficador()

    estilo = ttk.Style()
    estilo.configure("TButton", font=("Arial", 12))

    btn_tarea_fondo = ttk.Button(ventana, text="Iniciar Tarea de Fondo", command=iniciar_tarea_fondo)
    btn_tarea_fondo.pack(pady=20)

    # Aquí irían más botones y funciones para controlar el mBot y actualizar la gráfica
    # Por ejemplo, para mover el mBot hacia arriba y actualizar una gráfica con datos simulados

    ventana.mainloop()

if __name__ == "__main__":
    main()
