#imports
import random
import time
#subprograms
#user login takes username and password and outputs if the user is in the txt file and the passwords match
def login(username,password):
    file = open('names.txt',"r")
    name_list = []
    for line in file:
        name_list.append(line.strip())
    for i in range (0,len(name_list),1):
        if name_list[i] == username and name_list[i+1] == password:
            return True
    return ("Not in file")
    file.close() 
#creates an array out of the songs in the file
# then picks a random song using random.choice
#if the index of the item chosen is even then the artist is the next in the list
#if the random picker picks an odd number(an artist) then it will go to the previous song and choose that song and artist
#returns a random song and sets the global variable artist to whatever song was picked to then be used in the game loop
def song():
    global artist
    file = open('songs.txt',"r")
    song_list = []
    for line in file:
        song_list.append(line.strip())
    for i in range(len(song_list)):
        random_song = random.choice(song_list)
        if song_list.index(random_song)%2 == 0:
            artist = song_list[song_list.index(random_song)+1]
            return (random_song)
        else:
            random_song = song_list[song_list.index(random_song)-1]
            artist = song_list[song_list.index(random_song)+1]
            return (random_song)
    file.close()
#find the spaces in the song name and just return the first letters of the song title
#turns the random song chosen into an array of characters and then searches through those characters to find spaces
#if a space is found then in the next index will be the first letter of the word
#returns an array of the starting letters of each word in the song title
def strip_songname(random_song):
    letters = []
    for i, char in enumerate(random_song):
        if char == ' ':
            letters.append(random_song[i+1])
        elif i == 1:
            letters.append(random_song[i-1])
    return(letters)
#AI code mostly
#tried doing it with array again but couldn't write the array onto the text file
def log_score(username, score, filename='scores.txt'):
    try:
        file = open(filename, 'a')
        file.write(f"{username}: {score}\n")
        print("Score logged successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
    file.close()
#main program
#variables
score = 0
#get user name and password
username = str(input("Enter username: "))
password = str(input("Enter password: "))
run = login(username,password)
while run == True:
    attempts = 0
    chosen_song = song()
    print ("The song is: ",strip_songname(chosen_song) ," and the artist is ", artist)
    while attempts <=1:
        guess = str(input("What do you think the song is: "))
        if guess == chosen_song:
            score = score + 1
            print ("That is correct, well done!")
            attempts = 5
        elif attempts ==1:
            attempts = 69
            run = False            
        else:
            attempts = attempts + 1
        time.sleep(0.5)
# # #     #ENDWHILE
# # # #ENDWHILE
print("Im afraid you ran out of guesses, your score was: ",score)
print(log_score(username,score))
