# Eric Su
# Groupe 1234
# Jeu de combattre avec des monstres dont l'usager doit combattre avec des monstres avec de la chance!
# exercice 2

# combat_des_monstres_boss.py
# Jeu "Le combat des monstres" — variante exercice 2 (boss après 3 victoires consécutives)
# Français — Terminal

import random


def afficher_regles():  # montre les règles du jeu
    print("""
Règles :
- Vous commencez avec 20 points de vie.
- Adversaires normaux : force aléatoire entre 1 et 5.
- Boss (apparaît après 3 victoires consécutives) : force aléatoire entre 6 et 10.
- Combat normal : on lance 1 dé (1..6). Victoire si dé > force adversaire.
- Combat contre boss : on lance 2 dés (somme 2..12). Victoire si somme > force du boss.
- Victoire : vous gagnez en points de vie = force de l'adversaire (ajoutés).
- Défaite : vous perdez en points de vie = force de l'adversaire.
- Éviter un adversaire : -1 point de vie.
- La partie se termine si vos points de vie <= 0 ou si vous choisissez de quitter.
""")


def lancer_de(n=1):
    """Retourne la somme de n lancers de 1..6."""
    return sum(random.randint(1, 6) for _ in range(n))


def nouvelle_force_adversaire(victoires_consecutives, boss_after=3):
    """
    Renvoie (force, est_boss).
    Si victoires_consecutives >= boss_after => boss (force 6..10).
    Sinon adversaire normal (force 1..5).
    """
    if victoires_consecutives >= boss_after:
        return random.randint(6, 10), True
    else:
        return random.randint(1, 5), False


def dernier_combat(combat_statut, score_de, force_adversaire, niveau_vie, nombre_victoires_consecutives):
    """
    Affiche le resultat du dernier combat
    """
    print(f"\nRésultat du dernier combat ")
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
    vie = 20
    numero_adversaire = 0
    victoires = 0
    defaites = 0
    combat_num = 0
    victoires_consecutives = 0
    boss_after = 3  # paramètre : boss après 3 victoires consécutives
    dernier_combat_statut = None
    dernier_score_de = None
    derniere_force_adversaire = None

    print("=== Bienvenue : Le combat des monstres (variante boss) ===")

    while True:  # Deuxième boucle, combattre des monstres
        if vie <= 0:
            print("\nVous n'avez plus de points de vie. La partie est terminée.")
            break

        numero_adversaire += 1
        force, est_boss = nouvelle_force_adversaire(victoires_consecutives, boss_after=boss_after)

        if est_boss:
            print(f"\n!!! UN BOSS APPARAÎT (après {boss_after} victoires consécutives) !!!")
            # reset de la chaîne de victoires pour éviter réapparition immédiate
            victoires_consecutives = 0
        else:
            print(f"\nVous tombez face à face avec un adversaire de difficulté :", {force})  # Description du combat

            if dernier_combat_statut is not None:
                dernier_combat(
                    dernier_combat_statut,
                    dernier_score_de,
                    derniere_force_adversaire,
                    vie,
                    victoires_consecutives
                )

                dernier_combat_statut = None
                dernier_score_de = None
                derniere_force_adversaire = None

        print("""
Choix :
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
                  f"\nForce de l'adversaire : {force}"
                  f"\nNiveau de vie : {vie}"
                  f"\nCombat {combat_num} : {victoires} victoires et {defaites} défaites"
                  f"\nDernier combat : {dernier_combat_statut}")
            # combat
            if est_boss:
                # boss: lance 2 dés
                de = lancer_de(2)
                print(f"Lancer des 2 dés : {de}")
            else:
                de = lancer_de(1)
                print(f"lancer du dé : {de}")

            if de > force:
                # victoire
                vie += force
                victoires += 1
                victoires_consecutives += 1
                dernier_combat_statut = "victoire"
                dernier_score_de = de
                derniere_force_adversaire = force
                print("\n>>> VICTOIRE ! <<<")
                print(f"Vous gagnez {force} points de vie.")
                print(f"Points de vie : {vie}")
                print(f"Victoire(s) consécutive(s) : {victoires_consecutives}")
            else:
                # défaite (dé <= force)
                vie -= force
                defaites += 1
                victoires_consecutives = 0
                dernier_combat_statut = "défaite"
                dernier_score_de = de
                derniere_force_adversaire = force
                print("\n--- DÉFAITE ---")
                print(f"Vous perdez {force} points de vie.")
                print(f"Points de vie : {vie}")

        elif choix == "2":
            vie -= 1
            victoires_consecutives = 0
            print("\nVous évitez l'adversaire (coût : -1 point de vie).")
            print(f"Points de vie : {vie}")

        elif choix == "3":
            afficher_regles()

        elif choix == "4":
            print("\nVous quittez la partie.")
            break

        else:
            print("\nChoix invalide — taper 1, 2, 3 ou 4.")

    # résumé final
    print("\n=== Résumé de la partie ===")
    print(f"Victoires : {victoires}")
    print(f"Défaites  : {defaites}")
    print(f"Points de vie finaux : {max(vie, 0)}")
    print("Merci d'avoir joué !")


if __name__ == "__main__":
    jeu()
