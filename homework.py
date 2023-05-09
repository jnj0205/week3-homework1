#Exercise 2 - Write a Python class for an Animal that has a name and energy attributes. 
#The animal class should also have methods for eat, sleep, and play that will take in
# an integer and increase/decrease the energy of the animal with a formatted print statement

class Animals:
    buddy = 'dog'
    
    def __init__(self, breed, energy):
        self.breed = breed
        self.energy = energy
        
        
    def buddy_play(self, paying):
        self.energy -= play//5
        

    def buddy_sleep(self, sleeping):
        self.energy += sleep*10
        
    
    
animal1 = Animals('french_bulldog', '2')
animal2 = Animals('pitbull', '10')
animal3 = Animals('pudle', '8')

print(animal1.energy)