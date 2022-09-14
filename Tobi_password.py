#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
input("\nTo unlock the safe you need a 4-digit password. Here is a hint: 'https://lichess.org/isisissi'")

while True:
    if input("What does the variable 'i' stand for in the URL? ") == 'integer':
        break
while True:
    if input("What does the variable 's' stand for? ") == 'string':
        break

input('Now try to figure out the correct URL by using both textfiles...')
input("\nAfter reading the first text file, I couldn't find any 4-digit numbers. Can you?")
input("So many letters in the second text file, but which 4 letters do I need...")
while True:
    if input('Password: ') == 'Qc6#':
        input('\nYes. You unlocked the safe. Lets see what we can find in here.\n\nCity: 54.133333°, 12.3°')
        break
    else:
        print('Wrong')
input('\nCoordinates! Interesting...')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
"""
Solution:

with open('Tobi_i.txt', 'r') as file:
    word = file.readlines()
    word = [x.replace("\n","") for x in word]
    print(len(word))

with open('Tobi_s.txt', 'r') as file:
    word = file.readline()
    for i in range(len(word)):
        if word[i].isnumeric():
            print(word[i], word[i+1])
"""