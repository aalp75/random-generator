from .rng_state import _Random
from .discrete_distributions import *
from .continuous_distributions import *
from .utils import *
from .mcmc import *
from .statistical_test import *

def set_generator(method, seed=None):
    _Random.set_generator(method, seed)

__all__ = [
    # package
    'set_generator',

    # utils
    'expectation',
    'variance',
    'std',
    'autocorrelation',

    # continuous distributions
    'bernouilli',
    'uniform_discrete',
    'binomial',
    'geometric',
    'poisson',
    
    # continuous distributions
    'uniform',
    'exponential',
    'gaussian',
    'gaussian_vector',
    'gamma',
    'pareto,'
    'chisquare',

    # statistical tests
    'chi2_test',
    'indep_test',
    'ks_test',

    # MCMC
    'mcmc',
]