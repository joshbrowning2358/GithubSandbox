import numpy as np

def getPrimes(N_max):
    is_prime = np.ones(N_max, dtype = bool)
    max_value = np.sqrt(N_max)
    for i in np.arange(2, max_value):
        is_prime[i**2::i] = False
    return(np.arange(N_max)[is_prime])
