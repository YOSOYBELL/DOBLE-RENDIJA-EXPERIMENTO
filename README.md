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

![WhatsApp Image 2024-09-25 at 21 03 29_53bb7def](https://github.com/user-attachments/assets/f3034b73-9734-4220-8eea-69f9a0c58360)



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

nos entregará lo siguiente

![image](https://github.com/user-attachments/assets/6c9732b3-72ba-4dfb-aec5-e7318cefc2c5)


![image](https://github.com/user-attachments/assets/f820f4ba-21e7-4edc-8809-350933fa3abb)


