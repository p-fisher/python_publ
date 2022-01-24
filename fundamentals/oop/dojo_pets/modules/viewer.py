from dojo_pets_pet import Pet
from dojo_pets_ninja import Ninja

spot = Pet("Spot", "Cat", ["Dance","Hop","Speak"],70,50)
dingo = Ninja("Dingo","Demkowski",spot,["chickenbits","crickets","cotton balls"],"Cat Chow") #for use with module bonus exercise (pet class seoparated)

print(dingo.pet_food)
print(spot.tricks)

print(spot.tricks[2]) #for use with module bonus exercise (pet class separated)

dingo.feed()
dingo.bathe()
dingo.walk()