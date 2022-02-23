#/!usr/bin/env python
"""
`allesfitter_results_fp` was created in allesfit_transit_results.ipynb

"""
import flammkuchen as dd
import lightkurve as lk
import pandas as pd

phase_lim = 0.1
inst = 'tess'

allesfitter_results_fp = '../allesfitter/tess/allesfit_transit_results.h5'
results = dd.load(allesfitter_results_fp)
print('Loaded: ', allesfitter_results_fp)

df_samples = results[inst]['posterior_samples']
period = df_samples['b_period'].median()
t0 = df_samples['b_epoch'].median()

lc = lk.LightCurve(time=results[inst]['time'],
                     flux=results[inst]['flux'],
                     flux_err=results[inst]['flux_err'])
fold = lc.fold(period=period, t0=t0)
#ax = fold.scatter()

fp = 'tess_folded.csv'
columns_to_save = ['time', 'flux', 'flux_err']
df = fold.to_pandas().reset_index()[columns_to_save]
#trim only around the transit
idx = (df.time>-phase_lim) & (df.time<phase_lim)
df_trim = df[idx]
df_trim.to_csv(fp, sep=' ', header=False, index=False)
print("Saved: ", fp)

