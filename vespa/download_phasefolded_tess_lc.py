#!/usr/bin/env python
#import matplotlib.pyplot as pl
import chronos as cr
import pdb, sys, traceback

TOIID=1696


s = cr.ShortCadence(toiid=TOIID)
#pdcsap = s.lc_pdcsap
lc = s.get_lc(lctype='pdcsap')
#import pdb; pdb.set_trace()
try:
    fig = s.plot_trend_flat_lcs(lc)
    fp1 = f'toi{TOIID}_trend_flat.png'
    fig.savefig(fp1, bbox_inches='tight')
    print('Saved: ', fp1)
except:
    extype, value, tb = sys.exc_info()
    traceback.print_exc()
    pdb.post_mortem(tb)

flat = s.get_flat_lc(lc)
ax = s.plot_fold_lc(flat)
fp2 = f'toi{TOIID}_flat.png'
ax.figure.savefig(fp2, bbox_inches='tight')
print('Saved: ', fp2)

#fig = s.run_tls(flat, plot=True)
#pl.show()
