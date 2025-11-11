# Eric Su
# Groupe 1234
# Jeu de combattre avec des monstres dont l'usager doit combattre avec des monstres avec de la chance!

import random


def afficher_regles():  # montre les règles du jeu
    """
    Affiche les règles du jeu à l'utilisateur
    """
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
    """
    Simule le lancer d'un dé à 6 faces
    Retourne un nombre aléatoire entre 1 et 6
    """
    return random.randint(1, 6)


def nouvelle_force_adversaire():
    """
    Génère une force aléatoire pour un nouvel adversaire
    Retourne un nombre entre 1 et 5
    """
    return random.randint(1, 5)


def dernier_combat(combat_statut, score_de, force_adversaire, niveau_vie, nombre_victoires_consecutives):
    """
    Affiche le résultat du dernier combat
    Paramètres:
    - combat_statut: "victoire" ou "défaite"
    - score_de: résultat du lancer de dé
    - force_adversaire: force de l'adversaire combattu
    - niveau_vie: niveau de vie actuel du joueur
    - nombre_victoires_consecutives: nombre de victoires consécutives
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
    """
    Fonction principale qui gère le déroulement du jeu
    Contient la boucle de jeu principale et la logique des combats
    """
    # Initialisation des variables du jeu
    niveau_vie = 20  # Points de vie initiaux du joueur
    numero_adversaire = 0  # Compteur d'adversaires rencontrés
    nombre_victoires = 0  # Total des victoires
    nombre_defaites = 0  # Total des défaites
    victoires_consecutives = 0  # Victoires d'affilée
    combat_num = 0  # Numéro du combat actuel
    
    # Variables pour mémoriser le dernier combat
    dernier_combat_statut = None
    dernier_score_de = None
    derniere_force_adversaire = None
    
    print("Bienvenue — Le combat des monstres !")
    
    while True:  # Boucle principale du jeu
        # Vérifier si la partie est terminée (points de vie épuisés)
        if niveau_vie <= 0:
            print(f"\nLa partie est terminée, vous avez vaincu {nombre_victoires} monstre(s).")
            break

        # Préparation du nouvel adversaire
        numero_adversaire += 1
        force_adversaire = nouvelle_force_adversaire()
        print("\nVous tombez face à face avec un adversaire de difficulté :", {force_adversaire})

        # Affichage du résultat du combat précédent (si applicable)
        if dernier_combat_statut is not None:
            dernier_combat(
                dernier_combat_statut,
                dernier_score_de,
                derniere_force_adversaire,
                niveau_vie,
                victoires_consecutives
            )
            # Réinitialiser les données du dernier combat après affichage
            dernier_combat_statut = None
            dernier_score_de = None
            derniere_force_adversaire = None
            
        # Affichage du menu des actions possibles
        print("""
Que voulez-vous faire ?
 1 - Combattre cet adversaire
 2 - Contourner cet adversaire et ouvrir une autre porte (coûte 1 point de vie)
 3 - Afficher les règles du jeu
 4 - Quitter la partie
""")
        choix = input("Votre choix (1-4) : ").strip()
        
        # Option 1: Combattre l'adversaire
        if choix == "1":
            combat_num += 1
            # Affichage des informations du combat
            print(f"\nAdversaire : {numero_adversaire}"
                  f"\nForce de l'adversaire : {force_adversaire}"
                  f"\nNiveau de vie : {niveau_vie}"
                  f"\nCombat {combat_num} : {nombre_victoires} victoires et {nombre_defaites} défaites")
            
            # Lancer du dé pour déterminer l'issue du combat
            score_de = lancer_de()
            print("Lancer du dé :", score_de)
            
            if score_de > force_adversaire:
                # VICTOIRE: le dé est supérieur à la force de l'adversaire
                niveau_vie += force_adversaire  # Gain de points de vie
                nombre_victoires += 1
                victoires_consecutives += 1
                print("Résultat : VICTOIRE !")
                print(f"Niveau de vie : {niveau_vie}")
                print(f"Nombre de victoires consécutives : {victoires_consecutives}")
                
                # Mémoriser les données pour l'affichage du prochain tour
                dernier_combat_statut = "victoire"
                dernier_score_de = score_de
                derniere_force_adversaire = force_adversaire

            else:
                # DÉFAITE: le dé est inférieur ou égal à la force de l'adversaire
                niveau_vie -= force_adversaire  # Perte de points de vie
                nombre_defaites += 1
                victoires_consecutives = 0  # Réinitialiser le compteur de victoires consécutives
                print("Résultat : DÉFAITE.")
                print(f"Niveau de vie : {niveau_vie}")
                
                # Mémoriser les données pour l'affichage du prochain tour
                dernier_combat_statut = "défaite"
                dernier_score_de = score_de
                derniere_force_adversaire = force_adversaire

        # Option 2: Éviter le combat
        elif choix == "2":
            niveau_vie -= 1  # Pénalité pour avoir évité le combat
            victoires_consecutives = 0  # Réinitialiser le compteur de victoires consécutives
            print("\nVous évitez le combat (pénalité : -1 point de vie).")
            print(f"Niveau de vie : {niveau_vie}")

        # Option 3: Afficher les règles
        elif choix == "3":
            afficher_regles()

        # Option 4: Quitter le jeu
        elif choix == "4":
            print("\nMerci et au revoir...")
            print(f"Vous avez vaincu {nombre_victoires} monstre(s).")
            break

        # Gestion des choix invalides
        else:
            print("\nChoix invalide — réessayez.")


if __name__ == "__main__":  # Point d'entrée du programme
    jeu()  # Lancement du jeu
