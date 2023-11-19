from prettytable import PrettyTable

def f(x):
    return x**3 - 5*x + 2

def g_a(x):
    return round((x**3 + 2) / 5, 4)

def g_a_derivada(x):
    return round((3*x**2) / 5, 4)

def g_b(x):
    return round((5*x - 2)**(1/3), 4)

def g_b_derivada(x):
    return round(1 / (3*((5*x - 2)**(2/3))), 4)

def punto_fijo(x0, g, g_derivada, max_iter, tolerancia):
    tabla = PrettyTable()
    tabla.field_names = ["Iteración", "x", "g(x)", "g'(x)", "Error"]

    iteracion = 0
    error = tolerancia + 1  # Inicializar error para que entre al bucle

    while iteracion < max_iter and error > tolerancia:
        x1 = g(x0)
        error = abs(x1 - x0)

        tabla.add_row([iteracion + 1, round(x0, 4), round(x1, 4), round(g_derivada(x0), 4), round(error, 4)])

        x0 = x1
        iteracion += 1

    print(tabla)

    if error < tolerancia:
        print("Convergencia exitosa.")
    else:
        print("No se logró la convergencia.")
