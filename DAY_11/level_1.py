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