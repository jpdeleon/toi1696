from astroARIADNE.star import Star
from astroARIADNE.fitter import Fitter
from astroARIADNE.plotter import *

rerun_fit = True

ra = 65.280648
dec = 48.819831
starname = 'TOI 1696'
gaia_id = 270260649602149760

s = Star(starname, ra, dec, g_id=gaia_id)

use_weighted_priors = True
use_IRD_priors = False
use_IRTF_priors = False
use_default_priors = False

engine = 'dynesty'
nlive = 500
dlogz = 0.1
bound = 'multi'
sample = 'rwalk'
threads = 24
dynamic = False

setup = [engine, nlive, dlogz, bound, sample, threads, dynamic]

# Feel free to uncomment any unneeded/unwanted models
models = [
	'phoenix',
	'btsettl',
	'btnextgen',
	'btcond',
	'kurucz',
	'ck04'
]

f = Fitter()
f.star = s
f.setup = setup
f.av_law = 'fitzpatrick'
f.bma = True
f.models = models
f.n_samples = 10000

f.prior_setup = {
	'dist': ('default'), #from Gaia DR2
	'rad': ('default'),
	#'Av': ('fixed', 0)
	'Av': ('default') #is a flat prior that ranges from 0 to the maximum of line-of-sight as per the SFD map
}

if use_IRD_priors:
    out_folder = 'with_IRD_priors'
    f.prior_setup['teff'] = ('normal', 3116, 114)
    f.prior_setup['logg'] = ('normal', 4.95, 0.01)
    f.prior_setup['z'] = ('normal', -0.02, 0.35)
elif use_IRTF_priors:
    # from Giacalone
    out_folder = 'with_IRTF_priors'
    f.prior_setup['teff'] = ('normal', 3207, 99)
    f.prior_setup['logg'] = ('normal', 4.95859, 0.06267)
    f.prior_setup['z'] = ('normal', 0.3325, 0.0883)
elif use_weighted_priors:
    # default is RAVE
    out_folder = 'with_spec_priors'
    f.prior_setup['teff'] = ('normal', 3159, 63)
    f.prior_setup['logg'] = ('normal', 4.9562, 0.0531)
    f.prior_setup['z'] = ('normal', 0.3382, 0.0829)
elif use_default_priors:
    # default is RAVE
    out_folder = 'without_spec_priors'
    f.prior_setup['teff'] = ('default')
    f.prior_setup['logg'] = ('default')
    f.prior_setup['z'] = ('default')
else:
    raise ValueError()

f.out_folder = out_folder
if rerun_fit:
    f.initialize()
    f.fit_bma()



# Setting up plotter, which is independent to the main fitting routine
# Bear in mind this will only work if you have downloaded the models
# And have set up the ARIADNE_MODELS environment variable!
if True:
    artist = SEDPlotter(out_folder+'/BMA.pkl', out_folder, pdf=True)
    artist.plot_SED_no_model()  # Plots the stellar SED without the model
    artist.plot_SED()  # Plots stellar SED with model included
    artist.plot_bma_hist()  # Plots bayesian model averaging histograms
    artist.plot_bma_HR(10)  # Plots HR diagram with 10 samples from posterior
    artist.plot_corner()  # Corner plot of the posterior parameters
