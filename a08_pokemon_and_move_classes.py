# Haley Chadwick, Monica Arias, Ashlyn Crop, Zofia Lacka

# P3- Pokemon Battle (TEAM PROJECT)

import random

class Pokemon:
    def __init__(self, name, elemental_type, hit_points):
        self.name = name
        self.elemental_type = elemental_type
        self.hit_points = 0

    def get_info(self):
        return f"{self.name.title()} - Type: {self.elemental_type} - Hit Points: {self.hit_points}"
        
    
    def heal(self):
        self.hit_points+=15
        print(f"{self.name.title()} has been healed to {self.hit_points} points. ")

