from astroARIADNE.star import Star
from astroARIADNE.fitter import Fitter
from astroARIADNE.plotter import *

rerun_fit = False

ra = 65.280648
dec = 48.819831
starname = 'TOI 1696'
gaia_id = 270260649602149760

s = Star(starname, ra, dec, g_id=gaia_id)

out_folder = 'without_spec_priors'

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
f.out_folder = out_folder
f.bma = True
f.models = models
f.n_samples = 10000

f.prior_setup = {
    'teff': ('default'), # RAVE
    'logg': ('default'), # RAVE
    'z': ('default'),    # RAVE
    'dist': ('default'), #from Gaia DR2
    'rad': ('default'),
    'Av': ('default') #is a flat prior that ranges from 0 to the maximum of line-of-sight as per the SFD map
}

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
