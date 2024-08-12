#EJERCICIO 5 PARCIAL


def ordenar_arreglo(arr):
    
    #Ordena el arreglo de enteros de menor a mayor utilizando la función sorted().
    #return: Lista de enteros ordenada.
    
    return sorted(arr)

def calcular_mediana(arr):
    
    n = len(arr)  # Se obtiene el número de elementos en el arreglo
    mitad = n // 2  # Se calcula el índice del elemento central

    if n % 2 == 0:
        # Si el número de elementos es par, la mediana es el promedio de los dos números del medio
        mediana = (arr[mitad - 1] + arr[mitad]) / 2
    else:
        # Si el número de elementos es impar, la mediana es el elemento del medio
        mediana = arr[mitad]

    return mediana

def main():
    
    #Función principal donde se define un arreglo de enteros, se ordena y se calcula la mediana.
    #Luego, se muestran los resultados.
    
    # Definición de un arreglo de enteros
    arreglo = [7689, 834, 12, 25, 4]
    
    # Ordenar el arreglo
    arreglo_ordenado = ordenar_arreglo(arreglo)
    
    # Calcular la mediana del arreglo ordenado
    mediana = calcular_mediana(arreglo_ordenado)

    # Imprimir el arreglo ordenado y la mediana
    print(f"Arreglo ordenado: {arreglo_ordenado}")
    print(f"la mediana es: {mediana}")

# Ejecutar la función principal 
if __name__ == "__main__":
    main()
