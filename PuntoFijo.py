#Se hace uso de la libreria Prettytable, la cual nos servira para hacer la tabla
from prettytable import PrettyTable

#Función para encontrar la raíz
def f(x):
    return x**3 - 5*x + 2

#Función g(x) inciso a
def g_a(x):
    return round((x**3 + 2) / 5, 4)

#Derivada de la función del inciso a
def g_a_derivada(x):
    return round((3*x**2) / 5, 4)

#Funcion g(x) inciso b
def g_b(x):
    return round((5*x - 2)**(1/3), 4)

#Derivada de la funcion del inciso b
def g_b_derivada(x):
    return round(1 / (3*((5*x - 2)**(2/3))), 4)

#Se realiza el metodo del Punto Fijo
def punto_fijo(x0, g, g_derivada, num_iter, tolerancia):
    #Se inicializa la tabla para mostrar los resultados
    tabla = PrettyTable()
    #Se definen los nombres de la tabla
    tabla.field_names = ["Iteración", "x", "g(x)", "g'(x)", "Error"]

    #Se inicializan las variables de la iteracion
    iteracion = 0
    #Se inicializa la variable de error
    error = tolerancia + 1 #NOTA, LA TOLERACIA NOS AYUDA A SACAR LA CONVERGENCIA

    #Bucle while que ayuda a realizar las iteraciones
    while iteracion < num_iter and error > tolerancia:
        #Calcula el proxumo punto usando la funcion de iteracion
        x1 = g(x0)
        #Se calcula el error
        error = abs(x1 - x0)

        #Se agrega a la tabla la información resultante
        tabla.add_row([iteracion + 1, round(x0, 4), round(x1, 4), round(g_derivada(x0), 4), round(error, 4)])

        #Se usa x0 con x1 para la siguiente iteracion
        x0 = x1
        iteracion += 1

    #Se imprime el resultado
    print(tabla)

    #Una vez que se imprime la tabla, se define si hay convergencia o no.
    if error < tolerancia:
        print("Convergencia exitosa.")
    else:
        print("No se logró la convergencia.")
