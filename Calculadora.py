# Mi primer proyecto con Python
# Autora: Carla González Mina
# Fecha 2024-12-07

# Calculadora de operaciones
import math


# Funcion suma
def suma(num1, num2):
    return num1 + num2


# Función resta
def resta(num1, num2):
    return num1 - num2


# Función multiplicación
def multi(num1, num2):
    return num1 * num2


# Función divis
def div(num1, num2):
    return num1 / num2


# Funcion derivada de una funcion
def derivada(funcion, x):
    h = 0.0000001
    return (funcion(x + h) - funcion(x)) / h


# Funcion factorial
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


# Funcion Potencia
def potencia(num1, num2):
    return num1**num2


# Funcion sacar fi de un número
def fi(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fi(num - 1) + fi(num - 2)


# Funcion para sacar el numero euler
def euler(num):
    if num == 0:
        return 1
    else:
        return 1 / factorial(num) + euler(num - 1)


# Funcion para sacar modulo de un numero
def modulo(num):
    if num < 0:
        return num * -1
    else:
        return num


# Funcion para sacar el logaritmo de un numero
def logaritmo(num):
    return math.log(num)


# Funcion para sacar el seno de un numero
def seno(sum):
    return math.sin(sum)


# Funcion para sacar el coseno de un numero
def coseno(sum):
    return math.cos(sum)


# Funcion para sacar la tangente de un numero
def tangente(sum):
    return math.tan(sum)


# Funcion para sacar la raiz cuadrada de un numero
def raiz(num):
    return math.sqrt(num)


# Funcion para sacar el valor absoluto de un numero
def absoluto(num):
    return abs(num)


# Funcion para sacar el valor de pi
def pi():
    return math.pi


# Funcion para sacar integral indefinida de una funcion
def integral(funcion, a, b):
    h = 0.0000001
    sum = 0
    while a < b:
        sum += funcion(a) * h
        a += h
    return sum


# Funcion para sacar el area bajo la curva
def area(funcion, a, b):
    return integral(funcion, a, b)


# Menu de opciones
def menu():
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Derivada")
    print("6. Factorial")
    print("7. Potencia")
    print("8. Fi")
    print("9. Euler")
    print("10. Modulo")
    print("11. Logaritmo")
    print("12. Seno")
    print("13. Coseno")
    print("14. Tangente")
    print("15. Raiz")
    print("16. Valor absoluto")
    print("17. Pi")
    print("18. Integral")
    print("19. Area")
    print("20. Derivada de una función")
    print("21. Salir")

    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        print("La suma es: ", suma(num1, num2))
    elif opcion == 2:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        print("La resta es: ", resta(num1, num2))
    elif opcion == 3:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        print("La multiplicación es: ", multi(num1, num2))
    elif opcion == 4:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        print("La división es: ", div(num1, num2))
    elif opcion == 5:
        num = int(input("Ingrese el número: "))
        print("La derivada es: ", derivada(lambda x: x**2, num))
    elif opcion == 6:
        num = int(input("Ingrese el número: "))
        print("El factorial es: ", factorial(num))
    elif opcion == 7:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        print("La potencia es: ", potencia(num1, num2))
    elif opcion == 8:
        num = int(input("Ingrese el número: "))
        print("El número fi es: ", fi(num))
    elif opcion == 9:
        num = int(input("Ingrese el número: "))
        print("El número euler es: ", euler(num))
    elif opcion == 10:
        num = int(input("Ingrese el número: "))
        print("El modulo es: ", modulo(num))
    elif opcion == 11:
        num = int(input("Ingrese el número: "))
        print("El logaritmo es: ", logaritmo(num))
    elif opcion == 12:
        num = int(input("Ingrese el número: "))
        print("El seno es: ", seno(num))
    elif opcion == 13:
        num = int(input("Ingrese el número: "))
        print("El coseno es: ", coseno(num))
    elif opcion == 14:
        num = int(input("Ingrese el número: "))
        print("La tangente es: ", tangente(num))
    elif opcion == 15:
        num = int(input("Ingrese el número: "))
        print("La raiz cuadrada es: ", raiz(num))
    elif opcion == 16:
        num = int(input("Ingrese el número: "))
        print("El valor absoluto es: ", absoluto(num))
    elif opcion == 17:
        print("El valor de pi es: ", pi())
    elif opcion == 18:
        a = int(input("Ingrese el número a: "))
        b = int(input("Ingrese el número b: "))
        print("La integral es: ", integral(lambda x: x**2, a, b))
    elif opcion == 19:
        a = int(input("Ingrese el número a: "))
        b = int(input("Ingrese el número b: "))
        print("El área bajo la curva es: ", area(lambda x: x**2, a, b))
    elif opcion == 20:
        print("Ingrese la función a derivar")
        num = int(input("Ingrese el número: "))
        print("La derivada de la función es: ", derivada(lambda x: x**2, num))
    
    elif opcion == 21:
        print("Gracias por usar la calculadora de Carlix")
        exit()

if __name__ == "__main__":
    while True:
        menu()