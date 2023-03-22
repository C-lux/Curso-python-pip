"""
Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. 
Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
"""
asignaturas=["Matematicas","Fisica","Quimica","Historia","Lengua"]
nota=[]

for i in asignaturas:
    z=(int(input(f"Cual es la nota obtenia en {i}: ")))
    nota.append(z)

total=zip(asignaturas,nota)
notas={key:value for key,value in total}

for key,value in notas.items():
    if value<60:
        print(f"Materias que tiene que repetir{key,value}")
    else:
        print(f"Aprobo {key}")
