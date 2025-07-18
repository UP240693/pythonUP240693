print("Ejercicios de nivel 1:")
#Ejercicios Nivel 1:
#Ejercicio 1:
#Iterate 0 to 10 using for loop, do the same using while loop.
print("Ejerciico 1:")
#para
for i in range(11):
    print(i)


#Ejercicio 2
#Iterate 10 to 0 using for loop, do the same using while loop.
print("Ejercicio 2:")
for i in range (10, -1, -1):
    print(i)
i = 10
while i >= 0:
    print(i)
    i -= 1




#Ejercicio 3
#Write a loop that makes seven calls to print(), so we get on the output the following triangle:
print('Ejercicio 3:')
#         
##        
###
####
#####
######
#######

for i in range(8):
    print("#"*i)


#Ejercicio 4
#Use nested loops to create the following:
print('Ejercicio 4:')
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #

for i in range(8):
    for j in range(8):
        print('#', end='')
    print()





#Ejercicio 5
#Print the following pattern:
print("Ejercicio 5:")
# 0 x 0 = 0
#1 x 1 = 1
#2 x 2 = 4
#3 x 3 = 9
#4 x 4 = 16
#5 x 5 = 25
#6 x 6 = 36
#7 x 7 = 49
#8 x 8 = 64
#9 x 9 = 81
#10 x 10 = 100
num = 0
while num < 11:
     print('{} x {} = {}'.format(num, num, num * num))
     num = num + 1








#Ejercicio 6
#Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
print("Ejercicio 6:")
lenguajes_programacion  =['Python', 'Numpy','Pandas','Django', 'Flask']
for lenguajes in lenguajes_programacion :
    print( lenguajes)











#Ejercicio 7
#Use for loop to iterate from 0 to 100 and print only even numbers
print("Ejercicio 7:")
for num in range(0, 101):
    if num % 2 == 0:
        print(num)










#Ejercicio 8
#Use for loop to iterate from 0 to 100 and print only odd numbers
print("Ejercicio 8:")
for num in range(0, 101):
    if num % 2 != 0:
        print(num)











#Ejercicios Nivel 2
print("Ejercicios nivel 2:")

#Ejercicio 1
#Use for loop to iterate from 0 to 100 and print the sum of all numbers.
#The sum of all numbers is 5050.
print("Ejercicio 1:")
num = 0
for i in range(101):
     num = num + i 
     print(num)






#Ejercicio 2
#Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
#The sum of all evens is 2550. And the sum of all odds is 2500.
print("Ejercicio 2:")
print("Ejercicio 2:")
suma_pares = 0
suma_impares = 0

for num in range(0, 101):  
    if num % 2 == 0: 
        suma_pares += num
    else: 
        suma_impares += num

print("La suma de todos los números pares es:", suma_pares)
print("La suma de todos los números impares es:", suma_impares)




print("Ejercicios de Nivel 3:")
#Ejercicios de Nivel 3


#Ejercicio 1
# Go to the data folder and use the countries.py file.
# Loop through the countries and extract all the countries containing the word 'land'.
print("Ejercicio 1:")
import countries as p
paises = p.countries
paises_con_land = []
for pais in paises:
    if 'land' in pais:
        paises_con_land.append(pais)
print("Los paises que terminan con Land son:", paises_con_land)










        






#Ejercicio 2
#This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
print("Ejerciico 2:")
frutas = ['banana', 'orange', 'mango', 'lemon']
for i in range(len(frutas)-1, -1, -1):
    print(frutas[i])





#Ejercicio 3
# Go to the data folder and use the countries_data.py file.
# 3.1.What are the total number of languages in the data
print("Ejercicio 3 y 3.1:")
import countries_data as cd
number_of_lenguaje = cd.paises
lenguajes = set()
for pais in number_of_lenguaje:
    for idioma in pais['languages']:
        lenguajes.add(idioma)
print("El total de idiomas es:", len(lenguajes))
















#Ejercicio 3.2
#Find the ten most spoken languages from the data
print("Ejercicio 3.2:")
setLanguages = set()
dictLanguages = {}

for country in cd.paises:
    for language in country['languages']:
        setLanguages.add(language)

for language in setLanguages:
    dictLanguages[language] = 0

for language in dictLanguages:
    for country in cd.paises:  
        if language in country['languages']:
            dictLanguages[language] += country['population']

sortValuesLanguagesPopulation = sorted(dictLanguages.values(), reverse=True)
sorfKeysLanguagesPopulation = sorted(dictLanguages, key=dictLanguages.get, reverse=True)

print('Los 10 idiomas más hablados en el mundo son:')
for i in range(10):
    print(" El Idioma es:",  sorfKeysLanguagesPopulation[i])
    print("Cantidad de personas que lo hablan:", sortValuesLanguagesPopulation[i])






#Ejercicio 3.3
#Find the 10 most populated countries in the world
print("Ejercicio 3.3:")
paises = cd.paises
paises_poblacion = {}
for pais in paises:
    paises_poblacion[pais['name']] = pais['population']
paises_poblacion_ordenados = sorted(paises_poblacion.items(), key=lambda x: x[1], reverse=True)
print("Los 10 países más poblados del mundo son:")
for i in range(10):
    print(paises_poblacion_ordenados[i][0], ":", paises_poblacion_ordenados[i][1])


    
print("revisado")

        


         
 
 




















