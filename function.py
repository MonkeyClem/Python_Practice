# En Python, la création d'une fonction se fait à l'aide du mot-clé 
# def  , suivi du nom de la fonction et des éventuels paramètres entre parenthèses.

def afficher_un_message(): 
    print("Bonjour")

# Pour appeler cette fonction, il suffit d'utiliser son nom 
# et les parenthèses vides, car il n’y a pas de paramètres :

afficher_un_message()

# Utilisez une fonction avec paramètres :
# On peut également créer une fonction avec des paramètres, qui permettent de 
# transmettre des valeurs à la fonction. Les paramètres sont simplement listés 
# entre parenthèses, séparés par des virgules. Voici un exemple d'une fonction 
# qui prend deux paramètres, un nom et un prénom, et qui les affiche ensuite.

def afficher_un_utilisateur(nom, prenom, ddn):
    print("Nom: ", nom)
    print("Prénom :" , prenom)
    print("Date de Naissance :", ddn)

afficher_un_utilisateur("Clément" , "Jeulin", "30/12/1995")

#Possibilité d'obtenir une valeur de retour 
def somme(a, b):
    resultat = a + b
    return resultat

print(somme(12,24))

final_value = somme(12, 24) / 2 
print(final_value)

# EXERCICE : Calculateur de salaire horaire
# Créer un programme qui calcule le salaire horaire d'un employé, en fonction de son salaire mensuel
# et de son nombre d'heures travaillées par semaine. Le programme doit utiliser des fonctions pour effectuer les calculs.
# Créer une fonction appelée  salaire_mensuel(salaire_annuel)  qui prend en paramètre un salaire annuel, et retourne le salaire mensuel correspondant en divisant le salaire annuel par 12.
# Créer une fonction appelée  salaire_hebdomadaire(salaire_mensuel)  qui prend en paramètre un salaire mensuel et retourne le salaire hebdomadaire correspondant en divisant le salaire mensuel par 4.
# Créer une fonction appelée  salaire_horaire(salaire_hebdomadaire, heures_travaillees)  qui prend en paramètres un salaire hebdomadaire et le nombre d'heures travaillées par semaine, et retourne le salaire horaire correspondant en divisant le salaire hebdomadaire par le nombre d'heures travaillées par semaine.
# Demandez à l'utilisateur de saisir son salaire annuel.
# Demandez à l'utilisateur de saisir le nombre d'heures travaillées par semaine.
# Appelez les fonctions précédemment créées pour calculer le salaire horaire correspondant.
# Affichez le résultat sous la forme : "Votre salaire horaire est de XX euros".


salaire_annuel = input("Veuillez saisir votre salaire annuel (sans espace) : ")
nombres_heures = input("Veuillez renseigner le nombre d'heure effectuées par semaine : ")

salaire_annuel = int(salaire_annuel)
nombres_heures = int(nombres_heures)

def salaire_mensuel(salaire_annuel):
    return salaire_annuel / 12 


def salaire_hebdo(salaire_mensuel):
    return salaire_mensuel / 4


def salaire_horaire(salaire_hebdo, nombres_heures):
    return salaire_hebdo / nombres_heures

# Calcul du salaire horaire
salaire_mensuel = salaire_mensuel(salaire_annuel)
salaire_hebdo = salaire_hebdo(salaire_mensuel)
salaire_horaire = salaire_horaire(salaire_hebdo, nombres_heures)
# Affichage du résultat
print("Votre salaire horaire est de", salaire_horaire, "euros.")



