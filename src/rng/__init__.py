from .rng_state import _Random
from .discrete_laws import *
from .continue_laws import *
from .utils import *
from .metropolis_hastings import *
from .tests_statistic import *

def set_generator(method, seed=None):
    _Random.set_generator(method, seed)

__all__ = [
    # package
    "set_generator",

    #utils
    'expectation',
    'variance',
    'std',
    'autocorrelation',

    # discrete laws
    'bernouilli',
    'uniform_discrete',
    'binomial',
    'geometric',
    'poisson',
    
    # continue laws
    'uniform',
    'exponential',
    'gaussian',
    'gaussian_vector',
    'gamma',
    'pareto,'
    'khi_deux',

    # statistic tests
    'chi2_test',
    'indep_test',
    'ks_test',

    # MCMC
    'metropolis_hastings',
]