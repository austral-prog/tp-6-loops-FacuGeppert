# Replace the "ANSWER HERE" for your answer

def flatten(matrix):
    """
    Dada una lista de listas (matriz), retorna una unica lista
    con todos los elementos en orden.

    Ejemplo: flatten([[1, 2], [3, 4], [5, 6]]) -> [1, 2, 3, 4, 5, 6]
    """
    lista = []
    for i, fila in enumerate(matrix):
        for j, valor in enumerate(fila):
            lista.append(matrix[i][j])
    return lista

"""
Otra forma más corta que se me ocurrió para hacer la func flatten():

    def flatten(matrix):
    
    lista = []
    for fila in matrix:
        for valor in fila:
            lista.append(valor)
    return lista
    
Mucho más corta pero dejo la primera que se me ocurrió ya que funciona bien 
"""

def row_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la fila correspondiente.

    Ejemplo: row_sums([[1, 2, 3], [4, 5, 6]]) -> [6, 15]
    """
    lista = []
    for fila in matrix:
        suma = 0
        for valor in fila:
            suma += valor
        lista.append(suma)

    return lista



def col_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la columna correspondiente.
    Se asume que todas las filas tienen la misma longitud.

    Ejemplo: col_sums([[1, 2, 3], [4, 5, 6]]) -> [5, 7, 9]
    """
    resultado = [0] * len(matrix[0])
    for fila in matrix:
        for j, valor in enumerate(fila):
            resultado[j] += valor
    return resultado
