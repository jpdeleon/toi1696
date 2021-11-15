import numpy as np
from mk_mass import posterior

k,ek  = 8.782,0.02
dist  = 14.55
edist = 0.13
feh,efeh=0.3,0.1
mass      = posterior(k,dist,ek,edist)
mass_feh  = posterior(k,dist,ek,edist,feh,efeh)
print("Mass=%6.4f+/-%6.4f" % (np.median(mass),np.std(mass)))
#	Mass=0.1803+/-0.0047
