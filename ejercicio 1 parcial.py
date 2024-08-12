

def tiene_elementos_repetidos(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                return True
    return False

def main():
    # Solicitar al usuario que ingrese los elementos de la lista separados por comas
    entrada = input("Ingresa los elementos de la lista separados por comas: ")
    # Convertir la cadena de entrada en una lista eliminando espacios en blanco alrededor de los elementos
    lista = [elemento.strip() for elemento in entrada.split(",")]
    
    # Verificar si la lista tiene elementos repetidos
    if tiene_elementos_repetidos(lista):
        print("La lista tiene elementos repetidos.")
    else:
        print("La lista no tiene elementos repetidos.")

if __name__ == "__main__":
    main()

    