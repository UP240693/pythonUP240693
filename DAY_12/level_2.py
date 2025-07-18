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