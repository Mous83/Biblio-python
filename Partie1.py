#coding: utf-8
import csv
import re
import Partie1 as p1
from Partie2 import lire_liste_livres

# =================== BIENVENUE DANS LA PARTIE 1 ===============#


def personalisation(): # initialisation de la fonction personalisation
    ouinon = ['oui','non'] 
    personalisation = input('Voulez vous initialiser le lecteur ? (Entrez oui ou non) : ')
    while personalisation not in ouinon:            #Saisie Sécurisée pour que l'utilisateur entre oui ou non
        personalisation = input("Je n'ai pas compris votre choix, veuillez s'il vous plait bien repondre : ")
        
    if personalisation == 'oui':
        L = []  #Initialisation d'une liste qui sera ecrite dans le fichier readers.txt
        #---- PSEUDO ----#
        liste_lecteur = []  #on initialise une liste qui elle recupere la liste des lecteurs lors de l'initialisation du lecteur
        with open('readers.txt', 'r+',encoding='utf-8') as f: #Ouverture du fichier 
            lecteur = enumerate(csv.reader(f)) #On lit le fichier csv
            for i, ligne in lecteur: # i est le compteur et ligne est la ligne complete
                if i >= 0: #Si le compteur est supérieur à 0
                    prenom = ligne[0].split(',') #On decoupe les profil en virgules
                    nom = prenom[0].strip() #on supprime les espaces et crochet 
                    liste_lecteur.append(nom) #on ajoute a la liste les noms
                    
        pseudo = input("Veuillez un entrez un pseudo : ")
        vide = ""
        while pseudo in liste_lecteur or pseudo == vide: #Saisie sécurisée pour que l'utilisateur rentre un pseudo différent de ceux deja rentrés
            pseudo = input("pseudo deja pris veuillez en choisir un autre ! : ")
        liste_lecteur.append(pseudo) # Ajout du nouveau lecteur dans la liste des lecteurs            
        L.append(pseudo) # Ajout du pseudo dans la liste pour l'ecrire dans le fichier readers
        
        #---- SEXE ----#
        genre = ['HOMME','FEMME', 'PEU IMPORTE'] # Initialisation d'une liste en dur de la liste genre
        g = -2
        while g <= 0 or g > len(genre) or type(g)== str : # Saisie sécurisée pour ne pas qu'il entre un numéro supérieur a la taille de la liste ou qu'il entre des lettres
            try:
                g = int(input("Entrez votre genre :\n1. HOMME \n2. FEMME \n3. PEU IMPORTE \n"))
            except:
                print("On a dit mettre des chiffres pourquoi vous mettez des lettre")
                g = int(input("Entrez votre genre :\n1. HOMME \n2. FEMME \n3. PEU IMPORTE \n"))
                
        g = str(g) #mise en chaine de caracteres du nombre pour faciliter l'ecriture dans le fichier
        L.append(g)
        
        #----- AGE -----#
        age = ['<= 18 ans','Entre 18 et 25 ans','< 25 ans'] # Initialisation d'une liste en dur de la liste age
        a = -2
        while a <= 0 or a > len(age): # Saisie sécurisée pour ne pas qu'il entre un numéro supérieur a la taille de la liste
            a = int(input("Veuillez entrez votre age : \n1. <= 18 ans \n2. Entre 18 et 24 ans \n3. < 25 ans \n"))
        a = str(a)
        L.append(a)

        #------ GENRE LITTERAIRE ----#
        style = ['Science-fiction','Biographie','Horreur','Romance','Fable','Histoire','Comédie'] # Initialisation d'une liste en dur de la liste style
        s = -2
        while s <= 0 or s > len(style): # Saisie sécurisée pour ne pas qu'il entre un numéro supérieur a la taille de la liste
            s = int(input("Veuillez entrer votre genre litteraire : \n1. Science-fiction \n2. Biographie \n3. Horreur \n4. Romance \n5. Fable \n6. Histoire \n7. Comédie \n"))
        s = str(s)
        L.append(s)
        
        #------------------------------------ CREATION ET MODIFICATION DU FICHIER READERS.TXT --------------------------------------#
        with open('readers.txt', 'a', encoding='utf-8') as f: # Ouverture du fichier texte pour y ajouter du texte
            lines = ','.join(L) #on separe les elements de la liste par des virgules
            f.write(lines) #on écrits la lignes suivie d'un \n
            f.write('\n')
        
        #------------------------- PARTIE BOOKS --------------------------#
            ################################
        livres = ['Débuter la programmation Java','Apprendre Python','Les Citations du Président Mao Tse-Toung','Don Quichotte de la Manche','Un conte de deux villes',
            'Le Seigneur des Anneaux','Le Petit Prince','Harry Potter à l’école des sorciers','Le Hobbit','Dix Petits Nègres','Le rêve dans le Pavillon rouge',
            'Le Lion, la Sorcière blanche et l’Armoire magique','Elle – She : a history of Adventure','The Da Vinci Code','Réfléchissez et devenez riche',
            'Harry Potter et le Prince de Sang mêlé','L’Alchimiste','Harry Potter et la Chambre des Secrets','L’attrape-cœurs, The Catcher in the Rye'] 
            # Liste des livres initialisée pour la longueur des livres et effectuer la saisie sécurisées
            
        livres_lus = [] # Initialisastion de la liste livres lus qui nous servira a ecrire dans le fichier booksread
        livres_lus.append(pseudo) #on ajoute le pseudo 
        with open('books.txt','r',encoding = 'utf-8') as f: #lecture du fichier books.txt
            i = 1
            for ligne in f.readlines():
                print(i,'.',ligne) # On affiche chaque livres du fichier avec un nombre correspondant a son numéro de ligne
                i += 1

        # ---- ENTREE DES LIVRES DEJA LUS ----#

        l = int(input("Parmis les livres proposés, quels sont les livres que vous avez lus ? Veuillez entrer le numéro coorespondant : \n")) #On demande à l'utilisateur les livres qu'il a lus
        l = str(l) #mise en chaine de caracteres du nombre pour faciliter l'ecriture dans le fichier
        livres_lus.append(l)# ajout du nombre dans la liste
        l = -2
        
        again = 'oui'
        while again == 'oui':
            l = int(input("Parmis les livres proposés, quels sont les livres que vous avez lus ? Veuillez entrer le numéro coorespondant : \n")) 
            while l <= 0 or l > len(livres):
                l = int(input("Parmis les livres proposés, quels sont les livres que vous avez lus ? Veuillez entrer le numéro coorespondant : \n")) # Saisie Sécurisée lorsque l'on entre un chiffre n'etant pas dans l'intervalle indiqué
            l = str(l) #mise en chaine de caracteres du nombre pour faciliter l'ecriture dans le fichier
            livres_lus.append(l) # ajout du nombre dans la liste
            again = input("Voulez vous continuez ? : ")  # On redemande à l'utilisateur si il veut continuer a entrer des livres 
        with open('booksread.txt','a',encoding = 'utf-8') as f: #ouverture du fichier booksread.txt
            lines = ','.join(livres_lus) #on separe les elements de la liste par des virgules
            f.write(lines) #on écrits la lignes suivie d'un \n
            f.write('\n')
#===================================== FONCTION POUR METTRE LES LECTEURS SOUS UNE LISTE =================================#
def lire_liste_lecteur(): # intialisation de la fonction qui recupere les lecteur
    liste_lecteur = []
    with open('readers.txt', 'r+',encoding='utf-8') as f:
        lecteur = enumerate(csv.reader(f)) #On lit le fichier csv (comma separate values)
        i = 0
        for i, ligne in lecteur: # i est le compteur et ligne est la ligne complete
            if i >= 0:
                prenom = ligne[0].split(',') #On decoupe les profil en virgules
                nom = prenom[0].strip() #on supprime les espaces et crochet 
                liste_lecteur.append(nom) #on ajoute a la liste les noms
    return liste_lecteur # on retourner la liste des lecteurs pour pouvoir l'utiliser plustard dans le code

#===================================== FONCTION POUR AFFICHER UN LECTEUR =================================#
def print_readers(liste_lecteur): #fonction qui affiche un lecteur
    name= input('Veuillez entrer le pseudo que vous souhaitez afficher : ')
    vide = ""
    while name not in liste_lecteur or name == vide: # on effectue la saisie sécurisée au cas ou l'utilisateur entre un pseudo non existant
        name = input("Le pseudo que vous souhaitez afficher est inexistant veuillez entrez un pseudo existant : ") 
    with open('readers.txt', "r", encoding='utf-8') as f: # Lecture du fichier
        for profile in f:
            if name == profile.split(',')[0]: #on met sous forme de liste le profil recherché et ils seront separé a chaque fois que l'on trouve une virgule
                profile = profile.strip('\n') # on enleve le '\n' a la fin de la ligne pour ne pas qu'elle soit affichée
                print(profile) # affichage du profile 
                
#===================================== FONCTION POUR MODIFIER UN LECTEUR =================================#
# MODIFIER PSEUDO
def edit_profile_name(liste_lecteur): # fonction qui modifie le pseudo 
    name= input('Veuillez entrer le pseudo que vous souhaitez modifier : ') 
    while name not in liste_lecteur:  # on effectue la saisie sécurisée au cas ou l'utilisateur entre un pseudo non existant
        name = input("Pseudo non existant, veuillez entrez un pseudo correct : ")
    new_name = input("Veuillez entrer votre nouveau pseudo : ")
    vide = ""
    while new_name in liste_lecteur or new_name == vide: # on effectue la saisie sécurisée au cas ou l'utilisateur entre un pseudo existant
        new_name = input("pseudo deja pris veuillez en choisir un autre ! : ") 
    print("Desormais vous n'etes plus",name,"mais",new_name,'.')
    with open('readers.txt', 'r+', encoding='utf-8') as f: #Ouverture du fichier en lecture + ecriture  
            text = f.read() # lecture du fichier
            text = re.sub(name, new_name, text) # on echange l'ancien nom par le nouveau 
            f.seek(0) # on charge la position de la ligne sans cette fonction ca ecrit a la suite de ce qu'il y avais deja
            f.write(text) # on reecris la ligne dans le fichier
            f.truncate()
    with open('booksread.txt', 'r+', encoding='utf-8') as f: #Pour plus de cohérence, on le fait aussi sur le fichier booksread
            text = f.read()
            text = re.sub(name, new_name, text)
            f.seek(0) 
            f.write(text)
            f.truncate() 

# modifier genre
def edit_profile_genre(liste_lecteur): # fonction qui modifie le genre
    name= input('Veuillez entrer le pseudo que vous souhaitez modifier : ') 
    new_genre = -1
    vide = ""
    while name not in liste_lecteur or name == vide: # on effectue la saisie sécurisée au cas ou l'utilisateur entre un pseudo non existant
        name = input("Pseudo non existant, veuillez entrez un pseudo correct : ")
    while new_genre < 1 or new_genre > 3: # saisie sécurisée pour ne pas qu'il entre un nombre hors de rang
        new_genre = int(input("Entrez de nouveau votre genre :\n1. HOMME \n2. FEMME \n3. PEU IMPORTE \n"))
    new_genre = str(new_genre)
    with open('readers.txt','r', encoding='utf-8') as f: # ouverture du fichier en lecture
        lignes = f.readlines() # on lit chaque lignes et on le met sous liste
    newl = [] # creation de la liste newl (newline)
    for ligne in lignes: # on parcours la liste 
        words = ligne.strip().split(',') # on separe la liste les differences lignes et on les decoupes dans des listes 
        name_ = words[0] # on affecte le premier element de la liste qui est le pseudo de l'utilisateur 
        if name == name_: # on regarde si le nom entré correspond a celui dans la liste 
            words[1] = new_genre # si oui, on entre la nouvelle valeur
        newl.append(','.join(words)+'\n') # on ajoute dans la liste newl la liste word mais cette fois ci modifiée 
    with open('readers.txt','w',encoding='utf-8') as f: # ouverture du fichier
        f.writelines(newl) # on reecris dans le fichier

#modifier age
def edit_profile_age(liste_lecteur): # fonction qui modifie l'age
    new_age = -1
    name= input('Veuillez entrer le pseudo que vous souhaitez modifier : ')
    vide = ""
    while name not in liste_lecteur or name == vide: # on effectue la saisie sécurisée au cas ou l'utilisateur entre un pseudo non existant
        name = input("Pseudo non existant, veuillez entrez un pseudo correct : ")       
    while new_age < 1 or new_age > 3: 
        new_age = int(input("Veuillez entrez de nouveau votre age : \n1. <= 18 ans \n2. Entre 18 et 24 ans \n3. < 25 ans \n")) # on effectue la saisie sécurisée
    new_age = str(new_age)
    with open('readers.txt','r', encoding='utf-8') as f: #ouverture du fichier
        lignes = f.readlines() # lecture du fichier
    newl = [] # creation de la liste newl (newline)
    for ligne in lignes: # on parcours la liste 
        words = ligne.strip().split(',') # on separe la liste les differences lignes et on les decoupes dans des listes 
        name_ = words[0] # on affecte le premier element de la liste qui est le pseudo de l'utilisateur
        if name == name_: # on regarde si le nom entré correspond a celui dans la liste
            words[2] = new_age # si oui, on entre la nouvelle valeur
        newl.append(','.join(words)+'\n') # on ajoute dans la liste newl la liste word mais cette fois ci modifiée 
    with open('readers.txt','w',encoding='utf-8') as f: #ouverture du fichier
        f.writelines(newl) # on reecris dans le fichier

#modifier genre littéraire 
def edit_profile_genre_litteraire(liste_lecteur): # fonction qui modifie le genre littéraire
    new_style = -1
    name= input('Veuillez entrer le pseudo que vous souhaitez modifier : ')
    vide = ""
    while name not in liste_lecteur or name == vide: # on effectue la saisie sécurisée au cas ou l'utilisateur entre un pseudo non existant
        name = input("Pseudo non existant, veuillez entrez un pseudo correct : ")
    while new_style < 1 or new_style > 7:
        new_style = int(input("Veuillez entrer votre genre litteraire : \n1. Science-fiction \n2. Biographie \n3. Horreur \n4. Romance \n5. Fable \n6. Histoire \n7. Comédie \n"))
    new_style = str(new_style)
    with open('readers.txt','r', encoding='utf-8') as f: #ouverture du fichier
        lignes = f.readlines() # lecture du fichier
    newl = [] # creation de la liste newl (newline)
    for ligne in lignes: # on parcours la liste 
        words = ligne.strip().split(',') # on separe la liste les differences lignes et on les decoupes dans des listes 
        name_ = words[0] # on affecte le premier element de la liste qui est le pseudo de l'utilisateur
        if name == name_: # on regarde si le nom entré correspond a celui dans la liste
            words[3] = new_style # si oui, on entre la nouvelle valeur
        newl.append(','.join(words)+'\n') # on ajoute dans la liste newl la liste word mais cette fois ci modifiée
    with open('readers.txt','w',encoding='utf-8') as f: #ouverture du fichier
        f.writelines(newl) # on reecris dans le fichier
    # NB les trois fonctions se ressemblent ducoup il est logique que l'on se repete dans le code
    
    
#==================== SUPPRIMER LECTEUR =================#
def delete_readers(liste_lecteur): # fonction qui surrpime un lecteur
    suppr = '' # creation d'une variable suppr qui est un vide
    name= input('Veuillez entrer le nom du lecteur que vous souhaitez supprimer : ')
    vide = ""
    while name not in liste_lecteur or name == vide: # on effectue la saisie sécurisée au cas ou l'utilisateur entre un pseudo non existant
        name = input("Pseudo non existant, veuillez entrez un pseudo correct : ")
    print(name, "est desormais supprimé.")
    with open('readers.txt', "r", encoding='utf-8') as f: # on ouvre le fichier
        i = -1
        for profile in f:
            i += 1
            if name == profile.split(',')[0]:
                number_line = i # on recupere le numero de la ligne pour la matrice
                profile = profile.strip('\n')     
    with open('readers.txt','r', encoding='utf-8') as f: #ouverture du fichier
        lignes = f.readlines() # lecture du fichier
        newl = [] # creation de la liste newl (newline)
        for ligne in lignes: # on parcours la liste
            words = ligne.strip().split(',') # on separe la liste les differences lignes et on les decoupes dans des listes
            name_ = words[0] # on affecte le premier element de la liste qui est le pseudo de l'utilisateur
            if name == name_: # on regarde si le nom entré correspond a celui dans la liste
                words = ligne.strip('').split('\n') #on met tout les element de la meme ligne en une seule et meme chaine de caracteres ['efrei,1,9,3,3']
                words = suppr # on remplace le contenu de la liste words par la variable suprr 
            newl.append(','.join(words)+'\n') # a partir de la il va supprimer le nom que l'on veut supprimer
        with open('readers.txt','w',encoding='utf-8') as f: #on met w seulement car ce sera de passage on ne verra pas le contenu
            f.writelines(newl)  # en ecrivant que ca, il y aura un \n a l'endroit ou on supprime le lecteur
    with open('readers.txt','r',encoding='utf-8')as f: # a partir de la on va creer une liste puis la parcourir pour supprimer l'espace vide 
        lignes = f.readlines() # on lit le fichier et on cree une liste
    T = [] # initialisation d'une liste
    suppr = '' 
    with open('readers.txt','w',encoding='utf-8')as f: 
        for ligne in lignes: # parcours de la liste
            ligne = ligne.strip('\n') # on supprime les '\n'
            T.append(ligne) # on ajoute la variable ligne dans la liste 
        for i in range(len(T)-1): # on parcours la liste 
            if T[i] == suppr: 
                del T[i] # on a supprimer l'espace vide 
        for i in range(len(T)):
            f.write(T[i]+ '\n') # on reecris la liste dans le fichier incognito
    with open('booksread.txt','r', encoding='utf-8') as f:
        lignes = f.readlines()
        newl = []
        for ligne in lignes: # on fait comme noté precedemment
            words = ligne.strip().split(',')
            name_ = words[0]
            if name == name_:
                words = ligne.strip('').split('\n')
                words = suppr
            newl.append(','.join(words)+'\n')
        with open('booksread.txt','w',encoding='utf-8') as f: #on met w seulement car ce sera de passage on ne verra pas le contenu
            f.writelines(newl)  # en ecrivant que ca, il y aura un \n a l'endroit ou on supprime le lecteur
    with open('booksread.txt','r',encoding='utf-8')as f: # a partir de la on va creer une liste puis la parcourir pour supprimer l'espace vide 
        lignes = f.readlines()
    U = []
    suppr = ''        
    with open('booksread.txt','w',encoding='utf-8')as f: #on fait comme noté precedemment 
        for ligne in lignes:
            ligne = ligne.strip('\n')
            U.append(ligne)
        for i in range(len(U)-1):
            if U[i] == suppr:
                del U[i] # on a supprimer l'espace vide 
        for i in range(len(U)):
            f.write(U[i]+ '\n') # on reecris la liste dans le fichier incognito    
    return number_line #on la retourne pour pouvoir update notre matrice
        
def suppression_ligne_matrice(number_line):
    i = 0
    with open('matrice.txt','r',encoding='utf-8')as f:
        matrix = f.readlines()
        for ligne in matrix:
            if number_line == i:
                del matrix[i]
            i += 1
    with open('matrice.txt','w', encoding='utf-8')as f:
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    matrix[i] = str(matrix[i]).replace('[','').replace(']','').replace(',','') 
                f.write(matrix[i])
    return ligne
#suppression_ligne_matrice(delete_readers(lire_liste_lecteur()))

def ajout_ligne_matrice(liste_de_livre):
    with open('matrice.txt','r',encoding='utf-8')as f:
        lignes = f.readlines()
        
    l = [0] * len(liste_de_livre)
    #for i in range(len(liste_de_livre)):
        #l.append(0)
    for i in range(len(l)):
        l[i] = str(l[i]).replace('[','').replace(']','').replace(',','')
    lignes.append(l)
    
    with open('matrice.txt','a', encoding='utf-8')as f:
            for i in range(len(lignes)):
                for j in range(len(lignes[i])):
                    lignes[i] = str(lignes[i]).replace('[','').replace(']','').replace(',','').replace("'",'')
            f.write(lignes[i])   
            f.write('\n')
