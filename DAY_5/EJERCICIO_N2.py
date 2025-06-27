#Day 5
#Exercises: level 2

ages=[19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
edad_minima=min(ages)
edad_maxima=max(ages)
print("Edad minima de la lista: ", edad_minima)
print("Edad maxima de la lista: ", edad_maxima)
ages.append(edad_minima)
ages.append(edad_maxima)
print(ages)
median_age=(ages[5]+ages[6])/2
print("La edad media es: ", median_age)
average_age=(ages[0]+ages[1]+ages[2]+ages[3]+ages[4]+ages[5]+ages[6]+ages[7]+ages[8]+ages[9]+ages[10]+ages[11])/12
print("Average age: ", average_age)
rango=edad_maxima-edad_minima
print("Rango de edad: ", rango)
valor1=abs(edad_minima-average_age)
valor2=abs(edad_maxima-average_age)
print("Comparación: ¿El valor ", valor1, " es >= al valor ", valor2, "? ", valor1>=valor2)