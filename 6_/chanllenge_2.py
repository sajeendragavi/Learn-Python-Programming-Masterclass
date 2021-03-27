#Create a program that takes an IP address entered at the keyboard
#and prints out the number of segments it contains,and the length of each segment.

#An IP address consists of 4 numbers , seperated from each other with a full stop.but your
#program should just count however many are entered
#Example of the input you may get are:
#   127.0.0.1
#   .192.168.0.1
#   10.0.123456.255
#   172.16
#   255

# So your program should work even with invalid IP Addresses.We are just interested in the number
# of segments and how long each one is.

# Once you have a working program,here some more suggestions for invalid input to test:
#    .123.45.678.91
#    123.4567.8.9
#    123.156.289.10123456
#    10.10t.10.10
#    12.9.34.6.12.90
#    '' - this is,press enter without typing anything

# This challenge is intented to practise for loops and if/else statements, so although
# You could use other techniques (such as spliting the string up), that is not the
# Approach we are looking for here.

input_prompt =("please enter an IP adderess.An IP address consists of 4 numbers , "
               "seperated from each other with a full stop.:")

ipAddress = input(input_prompt)

if ipAddress[-1] != '.':
    ipAddress += '.'

segment = 1
segment_length = 0
#charater = ""

for character in ipAddress:
    if character == '.':
        print("segment {} contains {} characters".format(segment, segment_length))
        segment += 1
        segment_length = 0
    else:
        segment_length += 1

# unless the final character in the string was a . then we have not printed the last segment

#if character != '.':
 #  print("segment {} contains {} characters".format(segment, segment_length))





