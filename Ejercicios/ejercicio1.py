"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje 
En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> 
cada una de las correspondientes notas introducidas por el usuario.
"""
asignaturas=["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
nota=[]
for i in asignaturas:
    nota.append(int(input(f"Digite la nota obtenia en la siguiente asignatura {i}: ")))

a=list(zip(asignaturas,nota))
notas_asignaturas={key:value for key,value in a}

for key,value in notas_asignaturas.items():
    print(f"En la asignatura de {key} has sacado de nota {value}")
