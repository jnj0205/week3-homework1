#Exercise 2 - Write a Python class for an Animal that has a name and energy attributes. 
#The animal class should also have methods for eat, sleep, and play that will take in
# an integer and increase/decrease the energy of the animal with a formatted print statement

class Animals:
    buddy = 'dog'
    
    def __init__(self, breed, energy):
        self.breed = breed
        self.energy = energy
        
        
    def buddy_play(self, play):
        play_time = play //5
        self.energy -= play
        print(f"After paying {play} minutes, the {self.breed}now has a level of {self.energy}")
    

    def buddy_sleep(self, sleep):
        sleep_time = sleep * 10
        self.energy += sleep
        print(f"After paying {sleep} minutes, the {self.breed}now has a level of {self.energy}")
            
animal1 = Animals('french_bulldog', '2')
animal2 = Animals('pitbull', '10')
animal3 = Animals('puddle', '8')
