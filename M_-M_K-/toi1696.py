import numpy as np
from mk_mass import posterior

k,ek  = 11.331,0.1 #0.023
dist  = 64.9172
edist = 0.3525
#feh,efeh=-0.02,0.035 #IRD
#feh,efeh=0.0,0.5 #SED
feh,efeh=0.3325,0.0883 #SpeX
mass      = posterior(k,dist,ek,edist)
mass_feh  = posterior(k,dist,ek,edist,feh,efeh)
print("Mass=%6.4f+/-%6.4f" % (np.median(mass),np.std(mass)))
#	Mass=0.1803+/-0.0047
