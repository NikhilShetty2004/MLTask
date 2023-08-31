import random

class ChessPlayer:
    def __init__(self, name, age, elo, tenacity, is_boring):
        self.name = name
        self.age = age
        self.elo = elo
        self.tenacity = tenacity
        self.is_boring = is_boring
        self.tournament_score = 0
    
    def simulateMatch(self, opponent):
        eloDiff = abs(self.elo - opponent.elo)
        
        if eloDiff > 100:
            if self.elo > opponent.elo:
                self.tournament_score += 1
            else:
                opponent.tournament_score += 1
        elif eloDiff >= 50:
            lower_elo_player = self if self.elo < opponent.elo else opponent
            higher_elo_player = opponent if lower_elo_player is self else self
            
            random_factor = random.randint(1, 10)
            lower_elo_chance = random_factor * lower_elo_player.tenacity
            if lower_elo_chance > higher_elo_player.elo:
                lower_elo_player.tournament_score += 1
            else:
                higher_elo_player.tournament_score += 1
        else:
            if self.tenacity > opponent.tenacity:
                self.tournament_score += 1
            elif self.tenacity < opponent.tenacity:
                opponent.tournament_score += 1
            elif self.is_boring or opponent.is_boring:
                self.tournament_score += 0.5
                opponent.tournament_score += 0.5

players_data = [
    ("Courage the Cowardly Dog", 25, 1000.39, 1000, False),
    ("Princess Peach", 23, 945.65, 50, True),
    ("Walter White", 50, 1650.73, 750, False),
    ("Rory Gilmore", 16, 1700.87, 500, False),
    ("Anthony Fantano", 37, 1400.45, 400, True),
    ("Beth Harmon", 20, 2500.34, 150, False)
]

players = []
for data in players_data:
    player = ChessPlayer(*data)
    players.append(player)

# Simulate matches
for i in range(len(players)):
    for j in range(i + 1, len(players)):
        players[i].simulateMatch(players[j])
        players[j].simulateMatch(players[i])

# Print the final table of results
print("\nFinal Tournament Results:\n")
print("Player Name\t\t\tTournament Score")
for player in players:
    print(f"{player.name.ljust(25)}\t\t{player.tournament_score:.1f}")


   
  