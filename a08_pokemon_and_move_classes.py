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
