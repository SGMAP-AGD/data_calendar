# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 12:01:08 2015

@author: Flo
"""

import pandas as pd


# --  Données calendaires : 2012, 2013 et 2014 / vacances zone C


def get_calendar(ts, date_col=None):
    ''' Calculate calendar features from a pandas timeseries'''
    if(date_col is not None):
        if any(date_col in col for col in ts.columns):
            ts.set_index(date_col, inplace=True)
        else:
            raise Exception('The column \'date_col\' you entered is not in the DataFrame')


    if(type(ts.index) != pd.DatetimeIndex):
        raise Exception('date_col column must be in the pd.DateTimeIndex format')

    # -- Jours particuliers
    ts['dayofmonth'] = ts.index.day
    ts['dayofweek'] = ts.index.dayofweek
    ts['weekend'] = (ts.dayofweek.isin([5, 6])).astype('int')

    # -- Saisons (TODO or not)

    # -- Vacances scolaires (2012) - Zone C
    vac_toussain = ((ts.index >= '2012-10-27') & (ts.index < '2012-11-13')) + ((ts.index >= '2013-10-19') & (ts.index < '2013-11-04')) + ((ts.index >= '2014-10-18') & (ts.index < '2014-11-03'))
    vac_noel = ((ts.index >= '2012-12-22') & (ts.index < '2013-01-08')) + ((ts.index >= '2013-12-21') & (ts.index < '2014-01-06')) + ((ts.index >= '2014-12-20') & (ts.index < '2015-01-05'))
    vac_hiver = ((ts.index >= '2013-03-02') & (ts.index < '2013-03-18')) + ((ts.index >= '2014-02-15') & (ts.index < '2014-03-03')) + ((ts.index >= '2015-02-21') & (ts.index < '2015-03-09'))
    vac_printemps = ((ts.index >= '2013-04-27') & (ts.index < '2013-05-13')) + ((ts.index >= '2014-04-12') & (ts.index < '2014-04-28')) + ((ts.index >= '2015-04-25') & (ts.index < '2015-05-11'))
    vac_ete = ((ts.index >= '2013-07-06') & (ts.index < '2014-09-03')) + ((ts.index >= '2014-07-05') & (ts.index < '2015-09-02')) + ((ts.index >= '2015-07-03') & (ts.index < '2015-09-01'))

    ts['vacances'] = (vac_toussain + vac_noel + vac_hiver + vac_printemps + vac_ete).astype('int')

    # -- Fêtes nationales / jours fériés

    dates_jours_feries = ['2012-01-01', '2013-01-01', '2014-01-01'] + ['2012-04-09', '2013-04-01', '2014-04-21'] + \
                         ['2012-05-01', '2013-05-01', '2014-05-01'] + ['2012-05-08', '2013-05-08', '2014-05-08'] + \
                         ['2012-05-17', '2013-05-19', '2014-05-29'] + ['2012-05-28', '2013-05-20', '2014-05-29'] + \
                         ['2012-07-14', '2013-07-14', '2014-07-14'] + ['2012-08-15', '2013-08-15', '2014-08-15'] + \
                         ['2012-09-01', '2013-09-01', '2014-09-01'] + ['2012-09-11', '2013-09-11', '2014-09-11'] + \
                         ['2012-12-25', '2013-12-25', '2014-12-25'] + ['2012-12-31', '2013-12-31', '2014-12-31']

    ts['jours_feries'] = 0
    for jour in dates_jours_feries:
        ts.loc[jour, 'jours_feries'] = 1

    # -- Evènemenets (musique, nuit blanche, ..)
    dates_fete_musique = ['2012-10-06', '2013-10-05', '2014-01-04']
    dates_nuit_blanche = ['2012-01-21', '2013-01-21', '2014-01-21']

    ts['fete_musique'] = 0
    for fm in dates_fete_musique:
        ts.loc[fm, 'fete_musique'] = 1

    ts['nuit_blanche'] = 0
    for nb in dates_nuit_blanche:
        ts.loc[nb, 'nuit_blanche'] = 1

    return ts
