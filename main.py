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
    print("le resultat de la division est de",chiffre1 / chiffre2,)

def exercice9():
    print("Exercie 9 : donner un chiffre et obtenir le carre")
    chiffre = int(input("ton chiffre: "))
    print("le carre de ton chiffre est ",chiffre * chiffre,)

def exercice10():
    print("Exercie 10 : donner un chiffre et obtenir le double")
    chiffre = int(input("ton chiffre: "))
    print("le carre de ton chiffre est ",chiffre * 2,)

    

    
    


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
        elif choix == "q":
            print("Au revoir 👋")
            break
        else:
            print("⚠️ Choix non reconnu. Essayez encore.")

        # Pause entre deux exécutions pour laisser le temps de lire
        input("\nAppuyez sur Entrée pour revenir au menu...")

if __name__ == "__main__":
    main()
