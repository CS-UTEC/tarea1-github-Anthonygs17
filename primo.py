num = int(input("Ingrese un numero: "))

def esPrimo(num):
    cantDiv = 0
    for i in range(1,num+1):
        if(num%i==0):
            cantDiv+=1
    return (cantDiv==2)

if esPrimo(num):
    print("El numero es primo")
else:
    print("El numero no es primo")
