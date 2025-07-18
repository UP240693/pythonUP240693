#Ejercicios Nivel 1
print("Ejercicios Nivel 1;")
#Ejercicio 1
#Declare a function add_two_numbers. It takes two parameters and it returns a sum.
print('Ejercicio 1:')
def add_two_numbers ():
 num_one = int(input("Escribe el primer numero:"))
 num_two = int(input("Escribe el segundo numero:"))
 return num_one + num_two
print("El resultado de la suma es:", add_two_numbers())






#Ejercicio 2
#Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
print("Ejercicio 2:")
import math
def area_of_circle(radio):
 return math.pi * radio * radio
radio = float(input("Escribe el radio del circulo:"))
area = area_of_circle(radio)
print("El area del circulo es:", area)






#Ejercicio 3
#Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. 
#Check if all the list items are number types. If not do give a reasonable feedback.
# Ejercicio 3
# Escribe una función llamada add_all_nums que tome un número arbitrario de argumentos y sume todos los argumentos.
# Verifica si todos los elementos de la lista son números. Si no, proporciona un mensaje razonable.
print("Ejercicio 3:")

def add_all_nums(*argumentos):
    suma = 0
    for arg in argumentos:
        if isinstance(arg, (int, float)):
            suma += arg
        else:
            return "Error: Todos los argumentos deben ser números"
    return suma  # Este return ahora está correctamente fuera del bucle.

# Ejemplo de uso:
print(add_all_nums(1, 2, 3, 4, 5))  # Resultado esperado: 15
print(add_all_nums(1, 2, "tres", 4, 5))  # Ejemplo de error: mensaje de error.










#Ejercicio 4
#Temperature in °C can be converted to °F using this formula:
#  °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
print("Ejercicio 4:")
def convert_celsius_to_fahrenheit(celsius):
   return(celsius * 9/5) + 32
celsius = float(input("Escribe la temperatura en grados celsius:"))
fahrenheit = convert_celsius_to_fahrenheit(celsius)
print("La temperatura en grados fahrenheit es:", fahrenheit)







#Ejercicio 5
#Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
print('Ejercicio 5:')
mes = input("Escribe el mes:").strip().lower()
def check_season(mes):
 
 if mes in ['enero', 'febrero', 'marzo']:
    return 'Primavera'
 elif mes in ['abril', 'mayo', 'junio']:
    return 'Verano'
 elif mes in ['julio', 'agosto', 'septiembre']:
    return 'Otoño'
 elif mes in ['octubre', 'noviembre', 'diciembre']:
    return 'Invierno'
 else:
    return "Mes no válido"
 
print("La estación del año es:", check_season(mes))


 






#Ejercicio 6
#Write a function called calculate_slope which return the slope of a linear equation
print("Ejercicio 6:")
def calculate_slope(x1, y1, x2, y2):
   if x2 - x1 == 0:
      return "Error: division por cero"
   else:
      return (y2 - y1) / (x2 - x1)
x1 = float(input("Escribe el primer valor de x1:"))
y1 = float(input("Escribe el primer valor de y1:"))
x2 = float(input("Escribe el valor de x2:"))
y2= float(input("Escribe el valor de y2:"))
   
slope = calculate_slope(x1, y1, x2, y2)
print("La pendiente de la ecuacion lineal es:", slope)









#Ejercicio 7
#Quadratic equation is calculated as follows: ax² + bx + c = 0.
#Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
print("Ejercicio 7:")

def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No hay soluciones reales"
    elif discriminant == 0:
        x = -b / (2*a)
        return f"Una solución: x = {x}"
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"Dos soluciones: x1 = {x1}, x2 = {x2}"

a = float(input("Escribe el valor de a: "))
b = float(input("Escribe el valor de b: "))
c = float(input("Escribe el valor de c: "))

resultado = solve_quadratic_eqn(a, b, c)
print("El conjunto de soluciones es:", resultado)

      








#Ejercicio 8
#Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
print("Ejercicio 8:")
def print_list(lista):
   for elemento in lista:
      print(elemento)
mi_lista = ["ateez", "bts",  "stray kids", "twice", "nct127"]
print_list(mi_lista)










#Ejercicio 9
#Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
print("Ejercicio 9:")
def reverse_lista(lista):
   lista_invertida = []
   for elemento in lista:
      lista_invertida.insert(0, elemento)
   return lista_invertida

mi_lista = ["ateez", "bts",  "stray kids", "twice", "nct127"]
lista_invertida = reverse_lista(mi_lista)
print("La lista invertida es:", lista_invertida)








#Ejercicio 10
#Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
print("Ejercicio 10:")
def capitalize_lista_items(lista):
   lista_capitalizada = []
   for elemento in lista:
      lista_capitalizada.append(elemento.capitalize())
   return lista_capitalizada
mi_lista = ["ateez", "bts", "stray kids", "twice", "nct127"]
lista_capitalizada = capitalize_lista_items(mi_lista)
print("La lista capitalizada es:", lista_capitalizada)

   
   






#Ejercicio 11
#Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end
print("Ejercicio 11:")
def add_item(lista, item):
   lista.append(item)
   return lista 
mi_lista = [ "ateez","bts", "stray kids", "twice", "nct127"]
item = input("Escribe el item que quieras agregar:")
mi_lista = add_item(mi_lista, item)
print("La lista con el item agregado es:", mi_lista)









#Ejercicio 12
#Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
print("Ejercicio 12:")
def remove_item(mi_lista, item):
   if item in mi_lista:
      mi_lista.remove(item)
   return mi_lista
mi_lista = ["ateez", "bts", "stray kids", "twice", "nct127"]
item = input("Escribe el item que quieras eliminar:")
mi_lista = remove_item(mi_lista, item)
print("La lista con el item eliminado es:", mi_lista)









#Ejercicio 13
#Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
print("Ejercicio 13:")
def sum_of_numbers(numero):
   suma = 0
   for i in range(1, numero + 1):
      suma += i
   return suma
numero = int(input("Escribe el numero:"))       
suma = sum_of_numbers(numero)
print("La suma de los numeros es:", suma)








#Ejercicio 14
#Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
print("Ejercicio 14:")
def sum_of_odds(numero):
    suma = 0
    for i in range(1, numero + 1):
        if i % 2 != 0:
            suma += i
    return suma
numero = int(input("Escribe el número: "))
suma_impares = sum_of_odds(numero)
print("La suma de los números impares es:", suma_impares)









#Ejercicio 15 
#Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
print("Ejercicio 15:")
def sum_of_even(numero):
    suma = 0
    for i in range(1, numero + 1):
        if i % 2 == 0:
            suma += i
    return suma
numero = int(input("Escribe el número: "))
suma_pares = sum_of_even(numero)
print("La suma de los números pares es:", suma_pares)










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







print('Ejercicios de Nivel 3:')
#Ejercicios de Nivel 3:
#Ejercicio 1
#Write a function called is_prime, which checks if a number is prime.
print('Ejercicio 1:')
def is_prime(numero):
   if numero in (0,1):
      return False
   for i in range(2, int(numero**0.5) + 1):
      if numero % i == 0:
         return False
      return True 
   numero = int(input("Escribe un numero:"))
if is_prime(numero):
        print(f"{numero} es un número primo.")
else :
    print(f"{numero} no es un número primo.")







#Ejercicio 2
#Write a function which checks if all items are unique in the list.
print('Ejercicio 2:')
def check_unique_items(lista):
    return len(lista) == len(set(lista))
    
mi_lista = [1, 2, 3, 4, 5]
if check_unique_items(mi_lista):
        print("Todos los elementos son únicos.")
else:
        print("Hay elementos repetidos en la lista.")









#Ejercicio 3
#Write a function which checks if all items are of the same data type.
print('Ejercicio 3:')
def check_same_data_type(lista):
    if len(lista) == 0:
        return True
    tipo = type(lista[0])
    for elemento in lista:
        if type(elemento) != tipo:
            return False
    return True
mi_lista = [1, 2, 3, 4, 5]
if check_same_data_type(mi_lista):
        print("Todos los elementos son del mismo tipo de dato.")
else:
        print("Los elementos no son del mismo tipo de dato.")







#Ejercicio 4
#Write a function which check if provided variable is a valid python variable
print('Ejercicio 4:')
def is_valid_variable(variable):
    import re
    return bool(re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', variable))
variable = input("Escribe una variable:")
if is_valid_variable(variable):
        print(f"{variable} es una variable válida.")
else:
        print(f"{variable} no es una variable válida.")















#Ejercicio 5
#Go to the data folder and access the countries-data.py file.
print('Ejercicio 5:')
import countries_data as datac
data = datac.paises




#Ejercicio 5.1
#Create a function called the most_spoken_languages in the world. 
#It should return 10 or 20 most spoken languages in the world in descending order
print("Ejercicio 5.1:")
from collections import Counter
def mostSpokenLanguages (dict):
     allLanguages = [lang for country in dict for lang in country['languages']] 
     cout = Counter(allLanguages)
     top10 = cout.most_common(10)
     return top10
print("Los 10 idiomas más hablados son:" , mostSpokenLanguages(data))












#Ejerciico 5.2
#Create a function called the most_populated_countries. 
#It should return 10 or 20 most populated countries in descending order.
print("Ejercicio 5.2:")

def mostPopulatedCountries (dict):
     most_populated = []
     top_10Countries = sorted(dict, key=lambda x: x["population"], reverse=True)[:10]
     print('Los 10 países más poblados son:')
     for country in top_10Countries:
         most_populated.append(f"{country['name']} - {country['population']}")
     return most_populated
print(mostPopulatedCountries(data))

print("revisado")













    















   
