races_de_chats = ["Siamois", "Maine-Coon","Européen"]

for chat in races_de_chats: 
    print(chat)

# Pour boucler un certain nombre de fois, vous pouvez utiliser la 
# fonction  range()  . Elle renverra une séquence de nombres qui 
# vont de 0 à un nombre de fin déterminé.
# Les accolades prennent n’importe quelle valeur dans la variable   x  
# et la remplacent (n’oubliez pas le   “f”  au début de la string, qui signifie  format). 
# Donc dans cet exemple, le code s'affichera de 0 jusqu'à 9 :
for x in range(10): 
    print(f"{x} bouteilles sont acrochés") 

# Il est également posssible de fournir une range
#  comprise entre 2 entiers.
for x in range(5, 10): 
    print(f"{x} paire chausettes sont pliées") 




capacite_maximale = 10
capacite_actuelle = 3

print("La capacité maximale est de :", capacite_maximale)

while capacite_actuelle < capacite_maximale:

    capacite_actuelle += 1
    print("Votre capacité actuelle est de :", capacite_actuelle)


# À vous de jouer ! 
# Vous devez écrire un programme qui permet de calculer différentes statistiques pour un ensemble de nombres donné par l'utilisateur.
# Demandez à l'utilisateur de saisir une liste de nombres séparés par des virgules (par exemple : 1,2,3,4), et afficher cette liste.
# Calculez et affichez la somme des nombres dans la liste.
# Calculez et affichez la moyenne des nombres dans la liste.
# Calculez et affichez le nombre de nombres dans la liste qui sont supérieurs à la moyenne.
# Calculez et affichez le nombre de nombres dans la liste qui sont pairs.

1.
numberList = input("Veuillez s'il vous plait saisir une liste de nombre, sans espace, et séparés par des virgules : ")
print("liste de nombres :" ,numberList)
numberList = numberList.split(",")

somme = 0 
for number in numberList : 
    somme += int(number)

print("La somme des nombres renseignés est : ", somme)

print(len(numberList))

2.
moyenne = somme / len(numberList)
print("La moyenne des nombres renseignés est :", moyenne)

3.
upNumber = 0
lowNumber = 0
for number in numberList : 
    if int(number) > moyenne : 
        upNumber += 1
        print("Nous avons detecté un chiffre / nombre supérieur à la moyenne : ",  number , " il s'agit du :" , upNumber,"ème présent dans la liste" )
    else :
        lowNumber += 1
        print("Nous avons détécté un chiffre / nombre  inférieur à la moyenne :", number , " il s'agit du :" , lowNumber,"ème présent dans la liste" ) 