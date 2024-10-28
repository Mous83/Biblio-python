#coding: utf-8
import csv
from os import path
import Partie1 as p1
import Partie2 as p2

def matrice_a_vide():
    
    liste_de_livre = []
    liste_lecteur = []
    with open('readers.txt', 'r+',encoding='utf-8') as f:
        lecteur = enumerate(csv.reader(f)) #On lit le fichier csv
        i = 0
        for i, ligne in lecteur: # i est le compteur et ligne est la ligne complete
            if i >= 0:
                prenom = ligne[0].split(',') #On decoupe les profil en virgules
                nom = prenom[0].strip() #on supprime les espaces et crochet 
                liste_lecteur.append(nom) #on ajoute a la liste les noms
    liste_de_livre = []
    with open('books.txt', 'r',encoding='utf-8') as f:
        lecteur = f.readlines() 
        for  ligne in lecteur:
            ligne = ligne.strip('\n') 
            liste_de_livre.append(ligne)
    matrice_a_vide = []
    for i in range(len(liste_lecteur)):
        L = []
        for i in range(len(liste_de_livre)):
            L.append(0)
        matrice_a_vide.append(L)

    if not path.isfile('matrice.txt'): # JE VEUX LE FAIRE UNIQUEMENT SI LE FICHIER N'EXISTE PAS 
        with open('matrice.txt','w', encoding='utf-8')as f:
            for i in range(len(matrice_a_vide)):
                for j in range(len(matrice_a_vide[i])):
                    matrice_a_vide[i] = str(matrice_a_vide[i]).replace('[','').replace(']','').replace(',','') 
                f.write(matrice_a_vide[i]+'\n')

# JE SAIS INITIALSER UNE MATRICE A VIDE AU CAS OU IL LE FAUT

def notation_des_livre():
    
    liste_de_livre = []
    liste_lecteur = []
    with open('readers.txt', 'r',encoding='utf-8') as f:
        lecteur = enumerate(csv.reader(f)) #On lit le fichier csv
        i = 0
        for i, ligne in lecteur: # i est le compteur et ligne est la ligne complete
            if i >= 0:
                prenom = ligne[0].split(',') #On decoupe les profil en virgules
                nom = prenom[0].strip() #on supprime les espaces et crochet 
                liste_lecteur.append(nom) #on ajoute a la liste les noms
    liste_de_livre = []
    with open('books.txt', 'r',encoding='utf-8') as f:
        lecteur = f.readlines() 
        for  ligne in lecteur:
            ligne = ligne.strip('\n') 
            liste_de_livre.append(ligne)

    matrice_remplie = []
    with open('matrice.txt', 'r') as f:
            for line in f:
                matrice_remplie.append(list(map(int,line.split())))
            
    name= input('Veuillez entrer un pseudo avec lequel vous souhaiter noter les livres : ')
    while name not in liste_lecteur:
        name = input("Pseudo non existant, veuillez entrez un pseudo correct : ")

    with open('readers.txt', "r", encoding='utf-8') as f:
        i = -1
        for profile in f:
            i += 1
            if name == profile.split(',')[0]:
                number_line = i
                profile = profile.strip('\n')
    book_rate=input("Quel est le livre que vous voulez noter : ")
    while book_rate not in liste_de_livre:
        book_rate=input("Ce livre est inéxistant, veuillez saisir le livre que vous voulez noter : ")

    for i in range(len(liste_de_livre)):
        if book_rate == liste_de_livre[i]:
            indexbook = i
            indexbook = str(indexbook)

    profile = []
    with open('booksread.txt', "r", encoding='utf-8') as f:
        for profile in f:
            if name == profile.split(',')[0]:
                profile = profile.strip('\n')
                profile = profile.split(',')
    for i in range(1, len(profile)):
        if indexbook == profile[i]:
            print("eligible")

    print("Pouvez vous noter de 1 à 5 le livre : ",book_rate,"\nLe numero 1 veut dire que vous n'avez pas aimé le livre, le numéro 5 indique que le livre est excellent ") 
    rating = int(input())

    while rating < 1 or rating > 5:
        rating = int(input("Entrez un nombre entre 1 et 5 : \n"))

    indexbook = int(indexbook)
    matrice_remplie[number_line][indexbook] = rating
    txt_to_write = ""

    for i in range(len(matrice_remplie)):
        txt_to_write = txt_to_write+str(matrice_remplie[i]).replace('[','').replace(']','').replace(',','')+'\n'

    with open('matrice.txt', 'w', encoding='utf-8')as f:
        f.writelines(txt_to_write)
        


    