# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 09:47:48 2024

@author: hugo.cadario
"""

import os
import matplotlib.pyplot as plt

# Chemin vers le dossier source
source_folder = r"C:\Users\hugo.cadario"
source_folder = r"C:\Users\hugo.cadario"

################################################################################
############################ Tous #####################################
################################################################################
# Initialiser des listes pour stocker les noms des dossiers et leurs tailles
folders = []
sizes = []

# Parcourir les éléments du dossier source
for item in os.listdir(source_folder):
    # Construire le chemin complet de l'élément
    item_path = os.path.join(source_folder, item)
    # Vérifier si l'élément est un dossier
    if os.path.isdir(item_path):
        # Récupérer la taille du dossier en octets
        size = sum(os.path.getsize(os.path.join(item_path, file)) 
                   for file 
                   in os.listdir(item_path)
                   if os.path.isfile(os.path.join(item_path, file)))
        # Convertir la taille en gigaoctets (Go)
        size_gb = size / (1024 * 1024 * 1024)
        # Ajouter le nom du dossier et sa taille aux listes
        folders.append(item)
        sizes.append(size_gb)

# Créer un histogramme
plt.figure(figsize=(10, 6))
plt.bar(folders, sizes, color='skyblue')
plt.xlabel('Nom du dossier')
plt.ylabel('Taille (Go)')
plt.title('Taille des dossiers dans {}'.format(source_folder))
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()



################################################################################
############################ les 10 + gros #####################################
################################################################################
# Parcourir les éléments du dossier source
for item in os.listdir(source_folder):
    # Construire le chemin complet de l'élément
    item_path = os.path.join(source_folder, item)
    # Vérifier si l'élément est un dossier
    if os.path.isdir(item_path):
        # Récupérer la taille du dossier en octets
        size = sum(os.path.getsize(os.path.join(item_path, file)) 
                   for file 
                   in os.listdir(item_path) 
                   if os.path.isfile(os.path.join(item_path, file)))
        # Convertir la taille en gigaoctets (Go)
        size_gb = size / (1024 * 1024 * 1024)
        # Ajouter le nom du dossier et sa taille aux listes
        folders.append(item)
        sizes.append(size_gb)

# Trier les dossiers par taille (du plus grand au plus petit)
sorted_indices = sorted(range(len(sizes))
                        , key=lambda i: sizes[i], reverse=True)
folders_sorted = [folders[i] for i in sorted_indices]
sizes_sorted = [sizes[i] for i in sorted_indices]

# Sélectionner les 10 premiers dossiers
top_folders = folders_sorted[:10]
top_sizes = sizes_sorted[:10]

# Créer un histogramme pour les 10 premiers dossiers
plt.figure(figsize=(10, 6))
plt.bar(top_folders, top_sizes, color='skyblue')
plt.xlabel('Nom du dossier')
plt.ylabel('Taille (Go)')
plt.title('10 plus gros dossiers dans {}'.format(source_folder))
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


################################################################################
############################ Fichieren .txt ####################################
################################################################################

import os

# Chemin vers le répertoire principal
directory = r"C:\Users\hugo.cadario"

# Liste pour stocker les chemins des fichiers .txt
txt_files = []

# Parcourir le répertoire et ses sous-répertoires
for root, dirs, files in os.walk(directory):
    for file in files:
        # Vérifier si le fichier a l'extension .txt
        if file.endswith(".txt"):
            # Construire le chemin complet du fichier et l'ajouter à la liste
            file_path = os.path.join(root, file)
            txt_files.append(file_path)

# Trier les fichiers par date de modification
txt_files_sorted = sorted(txt_files, key=os.path.getmtime)

# Afficher la liste des fichiers .txt triés par date de modification
for txt_file in txt_files_sorted:
    print(txt_file)

