#!/usr/bin/env python
# coding: utf-8

# # Generator of Continue Random Variable with Mersenne Twister

# In[64]:


import numpy as np
from RNG_Uniform import *


# In[65]:


MT=MT19937()
MT.seed(3213)


# In[66]:


def Expectation(Xn):
    return sum(Xn)/len(Xn)

def Variance(Xn):
    exp=Expectation(Xn)
    var=0
    for i in range(len(Xn)):
        var += pow((Xn[i]-exp),2)
    return(var/len(Xn))


# # Uniform Law on $[a,b]$

# In[67]:


def Uniform_Continue(a,b,size=1):
    if size==1:
        U = MT.uniform()
        return a + U*(b-a)
    res =[]
    for i in range(size):
        U = MT.uniform()
        res.append(a+U*(b-a))
    return res


# In[68]:


Sn = Uniform_Continue(-5,7,10000)
print("Expectation :",Expectation(Sn))
print("Variance :",Variance(Sn))
plt.hist(Sn,density=True)


# # Exponential Law

# Simulation with the inverse of the cumulative distribution function

# In[70]:


def Exponential(lambdaa,size=1):
    if size==1:
        U = MT.uniform()
        return -1.0/lambdaa*np.log(U)
    res = []
    for i in range(size):
        U = MT.uniform()
        res.append(-1.0/lambdaa*np.log(U))
    return res


# In[71]:


Sn = Exponential(4,10000)
print("Expectation :",Expectation(Sn))
print("Variance :",Variance(Sn))
plt.hist(Sn,density=True)


# ## Gaussian Law

# Box Muller method

# In[72]:


def Gaussian(mu,sigma,size=1):
    if size==1:
        U1=MT.uniform()
        U2=MT.uniform()
        return (mu + np.sqrt(sigma)*np.sqrt(-2*np.log(U1))*np.cos(2*np.pi*U2))
    res = []
    r = size%2
    for i in range(int(size/2)):
        U1=MT.uniform()
        U2=MT.uniform()
        res.append(mu + np.sqrt(sigma)*np.sqrt(-2*np.log(U1))*np.cos(2*np.pi*U2))
        res.append(mu + np.sqrt(sigma)*np.sqrt(-2*np.log(U1))*np.sin(2*np.pi*U2))
    if (r==1):
        U1=MT.uniform()
        U2=MT.uniform()
        res.append(mu + np.sqrt(sigma)*np.sqrt(-2*np.log(U1))*np.cos(2*np.pi*U2))
    return res


# In[73]:


Sn = Gaussian(5,10,100001)
print("Expectation :",Expectation(Sn))
print("Variance :",Variance(Sn))
plt.hist(Sn,bins=20,density=True)


# In[225]:


def Gaussian_vector(Mu,Sigma,n):
    """
    return a gaussian vector of size n 
    here Mu should be a vector (numpy) and Sigma a Matrix n*n
    """
    L = np.linalg.cholesky(Sigma)
    gauss = np.asarray(Gaussian(0,1,n))
    #print(np.dot(L,gauss)
    return Mu + np.dot(np.dot(L,gauss),L.T)


# In[235]:


n = int(Uniform_Continue(2,10))
S = np.eye(n)
for i in range(n):
    for j in range(i+1,n):
        U = Uniform_Continue(-1,1,1)
        S[i,j] = U
        S[j,i] = U
print(S)
M = np.zeros(n)
print(M)


# In[236]:


gauss = Gaussian_vector(M,S,n)
print(gauss)


# ## Gamma law

# Following the paper of $\textit{Debasis Kundu1 Rameshwar D. Gupta}$, A Convenient Way of Generating Gamma Random Variables Using Generalized Exponential Distribution.
# 
# We use the following properties
# - Scaling property : $ \it{Gamma}(k,\theta) \sim \theta * \it{Gamma}(k,1)$
# - $\sum_{i=1}^n \mathcal{E}(1) \sim \it{Gamma}(n,1)$
# - Shape-addition property : $\it{Gamma}(k,1) \sim \it{Gamma}(n,1) + \it{Gamma}(\delta,1)$ with $\delta \in [0,1]$
# 
# Note that $\theta \left(\xi - \sum_{i=1}^{\lfloor k \rfloor} ln(U_i)\right) \sim \it{Gamma}(k,\theta)$ where $\xi$ is a $\it{Gamma}(\theta,k)$
# 
# $\xi$ is the most difficult to simulate, we use the Ahrens-Dieter acceptance–rejection method with the majorization function
# $
# g_k(x) = \left\{
#     \begin{array}{ll}
#         \frac{x^{k-1}}{\Gamma(k)}& x \in (0,1) \\
#         \frac{e^{-x}}{\Gamma(k)}& x \ge 1
#     \end{array}
# \right.
# $

# In[110]:


def Gamma(k,theta,size=1,max_iter=1000):
    e = np.exp(1)
    n = int(k)
    delta = k - n
    if (size == 1):
        gamma1 = 0 #Correspond to Gamma(delta,1)
        if ( delta > 0):
            it = 0
            while (it <= max_iter):
                U1 = MT.uniform()
                U2 = MT.uniform()
                U3 = MT.uniform()
                if (U1 < e / (e+delta)): #that mean we are on x in (0,1)
                    g = pow(U2,1/delta) #we generate g from the probability density link to the majorization function g
                    if (U3 < np.exp(-g)):#acceptance-rejection
                        gamma1 = g
                        break
                else:#that mean we are on x greater than 1
                    g = 1 - np.log(U2)
                    if (U3 < pow(g,delta-1)):
                        gamma1 = g
                        break
                it +=1
                if (it == max_iter):
                    "Algo didn't converge"
                    return 0
        return theta*(gamma1 - sum(np.log(Uniform_Continue(0,1,n))))
    res = []
    for i in range(size):
        ggamma1 = 0
        if ( delta > 0):
            it = 0
            while (it <= max_iter):
                U1 = MT.uniform()
                U2 = MT.uniform()
                U3 = MT.uniform()
                if (U1 < e / (e+delta)):
                    g = pow(U2,1/delta)
                    if (U3 < np.exp(-g)):
                        gamma1 = g
                        break
                else:
                    g = 1 - np.log(U2)
                    if (U3 < pow(g,delta-1)):
                        gamma1 = g
                        break
                it +=1
                if (it == max_iter):
                    "Algo didn't converge"
                    return 0
        res.append(theta*(gamma1 - sum(np.log(Uniform_Continue(0,1,n)))))
    return res
    


# In[111]:


k, theta = 2.3 , 5.8
Sn = Gamma(k,theta,100000)
print("Expectation :",Expectation(Sn))
print("Variance :",Variance(Sn))
plt.hist(Sn,bins=50,density=True)


# ## Pareto Law $(x_m,\alpha)$

# In[85]:


def Pareto(xm,alpha,size=1):
    if size ==1:
        U = MT.uniform()
        return xm / pow(U,1/alpha)
    res = []
    for i in range(size):
        U = MT.uniform()
        res.append(xm / pow(U,1/alpha))
    return res


# In[98]:


Sn = Pareto(1,1.16,10000)
print("Expectation :",Expectation(Sn))
print("Variance :",Variance(Sn))
plt.hist(Sn,range=[0,10],bins=50,density=True)


# ## $\chi^2(k)$ Law

# In[124]:


def khi_deux(k,size=1):
    if size == 1:
        return sum(np.asarray(Gaussian(0,1,k))**2)
    res = []
    for i in range(size):
        res.append(sum(np.asarray(Gaussian(0,1,k))**2))
    return res


# In[125]:


Sn = khi_deux(6,10000)
print("Expectation :",Expectation(Sn))
print("Variance :",Variance(Sn))
plt.hist(Sn,bins=50,density=True)

