from rng.rng_state import _Random
from scipy.stats import chi2
import math

def khi2_test(sample, proba_formula, alpha=0.05):
    N = len(sample)

    df = len()

    x_min = min(sample)
    x_max = max(sample)
    df = x_max - x_min # degree of freedom
    T = 0
    for i in range(x_min,x_max+1):
        T += pow( N * proba_formula(i) - sample.count(i),2)/ (N* proba_formula(i))
    print("degree of freedom :",df)
    if (chi2.cdf(T, df) < 1 - alpha):
        print("H Accepted")
    else:
        print("H rejected")
    return T