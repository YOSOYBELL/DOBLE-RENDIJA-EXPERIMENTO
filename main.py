import Libreria as lc    #Importamos la librería hecha previamente
import math
import matplotlib.pyplot as plt
from sys import stdin

#TERCER EXPERIMENTO
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

#4 Funcion graficas
def graficas(posicion, v):
    plt.bar(posicion, v, facecolor = "lime")
    plt.title("Gráfica de Probabilidades Finales")
    plt.xlabel("Posiciones")
    plt.ylabel("Probabilidad")
    plt.show()
    plt.savefig('Probabilidades.png')

#PRUEBAS

def main():
    matriz_1 = stdin.readline()
    v_inicial = stdin.readline()
    matriz_2 = stdin.readline()
    v_inicial2 = stdin.readline()
    matriz3 = stdin.readline()
    v_inicial3 = stdin.readline()
    exp_3(matriz3, v_inicial3)

main()