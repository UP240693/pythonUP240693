
print("Ejercicios de Nivel 3:")
#Ejercicios de Nivel 3:
#Ejercicio 1:
#Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
print("Ejercicio 1:")
def shuffle_list(lst):
    shuffled = lst[:]
    random.shuffle(shuffled)
    return shuffled

# Ejemplo de sus uso:
print("La shuffled list es:", shuffle_list([1, 2, 3, 4, 5]))


#Ejercicio 2:
#Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
print("Ejercicio 2:")
def unique_random_numbers():
    return random.sample(range(10), 7)

# Ejemplo de su uso:
print("Los numeros random en un rango de 0-9 es:", unique_random_numbers())



print("Terminados los ejercicios del dia 12.")

print("revisado")