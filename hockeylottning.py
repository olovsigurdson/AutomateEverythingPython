import random

list_players = ["Willhard", "Melwin", "Hudson", "Loui", "Hjalmar M", "Mio", "Thed"]
chosen_players = []

while len(chosen_players)<3:
    chosen_one = random.choice(list_players)
    list_players.remove(chosen_one)
    chosen_players.append(chosen_one)

print(chosen_players)
print('heh')

