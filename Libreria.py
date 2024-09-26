import numpy as np
import math
import matplotlib.pyplot as plt


#FUNCIONES NECESARIAS PARA HACER LA NUEVA LIBRERÍA

# Suma complejos representados como una tupla (real, imaginaria)
def sumacplx(a,b):
    real = a[0] + b[0]
    img = a[1] + b[1]
    return (real, img)

# Multiplica complejos representados como una tupla
def multcplx(a,b):
    real = (a[0] * b[0]) - (a[1]* b[1])
    img = (a[0] * b[1]) + (b[0]*a[1])
    return (real, img)

#Conjuga números complejos
def concplx (n):
    real = (n[0])
    img = ((n[1])*(-1))
    return (real, img)

#modulo
def modulocplx(a):
    return math.sqrt((a[0])**2 + (a[1])**2)


#SEGUNDA LIBRERÍA


#Adición vectores complejos

def adicionVectrs(v1,v2):
    sumavector = []
    c = 0
    while c < len(v1):
        sumav = sumacplx((v1[c]), (v2[c]))
        sumavector.append(sumav)
        c += 1
    print (sumavector)

#Inverso aditivo Vector

def inversoAditivoVec(v1):
    for i in range(len(v1)):
        for j in range(len(v1[0])):
            v1[i][j] = (v1[i][j][0] * (-1),  v1[i][j][1] * (-1))
    print(v1)

#Multiplicación Escalar

def multiplicacionEscalar(v1, c):
    v = []
    for i in range(len(v1)):
        multi = multcplx(v1[i], c)
        v.append(multi)
    print(v)

#Adición de matrices

def adicionMatrices (m1,m2):
    sumamtrx = []
    c = 0
    while c < len(m1):
        sumaM = sumacplx((m1[c]), (m2[c]))
        sumamtrx.append(sumaM)
        c += 1
    print(sumamtrx)

#Inverso aditivo matrices

def inversoaditivoMtx (m1):
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            m1[i][j] = ((-1) * m1[i][j][0], (-1) * m1[i][j][1])
    print (m1)

#multiplicación escalar de matrices

def multiplicacionEscalarMtrx(m1, v1):
    for i in range(len(m1)):
        for j in range(2):
            mltplxmat = multcplx(m1[i][j], v1)
            m1[i][j] = mltplxmat

    print(m1)

#Traspuesta de una matriz/vector

def traspuesta(m1):
    result = [[0 for i in range(len(m1))] for j in range(len(m1[0]))]

    for i in range(len(m1[0])):
        for j in range(len(m1)):
            result[i][j] = m1[j][i]

    return(result)

#conjugada de una Matriz o un vector

def conjugarMtrx (m1):
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            m1[i][j] = (m1[i][j][0], (-1) * m1[i][j][1])
    return (m1)

#Daga de una Matriz o un vector

def dagaMtrz (m1):
    m = traspuesta(m1)
    n = conjugarMtrx(m)
    return (n)

#Producto de 2 matrices nxn

def multmatrices(A, B):
    f = len(A)
    c = len(A[0])
    m = []
    for i in range(f):
        fila = []
        for j in range(f):
            suma = 0
            for k in range(c):
                suma = suma + A[i][k] * B[k][j]
            fila = fila + [suma]
        m = m + [fila]
    return m

#producto matrices complejas
def productomatricesComplex(A, B):
    filas = len(A)
    columnas = len(A[0])
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(filas):
            suma = (0,0)
            for k in range(columnas):
                suma = sumacplx(suma, multcplx(A[i][k], B[k][j]))
            fila = fila + [(suma)]
        matriz = matriz + [fila]
    return matriz

#Acción de una matriz sobre un vector

def accionmatrizvector(A, v):
    f = len(A)
    c = len(A[0])
    m = []
    for i in range(f):
        suma = 0
        for j in range(c):
            suma = suma + A[i][j] * v[j][0]
        m = m + [suma]
    return m

def accmatriz_vectorcplx(A, v):
    f = len(A)
    c = len(A[0])
    m = []
    for i in range(f):
        suma = (0,0)
        for j in range(c):
            suma = sumacplx(suma, multcplx(A[i][j], v[j][0]))
        m = m + [(suma)]
    return m

#Producto Interno de vectores

def producto_Int(v1, v2):
    Inner_productVec = 0
    for i in range(len(v1)):
        Inner_productVec += (v1[i] * v2[i])
    print(Inner_productVec)

#Norma de un vector

def norma_v(v1):
    norma = np.linalg.norm(v1)
    print (norma)

#Distancia entre dos vectores

def distance_v(v1, v2):
    real = v1[0] - v2[0]
    img = v1[1] - v2[1]
    v = (real, img)
    distance = np.linalg.norm(v)

    print (distance)


#Revisar si una matriz unitaria

def unitaria(m1):
    Trx = traspuesta(m1[:])
    result = Trx == m1
    if result == False:
        return ('No es unitaria')
    else:
        return ('Es unitaria')

#Revisar si una matriz es hermitiana
def hermitiana(m1):
    daga = dagaMtrz(m1[:])
    result = daga == m1
    if result == False:
        return ('No es hermitiana')
    else:
        return ('Es hermitiana')

#Producto Tensor
def productoTrsx(m1,m2):
    s = len(m1[0])*len(m2[0])
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            m1[i][j]=multiplicacionEscalarMtrx(m1[i][j],m2)
    for i in m1:
        return(i)
def n_tics(matriz):
    tics = []
    for i in range(len(matriz)):
        tics = tics + [i]
    return tics

def graficas(posicion, v):
    plt.bar(posicion, v, facecolor = "lime")
    plt.title("Gráfica de Probabilidades Finales")
    plt.xlabel("Posiciones")
    plt.ylabel("Probabilidad")
    plt.show()
    plt.savefig('Probabilidades.png')