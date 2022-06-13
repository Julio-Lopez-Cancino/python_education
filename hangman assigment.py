#requirements
#Python 3.9.7 or higher
#pip install random-word==1.0.7

from random_word import RandomWords


def hangman(word):
    wrong = 0
    stages = ["",
             " _________      ",
             "|        |      ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters = list(word)
    board = ['_'] * len(word)
    win = False
    print('Welcom to Hangman')
    print(f'\nThe word has {len(word)} letters')
    
    while wrong < len(stages) - 1:
        print('\n')
        msg = "Guess a letter\n"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            print((' '.join(board)))
            rletters[cind] = '$'
        else:
            wrong += 1
            print((' '.join(board)))
            e = wrong + 1
            print('\n'.join(stages[0: e]))
            if '_' not in board:
                print('You win!')
                print(' '.join(board))
                win = True
                break
    if not win:
        print('\n'.join(stages[0:wrong]))
        print(f'\nYou lose! It was {word}.')
        
        
r = RandomWords()
word = r.get_random_word(hasDictionaryDef="true",
                         includePartOfSpeech="noun,verb",
                         minCorpusCount=1, maxCorpusCount=10,
                         minDictionaryCount=1, maxDictionaryCount=10,
                         minLength=7, maxLength=12)

hangman(word)
