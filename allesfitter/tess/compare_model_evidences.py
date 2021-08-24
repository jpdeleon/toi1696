#!/usr/bin/env python
#https://www.allesfitter.com/api
import allesfitter

datadirs = 'spline gp'.split() #linear
fig, ax, logZ_evidences = allesfitter.ns_plot_bayes_factors(datadirs, labels=None, return_dlogZ=True, explanation=True)
#import pdb; pdb.set_trace()
fp = "model_evidence_"+"_".join(datadirs)+".pdf"
fig.savefig(fp, bbox_inches="tight")
print("Saved: ", fp)
