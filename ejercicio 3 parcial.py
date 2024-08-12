def elementosunicos(lista1, lista2):
    unicoslista1 = []
    unicoslista2 = []

    # Encontrar elementos únicos en lista1
    for elemento in lista1:
        if elemento not in lista2:
            unicoslista1.append(elemento)

    # Encontrar elementos únicos en lista2
    for elemento in lista2:
        if elemento not in lista1:
            unicoslista2.append(elemento)
    
    return unicoslista1, unicoslista2

def main():
    # Solicitar entrada del usuario para las listas
    entrada_lista1 = input("Introduce los elementos de la primera lista separados por comas: ")
    entrada_lista2 = input("Introduce los elementos de la segunda lista separados por comas: ")
    
    # Convertir las entradas en listas
    lista1 = [elemento.strip() for elemento in entrada_lista1.split(',')]
    lista2 = [elemento.strip() for elemento in entrada_lista2.split(',')]
    
    # Obtener las diferencias
    unicoslista1, unicoslista2 = elementosunicos(lista1, lista2)
    
    # Mostrar los resultados
    print("Elementos en la primera lista que no están en la segunda:", unicoslista1)
    print("Elementos en la segunda lista que no están en la primera:", unicoslista2)

if __name__ == "__main__":
    main()
