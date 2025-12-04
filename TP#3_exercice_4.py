# Eric Su
# Groupe 1234
# Jeu "Le combat des monstres" — variante exercice 4 (combat de 2 dés)

import random


def afficher_regles():  # montre les règles du jeu
    """
    Affiche les règles complètes du jeu incluant le système de boss et les 2 dés
    """
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


def lancer_de():
    """Retourne la somme de 2 lancers de dé à 6 faces. (exercice 4)."""
    return sum(random.randint(1, 6) for _ in range(2))


def nouvelle_force_adversaire(victoires_consecutives, boss_after=3):
    """
    Détermine la force et le type du prochain adversaire
    Paramètres:
    - victoires_consecutives: nombre de victoires d'affilée du joueur
    - boss_after: seuil de victoires pour faire apparaître un boss (défaut: 3)

    Retourne:
    - force: valeur numérique de la force
    - est_boss: booléen indiquant si c'est un boss
    """
    if victoires_consecutives >= boss_after:
        # Boss: force entre 9 et 12 (plus fort que l'exercice 2)
        return random.randint(9, 12), True
    else:
        # Adversaire normal: force entre 2 et 8 (modifié pour l'exercice 4)
        return random.randint(2, 8), False


def jeu():  # Boucle principale du jeu de combattre des monstres
    """
    Fonction principale qui gère une partie complète du jeu
    avec le système de boss et l'utilisation de 2 dés pour tous les combats
    """

    # Initialisation des statistiques du joueur
    vie = 20  # Points de vie initiaux
    numero_adversaire = 0  # Compteur d'adversaires rencontrés
    victoires = 0  # Total des victoires
    defaites = 0  # Total des défaites
    victoires_consecutives = 0  # Compteur de victoires d'affilée
    boss_after = 3  # Seuil pour faire apparaître un boss

    print("=== Bienvenue : Le combat des monstres (variante 2 dés) ===")
    afficher_regles()

    while True:  # Boucle principale du jeu - se répète pour chaque adversaire

        # Vérification de la condition de fin de partie (points de vie épuisés)
        if vie <= 0:
            print(f"\nLa partie est terminée, vous avez vaincu {victoires} monstre(s)")
            break

        # Préparation du nouvel adversaire
        numero_adversaire += 1
        force, est_boss = nouvelle_force_adversaire(victoires_consecutives, boss_after=boss_after)

        # Affichage spécial pour les boss
        if est_boss:
            print(f"\n!!! UN BOSS APPARAÎT (après {boss_after} victoires consécutives) !!!")
            print(f"Force du boss : {force}")
            # Réinitialisation du compteur pour éviter les boss en chaîne
            victoires_consecutives = 0
        else:
            print(f"\nVous tombez face à face un adversaire de difficulté: {force}")

        # Affichage des points de vie actuels
        print(f"Points de vie actuels : {vie}")

        # Menu des actions disponibles
        print("""
Que voulez-vous faire?
 1 - Combattre cet adversaire
 2 - Contourner cet adversaire et aller ouvrir une autre porte (coûte 1 point de vie)
 3 - Afficher les règles du jeu
 4 - Quitter la partie
""")
        choix = input("Votre choix (1-4) : ").strip()

        # Option 1: Combattre l'adversaire
        if choix == "1":
            # Combat : toujours 2 dés en exercice 4 (contrairement à l'exercice 2)
            de = lancer_de()

            # Affichage des informations du combat
            print(f"\nAdversaire : {numero_adversaire}")
            print(f"Force de l'adversaire : {force}")
            print(f"Niveau de vie de l'usager : {vie}")
            print(f"Combat {numero_adversaire} : {victoires} victoires et {defaites} defaites")
            print(f"Lancer des deux dé : {de}")

            # Résolution du combat
            if de > force:
                # VICTOIRE - le score des dés est supérieur à la force de l'adversaire
                vie += force  # Gain de points de vie égaux à la force de l'adversaire
                victoires += 1  # Incrémentation victoires totales
                victoires_consecutives += 1  # Incrémentation victoires consécutives
                print("\n>>> VICTOIRE ! <<<")
                print(f"Vous gagnez {force} points de vie.")
                print(f"Niveau de vie : {vie}")
                print(f"Nombre de Victoires consécutives : {victoires_consecutives}")
            else:
                # DÉFAITE - le score des dés est inférieur ou égal à la force de l'adversaire
                vie -= force  # Perte de points de vie égaux à la force de l'adversaire
                defaites += 1  # Incrémentation défaites totales
                victoires_consecutives = 0  # Réinitialisation victoires consécutives
                print("\n--- DÉFAITE ---")
                print(f"Vous perdez {force} points de vie.")
                print(f"Niveau de vie : {vie}")

        # Option 2: Éviter le combat
        elif choix == "2":
            vie -= 1  # Pénalité de 1 point de vie pour l'évitement
            victoires_consecutives = 0  # Réinitialisation victoires consécutives
            print("\nVous évitez l'adversaire (coût : -1 point de vie).")
            print(f"Points de vie : {vie}")

        # Option 3: Afficher les règles
        elif choix == "3":
            afficher_regles()  # Appel correct de la fonction (sans print supplémentaire)

        # Option 4: Quitter la partie en cours
        elif choix == "4":
            print("Merci et au revoir...")
            break

        # Gestion des choix invalides
        else:
            print("Choix invalide, taper 1, 2, 3 ou 4.")


def main():
    """
    Permet à l'utilisateur de rejouer sans relancer le programme
    """
    print("Combattre de monstres")

    while True:  # Boucle externe pour les parties multiples
        # Lancement d'une nouvelle partie
        jeu()

        # Proposition de rejouer
        while True:
            reponse = input("Rejouer? (o/n): ").strip().lower()
            if reponse in "o":
                break  # Sort de la boucle de confirmation et relance une nouvelle partie
            if reponse in "n":
                # Fin du programme
                print("Merci et au revoir")
                return
            # Gestion des réponses invalides
            print("Répondre avec 'o' ou 'n'.")


if __name__ == "__main__":  # Point d'entrée du programme
    main()  # Lancement du jeu
