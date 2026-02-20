## Random Generator

Pseudo-random generator Python library with the core uniform generators implemented in C++.

 - **Discrete distributions**: bernouilli, uniform, binomial, geometric, poisson.
 - **Continuous distributions**:, exponential, gaussian (scalar and vector), gamma, pareto, chi-square.
 - **MCMC**: Metropolis-Hastings for custom densities.
 - **Statistical tests**: chi-square (homogeneity and independence), Kolmogorov-Smirnov.

Different uniform generators are available: middle-square, linear congruence and mersenne twister (MT19937). It is highly recommended to use mersenne twister for practical applications.

## Usage

```bash 
git clone https://github.com/aalp75/random-generator.git

python -m venv .venv
source .venv/bin/activate

make build # builds the C++ extension and installs rng as a package
```

## Code Example

```python
import rng
import math

rng.set_generator('mt19937', 57)

sample = rng.gaussian(0, 1, size=100) # generate a sample of 100 gaussian N(0, 1)

def gaussian_density(x):
    mu, sigma = 5, 1 # mean and standard deviation
    num = math.exp(-(x - mu) ** 2 / (2.0 * sigma ** 2))
    normalization = math.sqrt(2 * math.pi * sigma ** 2)
    return  num / normalization

sample, ratio = rng.mcmc(gaussian_density, size=100) # generate the same sample using MCMC
print(f"Acceptance ratio: {ratio * 100:.2f}%")
```

```text
Acceptance ratio: 24.87%
```
More detailed examples are available in the **examples** folder.