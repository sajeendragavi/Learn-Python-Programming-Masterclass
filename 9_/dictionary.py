fruit = {"orange" : "a sweet, orange, citrus fruit",
         "apple"  : "good for making cider",
         "lemon"  : "a sour, yellow citrus fruit",
         "grape"  : "a small, sweet fruit growing in bunches",
         "lime"   : "a sour, green citrus fruit",
         "apple"  : "round and crunchy"}

# print(fruit)
# print(fruit["lemon"])  #searching with a key
# fruit["pear"] = "an odd shaped apple"
# print(fruit)
# fruit["lime"] = "great with tequila"
# print(fruit)
# del fruit["lemon"]
# print(fruit)
# print(fruit["tomato"])

print(fruit)
# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     description = fruit.get(dict_key, "we do not have a" + dict_key)
#     print(description)

    # if dict_key in fruit:
    #     descripton = fruit.get(dict_key)
    #     print(descripton)
    # else:
    #     print("we do not have a " + dict_key)

# for i in range(10):
#     for snack in fruit:
#         print(snack + " is " + fruit[snack])
#     print('-' * 40)

ordered_keys = list(fruit.keys())
ordered_keys.sort()
for f in ordered_keys:
    print(f + "-" + fruit[f])















