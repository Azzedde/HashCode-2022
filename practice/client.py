import numpy as np

class Client:
    def __init__(self, like, hate):
        self.like = like
        self.hate = hate

    def score(self, pizza):
        return self.like.issubset(pizza) and self.hate.isdisjoint(pizza)

def score(clients, pizza):
    return np.sum([c.score(pizza) for c in clients])
