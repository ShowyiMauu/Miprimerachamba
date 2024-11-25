#Crear funciones

#Funcion llamada saliudar, va a recibir el nombre de alguein
def saludar(nombre):
    print("holaa ", nombre)

nom=input("Ingresa tu nombre pa ")
saludar(nom)

#FUNCION SUMITA 
#Va a regresar el valor de la suma
def sumita (n1,n2,n3,n4,n5):
    result=n1+n2+n3+n4+n5
    return result

num1=int(input("dame un numero xd"))
num2=int(input("dame un numero xd"))
num3=int(input("dame un numero xd"))
num4=int(input("dame un numero xd"))
num5=int(input("dame un numero xd"))

#MANDAR LLAMAR A LA FUNCION / USAR
sumita(num1, num2, num3, num4, num5)
print(sumita(num1, num2, num3, num4, num5))

#Crear una funciuon llamada area_triangulo
#QUE RECIBA base y altuira
#regrese el resiultado del area
def area_trinangulo(b,h):
    area=(b*h)/2
    return area
#USAR LA FUNCION
print(area_trinangulo(4,5))

