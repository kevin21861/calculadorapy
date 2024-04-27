def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "No se puede dividir por cero"
    else:
        return a / b
    


print("Selecciona una opción:")

print("1. Sumar")

print("2. Restar")

print("3. Multiplicar")

print("4. Dividir")

while True:
    try:
       
        opcion = int(input("Elige una opcion: "))
        
        break
    except ValueError:
        print("Error: debes ingresar un número.")

if opcion == 1:
    n1 = float(input("Ingresa el primer número: "))
    n2 = float(input("Ingresa el segundo número: "))
    resultado = sumar(n1, n2)
elif opcion == 2:
    n1 = float(input("Ingresa el primer número: "))
    n2 = float(input("Ingresa el segundo número: "))
    resultado = restar(n1, n2)
elif opcion == 3:
    n1 = float(input("Ingresa el primer número: "))
    n2 = float(input("Ingresa el segundo número: "))
    resultado = multiplicar(n1, n2)
elif opcion == 4:
    n1 = float(input("Ingresa el primer número: "))
    n2 = float(input("Ingresa el segundo número: "))
    resultado = dividir(n1, n2)
else:
    resultado = 'opción invalida'

print("El resultado es: ", resultado)
