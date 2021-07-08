#! /usr/bin/env python3
#   Windows: #!python3
#
#   Hangman game
#
#   Dillon Yu
#

numWrong = 0  # number of wrong guesses so far
numTries = 6  # the total number of tries
ans = []  # the sentence solution
curAns = []  # the current guessed solution, which gets updated as the player guesses characters correctly
posAns = []  # possible answers


# change the current answer with input 'char' being the character that was guessed correctly
def change_curAns(char):
    for i in range(len(ans)):
        if ans[i] == char:
            curAns[i] = char


# show the current state of the hangman based on the number of wrong guesses so far ('state' input)
def show_hangman(state):
    states = ["""
    --------
    |     |
    |
    |
    |
    |
    |_________
        """,
              """
    --------
    |     |
    |     O
    |
    |
    |
    |_________
        """,
              """
    --------
    |     |
    |     O
    |     |
    |     |
    |
    |_________
        """,
              """
    --------
    |     |
    |     O
    |    /|
    |     |
    |
    |_________
        """,
              """
    --------
    |     |
    |     O
    |    /|\\
    |     |
    |
    |_________
        """,
              """
    --------
    |     |
    |     O
    |    /|\\
    |     |
    |    /
    |_________
        """,
              """
    --------
    |     |
    |     O
    |    /|\\
    |     |
    |    / \\
    |_________
        """]
    print(states[state])


# re-setup the hangman game after each attempt
def setup():
    show_hangman(numWrong)
    print('   ' + ' '.join(curAns) + '。')
    print('\n' + ' '.join(posAns))
    print('Please enter another character')


# the main function for running the game
def main():
    global ans
    global numWrong
    global numTries
    global curAns
    global posAns

    # re-setup for playing the game multiple times
    numWrong = 0
    numTries = 6
    ans = []
    curAns = []
    posAns = []

    # set correct answer
    print('Hello! Welcome to Hangman! Let\'s setup the game!')
    print('Type in the correct answer: ')
    ans = list(input())

    posA = ''
    while posA != 'done':
        print('Type in a possible answer (or type done to continue)')
        posA = input()
        if posA != 'done':
            posAns.append(posA)

    print('\n' * 100)
    print('Let\'s begin!')

    # initial game setup
    for i in range(len(ans)):
        curAns.append('_')
    show_hangman(numWrong)
    print('   ' + ' '.join(curAns) + '。')
    print('\n' + ' '.join(posAns))
    print('Please enter a character')

    # running game
    while (numWrong < numTries) and (curAns != ans):
        guess = input()
        # print('\n' * 100)
        if guess in ans:
            change_curAns(guess)
        else:
            numWrong += 1
            print('Sorry, that character is not in the answer.')
        setup()

    # game over
    if numWrong < numTries:
        print('Congratulations! You win!')
    else:
        print('\nSorry, you lose. The correct sentence was ' + ''.join(ans))

    # restart game here
    print('Would you like to play again? (Y/N)')
    response = input()
    if response == 'Y':
        main()


main()
