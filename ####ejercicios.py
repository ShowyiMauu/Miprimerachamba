####ejercicios
#1) crear una funcion llamada multiplicar
#que reciba 3 numeros,regresar el resultado
def multiplicar(num1, num2, num3):
    multi=(num1*num2*num3)
    return multi

nu1=int(input("dame un numero "))
nu2=int(input("dame un numero xd"))
nu3=int(input("dame un numero xd"))

multiplicar(nu1,nu2,nu3)
print(multiplicar(nu1,nu2,nu3))

#2)  Crear una funcion llamada largo_cadena
def largo_cadena(texto):
    cantidad=len(texto)
    return cantidad
print("TU TEXTO ES", len)


#3
def promedio(cal1, cal2):
    prom=(cal1+cal2)/2
    return prom

calf1=int(input("caul fue su calificacion"))
calf2=int(input("caul fue su calificacion"))

promedio(calf1,calf2)
print(promedio(calf1,calf2))


def disk_curp(nombre,edad,mes_de_nacimiento):
    letras=nombre[0:2]
    return letras

no=input("Dame tu nombre")
ed=int(input("dame tu edad"))
mes=input("Dame tu mes de nacimiento")
 
print(no[0:2],ed[0,2],mes[0,2])