from datetime import datetime, date

def calcular_edad(fecha_nacimiento):
    hoy = date.today()
    edad_años = hoy.year - fecha_nacimiento.year
    edad_meses = hoy.month - fecha_nacimiento.month
    edad_dias = hoy.day - fecha_nacimiento.day

    if edad_dias < 0:
        edad_meses -= 1
        edad_dias += (fecha_nacimiento.replace(month=fecha_nacimiento.month+1, day=1) - fecha_nacimiento.replace(day=1)).days

    if edad_meses < 0:
        edad_años -= 1
        edad_meses += 12

    return edad_años, edad_meses, edad_dias

def solicitar_fecha_nacimiento():
    fecha_nacimiento_str = input("Por favor, introduce tu fecha de nacimiento (dd/mm/yyyy) (recuerde usar / entre cada numero)): ")
    fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%d/%m/%Y").date()
    return fecha_nacimiento

def main():
    fecha_nacimiento = solicitar_fecha_nacimiento()
    edad_años, edad_meses, edad_dias = calcular_edad(fecha_nacimiento)
    print(f"Tienes {edad_años} años, {edad_meses} meses y {edad_dias} días.")

if __name__ == "__main__":
    main()
