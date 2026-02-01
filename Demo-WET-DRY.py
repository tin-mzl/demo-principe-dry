#la table de multiplication par 5
print("Table de multiplication par 5")
print (f"5x0 = {5*0}")
print (f"5x1 = {5*1}")
print(f"5x2 = {5*2}")
print (f"5x3 = {5*3}")
print(f"5x4 = {5*4}")
print (f"5x5 = {5*5}")
print(f"5x6 = {5*6}")
print (f"5x7 = {5*7}")
print(f"5x8 = {5*8}")
print (f"5x9 = {5*9}")
print(f"5x10 = {5*10}")
#si on veut par exemple changer de nombre on sera obliger de le faire manuellement
#donc il faut automatiser tout ça
#l'automatisation de la tache
def table_de_multiplication(n):
  print(f"la table de multiplication {n}")
  for i  in range(0,11):
        print(f"{n} x {i} = {i*n}")
  return i * n
#On cree une variable number pour demander a l'utilisateur quel table de multiplication il veut
num = int(input("veillez saisir un nombre: "))

table_de_multiplication(num)
