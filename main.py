import pygame
pygame.mixer.init()

songs=["music1.mp3","music2.mp3","music3.mp3"]

def playmusic(mymusic):
    pygame.mixer.music.load(mymusic)
    pygame.mixer.music.play()
    print(f"Now playing{mymusic}")
print("welcome to simple music")
print("avaliable songs")
 

for song in songs:
    print(song)

choice=int(input("enter your choice(1/2/3): "))
if choice==1:
    playmusic(songs[0])
if choice ==2:
    playmusic(songs[1])
if choice==3:
    playmusic(songs[2])

input("just press enter to stop:")
pygame.mixer.music.stop()
