print("bienvenido al preograma")

a=1
while a !=0:
    print("ingresa 1. Area Triangulo ")
    print("ingresa 2. Area Rectangulo")
    print("Ingresa 3. Area Circulo")
    print("Convertir temperatura °F O °C")
    print("convertir temperatura °C a °F")
    print("ingresa 0. salir del programa")
    op=int(input("Ingresa un numero de las opciones que quieres hacer "))

    if(op==1):
        bas=int(input("Cual es la base¿? "))
        alt=int(input("Cual es la altura¿? "))
        Area=(bas*alt)/2
        print("El area es:", Area)

    elif(op==2):
        Bas1=int(input("¿Cual es la base del rectangulo? "))
        alt1=int(input("¿Cual es la altura del rectangulo?"))
        Area1=Bas1*alt1
        print("El area del rectanglo es:", Area1)

    elif(op==3):
        rad=int(input("¿Cual es el radio del circulo? "))
        Area2=3.14*(rad*rad)
        print("El area del circulo es: ", Area1)

    elif(op==4):
        fah=int(input("ingresa la temperatura en Fahrenheit"))
        Celcius=((fah-32)*5)/9
        print("La conversion a grados celcius es: ", Celcius)

    elif(op==5):
        cel=int(input("Ingresa la temperatura en celcius"))
        Fah2=(cel*(9/5))+32
        print("La conversion a grados fahrenheit", Fah2)
    
    else:
        print("jajaj no")

    a=int(input("Quieres continuar, si no presiona 0 para salir¿?"))

    