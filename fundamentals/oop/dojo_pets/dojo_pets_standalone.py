#
class Ninja:
    def __init__(self, fname, lname, pet, treats, pet_food): 
        self.fname = fname
        self.lname = lname
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
        
    def walk(self):
        self.pet.play()
        print(f"{self.pet.pet_name} seems happy after the walk!")
        return self
    
    def feed(self):
        # self.pet_food -=1
        print(f"{self.fname} has fed {self.pet.pet_name}")
        return self
    
    def bathe(self):
        self.pet.noise()
        return self
    
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
Dingo = Ninja("Dingo","Demkowski",Spot,["chickenbits","crickets","cotton balls"],"Cat Chow")

print(Dingo.pet_food)
print(Spot.tricks[2])

Dingo.feed()
Dingo.bathe()
Dingo.walk()