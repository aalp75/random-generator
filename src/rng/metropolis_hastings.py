from rng.rng_state import _Random
from rng.continue_laws import gaussian, uniform
import math

def metroplis_hastings(pi, size=10000, sigma = 1,start_point=1):
    """
    Metropolis-Hasting algorithm

    Inputs:
        pi : target law (callable function)
        size :length of the output sample
        sigma : standard derviation of the gaussian law used to generate candidates
        start_point : iniail value of the sample

    Returns: list
        - sample : list
        - acceptance_ratio : double

    """
    x0 = start_point
    res = [x0]
    xt = x0
    acceptance = 0
    for i in range(size):
        y = xt + gaussian(0, sigma ** 2, 1)
        alpha = pi(y) / pi(xt)
        U = uniform()
        if (U<alpha):
            res.append(y)
            xt = y 
            acceptance += 1
        else:
            res.append(xt)
    acceptance_ratio = acceptance / size
    return [res, acceptance_ratio]
        