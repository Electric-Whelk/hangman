import random

def myhangman(word):
    wrongletters = 0
    hint = ["_"]* len(word)
    remainingletters = list(word)
    winstates = ["You lose! It was '" + word + ".'", "", "You win!"]
    guesses = []
    win = 1
    victim = ["________       ",
              "|      |       ",
              "|      O       ",
              "|     /|\      ",
              "|     / \      ",
              "|              ",
              "TTTTTTTTTTTT   "]
    while win == 1:
        if len(guesses)>0:
            print(guesses)
        print(hint)
        x = input("")
        indexticker = 0
        guess = 0
        while indexticker == 0:
            try:
                y = remainingletters.index(x)
                hint[y]=remainingletters[y]
                remainingletters[y] = "$"
                if remainingletters == ["$"] * len(remainingletters):
                    win += 1
                    break
                else:
                    guess += 1
            except(ValueError):
                if guess == 0:
                    wrongletters += 1
                    printedicon = "\n".join(victim[0:wrongletters])
                    print(printedicon)
                    guesses.append(x)
                    if wrongletters == len(victim):
                      win -= 1
                indexticker += 1
        print("\n")
    print(winstates[win])

        
def hangman(word):
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter"
        char = input(msg)
        if char in rletters:
            cind = rletters \
                   .index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n"
              .join(stages[0: e]))
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n"
              .join(stages[0: \
              wrong]))
        print("You lose! It was {}."
              .format(word))

workingnumbers = [29636, 32805] #intertwine
workingempty = [29635, 14225]
#54003 does not work
  
def entrygrabber():
    p = 0
    while p == 0:
        line_numbers = random.randint(5, 72320)
        try:
            with open("Oxford English Dictionary.txt", "r") as fp:
               i = 0
               while i == 0:
                    for  index, line in enumerate(fp):
                        if index == line_numbers:
                            if line == "\n":
                                line_numbers += 1
                            else:
                                entry = line
                                i += 1
                        elif index > line_numbers:
                            break
            p += 1
        except UnicodeDecodeError:
            p = 0
    return(entry)

def wordgrabber():
    permitted = ["â€”n.", "n.", "adj.", "v.", "n.pl", "adv.", 'â€”v.', "â€”adj."]
    #get a word - fail condition is making sure the thing is a word
    i = 0
    while i == 0:
        wordlist = entrygrabber().split(" ")
        if wordlist[2] in permitted:
            j = 0
            wordletters = []
            while j == 0:
                for character in wordlist[0]:
                    if character.isalpha() == True:
                        wordletters.append(character)
                    else:
                        break
                j +=1
            i += 1
        else:
            print(wordlist)
    #remove numbers/hyphens
    printout = "".join(wordletters)
    lowered = printout.lower()
    return(lowered)
        
myhangman(wordgrabber())



