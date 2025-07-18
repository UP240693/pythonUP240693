
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

   