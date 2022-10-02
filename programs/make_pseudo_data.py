import numpy as np

def make_data(probs, size=10, set_seed=True):

    data_mx = []
    for i, p in enumerate(probs):
        if set_seed:
            np.random.seed(i)
        data_mx.append(np.random.binomial(n=1, p=p, size=size).tolist())

    return np.array(data_mx).T

if __name__ == "__main__":
    """
    - categories: タグ
    - interest_prob: categoriesの要素に対応する,興味のあるユーザの割合
    """
    categories = ['economics', 'AI', 'business', 'sports']
    probs = [0.4, 0.8, 0.3, 0.3]
    size = 10000

    data = make_data(probs, size).astype(str)
    with open('../data/pseudo_user_interest.csv', 'w') as f:
        f.write(','.join(categories) + '\n')
        for line in data:
            f.write(','.join(line) + '\n')
