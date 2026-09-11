
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

# Ejercicio3 ()

def Ejercicio4():
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))

    print("Suma:", sumar(numero1, numero2))
    print("Resta:", restar(numero1, numero2))
    print("Multiplicación:", multiplicar(numero1, numero2))
    print("División:", dividir(numero1, numero2))


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "No se puede dividir entre cero."
    return a / b


# Ejercicio4()

def Ejercicio5 ():
    while True:
        print("\n========== CALCULADORA ==========")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "5":
            print("Programa finalizado.")
            break

        if opcion in ["1", "2", "3", "4"]:
            numero1 = float(input("Ingrese el primer número: "))
            numero2 = float(input("Ingrese el segundo número: "))

            if opcion == "1":
                print("Resultado:", sumar(numero1, numero2))

            elif opcion == "2":
                print("Resultado:", restar(numero1, numero2))

            elif opcion == "3":
                print("Resultado:", multiplicar(numero1, numero2))

            elif opcion == "4":
                print("Resultado:", dividir(numero1, numero2))

        else:
            print("Opción no válida.")


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "No se puede dividir entre cero."
    return a / b

# Ejercicio5 ()

def Ejercicio6():
    estudiantes = [
        "Ana", "Carlos", "Laura", "Juan", "Sofía",
        "Pedro", "Camila", "Andrés", "Valentina", "Mateo"
    ]

    print("Todos los estudiantes:")
    for estudiante in estudiantes:
        print(estudiante)

    print("\nPrimer estudiante:", estudiantes[0])
    print("Último estudiante:", estudiantes[-1])
    print("Cantidad de estudiantes:", len(estudiantes))

    nuevo_estudiante = input("\nIngrese el nombre del estudiante que desea agregar: ")
    estudiantes.append(nuevo_estudiante)

    print("\nLista después de agregar:")
    print(estudiantes)

    eliminar_estudiante = input("\nIngrese el nombre del estudiante que desea eliminar: ")

    if eliminar_estudiante in estudiantes:
        estudiantes.remove(eliminar_estudiante)
        print("Estudiante eliminado.")
    else:
        print("El estudiante no existe.")

    buscar_estudiante = input("\nIngrese el nombre del estudiante que desea buscar: ")

    if buscar_estudiante in estudiantes:
        print("El estudiante sí está en la lista.")
    else:
        print("El estudiante no está en la lista.")


# Ejercicio6()

def Ejercicio7():
    notas = [3.5, 4.2, 2.8, 4.5, 3.9, 2.5, 4.0, 4.7]

    cantidad_estudiantes = 0
    suma_notas = 0
    mayor = notas[0]
    menor = notas[0]
    aprobados = 0
    reprobados = 0

    # Recorrer las notas para contar, sumar y encontrar mayor/menor
    for nota in notas:
        cantidad_estudiantes += 1
        suma_notas += nota

        if nota > mayor:
            mayor = nota

        if nota < menor:
            menor = nota

        if nota >= 3.0:
            aprobados += 1
        else:
            reprobados += 1

    promedio = suma_notas / cantidad_estudiantes

    print("Número de estudiantes:", cantidad_estudiantes)
    print("Promedio:", promedio)
    print("Nota mayor:", mayor)
    print("Nota menor:", menor)
    print("Cantidad de aprobados:", aprobados)
    print("Cantidad de reprobados:", reprobados)

    print("\nNotas mayores que el promedio:")
    for nota in notas:
        if nota > promedio:
            print(nota)


# Ejercicio7()

def Ejercicio8():
    productos = [
        "Teclado",
        "Mouse",
        "Monitor",
        "Impresora",
        "Memoria RAM",
        "Disco SSD"
    ]

    producto_buscar = input("Ingrese el producto que desea buscar: ")

    encontrado = False

    for producto in productos:
        if producto.lower() == producto_buscar.lower():
            encontrado = True
            break

    if encontrado:
        print("Producto encontrado.")
    else:
        print("Producto no encontrado.")


# Ejercicio8()

def Ejercicio9():
    notas = [
        [4.0, 3.5, 4.2],
        [3.0, 4.1, 3.7],
        [4.5, 3.8, 4.0],
        [2.8, 3.2, 3.5],
        [3.9, 4.5, 4.2]
    ]

    asignaturas = ["Programación", "Matemáticas", "Inglés"]

    mayor = notas[0][0]
    menor = notas[0][0]

    # Promedio de cada estudiante y búsqueda de mayor/menor
    for i in range(len(notas)):
        suma = 0

        for j in range(len(notas[i])):
            nota = notas[i][j]
            suma += nota

            if nota > mayor:
                mayor = nota

            if nota < menor:
                menor = nota

        promedio_estudiante = suma / len(notas[i])
        print("Promedio del estudiante", i + 1, ":", promedio_estudiante)

    # Promedio de cada asignatura
    print("\nPromedio por asignatura:")

    for columna in range(3):
        suma_asignatura = 0

        for fila in range(len(notas)):
            suma_asignatura += notas[fila][columna]

        promedio_asignatura = suma_asignatura / len(notas)
        print(asignaturas[columna], ":", promedio_asignatura)

    print("\nNota mayor:", mayor)
    print("Nota menor:", menor)


Ejercicio9()

def Ejercicio10():
    estudiantes = []

    while True:
        print("\n========================")
        print("SISTEMA DE ESTUDIANTES")
        print("1. Registrar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Buscar estudiante")
        print("4. Mostrar promedio")
        print("5. Mostrar mayor nota")
        print("6. Mostrar menor nota")
        print("7. Mostrar aprobados")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_estudiante(estudiantes)

        elif opcion == "2":
            mostrar_estudiantes(estudiantes)

        elif opcion == "3":
            buscar_estudiante(estudiantes)

        elif opcion == "4":
            mostrar_promedio(estudiantes)

        elif opcion == "5":
            mostrar_mayor_nota(estudiantes)

        elif opcion == "6":
            mostrar_menor_nota(estudiantes)

        elif opcion == "7":
            mostrar_aprobados(estudiantes)

        elif opcion == "8":
            print("Programa finalizado.")
            break

        else:
            print("Opción no válida.")


def registrar_estudiante(estudiantes):
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))
    nota = float(input("Ingrese la nota: "))

    if nota < 0.0 or nota > 5.0:
        print("La nota no es válida.")
    else:
        estudiantes.append([nombre, edad, nota])
        print("Estudiante registrado correctamente.")


def mostrar_estudiantes(estudiantes):
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
    else:
        print("\nLista de estudiantes:")

        for estudiante in estudiantes:
            print("Nombre:", estudiante[0],
                  "| Edad:", estudiante[1],
                  "| Nota:", estudiante[2])


def buscar_estudiante(estudiantes):
    nombre_buscar = input("Ingrese el nombre que desea buscar: ")
    encontrado = False

    for estudiante in estudiantes:
        if estudiante[0].lower() == nombre_buscar.lower():
            print("Estudiante encontrado:")
            print("Nombre:", estudiante[0])
            print("Edad:", estudiante[1])
            print("Nota:", estudiante[2])
            encontrado = True
            break

    if encontrado == False:
        print("El estudiante no fue encontrado.")


def mostrar_promedio(estudiantes):
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
    else:
        suma = 0

        for estudiante in estudiantes:
            suma += estudiante[2]

        promedio = suma / len(estudiantes)
        print("Promedio del grupo:", promedio)


def mostrar_mayor_nota(estudiantes):
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
    else:
        mayor = estudiantes[0]

        for estudiante in estudiantes:
            if estudiante[2] > mayor[2]:
                mayor = estudiante

        print("Mayor nota:", mayor[2])
        print("Estudiante:", mayor[0])


def mostrar_menor_nota(estudiantes):
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
    else:
        menor = estudiantes[0]

        for estudiante in estudiantes:
            if estudiante[2] < menor[2]:
                menor = estudiante

        print("Menor nota:", menor[2])
        print("Estudiante:", menor[0])


def mostrar_aprobados(estudiantes):
    aprobados = 0

    for estudiante in estudiantes:
        if estudiante[2] >= 3.0:
            aprobados += 1
            print(estudiante[0], "- Nota:", estudiante[2])

    print("Cantidad de aprobados:", aprobados)


Ejercicio10()
    

    



