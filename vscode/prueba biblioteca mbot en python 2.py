from mbot import Mbot
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Crear una instancia de mBot
mbot = Mbot()

# Datos de movimiento recopilados
tiempos = []
posiciones = []

# Configuración de la figura para la gráfica en tiempo real
fig, ax = plt.subplots()
line, = ax.plot(tiempos, posiciones, marker='o')
ax.set_title('Gráfica de Posición vs. Tiempo')
ax.set_xlabel('Tiempo')
ax.set_ylabel('Posición')
ax.grid(True)

def mover_arriba():
    mbot.forward(b'w')
    print("Arriba")

def mover_abajo():
    mbot.backward(b's')
    print("Abajo")

def mover_izquierda():
    mbot.turn_left(b's')
    print("Izquierda")

def mover_derecha():
    mbot.turn_right(b'd')
    print("Derecha")

def detener():
    mbot.stop(b'f')
    print("Detener")

def actualizar_grafica():
    line.set_xdata(tiempos)
    line.set_ydata(posiciones)
    ax.relim()
    ax.autoscale_view()
    fig.canvas.flush_events()

def graficar_movimiento():
    ventana_grafica = tk.Toplevel()
    ventana_grafica.title("Gráfica de Movimiento")

    canvas = FigureCanvasTkAgg(fig, master=ventana_grafica)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Resto del código sin cambios

ventana = tk.Tk()
ventana.title("Movimiento de flechas")
ventana.geometry("400x200")

# Resto del código sin cambios

ventana.mainloop()
