#!/usr/bin/env python
import chronos as cr

TOIID=1696

p=cr.Planet(toiid=TOIID)
p.save_ini_vespa(outdir="./")
