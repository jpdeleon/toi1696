#!/usr/bin/env python
import chronos as cr

"""isochrones/with_spec/NIR/summary.txt
radius: 0.30-0.01+0.01
mass: 0.29-0.01+0.01
Teff: 3151.36-33.75+39.93
logg: 4.94-0.01+0.01
feh: 0.26-0.04+0.04
"""
TOIID = 1696
TEFF = (3151, 41)
FEH = (0.26, 0.04)
LOGG = (4.94, 0.01)
bands = "J H K G BP RP TESS".split() #TESS must be included for vespa run

s=cr.Star(toiid=TOIID)
s.save_ini_isochrones(teff=TEFF, logg=LOGG, feh=FEH, bands=bands, outdir='./')
