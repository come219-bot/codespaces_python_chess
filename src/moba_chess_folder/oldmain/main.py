from __future__ import annotations
import argparse
import random
import sys
from typing import Optional
from src.Board import Board 

WHITE = True
BLACK = False
TOWER_MOVES = False

def askForPlayerSide() -> bool:
    playerChoiceInput = input('What side would you like to play as [wB]? ').lower()
    if 'w' in playerChoiceInput:
        print('You will play as white')
        return WHITE
    else:
        print('You will play as black')
        return BLACK

def askForDepthOfAI() -> int:
    depthInput = 2

def printCommandOptions() -> None:
    printUI = 'p : print UI (board, game data)'
    undoOption = 'u : undo last move'
    printLegalMovesOption = 'l : show all legal moves'
    randomMoveOption = 'r : make a random move'
    printGameMoves = 'gm: moves of current game in PGN format'
    quitOption = 'quit : resign'
    moveOption = 'a3, Nc3, Qxa2, etc : make the move'
    options = [printUI, undoOption, printLegalMovesOption, randomMoveOption, printGameMoves, quitOption, moveOption, '']
    print('\n'.join(options))

def printAllLegalMoves() -> None:
    print("moves: ...")

def getRandomMove() -> None:
    print("random move called")
    return 0

def makeMove() -> None:
    print('Making move : ')

def undoLastTwoMoves() -> None:
    print("undo function .. to be removed")

def printBoard(Board: Board) -> None:
    print()
    print(Board)
    print()
    print("Board details: ...")

def printGameMoves() -> None:
    print()

def startGame(Board: Board) -> None:
    print("starting ai game ...")
    while True:
        if WHITE == WHITE:
            move = None
            command = input("It's your move. Type '?' for options. ? ")
            if command.lower() == 'u':
                undoLastTwoMoves()
                printBoard()
                continue
            elif command.lower() == 'p':
                print(Board)
                continue
            elif command.lower() == '?':
                printCommandOptions()
                continue
            elif command.lower() == 'l':
                printAllLegalMoves()
                continue
            elif command.lower() == 'gm':
                printGameMoves()
            elif command.lower() == 'r':
                move = getRandomMove()
            elif command.lower() == 'exit' or command.lower() == 'quit':
                return
            try:
                if move is None:
                    print("gg")
            except ValueError as error:
                print('%s' % error)
                continue
            makeMove()
            printBoard()

        else:
            print('AI thinking...')


# def twoPlayerGame(board: Board) -> None:
def twoPlayerGame(Board: Board) -> None:
    print("local host 2 player game")



def main() -> None:
    parser = argparse.ArgumentParser(
        prog='mobachess',
        description='A python program to play mobachess '
        'against an AI in the terminal or 2 player or multiplayer ...',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog='Enjoy the game!',
    )
    parser.add_argument(
        '-t',
        '--two',
        action='store_true',
        default=False,
        help='to play a 2-player game',
    )
    parser.add_argument(
        '-m',
        '--multiplayer',
        action='store_true',
        default=False,
        help='to play a multiplayer online game',
    )
    parser.add_argument(
        '-w',
        '--white',
        action='store',
        default='white',
        metavar='W',
        help='color for white player',
    )
    parser.add_argument(
        '-b',
        '--black',
        action='store',
        default='black',
        metavar='B',
        help='color for black player',
    )
    parser.add_argument(
        '-c',
        '--checkered',
        action='store_true',
        default=False,
        help='use checkered theme for the chess board',
    )

    args = parser.parse_args()
    #board.whiteColor = args.white
    #board.blackColor = args.black
    #board.isCheckered = args.checkered
    try:
        if args.two:
            twoPlayerGame()
        else:
            playerSide = askForPlayerSide()
            #board.currentSide = WHITE
            print()
            #aiDepth = askForDepthOfAI()
            #opponentAI = AI(board, not playerSide, aiDepth)
            print(Board)
            startGame(Board)
    except KeyboardInterrupt:
        sys.exit()


if __name__ == '__main__':
    main()

