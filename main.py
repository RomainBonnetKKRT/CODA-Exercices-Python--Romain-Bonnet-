def exercice1():
    print("Exercice 1 : Bonjour le monde !")
    print("Hello World !")

def exercice2():
    print("Exercice 2 : Quel est ton prenom ")
    name = input("Entre ton prenom: ")
    print("Hello,", name, "! Welcome!")

def exercice3():
    print("Premiere Ligne")
    print("Deuxieme Ligne")
    print("Troisieme ligne")

def exercice4():
    print("Exercice 4 : Quel est ton annee de naissance ")
    year = int(input("Année: "))
    print("tu as",2025 - year,"ans")
    
def exercice5():
    print("Exercie 5 : donner deux chiffres et les aditionner ")
    chiffre1 = int(input("ton premier chiffre: "))
    chiffre2 = int(input("ton deuxieme chiffre: "))
    print("la sommme des chiffres est de",chiffre1 + chiffre2,)

def exercice6():
    print("Exercie 6 : donner deux chiffres et les soustraire ")
    chiffre1 = int(input("ton premier chiffre: "))
    chiffre2 = int(input("ton deuxieme chiffre: "))
    print("le resultat de la soustraction est de",chiffre1 - chiffre2,)
    
def exercice7():
    print("Exercie 7 : donner deux chiffres et les multiplier")
    chiffre1 = int(input("ton premier chiffre: "))
    chiffre2 = int(input("ton deuxieme chiffre: "))
    print("le resultat de la multiplacation est de",chiffre1 * chiffre2,)

def exercice8():
    print("Exercie 8 : donner deux chiffres et les diviser")
    chiffre1 = int(input("ton premier chiffre: "))
    chiffre2 = int(input("ton deuxieme chiffre: "))
    if chiffre2 ==0:
        print("On ne peut pas diviser par 0")
    else:
        print("le resultat de la division est de",chiffre1 / chiffre2,)

def exercice9():
    print("Exercie 9 : donner un chiffre et obtenir le carre")
    chiffre = int(input("ton chiffre: "))
    print("le carre de ton chiffre est ",chiffre * chiffre,)

def exercice10():
    print("Exercie 10 : donner un chiffre et obtenir le double")
    chiffre = int(input("ton chiffre: "))
    print("le double de ton chiffre est ",chiffre * 2,)

def exercice11():
    print("Exercie 11 : donner un chiffre et obtenir la moitie")
    chiffre = int(input("ton chiffre: "))
    print("la moitie de ton chiffre est ",chiffre * 0.5,)

def exercice12():
        print("Exercie 12 : afficher 5 fois le meme message")
        for i in range(5):
            print("ez la commande")

def exercice13():
    for i in range(1,6):
        print(i)

def exercice14():
    for i in range(1, 6):
        print(f"2 × {i} = {2 * i}")

def exercice15():
       print("Exercie 15 : avoir le périmetre d'un carre")
       longueur_coté = int(input("longueur du coté: "))
       print("le périmetre du carré c'est ",longueur_coté * 4,)

def exercice16():
    print("Exercice 16 : avoir l'air d'un carré")
    longueur_coté = int(input("longueur du coté: "))
    print("l'air du carré est ",longueur_coté * longueur_coté,)

def exercice17():
    print("Exercice 17 : conversion euro dollars")
    nombre_euro = int(input("nombre euro: "))
    print("La valeur en dollars est de",nombre_euro * 1.1,)

def exercice18():
    print("Exercice 18 : conversion minutes secondes")
    nombre_minutes = int(input("nombre minutes: "))
    print("Le temps en seconde est de",nombre_minutes * 60,)

def exercice19():
    print("Exercice 19 : Prix TTC")
    Prix = int(input("PrixHT: "))
    print("Le TTC est de",Prix * 1.2,)

def exercice20():
    print("Exercice 20 : Nom/Age")
    nom =(input("votre nom: "))
    age =(input("votre age: "))
    print(nom," a ",age,"ans",)

def exercice21():
    print("Exercice 20 : Négatif/Positif/Nul")
    chiffre =int(input("votre chiffre: "))
    if chiffre == 0 :
        print("nul")
    elif chiffre < 0 :
        print("négatif")
    elif chiffre > 0 :
        print("positif")
def exercice22():
    nombre =int(input("entrer l'age "))
    if nombre >= 18 :
        print("majeur")
    else:
        print("mineur")

def exercice23():
    nombre =int(input("entrer la note "))
    if nombre >= 10 :
        print("validé")
    else:
        print("non validé")

def exercice24():
    nombre=int(input("Inserez un nombre"))
    number=int(input("Inserez un nombre"))
    if nombre>number:
       print(f"{nombre} est plus grand que {number}")
    elif nombre<number:
       print(f"{number} est plus grand que {nombre}")

def exercice25():
    nombre=int(input("Inserez un nombre "))
    number=int(input("Inserez un nombre "))
    if nombre>number:
       print(f"{nombre} et {number} ne sont pas croissant")
    elif nombre<number:
       print(f"{nombre} et {number} sont croissant")

def exercice26():
    nombre=int(input("Inserez un nombre "))
    diviseur=int(5)
    last_digit = nombre % 10
    if last_digit == 0 or last_digit == 5:
        print(f"{nombre} est un divisible de 5")
    elif last_digit != 0 or last_digit != 5:
        print(f"{nombre} est non divisible par 5")

def exercice27():
    âge=int(input("Inserez votre âge "))
    if âge<12:
        print("Enfant")
    elif âge>18:
        print("Adulte")
    elif 12 <= âge <= 17:
        print("Adolescent")

def exercice28():
    temperature=int(input("Inserez la température de l'eau "))
    if temperature<0:
        print("l'eau est solide")
    elif temperature>100:
        print("l'eau est gazeuse")
    elif 0 <= temperature <= 100:
        print("l'eau est liquide")

def exercice29():
    note=int(input("Entrez votre note"))
    if note<10.99:
        print("Recalé")
    elif note<=13.99:
        print("Passable")
    elif note<=16.99:
        print("Bien")
    elif note<=20:
        print("Très bien")

def exercice30():
    n=int(input("Inserez votre nombre "))
    for n in range(1, n):
        print(n)

def exercice31():
    n=int(input("Inserez votre nombre "))
    for n in range(n, -1, -1):
        print(n)

def exercice32():
    n=int(input("Entrez un nombre N : "))
    somme = 0
    for i in range(1, n + 1):
        somme += i
    print(f"La somme de 1 à {n} est {somme}")

def exercice33():
    nombre=int(3)
    for i in range(1, 11):
        print(f"{i} X 3", nombre*i)










    



        

    

    
    


def main():
    while True:
        print("\n=== Menu des exercices ===")
        print("q - Quitter")
        choix = input("Entrez le numéro de l'exercice à exécuter : ").strip().lower()

        if choix == "1":
            exercice1()
        elif choix == "2":
            exercice2()
        elif choix == "3":
            exercice3()
        elif choix == "4":
            exercice4()
        elif choix == "5":
            exercice5()
        elif choix == "6":
            exercice6()
        elif choix =="7":
            exercice7()
        elif choix == "8":
            exercice8()
        elif choix == "9":
            exercice9()
        elif choix == "10":
            exercice10()  
        elif choix == "11":
            exercice11()
        elif choix == "12":
            exercice12()
        elif choix == "13":
            exercice13()
        elif choix == "14":
            exercice14()
        elif choix == "15":
            exercice15()
        elif choix == "16":
            exercice16()
        elif choix == "17":
            exercice17()
        elif choix == "18":
            exercice18()
        elif choix == "19":
            exercice19()
        elif choix == "20":
            exercice20()
        elif choix == "21":
            exercice21()
        elif choix == "22":
            exercice22()
        elif choix == "23":
            exercice23()
        elif choix == "24":
            exercice24()
        elif choix == "25":
            exercice25()
        elif choix =="26":
            exercice26()
        elif choix == "27":
            exercice27()
        elif choix == "28":
            exercice28()
        elif choix == "29":
            exercice29()
        elif choix == "30":
            exercice30()
        elif choix == "31":
            exercice31()
        elif choix == "32":
            exercice32()
        elif choix == "33":
            exercice33()
        elif choix == "34":
            exercice34()
        elif choix == "35":
            exercice35()
        elif choix == "36":
            exercice36()
        elif choix == "37":
            exercice37()
        elif choix == "38":
            exercice38()
        elif choix == "39":
            exercice39()
        elif choix == "40":
            exercice40()
        elif choix == "q":
            print("Au revoir 👋")
            break
        else:
            print("⚠️ Choix non reconnu. Essayez encore.")

        # Pause entre deux exécutions pour laisser le temps de lire
        input("\nAppuyez sur Entrée pour revenir au menu...")

if __name__ == "__main__":
    main()
