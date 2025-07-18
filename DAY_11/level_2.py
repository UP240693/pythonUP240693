print("Ejercicios de NIvel 2:")
#Ejercicios de Nivel 2:

#Ejercicio 1
#Declare a function named evens_and_odds . 
#It takes a positive integer as parameter and it counts number of evens and odds in the number.
print("Ejercicio 1:")
def evens_and_odds(numero):
    pares = 0
    impares = 0
    for i in range(1, numero + 1):
        if i % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares
numero = int(input("Escribe un número positivo: "))
pares, impares = evens_and_odds(numero)
print(f"El número de pares es: {pares}")
print(f"El número de impares es: {impares}")


#Ejercicio 1.1
#Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
print('Ejercicio 1.1:')
def factorial(numero):
    if numero < 0:
        return "Error: El factorial no está definido para números negativos."
    elif numero == 0 or numero == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, numero + 1):
            resultado *= i
        return resultado
numero = int(input("Escribe un número entero: "))
print(f"El factorial de {numero} es: {factorial(numero)}")


#Ejercicio 1.2
#Call your function is_empty, it takes a parameter and it checks if it is empty or not
print("Ejercicio 1.2:")
def is_empty(param):
    return not bool(param)

# Ejemplo de uso:
param = input("Escribe algo (o deja vacío): ")
if is_empty(param):
    print("El parámetro está vacío.")
else:
    print("El parámetro no está vacío.")



#Ejercicio 1.3
#Write different functions which take lists. 
#They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
print('Ejercicio 1.3:')
def calculate_mean(lista):
    return sum(lista) / len(lista)
def calculate_median(lista):
    lista.sort()
    n = len(lista)
    if n % 2 == 0:
        return (lista[n//2 - 1] + lista[n//2]) / 2
    else:
        return lista[n//2]
def calculate_mode(lista):
    from collections import Counter
    contador = Counter(lista)
    max_count = max(contador.values())
    modes = [num for num, count in contador.items() if count == max_count]
    return modes if len(modes) > 1 else modes[0]
def calculate_range(lista):
    return max(lista) - min(lista)
def calculate_variance(lista):
    mean = calculate_mean(lista)
    return sum((x - mean) ** 2 for x in lista) / len(lista)
def calculate_std(lista):
    return calculate_variance(lista) ** 0.5
data = [1,2,3,4,5,6,7,8,9,10]
mean = calculate_mean(data)
median = calculate_median(data)
mode = calculate_mode(data)
range_value = calculate_range(data)
variance = calculate_variance(data)
std_dev = calculate_std(data)
print("Media:", mean)
print("Mediana:", median)
print("Moda:", mode)
print("Rango:", range_value)
print("Varianza:", variance)
print("Desviación estándar:", std_dev)