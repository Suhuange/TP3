# Eric Su
# Groupe 1234
# Jeu de combattre avec des monstres dont l'usager doit combattre avec des monstres avec de la chance!
# Exercice 4

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
Le Boss apparaît après 3 victoires consécutives : force aléatoire entre 9 et 12.
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
            print(f"\nLa partie est terminée, vous avez vaincu {victoires} monstre(s)")
            break

        numero_adversaire += 1
        force, est_boss = nouvelle_force_adversaire(victoires_consecutives, boss_after=boss_after)

        if est_boss:
            print(f"\n!!! UN BOSS APPARAÎT (après {boss_after} victoires consécutives) !!!")
            print(f"Force du boss : {force}")
            # reset de la chaîne de victoires pour éviter réapparition immédiate
            victoires_consecutives = 0
        else:
            print(f"\nVous tombez face à face un adversaire de difficulté: {force}")  # Description du combat
        print(f"Points de vie actuels : {vie}")
        print("""
Que voulez-vous faire?
 1 - Combattre cet adversaire
 2 - Contourner cet adversaire et aller ouvrir une autre porte (coûte 1 point de vie)
 3 - Afficher les règles du jeu
 4 - Quitter la partie
""")
        choix = input("Votre choix (1-4) : ").strip()
        if choix == "1":
            # combat : toujours 2 dés en exercice 4
            de = lancer_de(2)
            print(f"Adversaire : {numero_adversaire}"
                  f"Force de l'adversaire : {force}"
                  f"Niveau de vie de l'usager : {vie}"
                  f"Combat {numero_adversaire} : {victoires} victoires et {defaites} defaites"
                  f"Lancer du dé : {de}")

            if de > force:
                # victoire
                vie += force
                victoires += 1
                victoires_consecutives += 1
                print("\n>>> VICTOIRE ! <<<")
                print(f"Vous gagnez {force} points de vie.")
                print(f"Niveau de vie : {vie}")
                print(f"Nombre de Victoires consécutives : {victoires_consecutives}")
            else:
                # défaite (dé <= force)
                vie -= force
                defaites += 1
                victoires_consecutives = 0
                print("\n--- DÉFAITE ---")
                print(f"Vous perdez {force} points de vie.")
                print(f"Niveau de vie : {vie}")

        elif choix == "2":
            vie -= 1
            victoires_consecutives = 0
            print("\nVous évitez l'adversai")

        elif choix == "3":
            print(afficher_regles())

        elif choix == "4":
            print("Merci et au revoir...")
            break


def main():
    print("Combattre de monstres")
    while True:
        jeu()
        while True:
            reponse = input("Rejouer? (o/n): ").strip().lower()
            if reponse in "o":
                break  # rejouer
            if reponse in "n":  # fin du programme parce que l'usager quitte
                print("Merci et au revoir")
                return
            print("Répondre avec 'o' ou 'n'.")


if __name__ == "__main__":
    main()
