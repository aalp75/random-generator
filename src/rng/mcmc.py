from rng.rng_state import _Random
from rng.continuous_distributions import gaussian, uniform
import math

def mcmc(pi, size=1_000, sigma=1, starting_point=1):
    """
    Metropolis-Hasting algorithm using a N(xn, sigma) for exploration

    Inputs:
        pi : target law (callable function)
        size :length of the output sample
        sigma : standard derviation of the gaussian law used to generate candidates
        start_point : iniail value of the sample

    Returns: list
        - sample : list
        - acceptance_ratio : double

    """
    x0 = starting_point
    res = [x0]
    curr = x0
    acceptance = 0
    for i in range(size):
        y = curr + gaussian(0, sigma ** 2, 1)
        alpha = pi(y) / pi(curr)
        U = uniform()
        if (U<alpha):
            res.append(y)
            curr = y 
            acceptance += 1
        else:
            res.append(curr)
    acceptance_ratio = acceptance / size
    return [res, acceptance_ratio]
        