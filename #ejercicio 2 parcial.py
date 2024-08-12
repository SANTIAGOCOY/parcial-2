
def contar_vocales(cadena):
    vocales = "aeiouAEIOU"
    contador = sum(1 for letra in cadena if letra in vocales)
    return contador >= 2

def analizar_cadenas(cadenas):
    for cadena in cadenas:
        if contar_vocales(cadena):
            print(f"'{cadena}': contiene dos o más vocales.")
        else:
            print(f"'{cadena}': no contiene dos o más vocales.")

def main():
    entrada = input("Ingrese cadenas separadas por comas: ")
    cadenas = [cadena.strip() for cadena in entrada.split(",")]
    analizar_cadenas(cadenas)

if __name__ == "__main__":
    main()
