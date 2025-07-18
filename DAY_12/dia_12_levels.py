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







print("Ejercicios de Nivel 2:")
#Ejercicios de Nivel 2:
#Ejercicio 1:
#Write a function list_of_hexa_colors which returns any number of hexadecimal colors in a list 
#(six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f).
print("Ejercicio 1:")
def list_of_hexa_colors(num_colors):
    hex_colors = []
    for _ in range(num_colors):
        color = '#{:06X}'.format(random.randint(0, 0xFFFFFF))
        hex_colors.append(color)
    return hex_colors
print("La lista de hexa colors es:", list_of_hexa_colors(5))












#Ejercicio 2:
#Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
print("Ejercicio 2:")
def list_of_rgb_colors(num_colors):
    rgb_colors = []
    for i in range(num_colors):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        rgb_colors.append(color)
    return rgb_colors
print("La lista de rgb colors es :", list_of_rgb_colors(5))











#Ejercicio 3:
#Write a function generate_colors which can generate any number of hexa or rgb colors.
print("Ejercicio 3:")
def generate_colors(num_colors, color_type):
    colors = []
    if color_type == 'hexa':
        for i in range(num_colors):
            color = '#{:06X}'.format(random.randint(0, 0xFFFFFF))
            colors.append(color)
    elif color_type == 'rgb':
        for i in range(num_colors):
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            colors.append(color)
    return colors
print("La generada colors es:", generate_colors(5, 'hexa'))
print("La generada colors es:", generate_colors(5, 'rgb'))














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