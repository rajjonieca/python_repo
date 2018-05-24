from datetime import datetime
import sys
import os

humanPlayer = True
aiPlayer = False
currentPlayer = humanPlayer
pile = 21
playerMove = 0



while pile > 0:

    if currentPlayer == humanPlayer:
        playerMove = input("Pick up 1-7 sticks: ")
        validMove = int(playerMove) > 0 or int(playerMove) <= 7

        while not validMove:
            playerMove = input("Pick up 1-7 sticks: ")
            print("MAKE A FUCKING VALID CHOICE!")

        pile -= int(playerMove)
        print("Human player picks "+str(playerMove)+" sticks!")
        print("There are now "+str(pile)+" sticks in the pile")
        print("---------------------------------------------------")
        currentPlayer = aiPlayer

    elif currentPlayer == aiPlayer:
        aiMove = pile % 5
        pile -= int(aiMove)
        print("AI player picks " + str(aiMove) + " sticks!")
        print("There are now " + str(pile) + " sticks in the pile")
        print("---------------------------------------------------")
        currentPlayer = humanPlayer
    else:
        print("GAGO!")

    if pile < 0:
        if currentPlayer == humanPlayer:
            print("Human WINS!")
        if currentPlayer == aiPlayer:
            print("AI WINS!")










