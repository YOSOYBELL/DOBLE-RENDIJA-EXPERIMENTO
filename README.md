María Juliana Rodríguez Caicedo, Juan Sebastian Murcia Yanquen, Diego Alejandro Rojas Ramírez

# Experimento Doble Rendija

El patrón de interferencia sucede porque las ondas de luz que pasan por las dos rendijas se combinan. En los puntos donde las ondas están "en fase" (las crestas coinciden), se refuerzan y generan las franjas claras. En los puntos donde están "fuera de fase" (una cresta coincide con un valle), se cancelan, creando las franjas oscuras.

“Este es un experimento realizado a principios del siglo XIX por Thomas Young con el objetivo de apoyar la teoría de que la luz era una onda y rechazar la teoría de que esta estaba formada por partículas.

Young hizo pasar un haz de luz por dos rendijas y vio que sobre una pantalla se producía un patrón de interferencias, una serie de franjas brillantes y oscuras alternadas.

Este resultado es inexplicable si la luz estuviera formada por partículas porque deberían observarse sólo dos franjas de luz frente a las rendijas, pero es fácilmente interpretable asumiendo que la luz es una onda y que sufre interferencias. “ - BBC

# materiales

* Un láser de baja potencia.

* Papel aluminio para crear las dos rendijas.

* Una pantalla (usamos una hoja de papel, pero cualquier superficie blanca funciona).

* Un visturí con buen filo.

* Un marcador negro

# Observaciones

Cuando encendimos el láser y la luz pasó por las rendijas, vimos un patrón de interferencia en la pantalla. Aparecen franjas de luz y sombra alternadas, lo que nos mostró que la luz, a pesar de estar formada por partículas (fotones), también se comporta como una onda. 

# Procedimiento

1. en la pantalla de papel realizar dos rectangulos con un marcador negro

2. Tomar un pedazo de papel aluminio y realizar dos cortes con el visturí, luego posicionarlos en la pantalla de papel en donde estan los rectangulos anterioremente hechos 

3. Con la pantalla lista, posicionarlas mas o menos a 1.8 metros de distancia del lazer

4. finalmente se enciende el lazer apuntando al centro de ambos rectangulos
 
# Fotos del proceso realizado 

![WhatsApp Image 2024-09-25 at 21 03 28_205df279](https://github.com/user-attachments/assets/d60bd2b1-6a7d-4dc4-a755-9d1d327b8614)

![WhatsApp Image 2024-09-25 at 21 03 35_f4e3c0d0](https://github.com/user-attachments/assets/b2b8ae7d-bc23-45cd-a2b6-5b7d6c5b689b)

![image](https://github.com/user-attachments/assets/608ed267-03fd-4780-aa0b-d9da53c88a57)

![image](https://github.com/user-attachments/assets/5698e200-53f0-444e-8446-46d9478faa6e)


# videos del procedimiento

https://youtube.com/shorts/C6QRFFJpKTs?feature=share


# Simulación haciendo uso de la librería

Este experimento puede ser representado como sistemas probabilísticos, y de la misma forma, llevado a nuestra librería de la siguiente forma:

```python
def exp_3(matriz,v_inicial):
    print("Experimento Cuantico con 2 rendijas")
    matriz = [[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
              [(1 / math.sqrt(2), 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
              [(1 / math.sqrt(2), 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
              [(0, 0), (-1 / math.sqrt(6), 1 / math.sqrt(6)), (0, 0), (1, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
              [(0, 0), (-1 / math.sqrt(6), -1 / math.sqrt(6)), (0, 0), (0, 0), (1, 0), (0, 0), (0, 0), (0, 0)],
              [(0, 0), (1 / math.sqrt(6), -1 / math.sqrt(6)), (-1 / math.sqrt(6), 1 / math.sqrt(6)), (0, 0), (0, 0),
               (1, 0), (0, 0), (0, 0)],
              [(0, 0), (0, 0), (-1 / math.sqrt(6), -1 / math.sqrt(6)), (0, 0), (0, 0), (0, 0), (1, 0), (0, 0)],
              [(0, 0), (0, 0), (1 / math.sqrt(6), -1 / math.sqrt(6)), (0, 0), (0, 0), (0, 0), (0, 0), (1, 0)]]
    print("Matriz Asociada: ")

    for i in matriz:
        print(i)
    tics = 3

    X = [x[:] for x in matriz]
    for i in range(2, tics + 1):
        X = lc.productomatricesComplex(X, matriz)
    print("Estado inicial: ")
    v_inicial = [[(1, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)]]

    print("Numero de tics:", tics)
    for i in v_inicial:
        print(i)
    posicion = lc.accmatriz_vectorcplx(X, v_inicial)

    print("Vector Final")
    probabilidades = []
    for i in range(len(posicion)):
        probabilidades += [(lc.modulocplx(posicion[i])) ** 2]
    for i in probabilidades:
        print(i)
    lc.graficas(lc.n_tics(matriz), probabilidades)
```
```python
import numpy as np
import matplotlib.pyplot as plt

wavelength = 500e-9  # Longitud de onda (m)
d = 1e-6  # Distancia entre las dos rendijas (m)
D = 1.0   # Distancia a la pantalla (m)
k = 2 * np.pi / wavelength  # Número de onda
I0 = 1.0  # Intensidad máxima

screen_points = 500  # Número de puntos en la pantalla
screen_width = 0.05  # Ancho de la pantalla (m)
x = np.linspace(-screen_width / 2, screen_width / 2, screen_points)

# Funciones de onda para cada rendija
# Distancia de cada rendija a un punto de la pantalla
r1 = np.sqrt((x + d/2)**2 + D**2)
r2 = np.sqrt((x - d/2)**2 + D**2)

# Función de onda total es la suma de las ondas de ambas rendijas
wave1 = np.exp(1j * k * r1) / r1  # Función de onda de la primera rendija
wave2 = np.exp(1j * k * r2) / r2  # Función de onda de la segunda rendija

# Superposición de las ondas
wave_total = wave1 + wave2

# Intensidad es el cuadrado del módulo de la función de onda total
intensity = I0 * np.abs(wave_total) ** 2

# Normalizar la intensidad
intensity /= np.max(intensity)

# Graficar la distribución de la intensidad
plt.figure(figsize=(10, 6))
plt.bar(x, intensity, width=screen_width / screen_points, color='blue', edgecolor='black')
plt.title("Distribución de Intensidad en el Experimento Cuántico de la Doble Rendija")
plt.xlabel("Posición en la Pantalla (m)")
plt.ylabel("Intensidad (Probabilidad)")
plt.show()



```
nos entregará lo siguiente el primer codigo

![image](https://github.com/user-attachments/assets/6c9732b3-72ba-4dfb-aec5-e7318cefc2c5)


![image](https://github.com/user-attachments/assets/f820f4ba-21e7-4edc-8809-350933fa3abb)

nos entregará lo siguiente el segundo codigo 

![image](https://github.com/user-attachments/assets/ebe8dd9b-be43-4215-9b4d-91c5522d33d9)
