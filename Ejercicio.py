
def Ejercicio1 ():
    nombre= input ("ingrese su nombre: ")
    edad= int (input ("ingresa edad: ") )
    programa= input ("ingrese el nombre del programa:")
    promedio = float (input ("ingrese su promedio:") )
    print (nombre,edad,programa,promedio) 
    print (type(nombre),type(edad),type(programa),type(promedio))
    print (f"Hola {nombre}, tienes {edad} años, estas en el programa {programa} y tu promedio es {promedio}")
    
    

# Ejercicio1 ()

def Ejercicio2 ():
    nota= float (input ("ingrese la nota: ") )
    if nota >= 3.0:
        print ("Aprobado")
    else:
        print ("No aprobado")   
    if nota < 0.0 or nota > 5.0:
        print ("Nota invalida")
        
# Ejercicio2 ()

def Ejercicio3 ():
    print("Números del 1 al 100:")
    for numero in range(1, 101):
        print(numero)

    print("\nNúmeros pares:")
    for numero in range(2, 101, 2):
        print(numero)

    print("\nNúmeros impares:")
    for numero in range(1, 101, 2):
        print(numero)

    print("\nMúltiplos de 5:")
    for numero in range(5, 101, 5):
        print(numero)

    suma = 0
    for numero in range(1, 101):
        suma = suma + numero

    print("\nSuma de los números del 1 al 100:", suma)

    Ejercicio3()

    

    



