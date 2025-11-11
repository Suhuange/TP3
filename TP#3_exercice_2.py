# Eric Su
# Groupe 1234
# Jeu "Le combat des monstres" — variante exercice 2 (boss après 3 victoires consécutives)

import random


def afficher_regles():  # montre les règles du jeu
    """
    Affiche les règles complètes du jeu incluant le système de boss
    """
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
    """Retourne la somme de n lancers de dé à 6 faces"""
    return sum(random.randint(1, 6) for _ in range(n))


def nouvelle_force_adversaire(victoires_consecutives, boss_after=3):
    """
    Détermine la force et le type du prochain adversaire
    Paramètres:
    - victoires_consecutives: nombre de victoires d'affilée du joueur
    - boss_after: seuil de victoires pour faire apparaître un boss
    
    Retourne:
    - force: valeur numérique de la force
    - est_boss: booléen indiquant si c'est un boss
    """
    if victoires_consecutives >= boss_after:
        # Boss: force entre 6 et 10
        return random.randint(6, 10), True
    else:
        # Adversaire normal: force entre 1 et 5
        return random.randint(1, 5), False


def dernier_combat(combat_statut, score_de, force_adversaire, niveau_vie, nombre_victoires_consecutives):
    """
    Affiche le résultat détaillé du dernier combat
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
    """
    Fonction principale qui gère le déroulement complet du jeu
    avec le système de boss après 3 victoires consécutives
    """
    
    # Initialisation des statistiques du joueur
    vie = 20                           # Points de vie initiaux
    numero_adversaire = 0              # Compteur d'adversaires rencontrés
    victoires = 0                      # Total des victoires
    defaites = 0                       # Total des défaites  
    combat_num = 0                     # Numéro du combat actuel
    victoires_consecutives = 0         # Compteur de victoires d'affilée
    boss_after = 3                     # Seuil pour faire apparaître un boss
    
    # Variables pour mémoriser le dernier combat
    dernier_combat_statut = None       # "victoire" ou "défaite"
    dernier_score_de = None            # Score du dé du dernier combat
    derniere_force_adversaire = None   # Force du dernier adversaire

    print("=== Bienvenue : Le combat des monstres (variante boss) ===")

    while True:  # Boucle principale du jeu
        
        # Vérification de la condition de fin de partie
        if vie <= 0:
            print("\nVous n'avez plus de points de vie. La partie est terminée.")
            break

        # Préparation du nouvel adversaire
        numero_adversaire += 1
        force, est_boss = nouvelle_force_adversaire(victoires_consecutives, boss_after=boss_after)

        # Affichage spécial pour les boss
        if est_boss:
            print(f"\n!!! UN BOSS APPARAÎT (après {boss_after} victoires consécutives) !!!")
            # Réinitialisation du compteur pour éviter les boss en chaîne
            victoires_consecutives = 0
        else:
            print(f"\nVous tombez face à face avec un adversaire de difficulté :", {force})

            # Affichage du résultat du combat précédent (sauf pour les boss)
            if dernier_combat_statut is not None:
                dernier_combat(
                    dernier_combat_statut,
                    dernier_score_de,
                    derniere_force_adversaire,
                    vie,
                    victoires_consecutives
                )
                # Réinitialisation après affichage
                dernier_combat_statut = None
                dernier_score_de = None
                derniere_force_adversaire = None

        # Menu des actions disponibles
        print("""
Choix :
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
                  f"\nForce de l'adversaire : {force}"
                  f"\nNiveau de vie : {vie}"
                  f"\nCombat {combat_num} : {victoires} victoires et {defaites} défaites"
                  f"\nDernier combat : {dernier_combat_statut}")
            
            # Mécanique de combat différente pour les boss
            if est_boss:
                # Combat contre boss: 2 dés
                de = lancer_de(2)
                print(f"Lancer des 2 dés : {de}")
            else:
                # Combat normal: 1 dé
                de = lancer_de(1)
                print(f"lancer du dé : {de}")

            # Résolution du combat
            if de > force:
                # VICTOIRE
                vie += force                    # Gain de points de vie
                victoires += 1                 # Incrémentation victoires totales
                victoires_consecutives += 1    # Incrémentation victoires consécutives
                dernier_combat_statut = "victoire"
                dernier_score_de = de
                derniere_force_adversaire = force
                print("\n>>> VICTOIRE ! <<<")
                print(f"Vous gagnez {force} points de vie.")
                print(f"Points de vie : {vie}")
                print(f"Victoire(s) consécutive(s) : {victoires_consecutives}")
            else:
                # DÉFAITE
                vie -= force                    # Perte de points de vie  
                defaites += 1                  # Incrémentation défaites totales
                victoires_consecutives = 0     # Réinitialisation victoires consécutives
                dernier_combat_statut = "défaite"
                dernier_score_de = de
                derniere_force_adversaire = force
                print("\n--- DÉFAITE ---")
                print(f"Vous perdez {force} points de vie.")
                print(f"Points de vie : {vie}")

        # Option 2: Éviter le combat
        elif choix == "2":
            vie -= 1                           # Pénalité pour évitement
            victoires_consecutives = 0         # Réinitialisation victoires consécutives
            print("\nVous évitez l'adversaire (coût : -1 point de vie).")
            print(f"Points de vie : {vie}")

        # Option 3: Afficher les règles
        elif choix == "3":
            afficher_regles()

        # Option 4: Quitter la partie
        elif choix == "4":
            print("\nVous quittez la partie.")
            break

        # Gestion des choix invalides
        else:
            print("\nChoix invalide — taper 1, 2, 3 ou 4.")

    # Affichage du résumé final de la partie
    print("\n=== Résumé de la partie ===")
    print(f"Victoires : {victoires}")
    print(f"Défaites  : {defaites}")
    print(f"Points de vie finaux : {max(vie, 0)}")
    print("Merci d'avoir joué !")


if __name__ == "__main__":
    jeu()
