from da import count_ing


def no_haters(clients):
    likes, hates = count_ing(clients)
    likes = set(likes.keys())
    hates = set(hates.keys())
    return likes.difference(hates)
