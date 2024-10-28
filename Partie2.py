import csv 
import re

#=========== Recuperation des livres sous forme de liste ==================#
def lire_liste_livres(): # fonction qui permet de recuperer la liste des livres 
    liste_de_livre = [] # intitialisation de la liste de livres
    with open('books.txt', 'r',encoding='utf-8') as f: # lecture du fichier books.txt
        livre = f.readlines() #on lit le fichier ligne par lignes
        for  ligne in livre: # on parcour la liste "livre"
            ligne = ligne.strip('\n') #on enleve le '\n'
            liste_de_livre.append(ligne) # on ajoute la ligne dans la liste
    
    return liste_de_livre # on retourne la liste pour pouvoir l'importer
#=============== AJOUTER UN LIVRE ==============#
def add_books(liste_de_livre): # fonction qui permet d'ajouter un livre dans la liste des livres
    new_book=input("Veuillez entrer le nom du livre a ajouter : ")
    while new_book in liste_de_livre: # saisie sécurisée au cas ou l'utilisateur entre un livre existant 
        new_book = input("Ce livre existe déja veuillez entrer un livre n'existant pas dans notre biblitotheque : ")
    if new_book!="":
        with open("books.txt", "a")as f: 
            f.write('\n'+new_book) # ecriture du nouveau livre dans le fichier books.txt
            print("Youpi ! Vous venez d'ajouter le livre",new_book) 
            liste_de_livre.append(new_book) #on ajoute le nouveau livre a la liste

#============ MODIFIER LIVRE =============#
def rename_book(liste_de_livre): # fonction qui modifie le titre du livre
    old_book=input("Quel est le livre que vous voulez modifier : ") 
    while old_book not in liste_de_livre: # saisie sécurisée au cas ou l'utilisateur entre un livre non existant
        old_book=input("Ce livre est inéxistant, veuillez saisir le livre que vous voulez modifier : ")
    new_book =input("Entrez un nouveau titre pour votre livre : ")
    while new_book in liste_de_livre: # saisie sécurisée au cas ou l'utilisateur entre un livre existant
        new_book=input('Ce livre existe deja, veuillez entrez un nouveau titre : ')
    print(old_book,'devient maintenant',new_book,'.')
    fichier = open("books.txt", "r") # ouverture du fichier
    rep = ""
    for line in fichier: 
        line = line.strip()
        changement = line.replace(old_book,new_book) # on remplace l'ancien nom du livre par un nouveau
        rep = rep + changement + "\n"
    fichier.close()
    fichier1 = open("books.txt", "w")
    fichier1.write(rep)
    fichier1.close()
    
#================= SUPPRIMER LIVRE ====================#
def delete_book(liste_de_livre): # fonction qui supprime un livre
    deleted_book = input("Entrez le livre que vous souhaiter supprimer : ")
    while deleted_book not in liste_de_livre: # saisie sécurisée au cas ou l'utilisateur entre un livre non existant
        deleted_book = input("Ce livre n'existe pas veuillez entrer un livre valide : ")
    print(deleted_book,'est desormais supprimé')
    liste_de_livre.remove(deleted_book) #suppression du livre dans la liste de livre
    with open('books.txt','w', encoding='utf-8')as f: #ouverture du fichier
        for i in liste_de_livre:
            f.write(i+'\n') #ecriture des livres
