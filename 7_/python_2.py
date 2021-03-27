# r = range(0, 100)
# print(r)
#
# for i in r[::-2]:
#     print(i)
#
# for i in range(99, 0, -2):
#     print(i)
#
# for i in range(0, 100, -2):
#     print(i)

# o = range(0, 100, 4)
# print(o)
# p = o[::5]
# print(p)
# for i in p:
#     print(i)

#tuples

# t = "a", "b", "c"
# print(t)
#
# print("a" , "b", "c")
# print(("a", "b", "c"))

# welcome = "Welcome to my Nightmare" "alice cooper", 1975
# bad = "Bad company " "Bad company " , 1974
# budgie = "Nightflight", "Budgie", 1981
# imelda = "More Mayhem", "Emilda May", 2011,(
#     1, "pulling the rug", 2, "Psycho", 3, "Mayhem", 4,"kentish town wal")
#
# print(imelda)
#
# title, artist , year , tracks = imelda
# print(title)
# print(artist)
# print(year)
# print(tracks)




#metallica = "Ride the lightning" , "Metallica", 1984

# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])
#
# imelda = imelda[0], "Imelda May", imelda[2]
# print(imelda)
#
# metallica2 = ["Ride the lightning", "Metallica", 1984]
# print(metallica2)
#
# metallica2[0] = "Master of puppets"
# print(metallica2)


# welcome = "Welcome to my Nightmare" "alice cooper", 1975
# bad = "Bad company " "Bad company " , 1974
# budgie = "Nightflight", "Budgie", 1981
# imelda = "More Mayhem", "Emilda May", 2011,(1, "pulling the rug"), (2, "Psycho"), (3, "Mayhem"), (4,"kentish town wal")
#
# print(imelda)
#
# title, artist, year, track1, track2, track3 , track4= imelda
# print(title)
# print(artist)
# print(year)
# print(track1)
# print(track2)
# print(track3)
# print(track4)

imelda = "More Mayhem", "Emilda May", 2011,(
        [ (1, "pulling the rug"), (2, "Psycho"), (3, "Mayhem"), (4,"kentish town wal")])

print(imelda)

imelda[3].append((5, "All For YOu"))

title,artist, year, tracks = imelda
tracks.append((6, "Eternity"))
print(title)
print(artist)
print(year)
for song in tracks:
    track, title = song
    print("\tTrack number {}, Title: {}".format(track, title))

































