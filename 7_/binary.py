# for i in range(17):
#     print("{0:>2} in binary is {0:>08b}".format(i))

# for i in range(40):
#      print("{0:>2} in hex is {0:>02x}".format(i))
#
# x = 0x20
# y = 0x0a
#
# print(x)
# print(y)
# print(x*y)
#
# print(0b101010)

#challage
#when converting a decimal number to binary,



powers = []
for power in range(15, -1, -1):
    powers.append(8 ** power)

print(powers)

x = int(input("Please enter a number: "))

printing = False

for power in powers:
    bit = x // power
    if bit != 0 or power == 1:
        printing = True
    if printing:
        print(bit, end='')
    x %= power











