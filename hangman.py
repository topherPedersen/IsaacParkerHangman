import random
HANGMAN_PIC = [
'''
 +---+
     |
     |
     |
    ===
''',

'''
+---+
 O   |
     |
     |
    ===
''',

'''
 +---+
 O   |
 |   |
     |
    ===
''',

'''
 +---+
 O   |
/|   |
     |
    ===
''',

'''
 +---+
 O   |
/|\  |
     |
    ===
''',

'''
 +---+
 O   |
/|\  |
/    |
    ===
''',

'''
 +---+
 O   |
/|\  |
/ \  |
    ===
'''
]



# Isaac, you start on line 38 in the book on the line below....
words = 'ant babbon bager bat bear beaver camel cat clam corba cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt' 


















# Parker, you start at line 40 in the book on the line below...
def getRandomWord(wordlist):
    wordIndex = random.randint(0, len(wordlist) - 1)
    return wordlist[wordIndex]
