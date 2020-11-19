# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 10:48:09 2020

@author: Bast
"""

import pandas as pd
import glob

# 1) Récuperer l'ensemble des fichiers dans departements
# 2) Construction d'un dataset unique
# 3) Ajout colonne Region
# 4) Recherche coordonnées régions



# 1) Récuperer l'ensemble des fichiers dans departements
# 2) Construction d'un dataset unique

# Lire le dossier qui contient les datasets et créer un dataset unique sauvegardé dans le dossier dataset cleaned
# Le csv se mettra à jour si l'on importe de nouvelles données

final_path = r'..\..\datasets_cleaned\test.csv'

def concat_dataset():
    path = r'C:\Users\Bast\Desktop\TP_COVID_YNOV\covid_departements_datasets' # use your path
    all_files = glob.glob(path + "/*.csv")
    li = []
    
    for filename in all_files:
        df = pd.read_csv(filename)
        df.columns = ['departement', 'date', 'hospitalises', 'reanimations', 'nvx_hospitalises', 'nvlles_reanimations', 'gueris', 'deces']
        li.append(df)

 
    frame = pd.concat(li, ignore_index=True)
    frame.to_csv(final_path, index = False, header=True)
    
 
concat_dataset()



dataset = pd.read_csv(final_path)

print(dataset.head())

# 3) Ajout de la colonne des Régions

# 4) Recherche coordonnées

