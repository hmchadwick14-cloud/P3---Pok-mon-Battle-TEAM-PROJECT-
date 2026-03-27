# Haley Chadwick, Monica Arias, Ashlyn Crop, Zofia Lacka

# P3- Pokemon Battle (TEAM PROJECT)

import random

#create a class called move
#add a constructor called __init__ with the parameters for self, move_name, elemental_type, low_attack_points, and high_attack_points
class Move :
    def __init__ (self, move_name, elemental_type, low_attack_points, high_attack_points) :
        self.move_name = move_name
        self.elemental_type = elemental_type
        self.low_attack_points = low_attack_points
        self.high_attack_points = high_attack_points

    #add a constructor called get_info with just self as a parameter
    #should return a string that includes all of its variables 
    def get_info (self) :
        return f"{self.move_name} (Type: {self.elemental_type}): {self.low_attack_points} to {self.high_attack_points} Attack Points"
    
    #add a constructor called generate_attack_value with just self as a parameter
    #should generate a random number between the low_attack_points and high_attack_points and return that value
    def generate_attack_value (self) :
        return random.randint(self.low_attack_points, self.high_attack_points)
    
#create 9 move objects
move1 = Move("Tackle", "Normal", 5, 20)
move2 = Move("Quick Attack", "Normal", 6, 25)
move3 = Move("Slash", "Normal", 10, 30)
move4 = Move("Flamethrower", "Fire", 5, 30)
move5 = Move("Ember", "Fire", 10, 20)
move6 = Move("Water Gun", "Water", 5, 15)
move7 = Move("Hydro Pump", "Water", 20, 25)
move8 = Move("Vine Whip", "Grass", 10, 25)
move9 = Move("Solar Beam", "Grass", 18, 27)

#create a list that stores each of the 9 objects in it
move_list = [move1, move2, move3, move4, move5, move6, move7, move8, move9]

#do a for loop that runs 3 times, and in each iteration, do the following:
'''
Randomly select a Move object from the list you created
Print out the result of the get_info method of the randomly selected object.
Print out Generated attack value:  and then the returned value from running the generate_attack_value method on the randomly selected object.
Then delete the move from the list of moves. This ensures that you won't randomly select the same move twice. 
If you randomly select the same move twice, the automated tests won't pass.
'''

for i in range(3) :
    selected_move = random.choice(move_list)

    print(selected_move.get_info())
    print("Generated attack value:", selected_move.generate_attack_value())

    move_list.remove(selected_move)

#after finishing the loop, to add a pause in your program, add this line of code:

input("Press enter to continue...")

#create a class called Pokemon
#Create the constructor with parameters for self, name, elemental_type, and hit_points
class Pokemon :
    def __init__(self, name, elemental_type, hit_points) :
        self.name = name
        self.elemental_type = elemental_type
        self.hit_points = 0

    #Create a method called get_info that returns the name, elemental_type, and hit_points in a string.
    def get_info(self):
        return f"{self.name.title()} - Type: {self.elemental_type} - Hit Points: {self.hit_points}"
        
    #Create a method called heal with just self as a parameter. It increases the current value of hit_points by 15 and prints out a message with 
    # the Pokémon’s name and what their new value of hit_points are. It should print out the message directly in the method, and not return anything.
    def heal(self):
        self.hit_points+=15
        print(f"{self.name.title()} has been healed to {self.hit_points} points. ")