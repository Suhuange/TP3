# Eric Su
# Groupe 1234
# Jeu de combattre avec des monstres dont l'usager doit combattre avec des monstres avec de la chance!

import random


def afficher_regles(): # montre les règles du jeu
    print("""
Règles :
- Vous commencez avec 20 points de vie.
- À chaque adversaire une force aléatoire entre 1 et 5.
- Pour gagner il faut que le lancer (1-6) soit STRICTEMENT supérieur à la force de l'adversaire.
  - Victoire : vos points de vie augmentent de la force de l'adversaire.
  - Défaite : vos points de vie diminuent de la force de l'adversaire.
- Éviter un adversaire coûte 1 point de vie.
- La partie se termine si vos points de vie <= 0.
""")


def lancer_de(): # creation du dé
    return random.randint(1, 6)


def nouvelle_force_adversaire(): # creation du force de l'adversaire
    return random.randint(1, 5)


def jeu(): # Boucle principale du jeu de combattre des monstres
    niveau_vie = 20
    numero_adversaire = 0
    nombre_victoires = 0
    nombre_defaites = 0
    victoires_consecutives = 0
    combat_num = 0

    print("Bienvenue — Le combat des monstres !")
    while True: # Deuxième boucle, combattre des monstres
        # Vérifier fin de partie
        if niveau_vie <= 0:
            print(f"\nLa partie est terminée, vous avez vaincu {nombre_victoires} monstre(s).")
            break

        numero_adversaire += 1
        force_adversaire = nouvelle_force_adversaire()
        print("\nVous tombez face à face avec un adversaire de difficulté :", force_adversaire) # Description du combat

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
            print(f"\nStatut avant combat :"
                  f"\nAdversaire : {numero_adversaire}"
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

        elif choix == "4": # Fin du jeu
            print("\nMerci et au revoir...")
            print(f"Vous avez vaincu {nombre_victoires} monstre(s).")
            break

        else:
            print("\nChoix invalide — réessayez.")


if __name__ == "__main__": # Boucle du combattre des monstres
    jeu()
