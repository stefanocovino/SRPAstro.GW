""" Utility functions and classes for SRP

Context : SRP
Module  : SRPGW
Version : 1.0.1
Author  : Stefano Covino
Date    : 14/01/2020
E-mail  : stefano.covino@brera.inaf.it
URL:    : http://www.merate.mi.astro.it/utenti/covino

Usage   : GetApPhot

Remarks :

History : (11/02/2016) First version.
        : (14/01/2020) Gain as paramter.
"""



import sep
import numpy
import SRPGW as GW


def SexPhot(x,y,data,rds=(5,10,15),backgr=True,gain=GW.VSTgain):
    dat = data.astype(numpy.float32)
    if backgr:
        flux,fluxerr,flag = sep.sum_circle(dat,x,y,rds[0],bkgann=(rds[1],rds[2]),gain=gain)
    else:
        flux,fluxerr,flag = sep.sum_circle(dat,x,y,rds[0],gain=gain)
    #
    return flux, fluxerr
