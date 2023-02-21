import pandas as pd
import numpy as np
import re

data = pd.read_csv('operations.csv')
data.head()

#on utilise le format date pour la colonne 'date_operation'
data['date_operation'] = pd.to_datetime(data['date_operation'])

# on stocke le df des valeurs manquantes dans un nouveau df
data_na = data.loc[data['montant'].isnull(),:]

# pour chaque ligne de mon df, on récupère les index (qui ne changent pas au travers du .loc)
for index in data_na.index:
    # calcul du montant à partir des soldes précédents et actuels
    data.loc[index, 'montant'] = data.loc[index+1, 'solde_avt_ope'] - data.loc[index, 'solde_avt_ope']

data.loc[data['categ'].isnull(), 'categ'] = 'FACTURE TELEPHONE'

data.drop_duplicates(subset=['date_operation', 'libelle', 'montant', 'solde_avt_ope'], inplace=True, ignore_index=True)

#i = data.loc[data['montant']==-15000,:].index[0] # récupération de l'index de la transaction à -15000
#data.iloc[i-1:i+2,:] # on regarde la transaction précédente et la suivante

data.loc[data['montant']==-15000, 'montant'] = -14.39

data.to_csv('operations.csv')