# Eric Su
# Groupe 1234
# Jeu de combattre avec des monstres dont l'usager doit combattre avec des monstres avec de la chance!
# Exercice 4

import random


def afficher_regles():  # montre les règles du jeu
    print("""
Règles :
- Vous commencez avec 20 points de vie.
- Adversaires normaux : force aléatoire entre 2 et 8 (adapté au lancer de 2 dés).
- Boss (apparaît après 3 victoires consécutives) : force aléatoire entre 9 et 12.
- Combat : on lance 2 dés (somme 2..12). Victoire si somme > force adversaire.
- Victoire : vous gagnez en points de vie = force de l'adversaire (ajoutés).
- Défaite : vous perdez en points de vie = force de l'adversaire.
- Éviter un adversaire : -1 point de vie.
- La partie se termine si vos points de vie <= 0 ou si vous choisissez de quitter.
""")


def lancer_de(n=2):
    """Retourne la somme de n lancers de 1..6. Par défaut n=2 (exercice 4)."""
    return sum(random.randint(1, 6) for _ in range(n))


def nouvelle_force_adversaire(victoires_consecutives, boss_after=3):
    """
    Renvoie (force, est_boss).
    Si victoires_consecutives >= boss_after => boss (force 9..12).
    Sinon adversaire normal (force 2..8).
    """
    if victoires_consecutives >= boss_after:
        return random.randint(9, 12), True
    else:
        return random.randint(2, 8), False


def jeu():  # Boucle principale du jeu de combattre des monstres
    vie = 20
    numero_adversaire = 0
    victoires = 0
    defaites = 0
    victoires_consecutives = 0
    boss_after = 3  # boss après 3 victoires consécutives

    print("=== Bienvenue : Le combat des monstres (variante 2 dés) ===")
    afficher_regles()

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
            print(f"\nVous rencontrez un adversaire (numéro {numero_adversaire}).")  # Description du combat

        print(f"Force de l'adversaire : {force}")
        print(f"Points de vie actuels : {vie}")
        print("""
Choix :
 1 - Combattre
 2 - Éviter (coûte 1 point de vie)
 3 - Afficher les règles
 4 - Quitter la partie
""")
        choix = input("Votre choix (1-4) : ").strip()

        if choix == "1":
            # combat : toujours 2 dés en exercice 4
            de = lancer_de(2)
            print(f"Vous lancez 2 dés -> total : {de}")

            if de > force:
                # victoire
                vie += force
                victoires += 1
                victoires_consecutives += 1
                print("\n>>> VICTOIRE ! <<<")
                print(f"Vous gagnez {force} points de vie.")
                print(f"Points de vie : {vie}")
                print(f"Victoire(s) consécutive(s) : {victoires_consecutives}")
            else:
                # défaite (dé <= force)
                vie -= force
                defaites += 1
                victoires_consecutives = 0
                print("\n--- DÉFAITE ---")
                print(f"Vous perdez {force} points de vie.")
                print(f"Points de vie : {vie}")

        elif choix == "2":
            vie -= 1
            victoires_consecutives = 0
            print("\nVous évitez l'adversai")


if __name__ == "__main__":
    jeu()
