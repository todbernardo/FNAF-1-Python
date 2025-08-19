class Animatronic:
    def __init__(self, name, cam):
        self.name = name
        self.cam = cam

freddy = Animatronic("Freddy", 1)
bonnie = Animatronic("Bonnie", 1)
chica = Animatronic("Chica", 1)
foxy = Animatronic("Foxy", 4)
golden_freddy = Animatronic("Golden Freddy", 2)

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
    "e",
    6,
    7,
    "a",
    "b",
    "c",
    "d"
}

def animatronic_on():
    print("tamo on")

def animatronic_off():
    print("tamo off")

