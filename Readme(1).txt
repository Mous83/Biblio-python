CE FICHIER VOUS PERMETTRA DE COMPRENDRE L'UTILISATION DE NOTRE SYSTEME DE RECOMMANDATION DE LIVRES:

Les membres de l'équipe ayant réalisé le projet sont:
Yilmaz Arnaud
Munto Kevin
Valatta Hippolyte

Le but principal est de créer un outil informatique qui permet de suggérer aux lecteurs des livres en fonction de leurs précédentes lectures et de leurs profils.

Vous avez à dispoition les fichiers 'books.txt' et 'booskread'. Le fichier 'booksread' se remplira au fur et à mesure du programme et le fichier 'books.txt' sera manipulable par l'utilisateur. 

Ouvrez au préalable les fichiers 'matrice.txt' 'books.txt' 'readers.txt' 'booksread.txt' pour une éxperience optimale
Afin d'être dans des conditions optimales n'hésitez pas à mettre à jour votre version de python (python 3.10 nécessaire).
Ce projet à était réaliser avec python 3.10

Afin que vous lecteur puissiez sans problème tester notre programme utiliser un interpreteur python quelquonque(qui soit en 3.10)

Ce programme à était optimiser au maximum afin de le rendre le plus fluide possible lors de l'éxécution pour l'utilsateur, une grande partie des informations apparaissent sous forme de numero
pour décrire la position des livres, leurs noms...
L'utilisateur devra porter un regard attentif à la console afin de ne pas se perdre et devra parfois renseigner des informations lors de l'éxécution du programme.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~PARTIE 1: PROFILS DES LECTEURS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def personnalisation():
Permet de personnaliser le genre, le sexe, le nom et le prénom de l'utilisateur grâce aux informations que ce dernier va renseigner.

def lire_liste_lecteur():
Permet de mettre tout les lecteurs sous une liste.

def print_readers(liste_lecteur)
Affiche le nom des lecteurs qui sont présent dans la liste.

def edit_profile(liste_lecteur)
Grâce à cette fonction, on pourra entrer le nom du pseudo que l'on souhaite modifié et le modifié grâce à '.sub' nottament.

def edit_profile_genre(liste_lecteur)
Permet de modifier le genre en entrant le pseudo lié au changement.

def edit_profil_age(liste_lecteur)
Permet de modifier l'âge en entrant le pseudo lié au changement.

def edit_profile_genre_litteraire(liste_lecteur)
Permet de modifier le genre littereaire d'un lecteur en entrant son pseudo.

def delete_readers(liste_lecteur)
Permet de simplement supprimer un lecteur.


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~PARTIE 2: VISITER LE DEPOT DES LIVRES~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def lire_liste_livres()
On récupère les livres sous formes de liste.

def add_books(liste_de_livre)
permet d'ajouter un livre dans la liste des livres.

def rename_book(liste_de_livre)
Permet de renommer un livre en indiquant le livre à modifier et le nom du livre par quoi on souhaite le modifier.

def delete_book(liste_de_livre)
Permet de supprimer le livre renseigner.


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~PARTIE 3: RECOMMANDATION~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Si c'est la première fois que vous éxecuter ce programme n'ouvrez pas le fichier matrice car il s'ouvrira automatiquement à vide.
def matrice_a_vide()
Permet de créer une matrice qui va recommander des livres à un utilisateur par rapport à ces lectures précédentes, son genre et son âge.


Pour toute question ou problème rencontré n'hésiter pas à nous contacter sur: Yilkevhip@hotmail.com


BON LECTURE!