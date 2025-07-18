print("Ejercicios de Nivel 1:")
#Ejercicios de Nivel 1:
#Writ a function which generates a six digit/character random_user_id
print("Ejercicio 1:")
import random 
import string
def generate_random_user_id():
    characters = string.ascii_letters + string.digits
    user_id = ''.join(random.choice(characters) for _ in range(6))
    return user_id
print("El random user id es :", generate_random_user_id())


#Ejercicio 2:
#Modify the previous task. Declare a function named user_id_gen_by_user. 
#It doesn’t take any parameters but it takes two inputs using input(). 
#One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
print("Ejercicio 2:")
def user_id_gen_by_user():
    num_chars = int(input("Escribe el numero de caracteres para el identificador de usuario:"))
    num_ids = int(input("Escribe el numero de identificadores de usuario que desea generar:"))
    characters = string.ascii_letters + string.digits
    user_ids = []
    for _ in range(num_ids):
        user_id = ''.join(random.choice(characters) for _ in range(num_chars))
        user_ids.append(user_id)
    return user_ids
print("Los random user son:", user_id_gen_by_user())


#Ejercicio 3:
#Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
print("Ejercicio 3:")
def rgb_color_gen():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)
print("El rgb colors es :", rgb_color_gen())
