#!/usr/bin/env python
# coding: utf-8

# # Generator of Discrete Random Variable with Mersenne Twister

# In[94]:


import numpy as np
from RNG_Uniform import *


# In[95]:


MT=MT19937()
MT.seed(3213)


# In[96]:ef 


def Expectation(Xn):
    return sum(Xn)/len(Xn)

def Variance(Xn):
    exp=Expectation(Xn)
    var=0
    for i in range(len(Xn)):
        var += pow((Xn[i]-exp),2)
    return(var/len(Xn))


# ## Uniform Discrete

# In[172]:


def Uniform_Discrete(a,b,size=1):
    '''
    Give a random number between a and b with uniform probability
    '''
    if size==1:
        U = MT.uniform()
        return a + int( U * (b-a+1))
    res = []
    for i in range(size):
        U = MT.uniform()
        res.append(a + int( U * (b-a+1)))
    return res
        


# In[179]:


Sn = Uniform_Discrete(-5,5,10000)
print("Expectation :",Expectation(Sn))
print("Variance :",Variance(Sn))
plt.hist(Sn,bins=11)


# ## Bernouilli

# In[62]:


def Bernouilli(p,size=1):
    if size==1:
        U = MT.uniform()
        if (U<1-p):
            return 0
        else:
            return 1
    res=[]
    for i in range(size):
        U = MT.uniform()
        if (U<1-p):
            res.append(0)
        else:
            res.append(1)
    return res


# In[60]:


size = 100000
Sn=Bernouilli(0.3,size)
print("Expectation :",Expectation(Sn))
print("Variance :",Variance(Sn))
print(0.3*0.7)
plt.hist(Sn)


# ## Binomial

# In[194]:


def Binomial(n,p,size=1):
    if size == 1 :
        return(sum(Bernouilli(p,n)))
    res = []
    for i in range(size):
        res.append(sum(Bernouilli(p,int(n))))
    return res
        


# In[195]:


Sn = Binomial(10,0.3,size=100000)
print("Expectation :",Expectation(Sn))
print("Variance :",Variance(Sn))
plt.hist(Sn)


# ## Geometric
# 

# In[196]:


def Geometric(p,size=1):
    if size==1:
        res = 1
        U = MT.uniform()
        while (U>p):
            U = MT.uniform()
            res +=1
        return res
    res = []
    for i in range(n):
        U = MT.uniform()
        res_tmp = 1
        while (U>p):
            U = MT.uniform()
            res_tmp +=1
        res.append(res_tmp)
    return res


# In[197]:


Sn = Geometric(0.5,size=10000)
print("Expectation :",Expectation(Sn))
print("Variance :",Variance(Sn))
plt.hist(Sn)


# ## Poisson

# Simultion method using the Th. : $(X_n)$ is an i.i.d. sequence of exponential law of parameters $\lambda$ then for $S_n = \sum_{i=1}^n X_n$ $\forall n \in \mathbb{N}, \mathbb{P}(S_n \le 1 \le S_{n+1})=\frac{\lambda^k}{k!}e^{-k}$ 
# $\textit{Looking for Proof}$

# In[237]:


def Poisson(lambdaa,size=1):
    if size==1:
        k=0
        p=1
        while (p > np.exp(-lambdaa)):
            U = MT.uniform()
            p = p*U
            k +=1
        return (k-1)
    res = []
    for i in range(size):
        k=0
        p=1
        cond = np.exp(-lambdaa)
        while (p > cond):
            U = MT.uniform()
            p = p*U
            k +=1
        res.append(k-1)
    return res


# In[239]:


Sn = Poisson(5,size=10000)
print("Expectation :",Expectation(Sn))
print("Variance :",Variance(Sn))
plt.hist(Sn)


# Another simulation method using the fact that the Poisson law is the limit of a Binomial($n$,$p_n$) with $p_n = \frac{\lambda}{n}$.
# A minimal condition is $\lambda <10$

# In[204]:


def Poisson_2(lambdaa,size=1):
    n = 100.0
    p = lambdaa/n
    if size==1:
        return Binomial(n,p,1)
    return Binomial(n,p,size)


# In[207]:


Sn = Poisson_2(4,size=10000)
print("Expectation :",Expectation(Sn))
print("Variance :",Variance(Sn))
plt.hist(Sn)

