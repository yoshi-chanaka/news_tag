import numpy as np

def make_data(probs, size=10, set_seed=True):

    data_mx = []
    for i, p in enumerate(probs):
        if set_seed:
            np.random.seed(i)
        data_mx.append(np.random.binomial(n=1, p=p, size=size).tolist())

    return np.array(data_mx).T
