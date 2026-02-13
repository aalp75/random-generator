from rng.rng_state import _Random
import numpy as np
import math

def uniform(a=0, b=1, size=1):
    '''
    uniform law on [a, b]
    '''
    if size == 1:
        x = _Random.generate()
        return a + x * (b - a)
    res = []
    for i in range(size):
        x = _Random.generate()
        res.append(a + x * (b - a))
    return res

# Inverse of the cumulative distribution function
def exponential(lamb, size=1):
    if size == 1:
        x = _Random.generate()
        return -1.0 / lamb * math.log(x)
    res = []
    for i in range(size):
        x = _Random.generate()
        res.append(-1.0 / lamb * math.log(x))
    return res

# Box-Muller method
def gaussian(mu, sigma, size=1):
    if size == 1:
        x1 = _Random.generate()
        x2 = _Random.generate()
        return (mu + math.sqrt(sigma) * math.sqrt(-2 * math.log(x1)) * math.cos(2 * math.pi * x2))
    res = []
    r = size % 2
    for _ in range(int(size/2)):
        x1 = _Random.generate()
        x2 = _Random.generate()
        res.append(mu + math.sqrt(sigma) * math.sqrt(-2 * math.log(x1))*math.cos(2 * math.pi * x2))
        res.append(mu + math.sqrt(sigma) * math.sqrt(-2 * math.log(x1))*math.sin(2 * math.pi * x2))
    if size % 2:
        x1 = _Random.generate()
        x2 = _Random.generate()
        res.append(mu + math.sqrt(sigma) * math.sqrt(-2 * math.log(x1)) * math.cos(2 * math.pi*x2))
    return res

def gaussian_vector(mu, sigma, n):
    '''
    return a gaussian vector of length n
    mu should be a vector and sigma a matrix (n x n)
    '''
    sigma_sqrt = np.linalg.cholesky(sigma)
    z = np.asarray(gaussian(0.0, 1.0, n))
    return mu + sigma_sqrt @ z


"""
This implementation follows the paper by Debasis Kundu and
Rameshwar D. Gupta: "A Convenient Way of Generating Gamma Random 
Variables Using the Generalized Exponential Distribution"

The method relies on classical properties of the Gamma distribution.

1) Scaling property
If X ~ Gamma(k, 1), then theta * X ~ Gamma(k, theta).

2) Sum of exponentials
The sum of n independent Exponential(1) variables follows
Gamma(n, 1).

3) Shape-addition property
For any real k > 0, write:
    k = n + delta
where n = floor(k) and delta in [0, 1).

Then:
    Gamma(k, 1) = Gamma(n, 1) + Gamma(delta, 1)

Using these properties, a Gamma(k, theta) random variable can be
generated as:

    theta * ( xi - sum_{i=1}^{floor(k)} ln(U_i) )

where:
    - U_i are independent Uniform(0, 1) variables,
    - xi ~ Gamma(delta, 1),
    - delta = k - floor(k).

The main difficulty is simulating xi when delta is in (0, 1).
For this fractional shape case, we use the Ahrens-Dieter
acceptance-rejection method with the following majorizing function:

For x in (0, 1):
    g_k(x) = x^(k - 1) / Gamma(k)

For x >= 1:
    g_k(x) = exp(-x) / Gamma(k)
"""

def gamma(k, theta, size=1, max_iter=1000):
    e = math.exp(1)

    n = int(k)
    delta = k - n

    def safe_u():
        u = _Random.generate()
        if u <= 0.0:
            return 1e-15
        return u

    if (size == 1):
        gamma1 = 0.0  # corresponds to Gamma(delta, 1)

        if (delta > 0.0):
            it = 0
            while (it <= max_iter):
                u1 = _Random.generate()
                u2 = _Random.generate()
                u3 = _Random.generate()

                if (u1 < e / (e + delta)):  # x in (0, 1)
                    g = pow(u2, 1.0 / delta)
                    if (u3 < math.exp(-g)):
                        gamma1 = g
                        break
                else:  # x >= 1
                    g = 1.0 - math.log(u2)
                    if (u3 < pow(g, delta - 1.0)):
                        gamma1 = g
                        break

                it += 1
                if (it == max_iter):
                    raise RuntimeError("Gamma simulation algorithm did not converge")
                    return 0

        s = 0.0
        for _ in range(n):
            Ui = safe_u()
            s += -math.log(Ui)

        return theta * (gamma1 + s)

    res = []
    for i in range(size):
        gamma1 = 0.0

        if (delta > 0.0):
            it = 0
            while (it <= max_iter):
                u1 = safe_u()
                u2 = safe_u()
                u3 = safe_u()

                if (u1 < e / (e + delta)):
                    g = pow(u2, 1.0 / delta)
                    if (u3 < math.exp(-g)):
                        gamma1 = g
                        break
                else:
                    g = 1.0 - math.log(u2)
                    if (u3 < pow(g, delta - 1.0)):
                        gamma1 = g
                        break

                it += 1
                if (it == max_iter):
                    raise RuntimeError("Gamma simulation algorithm did not converge")

        s = 0.0
        for _ in range(n):
            Ui = safe_u()
            s += -math.log(Ui)

        res.append(theta * (gamma1 + s))

    return res

def pareto(xm, alpha, size=1):
    if size == 1:
        u = _Random.generate()
        return xm / pow(u, 1 / alpha)
    res = []
    for i in range(size):
        u = _Random.generate()
        res.append(xm / pow(u, 1 / alpha))
    return res

def chisquare(k, size=1):
    if size == 1:
        return sum(np.asarray(gaussian(0.0, 1.0, k)) ** 2)
    res = []
    for i in range(size):
        res.append(sum(np.asarray(gaussian(0.0, 1.0, k)) ** 2))
    return res