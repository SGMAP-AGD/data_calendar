# data_calendar
Ajout des données calendaires françaises (vacances, jours fériés, fêtes nationales, etc.) à partir d'un DataFrame et d'une colonne date.

## Use
Ces données calendaires peuvent avoir un très fort pouvoir explicatif/prédictifs dans certains domaines d'application (ex : temps d'attente aux urgences, consommation d'alcool). Récupérer ces données calendaires est souvent long et fastidieux, là au moins c'est déjà fait !

### Requirements
- [pandas](http://pandas.pydata.org/)

### initial commit

Fonction ``get_calendar(df, date_col)`` : Calcule les données calendaires à partir de la série temporelle d'une table.


  + df : ``pd.DataFrame``

  Tabe contenant au moins une colonne date de type ``pd.tseries`` (ou un index).
  + date\_col : str, _Optional_ (default = None)

  La colonne date du Dataframe. Par défaut, la fonction cherchera dans l'index.

### Données calendaires : 2012 - 2014

- Vacances scolaires (zone C uniquement)
- Jours fériés, fêtes nationales, ...
- Evenements : fête de la musique, nuit blanche.

### Remarque
Pour l'instant c'est vraiment un pâté, mais ça peut toujours rendre service :-) !
