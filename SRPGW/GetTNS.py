""" Utility functions and classes for SRP

Context : SRP
Module  : SRPGW
Version : 1.0.0
Author  : Stefano Covino
Date    : 11/12/2019
E-mail  : stefano.covino@brera.inaf.it
URL:    : http://www.merate.mi.astro.it/utenti/covino

Usage   :

Remarks :

History : (11/12/2019) First version.
"""


import requests


def GetTNS(rad,decd,rds):
    tnsaddress = "https://wis-tns.weizmann.ac.il/search"
    #
    tns = []
    #
    for r,d in zip(rad,decd):
        search_obj = {"ra" : str(r), "decl" : str(d), "radius" : str(rds), "coords_unit" :"arcsec", "discovered_period_value" : str(0)}
        res = requests.get(tnsaddress, params=search_obj)
        #
        if res != None and res.status_code == 200:
            nentry = 'No'
            for i in reversed(res.text.split('\n')):
                loc = i.find('object')
                nloc = i.find('title')
                if loc > -1 and nloc < 0:
                    ris = i[loc:]
                    locf = ris.find('</a')
                    loci = ris.find('>')
                    if locf > -1 and loci > -1:
                        nentry = ris[loci+1:locf]
                        break
            tns.append(nentry.split('/')[-1])
        else:
            tns.append('No')
    #
    return tns


