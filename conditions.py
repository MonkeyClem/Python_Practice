ensoleille = False
neige = True

if ensoleille:

    print("on va à la plage !")
elif neige: 
    
    print("Faisons un bonhomme de neige")
else : 

    print("On reste à la maison")

#Définir des conditions multiples avec des opérateurs logiques : 
print("Les opérateurs logiques :    ")

avec_soleil = True
en_semaine = False

if avec_soleil or not en_semaine: 
    print("Courage, au boulot !")
elif avec_soleil and not en_semaine:
    print("Plage, Restau ou Terrasse ?")
else : 
    print("On vas à la plage !")