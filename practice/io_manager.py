from client import Client

def read_input(character):
    clients = []
    with open(f"data/{character}.in.txt") as f:
        for i, line in enumerate(f):
            if i == 0:
                print(f"Case {character}: {line.strip()} clients")
                continue
            elif i%2 == 1:
                like = set(line.strip().split()[1:])
            else:
                hate = set(line.strip().split()[1:])
                clients.append(Client(like, hate))
    return clients

def write_output(pizza, character):
    with open(f"output/{character}.out.txt", "w") as f:
        line = [str(len(pizza))] + list(pizza)
        f.write(" ".join(line))

