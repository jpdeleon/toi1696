"""
relation holds true when 4<Kmag<11
"""
import numpy as np
from mk_mass import posterior

k,ek  = 11.331,0.023
dist,edist  = 64.9172, 0.3525 #pc
feh,efeh = 0.3382, 0.0829 #wmean
#feh,efeh=0.38,0.24 #IRD
#feh,efeh=0.3325,0.0883 #SpeX
#feh,efeh=0.0,0.5 #SED
mass      = posterior(k,dist,ek,edist)
mass_feh  = posterior(k,dist,ek,edist,feh,efeh)
print("Mass=%6.4f+/-%6.4f" % (np.median(mass),np.std(mass)))
#	Mass=0.1803+/-0.0047
