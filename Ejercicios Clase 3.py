#Ejercicio 1
print("introduzca dos numeros")
a=float(input("introduzca el primer numero: "))
b=float(input("introduzca el segundo numero: "))
num_mayor= a if a>b else b
print(f"el numero mayor es {num_mayor}") 

#Ejercicio 2
print("introduzca 5 elementos para una lista")
lista=[input() for i in range (5)]
print(f"la lista es:  {lista}\nintroduzca un elemento que quiera buscar")
elemento=input()

def busqueda(i, *args):
    return f"La palabra '{i}' {'sí está' if i in args else 'no está'} en la lista."
print(busqueda(elemento,*lista))

#Ejercicio 3
print(input("introduzca un numero: " ))
print("es par" if a%2==0 else "es impar")

#Ejercicio 4 
print("introduzca 5 numeros:")
lista=[float(input()) for i in range (5)]
print(f"la lista es:  {lista}" )
def promedio(*args):
    return sum(lista)/len(lista) if len(lista)>0 else "la lista está vacía"
resultado=promedio(*lista)
print(f"el promedio es: {resultado}")

#Ejercicio 5
def verificar_argumentos(*args):
    print("Error: No se pasaron suficientes argumentos") if len(args) < 3 else print("Argumentos válidos")

verificar_argumentos(1, 2) 
verificar_argumentos(1, 2, 3)