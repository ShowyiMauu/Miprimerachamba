opcion=1

while opcion !=0:
    num1=int(input("ingresa el primer numero"))
    num2=int(input("ingresa el segundo numero"))
    print("ingresa 1 sumar")
    print("ingresa 2 restar")
    print("ingresa 3 multiplicar")
    print("ingresa 4 Dividir")
    op=int(input("¿Que operacion quieres hacer?"))

    if(op==1):
        res=num1 + num2 
        print("La suma de los numeros es: ",res)

    elif(op==2):
        resta=num1-num2
        print("LA RESTA ES:", resta)
        
    elif(op==3):
        multi=num1*num2
        print("la multiplicacion es: ", multi)

    elif(op==4):
        div=num1/num2
        print("la divicion es: ", div)

    else:
        print("no es valido")
    
    opcion=int(input("deseas continuar, si no presiona 0. para salir"))

