import math



potions = float(input("Enter your score on Potions: "))
history = float(input("Enter your score on History of Magic:  "))
defense = float(input("Enter your score on Defense Against The Dark Arts: "))

if defense>100 or defense <1 or potions > 100 or potions < 1 or history > 100 or history < 1:
    print("INVALID SCORE")

if potions >= 90 and defense >= 90 and history >=90:
    print("Auror")
    quit()
if potions >= 70 and defense >= 70 and history >= 90:
    print("Hogwarts Professor")
    quit()
if history >= 80 and defense >= 70:
    print("Wandmaker")
    quit()
if defense >= 70:
    print("Gringotts Gaurd")
    quit()
if potions >= 90:
    print("Healer")
    quit()
if history >= 70:
    print("Ministry Worker")
    quit()
else:
    print("Owl Wrangler")
    quit()
