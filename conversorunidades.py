def convertir_longitud(cantidad, unidad_origen, unidad_destino):
    conversiones = {
        'metros': {'pies': cantidad * 3.28084, 'yardas': cantidad * 1.09361, 'millas': cantidad * 0.000621371},
        'pies': {'metros': cantidad / 3.28084, 'yardas': cantidad / 3, 'millas': cantidad / 5280},
        'yardas': {'metros': cantidad / 1.09361, 'pies': cantidad * 3, 'millas': cantidad / 1760},
        'millas': {'metros': cantidad / 0.000621371, 'pies': cantidad * 5280, 'yardas': cantidad * 1760}
    }
    return conversiones[unidad_origen][unidad_destino]

def convertir_masa(cantidad, unidad_origen, unidad_destino):
    conversiones = {
        'kilogramos': {'libras': cantidad * 2.20462, 'onzas': cantidad * 35.274},
        'libras': {'kilogramos': cantidad / 2.20462, 'onzas': cantidad * 16},
        'onzas': {'kilogramos': cantidad / 35.274, 'libras': cantidad / 16}
    }
    return conversiones[unidad_origen][unidad_destino]

def convertir_temperatura(cantidad, unidad_origen, unidad_destino):
    if unidad_origen == 'celsius':
        if unidad_destino == 'fahrenheit':
            return cantidad * 9/5 + 32
        elif unidad_destino == 'kelvin':
            return cantidad + 273.15
    elif unidad_origen == 'fahrenheit':
        if unidad_destino == 'celsius':
            return (cantidad - 32) * 5/9
        elif unidad_destino == 'kelvin':
            return (cantidad - 32) * 5/9 + 273.15
    elif unidad_origen == 'kelvin':
        if unidad_destino == 'celsius':
            return cantidad - 273.15
        elif unidad_destino == 'fahrenheit':
            return (cantidad - 273.15) * 9/5 + 32

def main():
    print("Selecciona el tipo de conversión: ")
    print("1. Longitud")
    print("2. Masa")
    print("3. Temperatura")
    tipo = int(input("Introduce el número correspondiente: "))

    if tipo == 1:
        cantidad = float(input("Introduce la cantidad: "))
        unidad_origen = input("Introduce la unidad de origen (metros, pies, yardas, millas): ").lower()
        unidad_destino = input("Introduce la unidad de destino (metros, pies, yardas, millas): ").lower()
        resultado = convertir_longitud(cantidad, unidad_origen, unidad_destino)
    elif tipo == 2:
        cantidad = float(input("Introduce la cantidad: "))
        unidad_origen = input("Introduce la unidad de origen (kilogramos, libras, onzas): ").lower()
        unidad_destino = input("Introduce la unidad de destino (kilogramos, libras, onzas): ").lower()
        resultado = convertir_masa(cantidad, unidad_origen, unidad_destino)
    elif tipo == 3:
        cantidad = float(input("Introduce la cantidad: "))
        unidad_origen = input("Introduce la unidad de origen (celsius, fahrenheit, kelvin): ").lower()
        unidad_destino = input("Introduce la unidad de destino (celsius, fahrenheit, kelvin): ").lower()
        resultado = convertir_temperatura(cantidad, unidad_origen, unidad_destino)
    else:
        print("Selección no válida.")
        return

    print(f"{cantidad} {unidad_origen} equivalen a {resultado:.2f} {unidad_destino}.")

if __name__ == "__main__":
    main()
