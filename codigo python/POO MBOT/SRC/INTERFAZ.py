from mbot_control import MbotControl
from graficador import Graficador
import tkinter as tk
from tkinter import ttk

# Instanciar los objetos
mbot = MbotControl('COM5')
graficador = Graficador()

def mover_arriba():
    mbot.mover_arriba()
    # Aquí puedes agregar lógica para actualizar los datos de la gráfica si es necesario

def mover_abajo():
    mbot.mover_abajo()
    # Similarmente, actualiza los datos de la gráfica si es necesario

def mover_izquierda():
    mbot.mover_izquierda()
    # Actualiza los datos de la gráfica si es necesario

def mover_derecha():
    mbot.mover_derecha()
    # Actualiza los datos de la gráfica si es necesario

def graficar_movimiento():
    # Aquí debes implementar la lógica para mostrar la gráfica.
    # Por ejemplo, puedes hacer que graficador muestre los datos actuales.
    graficador.mostrar_grafica()

def actualizar_grafica():
    # Esta función debe actualizar la gráfica en tiempo real
    # Asegúrate de que Graficador tenga un método para actualizar los datos y redibujar la gráfica
    graficador.actualizar_grafica()
    ventana.after(1000, actualizar_grafica)  # Re-planificar la actualización

# Configuración de la interfaz de usuario de Tkinter
ventana = tk.Tk()
ventana.title("Movimiento de flechas")
ventana.geometry("400x200")

estilo = ttk.Style()
estilo.configure("TButton", font=("Arial", 12))
estilo.configure("TLabel", font=("Arial", 12))

# Crear botones y asignar las funciones definidas anteriormente
btn_arriba = ttk.Button(ventana, text="↑", command=mover_arriba, width=5)
btn_abajo = ttk.Button(ventana, text="↓", command=mover_abajo, width=5)
btn_izquierda = ttk.Button(ventana, text="←", command=mover_izquierda, width=5)
btn_derecha = ttk.Button(ventana, text="→", command=mover_derecha, width=5)
btn_detener = ttk.Button(ventana, text="Detener y Graficar", command=graficar_movimiento, width=20)

# Organizar los botones en la ventana
btn_arriba.grid(row=0, column=1, pady=10)
btn_abajo.grid(row=2, column=1, pady=10)
btn_izquierda.grid(row=1, column=0, padx=20)
btn_derecha.grid(row=1, column=2, padx=20)
btn_detener.grid(row=1, column=1, pady=10)

# Iniciar la actualización de la gráfica
ventana.after(1000, actualizar_grafica)

# Iniciar el bucle principal de Tkinter
ventana.mainloop()
