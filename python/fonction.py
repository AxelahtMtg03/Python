def majeur(age):
    if age >=18:
        return True
    return False

def info (nom="", age=0):
    if nom == "":
        print("vous n'avez pas donner le nom, l'age vaut", age)
        return
    
    if age == 0:
        print("la personne est ",nom)
    else:
        print("la persone est ", nom + "son age est ", age)
    print("le nom comporte", len(nom) + "caractère")
age = 15
print("début")
# info( age="20")
print( "est majeur", majeur(15))
print("fin")