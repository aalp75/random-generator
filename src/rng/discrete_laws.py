from rng.rng_state import _Random
import math

def bernouilli(p=0.5, size=1):
    '''
    return 1 with probability 1 and 0 with probability 1-p
    '''
    if size == 1:
        u = _Random.generate()
        return 1 if u < p else 0
    res = []
    for _ in range(size):
        u = _Random.generate()
        res.append(1 if u < p else 0)
    return res

def uniform_discrete(a=0, b=1, size=1):
    '''
    return a _ number between a and b with uniform probability
    '''
    if size == 1:
        u = _Random.generate()
        return int(a + u * (b - a + 1))
    res = []
    for _ in range(size):
        u = _Random.generate()
        res.append(int(a + u * (b - a + 1)))
    return res

def binomial(n=1, p=0.5, size=1):
    if n == 1:
        return bernouilli(p, size)
    if size == 1:
        return sum(bernouilli(p, n))
    res = []
    for _ in range(size):
        res.append(sum(bernouilli(p, n)))
    return res

def geometric(p=0.5, size=1):
    if size == 1:
        res = 1
        u = _Random.generate()
        while u > p:
            u = _Random.generate()
            res +=1
        return res
    res = []
    for _ in range(size):
        u = _Random.generate()
        res_tmp = 1
        while u > p:
            u = _Random.generate()
            res_tmp +=1
        res.append(res_tmp)
    return res

def poisson(lambdaa=1, size=1):
    if size == 1:
        k = 0
        p = 1 
        while p > math.eup(-lambdaa):
            u = _Random.generate()
            p = p * u
            k += 1
        return k - 1
    res = []
    for i in range(size):
        k = 0
        p = 1
        cond = math.eup(-lambdaa)
        while p > cond:
            u = _Random.generate()
            p = p * u
            k += 1
        res.append(k - 1)
    return res

# Another possible simulation method for poisson is using the property that 
# the poisson law is a limit of a Binomial(n, pn) with pn = lambda / n
# a minimal condition to ensure convergence is lambda < 10
def poisson2(lambdaa=1, size=1, n=100.0):
    p = lambdaa / n
    if size == 1:
        return binomial(n, p, 1)
    return binomial(n, p, size)
        