class Animatronic:
    def __init__(self, name, cam, difficulty):
        self.name = name
        self.cam = cam
        self.difficulty = difficulty
        
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

def night_one_ai(night, hour):
    global freddy, bonnie, chica, foxy
    if night == 1:
        freddy.difficulty -= 1
        if hour == 2:
            bonnie.difficulty += 1
        if hour == 3 or hour == 4:
            bonnie.difficulty += 1
            chica.difficulty += 1
            foxy.difficulty += 1

def night_two_ai(night, hour):
    global freddy, bonnie, chica, foxy

def animatronic_on(night):
    if night == 1:
        None
def animatronic_off():
    print("tamo off")

