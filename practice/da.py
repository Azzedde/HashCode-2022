from collections import Counter

def count_ing(clients):
    likes = Counter()
    hates = Counter()
    for client in clients:
        likes += Counter(client.like)
        hates += Counter(client.hate)
    return likes, hates

