print("holaas")

deportes=["fubol", "Voleibol", "Natacion", "Basquetbol"]

print(deportes)
print(deportes[2])

#posicion de natacion
posi=deportes.index("Natacion")
print("la posicion de natacion es:", posi)

deportes.append("Hanball")
print(deportes)

deportes.insert(2, "tenis")
print(deportes)

cantidad_saludos=int(input("cuantos saludos quiereS? "))

for i in range(cantidad_saludos):
    print("hola")


num_deportes=int(input("cuantos deportes quieres "))
for i in (range(num_deportes)):
    dep=input("ingresa deporte ")
    deportes.append(dep)

    print(deportes)