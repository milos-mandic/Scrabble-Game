# Hangman Word Game
# Created by: Milos Mandic <shomyserbia>
# Specifications by: MIT 6.00x staff
#

from Hangman_game_functions import *

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    n = HAND_SIZE
    checker = False
    
    while True:
        decision = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if decision == 'e':
            break
        elif decision == 'n':
            while True:
                decision1 = raw_input('Enter u to have yourself play, c to have the computer play: ')
                if decision1 == 'u':
                    hand = dealHand(n)
                    print
                    playHand(hand, wordList, n)
                    current_hand = hand
                    checker = True
                    break
                elif decision1 == 'c':
                    hand = dealHand(n)
                    print
                    compPlayHand(hand, wordList, n)
                    current_hand = hand
                    checker = True
                    break
                else:
                    print('Invalid command.')
        elif decision == 'r' and checker == True:
            while True:
                decision1 = raw_input('Enter u to have yourself play, c to have the computer play: ')
                if decision1 == 'u':
                    playHand(current_hand, wordList, n)
                    print
                    break
                elif decision1 == 'c':
                    compPlayHand(current_hand, wordList, n)
                    print
                    break
                else:
                    print('Invalid command.')
        elif decision == 'r' and checker == False:
            print('You have not played a hand yet. Please play a new hand first!')
        else:
             print('Invalid command.')
                         
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)