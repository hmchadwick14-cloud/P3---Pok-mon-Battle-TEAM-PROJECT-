# Haley Chadwick, Monica Arias, Ashlyn Crop, Zofia Lacka

# P3- Pokemon Battle (TEAM PROJECT)

import random

<<<<<<< Updated upstream
class Move :
    def __init__ (self, move_name, elemental_type, low_attack_points, high_attack_points) :
        self.move_name = move_name
        self.elemental_type = elemental_type
        self.low_attack_points = low_attack_points
        self.high_attack_points = high_attack_points

    def get_info (self) :
        return f"{self.move_name} (Type: {self.elemental_type}): {self.low_attack_points} to {self.high_attack_points} Attack Points"
    
    def generate_attack_value (self) :
        return random.randint(self.low_attack_points, self.high_attack_points)
    
    
=======


>>>>>>> Stashed changes
