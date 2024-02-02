# Solicitar al usuario que introduzca un número
n = int(input("Introduce un número: "))

# Definir una función llamada fibonacci que genera la secuencia de Fibonacci hasta el término n
def fibonacci(n):
    # Caso base: si n es 0, devuelve una lista que contiene solo el 0
    if n == 0:
        return [0]
    # Caso base: si n es 1, devuelve una lista que contiene 0 y 1
    elif n == 1:
        return [0, 1]
    else:
        # Si n es mayor que 1, llamamos recursivamente a la función para obtener la lista hasta n-1
        fib_list = fibonacci(n - 1)
        # Agregamos el siguiente término a la lista sumando los dos últimos términos
        fib_list.append(fib_list[-1] + fib_list[-2])
        # Devolvemos la lista actualizada
        return fib_list

# Llamar a la función fibonacci con el número proporcionado por el usuario
resultado = fibonacci(n)

# Imprimir la lista de Fibonacci hasta el término n
print("La lista de Fibonacci hasta el término", n, "es:", resultado)

# Imprimir el resultado final, que es el último elemento de la lista
print("El resultado es:", resultado[-1])
