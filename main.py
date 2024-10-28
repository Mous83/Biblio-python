# coding: utf-8
import csv 
import re
import Partie1 as p1
import Partie2 as p2
import Partie3 as p3

if __name__ == "__main__":
    p1.personalisation()
    action = -1
    while action < 1 or action > 8:
        p1.ajout_ligne_matrice(p1.lire_liste_livres())
        action = int(input("Choisissez votre action : \n1. Afficher un lecteur\n2. Modifier un lecteur\n3. Supprimer un lecteur\n4. Ajouter un livre\n5. Modifier un livre\n6. Supprimer un livre\n7. Noter les livres\n8. Ne rien faire\n"))
    if action == 1: #L'utilisateur à  choisi la premiere option
        print("========== Vous avez choisis la 1ere option ============")
        p1.print_readers(p1.lire_liste_lecteur())
    elif action == 2:
        print("========== Vous avez choisis la 2eme option ============")
        edit = -1
        while edit < 1 or edit >4:
            edit = int(input("Que souhaitez vous modifier ? :\nEntrez 1 pour modifier le pseudo\nEntrez 2 pour modifier le genre\nEntrez 3 pour modifier l'age\nEntrez 4 pour modifier le genre littéraire\n"))
        if edit == 1:
            edit = str(edit)
            p1.edit_profile_name(p1.lire_liste_lecteur())
        elif edit == 2:
            edit = str(edit)
            p1.edit_profile_genre(p1.lire_liste_lecteur())
        elif edit == 3:
            edit = str =(edit)
            p1.edit_profile_age(p1.lire_liste_lecteur())
        else:
            edit = str(edit)
            p1.edit_profile_genre_litteraire(p1.lire_liste_lecteur())
    elif action == 3:
        print("========== Vous avez choisis la 3eme option ============")
        #p1.delete_readers(p1.lire_liste_lecteur())
        p1.suppression_ligne_matrice(p1.delete_readers(p1.lire_liste_lecteur()))
    elif action == 4:
        print("========== Vous avez choisis la 4eme option ============")
        p2.add_books(p2.lire_liste_livres())
    elif action == 5:
        print("========== Vous avez choisis la 5eme option ============")
        p2.rename_book(p2.lire_liste_livres())
    elif action == 6:
        print("========== Vous avez choisis la 6eme option ============")
        p2.delete_book(p2.lire_liste_livres())
    elif action == 7:
        print("========== Vous avez choisis la 7eme option ============")
        p3.notation_des_livre()
        
    else:
        print("Merci et à Bientot")