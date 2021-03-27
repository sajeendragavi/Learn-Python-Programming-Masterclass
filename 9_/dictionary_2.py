# fruit = {"orange" : "a sweet, orange, citrus fruit",
#          "apple"  : "good for making cider",
#          "lemon"  : "a sour, yellow citrus fruit",
#          "grape"  : "a small, sweet fruit growing in bunches",
#          "lime"   : "a sour, green citrus fruit",
#          "apple"  : "round and crunchy"}
#
#
# print(fruit)
#
# print(fruit)
# print(fruit.items())
# f_tuple = tuple(fruit.items())
# print(f_tuple)
#
# for snack in f_tuple:
#     item, description = snack
#     print(item + " is " + description)
# print(dict(f_tuple))

#Modify  the programme so that the exits is a dictionary rather than a list,
#with the keys being the numbers of the locations and the values being
#dictionaries holding the exits (as they do at present ).No change should
#be needed to the actual code.
#once that is working,create another dictionary that contains word that
#playes must use.these words will be the keys.and their values  will be
#a single letter that the program can use to determine which way to go.

locations = {0: "You are sitting in front of a computer learning python ",
             1: "you are standig at the end of a road before a small brick building ",
             2: "you are at the top of a hill",
             3: "You are inside a building, a well house for a small stream ",
             4: "you are in a valley besides a stream",
             5: "You are in the forest"}

exits = [{"Q" : 0},
         {"W" : 2, "E": 3, "N": 5, "s": 4,"Q": 0},
         {"N":5 , "Q": 0},
         {"W":1 , "Q": 0},
         {"N":1 , "W":2 , "Q": 0},
         {"W":2 , "S" :1 , "Q": 0},
         ]

loc = 1
while  True:
    availableExits = ", ".join(exits[loc].keys())

    print(locations[loc])

    if loc == 0:
        break

    direction = input("Available exits are " + availableExits + " ").upper()
    print()
    if direction in exits[loc] :
        loc = exits[loc][direction]
    else:
        print("You can not go in the direction")















