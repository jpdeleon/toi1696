import pandas as pd
from pathlib import Path
from glob import glob
import numpy as np

#outdir = './with_spec/NIR_optical'
outdir = './with_spec/NIR'
#outdir = './without_spec/NIR_optical'
#outdir = './without_spec/NIR'
cols = "radius mass Teff logg feh".split()
fp = Path(outdir, "mist_starmodel_single.h5")
df = pd.read_hdf(fp, key='derived_samples').dropna()

d = {}
texts = []
for col in cols:
    v, vlo, vhi = np.percentile(df[col], q=[50, 16, 84])    
    msg = f"{col}: {v:.2f}-{v-vlo:.2f}+{vhi-v:.2f}"
    texts.append(msg)           
    print(msg)
    if col == "Teff":
        d[col] = f"{v:.0f}"
        d[col + "_m"] = f"{v-vlo:.0f}"
        d[col + "_p"] = f"{vhi-v:.0f}"
    else:
        d[col] = f"{v:.2f}"
        d[col + "_m"] = f"{v-vlo:.2f}"
        d[col + "_p"] = f"{vhi-v:.2f}"
ofp = Path(outdir, 'summary.txt')
np.savetxt(ofp, texts, fmt='%s')
print(f"Saved: {ofp}")
