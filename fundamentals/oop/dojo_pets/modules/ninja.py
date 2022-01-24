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