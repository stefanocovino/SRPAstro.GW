""" Utility functions and classes for SRP

Context : SRP
Module  : SRPGW
Version : 1.0.3
Author  : Stefano Covino
Date    : 14/01/2020
E-mail  : stefano.covino@brera.inaf.it
URL:    : http://www.merate.mi.astro.it/utenti/covino

Usage   : GetApPhot

Remarks :

History : (11/02/2016) First version.
        : (13/02/2016) Improved error estimate.
        : (19/04/2017) SRPFITS added.
        : (14/01/2020) Gain and ron as parameters.
"""



import SRP.SRPAstro as SRPAstro
import SRPGW as GW
import numpy
from SRPFITS.Photometry.getBackground import getBackground


def MyPhot(x,y,data,rds=(5,10,15),backgr=True,gain=GW.VSTgain,ron=GW.VSTron):
    flux = []
    fluxerr = []
    for i,l in zip(x,y):
       totf,npix,maxf = SRPAstro.sumApert(data,i-1,l-1,rds[0])
       if backgr:
            bg,sbg,ebg,chbg,nbg = getBackground(data,i-1,l-1,rds[1],rds[2])
       else:
            bg = 0.0
            ebg = 0.0
       #
       tflux = totf-bg*npix
       tfluxerr = numpy.sqrt(numpy.fabs(totf)*gain + npix*(ebg*gain)**2 + npix*ron)
       flux.append(tflux)
       fluxerr.append(tfluxerr)
    #
    return numpy.array(flux),numpy.array(fluxerr)
    
