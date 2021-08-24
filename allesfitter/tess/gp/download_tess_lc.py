#!/usr/bin/env python
import chronos as cr

TOIID = 1696

s = cr.ShortCadence(toiid=TOIID)
pdcsap = s.get_lc(lctype='pdcsap')
#remove outliers
lc = pdcsap.remove_outliers(sigma_upper=5)
#fig = s.plot_trend_flat_lcs(pdcsap, window_length=window_length)
#fig.savefig('sap.pdf', bbox_inches='tight')

fp = 'tess.csv'
columns_to_save = ['time', 'flux', 'flux_err']
df = lc.to_pandas()[columns_to_save]
df.to_csv(fp, sep=',', header=False, index=False)
print("Saved: ", fp)
