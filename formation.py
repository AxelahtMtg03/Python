    # premiere partie de la form
"""
x = input("Name ?")
print("Hello " +  x)
"""
    #type a l'interieur des()
"""
print(type("salutation")) = chaine de caractere = string(str)
print(type(30)) = nombre entier = int 
print(type(1.5)) = nombre decimal = float
print(type(True)) bolean = bool
"""
    # exercice n*1
"""
nom = input("Quel est votre nom? ")
age = input("Quel est votre age? ")
try:
    age_prochain = int(age) + 1
except:
    print("Error juste les nombre")
else:
    print("Bonjour " + nom  + ". Vous avez " + age + " ans.")
    print("Bonjour " + nom  + ". Vous aurez " + str(age_prochain) + " ans l'annee prochaine.")
"""
    #Boucle avec while
"""
n = 0

while n < 10:
    print("Valeur de n : " + str(n))
    n = n + 1
print("")
print("Fin de la boucle")
"""
    #exemple de boucle cas concret
"""
motDePasse = ""

while not motDePasse == "toto":
    motDePasse = input("Quel est votre mot de passe? ")
    print("mot de passe pas corect")
print("mot de passe corect")
"""
    #ameliorer le programme grace aux boucle
def demanderLeNom():
    Nom = ""
    while Nom == "":
        Nom = input("Quel est votre nom? ")
    return Nom

def demander_age():
    ageInt = 0
    while ageInt <= 0:
        age_str = input("Quel est votre age? ")
        try:
            ageInt = int(age_str)
        except:
            print("Error juste les nombres")

        if ageInt < 0:
            print("Error juste les nombres positifs")

    return ageInt

def retour():
    print("Bonjour " + nom  + ". Vous avez " + str(age) + " ans.")
    print("Bonjour " + nom  + ". Vous aurez " + str(age+1) + " ans l'annee prochaine.")

nom = demanderLeNom()
age = demander_age()

if age > 18:
    print("Vous etes majeur")
elif age == 17:
    print("Vous etes preque majeur")
elif age == 1 or age == 2:
    print("Vous etes un bebe")
elif 12 <= age < 18:
    print("Vous etes un ado")
elif age == 18:
    print("felicitation pile majeur")
elif age > 60:
    print("Vous etes senior")
else:
    print("Vous n'etes pas majeur")

console = retour()