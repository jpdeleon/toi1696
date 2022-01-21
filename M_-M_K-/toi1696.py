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
mass  = posterior(k,dist,ek,edist)
#mass  = posterior(k,dist,ek,edist,feh,efeh)
m=np.median(mass)
em=np.std(mass)
text=f"Mass={m:.4f}+/-{em:.4f}"
print(text)
ofp="summary.txt"
np.savetxt(ofp, [text], fmt='%s')
#	Mass=0.2537+/-0.0064
