from rng.rng_state import _Random
from scipy.stats import chi2, ksone
import numpy as np
import math

def chi2_test(sample, proba_formula, alpha=0.05):
    N = len(sample)

    values, counts = np.unique(sample, return_counts=True)
    df = len(values) - 1

    expected = np.array([N * proba_formula(v) for v in values])

    # Remove values with zero expected probability to avoid division by 0
    mask = expected > 0
    observed = counts[mask]
    expected = expected[mask]

    # Chi-square statistic
    T = np.sum((observed - expected) ** 2 / expected)

    # Degrees of freedom
    df = len(expected) - 1
    
    critical = chi2.ppf(1 - alpha, df)

    if T < critical:
        print("H accepted")
    else:
        print("H rejected")

    return T, critical

def indep_test(sample1, sample2, alpha=0.05):
    """
    Chi-2 test of indepedance

    Inputs:
        sample1: iterable of length n
        sample2: iterable of length m
    """

    n = len(sample1)

    s1_values = np.unique(sample1)
    s2_values = np.unique(sample2)

    T = 0

    for i in s1_values:
        for j in s2_values:

            observed = np.sum((sample1 == i) & (sample2 == j))
            exepected = (np.sum(sample1 == i) * np.sum(sample2 == j)) / n

            if exepected > 0:
                T += (observed - exepected) ** 2 / exepected

    # degrees of freedom
    df = (len(s1_values) - 1) * (len(s2_values) - 1)

    critical = chi2.ppf(1 - alpha, df)

    if T < critical:
        print("H Accepted")
    else:
        print("H rejected")

    return T

def ks_test(sample, cdf, alpha=0.05):
    """
    Kolmogorov-Smirnov test
    """

    sample = np.sort(np.asarray(sample))
    n = len(sample)

    D_plus = 0.0
    D_minus = 0.0

    for i in range(n):
        F_x = cdf(sample[i])

        D_plus = max(D_plus, (i + 1) / n - F_x)
        D_minus = max(D_minus, F_x - i / n)

    D = max(D_plus, D_minus)

    critical = ksone.ppf(1 - alpha / 2, n)

    if D < critical:
        print("H Accepted")
    else:
        print("H rejected")

    return D

