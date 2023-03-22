"""
Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras 
que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
a=int(len(alphabet))
number=[]
for i in range(1,a+1):
    number.append(i)
print(number)

z=zip(alphabet,number)
numbers=[i for i in range(1,a+1) if i/3==0]
total={key:value for key,value in z}
print(total)

for key,value in total.items():
    if value%3!=0:
        print(key,'\end')
