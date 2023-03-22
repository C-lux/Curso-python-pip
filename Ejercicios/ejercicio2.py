"""
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva,
los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
"""
loteria=[]

for i in range(1,6+1):
    loteria.append(int(input("Cuales son los numero ganadores de la loteria: ")))

loteria.sort()
print(loteria)