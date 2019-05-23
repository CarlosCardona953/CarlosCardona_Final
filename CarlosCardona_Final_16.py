import numpy as np

x1=4
y1=100
x2=10
y2=2
x3=12
y3=80
x4=80
y4=50
x5=50
y5=50
x6=40
y6=200

v=0.00001
dv=0.1

xx=np.random.random()
yy=np.random.random()

for i in range (10**6):
    
    #La idea es bucar que el tiempo desde una posición aleatoria x y   hasta la ubicación del barco,
    #a una velocidad que se va a ir cambiado,  coincidan con los valores dados inicialmente.

    for j in range (10**6):

  #Aquí se va variando la velocidad del sonido en pequeños pasos de buscando que pueda solucionar la ecuación y calcular el error
# si el error es aceptable entonces deja ese valor y lo guarda en un array.

#Finalmente promedia las velocidades que se encontraron  y se recalcula la posición real del barco.