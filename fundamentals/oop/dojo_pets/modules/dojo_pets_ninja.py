import dojo_pets_pet #for use with module bonus exercise (pet class seoparated)
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

# Dingo = Ninja("Dingo","Demkowski",Spot,["chickenbits","crickets","cotton balls"],"Cat Chow")

Dingo = Ninja("Dingo","Demkowski",dojo_pets_pet.Spot,["chickenbits","crickets","cotton balls"],"Cat Chow") #for use with module bonus exercise (pet class seoparated)

print(Dingo.pet_food)
# print(Spot.tricks[2])

print(dojo_pets_pet.Spot.tricks[2]) #for use with module bonus exercise (pet class separated)

Dingo.feed()
Dingo.bathe()
Dingo.walk()