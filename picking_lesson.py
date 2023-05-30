class Character:
    
    def __init__(self, race, damage = 10):
        self.race = race
        self.damage = damage
        self.health = 100
        
    def hit(self, damage):
        self.health -= damage
        
    def is_dead(self):
        return self.health == 0
    