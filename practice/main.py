from client import score
from da import count_ing
from io_manager import read_input, write_output
from strategy import no_haters as method


for char in "abcde":
    clients = read_input(char)
    pizza = method(clients)
    print(f"Case {char}: {score(clients, pizza)} score")
    write_output(pizza, char)
    print()
