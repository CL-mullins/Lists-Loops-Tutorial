songs = ["ROCKSTAR", "Do It", "For The Night"]
print(songs[1:3])

songs[2] = 'Dragged'
print(songs)

songs.append("Overgrown")
songs.append("Thrown")
songs.append("Sympathy")
print(songs)

del songs[0]
print(songs)

animals = ["Dogs","Dragons","Lizards"]
animals.append("Cats")
print(animals[2])
del animals[0]

for animal in animals:
    print(animal)