import math
# Se escribe la funcion a la cual queremos averiguar la raíz
def funcion(x):
    return math.cos(x) + 2*x - 3

#Se define la funcion bisección con los parametros a y b, que serviran para nuestro rango
#Y num_iter que nos ayudara para definir el numero de iteraciones
def biseccion(a, b,num_iter):
    #Verifica el cambio de signo de la funcion, de no cumplirlo regresa un null
    if funcion(a) * funcion(b) >= 0:
        print("La función no cumple con el requisito de cambio de signo en el intervalo.")
        return None
    #Variable que inicializa la iteración
    iteracion = 1

    while iteracion <= num_iter:
        #Operación que realiza la división de los intervalos
        c = (a + b) / 2
        #verifica que el punto medio sea una raiz exacta
        if funcion(c) == 0:
            break
        #Realiza la función de encontrar el valor negativo y positivo de los intervalos
        elif funcion(c) * funcion(a) < 0:
            b = c
        else:
            a = c
        #Calcula el Error de la iteracion
        if iteracion > 1:
            error_relativo = abs((c - anterior) / c)
            print(f"Iteración {iteracion}: Raíz = {c}, Error = {round(error_relativo, 4)}")
        else:
            print(f"Iteración {iteracion}: Raíz = {c}")
        #Almacena el valor anterior para las iteraciones posteriores
        anterior = c
        iteracion += 1
    #Regresa la raíz, pero se redondea para que salga un valor más preciso
    return round(c, 6)

