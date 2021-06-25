from main import Captains
import random
from collections import Counter

Tyler1 = Captains("Tyler1", 30000)
Yassuo = Captains("Yassuo", 6000)
NB3 = Captains("NB3", 5000)
Voyboy = Captains("Voyboy", 7000)

Shroud = Captains("Shroud", 30000)
Summit1G = Captains("Summit1G", 25000)
Ninja = Captains("Ninja", 25000)
Sliker = Captains("Sliker", 5000)

Bhuga = Captains("Bhuga", 200)
Tfue = Captains("Tfue", 10000)
virgin3 = Captains("virgin3", 1)
virgin4 = Captains("virgin4", 2)

xQc = Captains("xQc", 50000)
Dr_Lupo = Captains("DrLupo", 8000)
Hikaru = Captains("Hikaru", 9000)
Nutwig = Captains("Nutwig", 40000)

LOL = [Tyler1, Yassuo, NB3, Voyboy]
Valorant = [Shroud, Summit1G, Ninja, Sliker]
Fortnite = [Bhuga, Tfue, virgin3, virgin4]
FG = [xQc, Dr_Lupo, Hikaru, Nutwig]

Team1 = ["Team1"]
Team2 = ["Team2"]
Team3 = ["Team3"]
Team4 = ["Team4"]
Teams = [Team1, Team2, Team3, Team4]

x = random.choice(LOL)
y = random.choice(Teams)

z = random.choice(Valorant)
y = random.choice(Teams)

d = random.choice(Fortnite)
y = random.choice(Teams)

h = random.choice(FG)
y = random.choice(Teams)

pickings = (x, z, d, h)

def IsContentGolem(name):
    if name.content_golem >= 20000:
        return True
    else:
        return False

def pick():
    phrase = input("Type start to randomly select!: ")
    print(random.choice(pickings) + y)



print(pick())





















