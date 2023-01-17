""" Utility functions and classes for SRP

Context : SRP
Module  : SRPGW
Version : 1.1.1
Author  : Stefano Covino
Date    : 14/01/2020
E-mail  : stefano.covino@brera.inaf.it
URL:    : http://www.merate.mi.astro.it/utenti/covino

Usage   : GetApPhot

Remarks :

History : (25/02/2016) First version.
        : (22/08/2017) SRPFITS version.
        : (14/01/2020) Gain and Ron as parameters.
"""


import SRPGW as GW
import SRPFITS.Photometry.DaoPhot as SPD
#import numpy
#from PythonPhot import aper


def DaoPhot(x,y,data,rds=(5,10,15),backgr=True,gain=GW.VSTgain,ron=GW.VSTron):
    return SPD.DaoPhot(x,y,data,rds,backgr,gain,ron)



