import json

class Tournament:
    
    def __init__(self, name, year):
        self.name = name
        self.year = year
    
tournametns = {
    "AO" : 2010,
    "FVC" : 2018,
    "FGS" : 2020
}

# json_data = json.dumps(tournametns, indent = 2)   #serialization
# print(json_data)

# loaded = json.loads(json_data)   #deserialization
# print(type(loaded))
# print(loaded)

# t1 =Tournament("AO", 2010)
# json_data = json.dumps(t1.__dict__)
# print(json_data)
# t = Tournament(**json.loads(json_data))
# print(f'name = {t.name}, year = {t.year}')

class ChessPlayer:
    
    def __init__(self, tournaments):
        self.tournaments = tournaments

t1 = Tournament("AO", 2010)
t2 = Tournament("FVC", 2018)
t3 = Tournament("FGS", 2020)

p1 = ChessPlayer([t1, t2, t3])

json_data = json.dumps(p1.__dict__, default = lambda obj : obj.__dict__)

print(json_data)

decoded_player = ChessPlayer(**json.loads(json_data))
print(decoded_player)

player_tournament = decoded_player.tournaments[0]
print(type(player_tournament))



with open('player.json', 'w') as file:
    json.dump(p1, file, default= lambda obj: obj.__dict__)

with open('player.json', 'r') as read_file:
    data = json.load(read_file)

print(data)
