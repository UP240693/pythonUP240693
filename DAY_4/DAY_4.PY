#1
print("30", " days", " of", " python")
#2
print("coding ", "FOR ", "all")
#3
company= "coding for all"
#4
print(company)
#5
print(len(company))
#6
print(company.lower())
#7
print(company.upper())
#8
print(company.capitalize())
print(company.title())
print(company.swapcase())
#9
print(company [7:] )
#10
print(company.index("coding"))
#11
print(company.replace("coding", "python"))
#12
frase="python for everyone"
print(frase.replace("everyone", "all"))
#13
print(company.split())
#14
companies= "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(", "))
#15
print(company[0])
#16
print(len(company)-1)
#17
print(company[10])
#18
acronimo_pfe= "" .join([ word[0] for word in frase.split()])
print(acronimo_pfe)
#19
acronimo_cfa= "" .join([ word[0] for word in company.split()])
print(acronimo_cfa)
#20
print(company.index("c"))
#21
print(company.index("f"))
#22
str_p="coding for all people"
print(str_p.rfind("1"))
#23
sentence= "You cannot end a sentence with because because because is a conjunction"
print(sentence.find("because"))
#24
print(sentence.rindex("because"))
#25
ini= sentence.find("because")
fin=sentence.rindex("because") + len("because")
print(sentence[ini:fin])
#26
print(sentence.find("because"))
#27
print(sentence[sentence.find("because"):sentence.rindex("because") + len("because")])
#28
print(company.startswith("coding"))
#29
print(company.endswith("coding"))
#30
cfa="coding for all"
print(cfa.strip())
#31
print("30DiasDePython".isidentifier())
print("Treinta_Dias_De_Python".isidentifier())
#32
libros=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(" # ".join(libros))
#33
print("im enjoying this challenge.\nI just wonder what is next")
#34
print("name\tAge \t Country \t City \nAsabeneh \t 250 \t Findland \t Helsinki")
#35
radio=10
area=3.1416*radio**2
print(f"el area del circulo con radio de {radio} es {area:.0f} metros cuadrados ")
#36
a=8
b=6
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} x {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")