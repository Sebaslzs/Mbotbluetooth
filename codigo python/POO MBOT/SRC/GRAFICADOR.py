import matplotlib.pyplot as plt

class Graficador:
    def __init__(self):
        self.tiempos = []
        self.posiciones = []
        self.fig, self.ax = plt.subplots()
        self.ax.set_title('Gráfica de Posición vs. Tiempo')
        self.ax.set_xlabel('Tiempo')
        self.ax.set_ylabel('Posición')
        self.line, = self.ax.plot(self.tiempos, self.posiciones, 'o-')  # Inicializa la línea con los datos iniciales vacíos

    def actualizar_grafica(self, nuevo_tiempo, nueva_posicion):
        # Añade los nuevos datos a las listas
        self.tiempos.append(nuevo_tiempo)
        self.posiciones.append(nueva_posicion)
        
        # Actualiza los datos de la línea en la gráfica
        self.line.set_data(self.tiempos, self.posiciones)
        
        # Reajusta los límites de la gráfica para acomodar los nuevos datos
        self.ax.relim()
        self.ax.autoscale_view(True,True,True)
        
        # Refresca la figura
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

# Ejemplo de uso
graficador = Graficador()

# Supongamos que esto se llama cada vez que tienes nuevos datos
graficador.actualizar_grafica(nuevo_tiempo=1, nueva_posicion=5)
graficador.actualizar_grafica(nuevo_tiempo=2, nueva_posicion=3)
graficador.actualizar_grafica(nuevo_tiempo=3, nueva_posicion=8)

plt.show()  # Muestra la ventana de la gráfica (bloqueante)
