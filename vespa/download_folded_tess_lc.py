#!/usr/bin/env python
import chronos as cr

TOIID = 1696
phase_lim = 0.05 #save phase folded lc: (-phase_lim, phase_lim)
window_length = 1.4 #day, roughly equal to window=1001 in Mori+ Fig. 1

s = cr.ShortCadence(toiid=TOIID)
period = s.toi_period
t0 = s.toi_epoch+0.00025

sap = s.get_lc(lctype='sap')
#remove outliers
sap = sap.remove_outliers(sigma_upper=5)

fig = s.plot_trend_flat_lcs(sap, window_length=window_length)
fig.savefig('sap.pdf', bbox_inches='tight')

#flatten
flat = s.get_flat_lc(sap, window_length=window_length)

#phase-fold
fold = flat.fold(period=period, t0=t0)
ax = fold.scatter(label='SAP')
_ = fold.bin(10).scatter(ax=ax, label='bin', s=10)
ax.set_xlim(-0.05, 0.05)
ax.figure.savefig('sap_fold.pdf', bbox_inches='tight')


fp = 'tess_folded.csv'
columns_to_save = ['time', 'flux', 'flux_err']
df = fold.to_pandas()[columns_to_save]
#trim only around the transit
idx = (df.time>-phase_lim) & (df.time<phase_lim)
df_trim = df[idx]
df_trim.to_csv(fp, sep=' ', header=False, index=False)
print("Saved: ", fp)
