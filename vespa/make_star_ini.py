#!/usr/bin/env python
import chronos as cr

TOIID = 1696
TEFF = (3350,120)
FEH = (0.04,0.16)
LOGG = (4.988,0.026)
bands = "J H K G BP RP TESS".split()

s=cr.Star(toiid=TOIID)
s.save_ini_isochrones(teff=TEFF, logg=LOGG, feh=FEH, bands=bands, outdir='./')
