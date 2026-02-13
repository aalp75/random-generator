import math

def expectation(seq):
    return sum(seq) / len(seq)

def variance(seq, unbiaised=True):
    E = expectation(seq)
    var = 0
    var = sum([(x - E) * (x - E) for x in seq])
    if unbiaised and len(seq) > 1:
        return var / (len(seq) - 1)
    return var / len(seq)

def std(seq, unbiaised=True):
    return math.sqrt(variance(seq, unbiaised))

def autocorrelation(sample, lags=50):
    res= []
    n = len(sample)
    mu = expectation(sample)
    sigma = variance(sample)
    for k in range(lags):
        R = 0.0
        for i in range(n - k):
            R += (sample[i] - mu) * (sample[i + k] - mu)
        res.append(abs(R / ((n - k) * sigma)))
    return res