import random as rand

class Animatronic:
    def __init__(self, name, cam, ai_level):
        self.name = name
        self.cam = cam
        self.ai_level = ai_level
        
freddy = Animatronic("Freddy", 1, 1)
bonnie = Animatronic("Bonnie", 1, 0)
chica = Animatronic("Chica", 1, 0)
foxy = Animatronic("Foxy", 4, 0)
golden_freddy = Animatronic("Golden Freddy", 2, None)

ANIMATRONICS = {
    freddy,
    bonnie,
    chica,
    foxy,
    golden_freddy
}
CAM = {
    1,
    2,
    3,
    4,
    5, # e
    6,
    7,
    8, # a
    9, # b
    10, # c
    11 # d
}

def movement_timer(animatronic):
    match animatronic.name:
        case "Bonnie": 
            None


def increase_ai_level(hour, night):
    global freddy, bonnie, chica, foxy

    if hour == 2:
        bonnie.ai_level += 1
    if hour == 3 or hour == 4:
        bonnie.ai_level += 1
        chica.ai_level += 1
        foxy.ai_level += 1
    if (night == 4) and ((hour == 1) or (hour == 2) or (hour == 3) or (hour == 4)):
        freddy.ai_level = rand.randint(1, 2) 

def night_ai(night, hour):
    global freddy, bonnie, chica, foxy
    
    match night:
        case 1:
            freddy.ai_level -= 1
            increase_ai_level(hour, night)
        case 2:
            freddy.ai_level -= 1
            bonnie.ai_level = 3
            chica.ai_level = 1
            foxy.ai_level = 1
            increase_ai_level(hour, night)
        case 3:
            chica.ai_level = 5
            foxy.ai_level = 2
            increase_ai_level(hour, night)
        case 4:
            freddy.ai_level = rand.randint(1,2)
            bonnie.ai_level = 2
            chica.ai_level = 4
            foxy.ai_level = 6
            increase_ai_level(hour, night)
        case 5:
            freddy.ai_level = 3
            bonnie.ai_level = 5
            chica.ai_level = 7
            foxy.ai_level = 5
            increase_ai_level(hour, night)
        case 6:
            freddy.ai_level = 4
            bonnie.ai_level = 10
            chica.ai_level = 12
            foxy.ai_level = 6
            increase_ai_level(hour) 

def animatronic_on(night):
    if night == 1:
        None
        
def animatronic_off():
    print("tamo off")

