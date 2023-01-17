""" Utility functions and classes for SRP

Context : SRP
Module  : SRPGW
Version : 1.0.4
Author  : Stefano Covino
Date    : 14/01/2020
E-mail  : stefano.covino@brera.inaf.it
URL:    : http://www.merate.mi.astro.it/utenti/covino

Usage   : GetApPhot

Remarks :

History : (11/02/2016) First version.
        : (13/02/2016) Improved error estimate.
        : (18/02/2016) Quicker photometry.
        : (23/08/2017) SRPFITS version.
        : (14/01/2020) GAIN and RON as parameters.
"""


import SRPGW as GW
#import numpy
#from photutils import CircularAperture, CircularAnnulus, aperture_photometry
#from astropy.table import hstack
import SRPFITS.Photometry.ApyPhot as SPA



def ApyPhot(x,y,data,rds=(5,10,15),backgr=True,gain=GW.VSTgain,ron=GW.VSTron):
    return SPA.ApyPhot(x,y,data,rds,backgr,gain,ron)
    

