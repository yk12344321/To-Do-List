import datetime
import os
import json 

def charger_memoire():
    if os.path.exists("memoire.json"):
        with open("memoire.json","r", encoding="utf-8")as fichier:
            return json.load(fichier)
    else:
        return {"taches": []}

def sauvegarder_memoire(donnees):
    with open("memoire.json", "w", encoding="utf-8")as fichier:
        json.dump(donnees, fichier, indent=4, ensure_ascii=False)

def ajouter_tache(donnees):
    nom=input("Nom de la tâche : ")
    date=datetime.datetime.now().strftime("%d/%m/%Y")

    nouvelle_tache = {
        "nom" : nom ,
        "date": date ,
        "statut" :"en cours"
    }
    donnees["taches"].append(nouvelle_tache)
    sauvegarder_memoire(donnees)
    print("Tâche ajoutée !")

def afficher_taches(donnees):

    for i, tache in enumerate(donnees["taches"]):

        print("-------------------")
        print("Numéro :", i + 1)
        print("Tâche :", tache["nom"])
        print("Date :", tache["date"])
        print("Statut :", tache.get("statut","en cours"))

def terminer_tache(donnees):

    afficher_taches(donnees)

    numero = int(input("Numéro de la tâche : "))

    if 1 <= numero <= len(donnees["taches"]):

        donnees["taches"][numero - 1]["statut"] = "terminee"

        sauvegarder_memoire(donnees)

        print("Tâche terminée !")

    else:
        print("Numéro invalide.")


def supprimer_tache(donnees):

    afficher_taches(donnees)

    numero = int(input("Numéro de la tâche : "))

    if 1 <= numero <= len(donnees["taches"]):

        donnees["taches"].pop(numero - 1)

        sauvegarder_memoire(donnees)

        print("Tâche supprimée !")

    else:
        print("Numéro invalide.")



def To_Do():

    donnees = charger_memoire()

    while True:

        print("\n========== TO DO LIST ==========")
        print("0 - Ajouter une tâche")
        print("1 - Afficher les tâches")
        print("2 - Terminer une tâche")
        print("3 - Supprimer une tâche")
        print("4 - Quitter")

        try:
            choix = int(input("Votre choix : "))

            if choix == 0:
                ajouter_tache(donnees)

            elif choix == 1:
                afficher_taches(donnees)

            elif choix == 2:
                terminer_tache(donnees)

            elif choix == 3:
                supprimer_tache(donnees)

            elif choix == 4:
                print("Fermeture du programme.")
                break

            else:
                print("Choix invalide.")

        except ValueError:
            print("Veuillez entrer un nombre valide.")


To_Do()