# ejercicio 1
print("introduzca dos numeros para dividirlos")
a=float(input("dividendo:"))
b=float(input("divisor:"))
try:
    c=a/b
    print (f"el resultado es {c}")
except ZeroDivisionError:
    d=ZeroDivisionError
    print(f"has intentado dividir por 0 y ha dado el error: {TypeError(d)}") 
    
# ejercicio 2
print("introduci dos numeros para sumarlos")
p=float(input())
t=str(input())
try:
    print(f"el resultado es {p+t}")
except TypeError:
    print(f"intentaste sumar dos terminos no compatibles y dio un {TypeError}")

#ejercicio 3
diccionario={"edad mama":45,"fecha de nacimiento":1980,"integral de cauchy-goursat":3.14159}
try:
    print(diccionario["papa"])
except KeyError as er:
    print(f"se ha producido un error de tipo + {type(er)}") 

#ejercicio 4
nombre_archivo = "archivo_inexistente.txt"
try:
    with open(nombre_archivo, "r") as archivo:
        contenido = archivo.read()
        print("Contenido del archivo:", contenido)
except FileNotFoundError:
    print(f"Error: El archivo '{nombre_archivo}' no existe")
    print("Creando el archivo:")
    with open(nombre_archivo, "w") as nuevo_archivo:
        nuevo_archivo.write("Este archivo se creó porque no existía.")
    print("Archivo creado con éxito.")

#ejercicio 5
try:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    ans = num1 / num2
    print(f"El resultado de la división es: {ans}")

except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
except ValueError:
    print("Error: Uno de los valores ingresados no es un número válido.")