class Pet:
    def __init__(self, pet_name, type, tricks, health, energy):
        self.pet_name = pet_name
        self.type = type
        # self.tricks = {tricks}: ["rollover", "sit", "shake", "speak"]
        self.tricks = tricks
        self.health = health
        self.energy = energy
        # self.noise = noise  #if using this, add as attribute too!
        
    def sleep(self):
        self.health += 5
    
    def eat(self):
        print(self.noise)
        self.health += 3
        self.energy += 5
    
    def play(self):
        self.health += 10
        self.energy -= 5
    
    def noise(self):
        print(f"Meow... Purr, Purr, Purr... Hiss")


Spot = Pet("Spot", "Cat", ["Dance","Hop","Speak"],70,50)