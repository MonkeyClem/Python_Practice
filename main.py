social_platforms = ["Instagram", "Facebook", "Twitter", "Snapchat", "TikTok"]

# dans Python, vous pouvez aussi accéder aux éléments en sens 
# inverse, en utilisant des nombres négatifs. Pour accéder au 
# dernier élément de la liste, utilisez l’indice -1.

print(
        "Which one's your favorite ?",
        social_platforms[-1],"?", 
        social_platforms[1],"?"
        )

# Le input en python sert, comme dans HTML, à laisser l'user saisir des données
# input()


# Pour modifier une case d'une liste, il suffit d'utiliser l'indice de la case que l'on 
# souhaite modifier, et d'y affecter la nouvelle valeur à l'aide de 
# l'opérateur d'affectation (=), tout comme pour une variable.
social_platforms[0] = social_platforms[0]
print(social_platforms[0]) #Should Be Facebook, if everything's working 

# Pour ajouter un élément spécifique à une liste, vous pouvez
# utiliser la méthode  remove()
social_platforms.append("LinkedIn")
print(social_platforms)

# Pour retirer un élément spécifique d’une liste, vous pouvez
# utiliser la méthode  remove()
social_platforms.remove("LinkedIn")
print(social_platforms)

# Pour connaître la longueur de la liste, utilisez la méthode  len()
print(len(social_platforms))

# La dernière méthode que nous allons voir est  sort(). Elle trie les 
# éléments de la liste. Le tri se fait alphabétiquement pour les listes 
# de chaînes, et numériquement pour les listes de nombres.
social_platforms.sort()
print(social_platforms)

# Réalisez cet exercice guidé étape par étape :
# Créez une liste nommée fruits contenant les éléments "pomme", "banane" et "orange".
# Ajoutez "kiwi" à la liste fruits.
# Supprimez "orange" de la liste fruits.
# Modifiez le deuxième élément de la liste fruits en "ananas".
# Affichez la longueur de la liste fruits.
# Triez la liste fruits par ordre alphabétique et affichez-la.

fruits = [ "pomme", "banane","orange"]
fruits.append("kiwi")
fruits.remove("orange")
fruits[1] = "ananas"
print(len(fruits))
fruits.sort()
print(fruits)



#Il est possible de créer un nouveau dictionnaire déclarant le nom désiré pour 
# ce dernier puis en lui assignant une paire d'accolades vide 
firstDictionnary = {}

firstDictionnary["Ajout d'une clé"] = "Valeur"
firstDictionnary["Nouvelle clé"] = "Nouvelle Valeur"
print(firstDictionnary)

#La suppression d'un élément du dictionnaire se fait via la méthode 
# del,avec le nom du dictionnaire en argument, et la clef situé entre accolades.
# del firstDictionnary["Ajout d'une clé"]
# print(firstDictionnary)

# key values items

print("firstDictionnary.values = " , firstDictionnary.values())
print("firstDictionnary.keys = " , firstDictionnary.keys())
print(firstDictionnary.items())


# Vous pouvez utiliser le mot-clé in  pour vérifier si une clé spécifique existe 
# dans un dictionnaire. Pour faire cela, spécifiez la clé que vous voulez rechercher, écrivez 
# le mot-clé in  et le nom de la variable du dictionnaire que vous examinez. Le résultat 
# renvoie un booléen qui indique si la clé est dans ce dictionnaire. Par exemple, si vous 
# voulez voir si la clé « poids » existe dans votre dictionnaire  
print("Nouvelle clé" in firstDictionnary)
print("Derniere clé" in firstDictionnary)

print(firstDictionnary)

#----------  EXERCICE :
#Créez un dictionnaire appelé fruits avec les clés "pomme", "banane" et "orange", et les valeurs "rouge", "jaune" et "orange".
# Ajoutez la clé "kiwi" avec la valeur "vert" au dictionnaire fruits.
# Accédez à la valeur correspondant à la clé "banane" et stockez-la dans une variable appelée couleur_banane.
# Modifiez la valeur associée à la clé "pomme" pour "vert".
# Supprimez la clé "orange" du dictionnaire fruits.
# Affichez les clés restantes dans le dictionnaire.


#Création du dictionnaire "fruits"
fruits = {
    "pomme": "rouge",
    "banane": "jaune",
    "orange": "orange"
}

#On injecte la clé kiwi, ayant "vert comme valeur"
fruits["kiwi"]=["vert"]

#Nous pouvons stocker la valeur correspondante à une clédans une variable: 
couleur_banane = fruits["banane"]
print(couleur_banane)

#Il est aussi possible de modifier la valeur d'une clé : 
fruits["pomme"]=["vert"]

#Suppression de la clé "orange  "
del fruits['orange']

print(fruits.keys())
