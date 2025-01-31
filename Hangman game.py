import random 

from logging import PlaceHolder

words_list = [
    "apple", "banana", "chair", "python", "coffee", "window", "flower", "table", "water", "orange",
    "kitten", "laptop", "mountain", "bottle", "cookie", "garden", "river", "sunset", "mirror", "camera",
    "pencil", "monkey", "desert", "forest", "music", "puzzle", "rocket", "balloon", "planet", "castle",
    "bridge", "island", "diamond", "shadow", "dragon", "candle", "tiger", "thunder", "pillow", "castle",
    "violin", "glacier", "rainbow", "helmet", "jungle", "carpet", "crystal", "giraffe", "volcano", "zipper",
    "elephant", "notebook", "bracelet", "scarf", "popcorn", "umbrella", "bicycle", "backpack", "sandwich", "penguin",
    "mushroom", "galaxy", "clock", "airplane", "rainbow", "treasure", "compass", "glasses", "bookshelf", "dolphin",
    "butterfly", "telescope", "horizon", "coral", "sunflower", "hammock", "cactus", "meadow", "lantern", "spiral",
    "anchor", "waterfall", "pirate", "compass", "mermaid", "submarine", "explorer", "seagull", "reef", "icicle",
    "otter", "fireplace", "sled", "igloo", "polar", "aurora", "cocoa", "iceberg", "mitten", "sleigh",
    "rainstorm", "cupcake", "pyramid", "zombie", "penguin", "volcano", "avocado", "squirrel", "galaxy", "parrot",
    "butterfly", "guitar", "dinosaur", "spaceship", "cloud", "whale", "sunrise", "tornado", "trolley", "puzzle",
    "snowman", "clouds", "highway", "turtle", "waterfall", "painting", "starfish", "mystery", "dragonfly", "rainbow",
    "unicorn", "mermaid", "seahorse", "castle", "lighthouse", "reindeer", "compass", "mountain", "snowflake", "raccoon",
    "moonlight", "crystal", "puzzle", "balloon", "paradise", "mango", "oceans", "lightning", "trolley", "chocolate",
    "storm", "mountain", "mountain", "cloud", "carpet", "diamond", "orchid", "volcano", "pirate", "breeze",
    "horizon", "rider", "thunder", "explorer", "treasure", "exploration", "keyboard", "telescope", "island", "rocket",
    "scarf", "storm", "fireplace", "zebra", "trolley", "flamingo", "bicycle", "sandwich", "telescope", "dream",
    "glasses", "cherry", "polar", "sunflower", "dolphin", "snowball", "igloo", "umbrella", "pillow", "space",
    "kitchen", "ocean", "vacation", "rain", "mountain", "bubble", "cactus", "butterfly", "parrot", "hedgehog",
    "jungle", "clothesline", "camera", "sunshine", "icecream", "puzzle", "planets", "firefly", "breeze", "pineapple",
    "oasis", "scissors", "breeze", "peach", "elephant", "lighthouse", "skyscraper", "balloon", "piano", "lighthouse"
]


# Hangman stages
hangman_stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


logo = ''' 
██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝
''' 


print(logo)


lives = 6

# Generate random word from list
word = random.choice(words_list)


# Create empty space 
PlaceHolder = ""

for position in range(len(word)):
    PlaceHolder += "_ "
print(PlaceHolder)

game_over = False

correct_letter = []

while not game_over:
    print(f'****************** {lives} LIVES Left ****************')
    
    
    guess= input('Guess the letter: ').lower() 


    display = ""

    # Checking the letter in word or not
    for letter in word:
        
        if letter == guess:
            display += letter
            correct_letter.append(guess)
            
        elif letter in correct_letter:
            display += letter
            
        else:
            display += "_ "

    print(display)
    
    if guess not in word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        
        if lives ==  0:
            game_over = True 
            print(f"************************ IT WAS {word}! YOU LOSE **************************")
            print(f"The word was {word} ")
    
    if "_ " not in display:
        game_over = True
        print("************************ YOU WIN **************************")
        
        
    print(hangman_stages[lives])
    
    


