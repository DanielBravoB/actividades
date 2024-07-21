# Esta funcion suma dos numeros
def add(x, y):
    return x + y

# Esta funcion resta dos numeros
def subtract(x, y):
    return x - y

# Esta funcion multiplica dos numeros
def multiply(x, y):
    return x * y

# Esta funcion divide dos numeros
def divide(x, y):
    return x / y


print("Seleccione una operacion.")
print("1.Suma")
print("2.Resta")
print("3.Multiplicacion")
print("4.Division")

while True:
    # Tomar la opcion deseada del usuario
    decision = input("Ingrese su opcion deseada(1/2/3/4): ")

    # Se checa si se escogio uno de los numeros presentados
    if decision in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))
        except ValueError:
            print("Valor incorrecto, porfavor introdusca un numero")
            continue

        if decision == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif decision == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif decision == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif decision == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # Checar si el usuario quiere otra operacion
        # se rompe el ciclo si la respuesta es no
        nuevo_calculo = input("Quiere realizar otro calculo? (si/no): ")
        if nuevo_calculo == "no":
          break
    else:
        print("Opcion no valida")