#la table de multiplication par 5
print (5*0)
print (5*1)
print(5*2)
print (5*3)
print(5*4)
print (5*5)
print(5*6)
print (5*7)
print(5*8)
print (5*9)
print(5*10)
#si on veut par exemple changer de nombre on sera obliger de le faire manuellement
#donc il faut automatiser tout ça
#l'automatisation de la tache
def table_de_multiplication(n):
    for i  in range(0,11):
        print(f"{n} x {i} = {i*n}")
    return i * n
#On cree une variable number pour demander a l'utilisateur quel table de multiplication il veut
num = int(input("veillez saisir un nombre: "))

table_de_multiplication(num)
