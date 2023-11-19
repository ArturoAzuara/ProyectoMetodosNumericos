import math

def funcion(x):
    return math.log(x) - math.cos(2 * x)

def derivada(x):
    return 1 / x + 2 * math.sin(2 * x)

def newton_raphson(x0, tolerancia=1e-4, max_iter=100):
    iteracion = 1
    error = float('inf')

    print(f"Iteración\tRaíz Aproximada\tError")

    while error > tolerancia and iteracion <= max_iter:
        x1 = x0 - funcion(x0) / derivada(x0)
        error = abs(x1 - x0) / abs(x1)

        if iteracion == 1:
            print(f"{iteracion}\t\t{round(x1, 4)}\t\t")
        else:
            # Mostrar el error con 4 decimales
            print(
                f"{iteracion}\t\t{round(x1, 4)}\t\t{0.0 if math.isclose(error, 0, abs_tol=1e-15) else '{:.4f}'.format(error)}")

        x0 = x1
        iteracion += 1

    if error <= tolerancia:
        print(f"\nLa raíz aproximada es: {round(x1, 4)} con {iteracion - 1} iteraciones.")
    else:
        print("El método de Newton-Raphson no convergió después de", max_iter, "iteraciones.")
