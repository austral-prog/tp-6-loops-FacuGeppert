# Replace the "ANSWER HERE" for your answer

def sum_to_n(n):
    numero = 0

    if n <= 0:

        return 0

    else:

        for n in range(1, n + 1):
            numero += n

    return numero


def sum_evens(n):
    suma = 0
    if n <= 0:
        return 0

    for numero in range(1, n + 1):

            if numero % 2 == 0:
                suma += numero

    return suma


def factorial(n):
    """
    Retorna el factorial de n (n!).
    Si n <= 0, retorna 1.

    Ejemplo: factorial(5) -> 120  (1*2*3*4*5)
    """
    factorial = 1
    if n <= 0:
        return 1
    else:
        for numero in range(1, n + 1):
            factorial *= numero
    return factorial  # Remove this line and implement