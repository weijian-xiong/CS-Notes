import random

def getData(song):
    f = raw_input("Enter a song and band(song-band) or exit to quit: ")
    while(f!='exit'):
        f = raw_input("Enter a song and band(song-band) or exit to quit: ")
        song.append(f)
        
    

def playRandom(song):
    print("Now Playing: ", random.choice(song))


def main():
    song = []
    getData(song)
    playRandom(song)


if __name__ =='__main__':
    main()