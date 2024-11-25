equipo=["izak", "yo", "la maestra"]
print(equipo)

num_equipo=int(input("cuantos integrantes mas quieres? "))
for i in (range(num_equipo)):
    dep=input("ingresa tus integrantes ")
    equipo.append(dep)
    print(equipo)