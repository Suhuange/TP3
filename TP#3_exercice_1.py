# Eric Su
# Groupe 1234
# Jeu de combattre avec des monstres dont l'usager doit combattre avec des monstres avec de la chance!

import random


def afficher_regles():  # montre les règles du jeu
    print("""
Règles :
Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.  Dans ce cas,
le niveau de vie de l’usager est augmenté de la force de l’adversaire.
Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.
Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.
La partie se termine lorsque les points de vie de l’usager tombent sous 0.
L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.
""")


def lancer_de():
    return random.randint(1, 6)


def nouvelle_force_adversaire():
    return random.randint(1, 5)


def dernier_combat(combat_statut, score_de, force_adversaire, niveau_vie, nombre_victoires_consecutives):
    """
    Affiche le resultat du dernier combat
    """
    print(f"\n Résultat du dernier combat ")
    print(f"Lancer du dé : {score_de}")
    print(f"Force de l'adversaire : {force_adversaire}")

    if combat_statut == "victoire":
        print(f"Dernier combat : VICTOIRE")
        print(f"Niveau de vie : {niveau_vie}")
        print(f"Nombre de victoires consécutives : {nombre_victoires_consecutives}")
    else:
        print(f"Dernier combat : DÉFAITE")
        print(f"Niveau de vie : {niveau_vie}")


def jeu():  # Boucle principale du jeu de combattre des monstres
    niveau_vie = 20
    numero_adversaire = 0
    nombre_victoires = 0
    nombre_defaites = 0
    victoires_consecutives = 0
    combat_num = 0
    dernier_combat_statut = None
    dernier_score_de = None
    derniere_force_adversaire = None
    print("Bienvenue — Le combat des monstres !")
    while True:  # Deuxième boucle, combattre des monstres
        # Vérifier fin de partie
        if niveau_vie <= 0:
            print(f"\nLa partie est terminée, vous avez vaincu {nombre_victoires} monstre(s).")
            break

        numero_adversaire += 1
        force_adversaire = nouvelle_force_adversaire()
        print("\nVous tombez face à face avec un adversaire de difficulté :", {force_adversaire})

        if dernier_combat_statut is not None:
            dernier_combat(
                dernier_combat_statut,
                dernier_score_de,
                derniere_force_adversaire,
                niveau_vie,
                victoires_consecutives
            )

            dernier_combat_statut = None
            dernier_score_de = None
            derniere_force_adversaire = None
        # menu
        print("""
Que voulez-vous faire ?
 1 - Combattre cet adversaire
 2 - Contourner cet adversaire et ouvrir une autre porte (coûte 1 point de vie)
 3 - Afficher les règles du jeu
 4 - Quitter la partie
""")
        choix = input("Votre choix (1-4) : ").strip()
        if choix == "1":
            combat_num += 1
            print(f"\nAdversaire : {numero_adversaire}"
                  f"\nForce de l'adversaire : {force_adversaire}"
                  f"\nNiveau de vie : {niveau_vie}"
                  f"\nCombat {combat_num} : {nombre_victoires} victoires et {nombre_defaites} défaites")
            score_de = lancer_de()
            print("Lancer du dé :", score_de)
            if score_de > force_adversaire:
                # victoire
                niveau_vie += force_adversaire
                nombre_victoires += 1
                victoires_consecutives += 1
                print("Résultat : VICTOIRE !")
                print(f"Niveau de vie : {niveau_vie}")
                print(f"Nombre de victoires consécutives : {victoires_consecutives}")

            else:
                # défaite (<=)
                niveau_vie -= force_adversaire
                nombre_defaites += 1
                victoires_consecutives = 0
                print("Résultat : DÉFAITE.")
                print(f"Niveau de vie : {niveau_vie}")

        elif choix == "2":
            niveau_vie -= 1
            victoires_consecutives = 0
            print("\nVous évitez le combat (pénalité : -1 point de vie).")
            print(f"Niveau de vie : {niveau_vie}")

        elif choix == "3":
            afficher_regles()

        elif choix == "4":  # Fin du jeu
            print("\nMerci et au revoir...")
            print(f"Vous avez vaincu {nombre_victoires} monstre(s).")
            break

        else:
            print("\nChoix invalide — réessayez.")


if __name__ == "__main__":  # Boucle du combattre des monstres
    jeu()
