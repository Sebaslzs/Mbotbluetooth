import tkinter as tk
from tkinter import ttk
import serial
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

puerto = serial.Serial('COM5', 9600)

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
    puerto.write(b'w')
    print("Arriba")

def mover_abajo():
    puerto.write(b's')
    print("Abajo")

def mover_izquierda():
    puerto.write(b'd')
    print("Izquierda")

def mover_derecha():
    puerto.write(b'a')
    print("Derecha")

def detener():
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
btn_detener = ttk.Button(ventana, text="Detener y Graficar", command=graficar_movimiento, width=20)

btn_arriba.grid(row=0, column=1, pady=10)
btn_abajo.grid(row=2, column=1, pady=10)
btn_izquierda.grid(row=1, column=0, padx=20)
btn_derecha.grid(row=1, column=2, padx=20)
btn_detener.grid(row=1, column=1, pady=10)

ventana.after(1000, actualizar_grafica)  # Actualizar cada 1000 ms (1 segundo)
ventana.mainloop()