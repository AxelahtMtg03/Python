    #faire un calcul puis le revoyer dans la console
"""""
def f (x):
    return 2*x + 4

print (f (3))
"""""
    #autre maniere
"""""
def f (a,b,c):
    return a*b +c
print (f(1,2,3))
"""""
    #faire dire un message dans la console de plusieur maniere
"""""
def mes (message):
    print(message)
mes("hello word")
"""""
    #autre maniere
"""""
def mes ():
    print("hello word")
mes()
"""""
    #autre maniere 
"""""
print("Hello world")
"""""
    #type a l'interieur des()
"""
print(type("salutation")) = chaine de caractere = string(str)
print(type(30)) = nombre entier = int 
print(type(1.5)) = nombre decimal = float
print(type(True)) bolean = bool
"""
    #boucle while

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
    #boucle avec for
"""
for i in range(100):
    print(str(i).zfill(5))
"""
    #operateur
"""
additionner = +
soustraire = -
diviser = /
multiplier = *
modulo = %  = recupere le reste d'une division
division entiere = // = faire un division et de rexupere le nombre entier
puissance = ** 
egal a = == 
different de = !=
"""
