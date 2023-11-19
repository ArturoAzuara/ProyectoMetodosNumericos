"""
Universidad Nacional Autónoma de México
Facultad de Estudios Superiores Aragón
    Proyecto de Métodos numericos
        Métodos iterativos
        1) Método de Bisección
        2) Método de punto fijo
        3) Método de Newton - Raphson
        Integrantes:
        Azuara Ocotitla Arturo Ivan
        Monroy Quintero Eliezer Isaí
        Profesor:
        Ing.Rafael González Betancourt
        """
#Se importan los metodos programados en los otros archivos .py, todos se mandan a llamar de forma local.
import Biseccion
import PuntoFijo
import NR
def menu():
    #Se usa un ciclo while true para el menu, no se detiene hasta que el usuario lo indique
    while True:
        print("""
    Menú de Métodos Iterativos
    1) Método de Bisección
    2) Método de punto fijo
    3) Método de Newton - Raphson
    4) Salir
    """)
        #Se utiliza excepciones para evitar generar errores en el programa, principalmente con los signos .-/* y letras.
        try:
            opcion = int(input("Introduce una opcion: "))
            if opcion == 1:
                biseccion_option()
            elif opcion == 2:
                puntofijo_option()
            elif opcion == 3:
                Nr_option()
            elif opcion == 4:
                print("Gracias por probar la aplicación, vuelve pronto")
                break
            else:
                print("Error, solo hay 4 opciones, intenta de nuevo")
        except ValueError:
            print("Error, solo acepta valores numericos, intenta de nuevo")
def biseccion_option():
    while True:
        print("")
        message = str(input('Presiona "Y" si quieres resolver f(x) = cos(x) + 2x - 3,\n'
                             ' con el intervalo [1,2], hasta la 6ta iteración,\n'
                             'presiona "N", si quieres regresar al menú principal: ')).lower()
        print("")
        if message == "y":
            #Se coloca el intervalo en a y b.
            a = 1
            b = 2
            #Se define el numero de iteraciones
            num_iter = 6
            #metodo para allar la raíz
            raiz = Biseccion.biseccion(a, b, num_iter)
            #Imprime la raíz aproximada
            print(f"\nLa raíz aproximada es: {raiz}")
            print("")
            print("Excelente, haz probado el metodo de bisección, ¿Por que no pruebas con otro?")
            break
        elif message == "n":
            menu()
        else:
            print("")
            print("La instrucción que mandaste no fue la correcta, intenta de nuevo con las que se muestran en pantalla.")
            print("")
def puntofijo_option():
    while True:
        print("")
        message = str(input('Presiona "Y" si quieres resolver f(x) = x^3 - 5x + 2,\n'
                             'utilizando la opcion a y b, a) g(x) = x^3 + 2 / 5 y b) g(x) ∛ 5x - 2,\n'
                             'sabiendo que x0 = 1, hasta la 6ta iteración'
                             'presiona "N", si quieres regresar al menú principal: ')).lower()
        print("")
        if message == "y":
            #condiciones iniciales
            x0 = 1
            max_iter = 6
            tolerancia = 1e-5

            #inciso a
            print("\nOpción a:")
            # Se importan los metodos de forma local, algo similar al metodo set de java
            PuntoFijo.punto_fijo(x0, PuntoFijo.g_a, PuntoFijo.g_a_derivada, max_iter, tolerancia)

            #Inciso b
            print("\nOpción b:")
            #Se importan los metodos de forma local, algo similar al metodo set de java
            PuntoFijo.punto_fijo(x0, PuntoFijo.g_b, PuntoFijo.g_b_derivada, max_iter, tolerancia)
            print("")
            print("Excelente, haz probado el metodo de Punto Fijo, ¿Por que no pruebas con otro?")
            break
        elif message == "n":
            menu()
        else:
            print("")
            print("La instrucción que mandaste no fue la correcta, intenta de nuevo con las que se muestran en pantalla.")
            print("")
def Nr_option():
    while True:
        print("")
        message = str(input('Presiona "Y" si quieres encontrar la raíz de la funcion f(x) = ln(x) - cos(2x),\n'
                             'Sabiendo que x0 = 1, hasta que el error sea cero, tomando en cuenta 4 decimales: ')).lower()
        print("")
        if message == "y":
            #punto de inicio
            x0 = 1

            #llamada a la función
            NR.newton_raphson(x0)
            print("")
            print("Excelente, haz probado todos los metodos.")
            break
        elif message == "n":
            menu()
        else:
            print("")
            print("La instrucción que mandaste no fue la correcta, intenta de nuevo con las que se muestran en pantalla.")
            print("")

menu()
