#display instructions for the player
print("The object of Tic Tac Toe is to get three in a row. \n"
      "You play on a three by three game board. \n"
      "The first player is known as X and the second is O. \n"
      "Players alternate placing Xs and Os on the game board until\n"

      "either opponent has three in a row or all nine squares are filled.\n")

move=[0,1,2,3,4,5,6,7,8]


#function that prints board
def board():

    print("::======:=======:======::")
    print("||  ",move[0]," |  ",move[1],"  |  ",move[2]," ||")
    print("::------|-------|------::")
    print("||  ",move[3]," |  ",move[4],"  |  ",move[5]," ||")
    print("::------|-------|------::")
    print("||  ",move[6]," |  ",move[7],"  |  ",move[8]," ||")
    print("::======:=======:======::")
    print("\n\n")
#function that clears the board
def resetBoard():
    for i in range(0,9):
        move[i]=" "

userXO=" "
AI_XO=" "

#function that makes a random selection of X or O for the user
from random import randrange,uniform

print("Do you want to be X or O?:")
playerXO=input()

playerXO=str(playerXO)

xrand=randrange(0,2)
if(playerXO=="X" or playerXO=="x"):
    userXO="X"
    AI_XO="O"
elif(playerXO=="O" or playerXO=="o"):
    userXO="O"
    AI_XO="X"
else:
    while(playerXO!="X" or playerXO!="x" or playerXO!="O" or playerXO!="o"):
        print("Wrong input\nDo you want to be X or O?:")
        playerXO=input()
        playerXO=str(playerXO)
        if(playerXO=="X" or playerXO=="x"):
           userXO="X"
           AI_XO="O"
           break
        elif(playerXO=="O" or playerXO=="o"):
           userXO="O"
           AI_XO="X"
           break

# function that sets moves
def set(setMove,XO):
    move[setMove]=XO

#function that sets user's move
def userMove():


    print("Please select a move for "+userXO+":")
    user=input()
    user=int(user)

    if(move[user]=="X" or move[user]=="O"):

        while(move[user]=="X" or move[user]=="O"):
           print("Move not available please select another move for ",userXO,":")
           user=input()
           user=int(user)
        set(user,userXO)

    else:
        set(user,userXO)



def checkForWinner():

    if(move[0]==AI_XO and move[1]==AI_XO and move[2]==AI_XO):
        resetBoard()
        set(0,AI_XO)
        set(1,AI_XO)
        set(2,AI_XO)
        return 1
    elif(move[3]==AI_XO and move[4]==AI_XO and move[5]==AI_XO ):
        resetBoard()
        set(3,AI_XO)
        set(4,AI_XO)
        set(5,AI_XO)
        return 1
    elif(move[6]==AI_XO and move[7]==AI_XO and move[8]==AI_XO ):
        resetBoard()
        set(6,AI_XO)
        set(7,AI_XO)
        set(8,AI_XO)
        return 1
    elif(move[0]==AI_XO and move[3]==AI_XO and move[6]==AI_XO ):

        resetBoard()
        set(0,AI_XO)
        set(3,AI_XO)
        set(6,AI_XO)
        return 1
    elif(move[1]==AI_XO and move[4]==AI_XO and move[7]==AI_XO ):
        resetBoard()
        set(1,AI_XO)
        set(4,AI_XO)
        set(7,AI_XO)
        return 1
    elif(move[2]==AI_XO and move[5]==AI_XO and move[8]==AI_XO ):
        resetBoard()
        set(2,AI_XO)
        set(5,AI_XO)
        set(8,AI_XO)
        return 1
    elif(move[0]==AI_XO and move[4]==AI_XO and move[8]==AI_XO ):
        resetBoard()
        set(0,AI_XO)
        set(4,AI_XO)
        set(8,AI_XO)
        return 1
    elif(move[6]==AI_XO and move[4]==AI_XO and move[2]==AI_XO ):
        resetBoard()
        set(6,AI_XO)
        set(4,AI_XO)
        set(2,AI_XO)
        return 1


    elif(move[0]==userXO and move[1]==userXO and move[2]==userXO):
        resetBoard()
        set(0,userXO)
        set(1,userXO)
        set(2,userXO)
        return -1

    elif(move[3]==userXO and move[4]==userXO and move[5]==userXO ):
        resetBoard()
        set(3,userXO)
        set(4,userXO)
        set(5,userXO)
        return -1
    elif(move[6]==userXO and move[7]==userXO and move[8]==userXO ):
        resetBoard()
        set(6,userXO)
        set(7,userXO)
        set(8,userXO)
        return -1
    elif(move[0]==userXO and move[3]==userXO and move[6]==userXO ):
        resetBoard()
        set(0,userXO)
        set(3,userXO)
        set(6,userXO)
        return -1
    elif(move[1]==userXO and move[4]==userXO and move[7]==userXO ):
        resetBoard()
        set(1,userXO)
        set(4,userXO)
        set(7,userXO)
        return -1
    elif(move[2]==userXO and move[5]==userXO and move[8]==userXO ):
        resetBoard()
        set(2,userXO)
        set(5,userXO)
        set(8,userXO)
        return -1
    elif(move[0]==userXO and move[4]==userXO and move[8]==userXO ):
        resetBoard()
        set(0,userXO)
        set(4,userXO)
        set(8,userXO)
        return -1
    elif(move[6]==userXO and move[4]==userXO and move[2]==userXO ):
        resetBoard()
        set(6,userXO)
        set(4,userXO)
        set(2,userXO)
        return -1

    else:
        return 0


def chechIfBoardIsFull():

    checkBoard=1
    for i in range(0,9):
        if(move[i]==" "):
            checkBoard=0

    return checkBoard




#function that sets  AI's move
def AI_Move():

    ai=randrange(0,9)

### best move across the top

    if(move[0]==AI_XO and move[1]==AI_XO and move[2]!=userXO):
        set(2,AI_XO)
    elif(move[2]==AI_XO and move[1]==AI_XO and move[0]!=userXO):
        set(0,AI_XO)
    elif(move[0]==AI_XO and move[2]==AI_XO and move[1]!=userXO):
        set(1,AI_XO)

## best move across the middle
    elif(move[3]==AI_XO and move[4]==AI_XO and move[5]!=userXO):
        set(5,AI_XO)

    elif(move[5]==AI_XO and move[4]==AI_XO and move[3]!=userXO):
        set(3,AI_XO)

    elif(move[3]==AI_XO and move[5]==AI_XO and move[4]!=userXO):
        set(4,AI_XO)

## best move across the bottom

    elif(move[6]==AI_XO and move[7]==AI_XO and move[8]!=userXO):
        set(7,AI_XO)

    elif(move[8]==AI_XO and move[7]==AI_XO and move[6]!=userXO):
        set(6,AI_XO)

    elif(move[6]==AI_XO and move[8]==AI_XO and move[7]!=userXO):
        set(7,AI_XO)

### best move down the right
    elif(move[0]==AI_XO and move[3]==AI_XO and move[6]!=userXO):
        set(6,AI_XO)

    elif(move[6]==AI_XO and move[3]==AI_XO and move[0]!=userXO):
        set(0,AI_XO)

    elif(move[0]==AI_XO and move[6]==AI_XO and move[3]!=userXO):
        set(3,AI_XO)

### best move down the middle
    elif(move[1]==AI_XO and move[4]==AI_XO and move[7]!=userXO):
        set(7,AI_XO)

    elif(move[7]==AI_XO and move[4]==AI_XO and move[1]!=userXO):
        set(1,AI_XO)

    elif(move[1]==AI_XO and move[7]==AI_XO and move[4]!=userXO):
        set(4,AI_XO)


### best move down the left
    elif(move[2]==AI_XO and move[5]==AI_XO and move[8]!=userXO):
        set(8,AI_XO)

    elif(move[8]==AI_XO and move[5]==AI_XO and move[2]!=userXO):
        set(2,AI_XO)

    elif(move[2]==AI_XO and move[8]==AI_XO and move[5]!=userXO):
        set(5,AI_XO)


## best move diagonal

    elif(move[0]==AI_XO and move[4]==AI_XO and move[8]!=userXO):
        set(8,AI_XO)

    elif(move[8]==AI_XO and move[4]==AI_XO and move[0]!=userXO):
        set(0,AI_XO)

    elif(move[0]==AI_XO and move[8]==AI_XO and move[4]!=userXO):
        set(4,AI_XO)


## best move diagonal

    elif(move[2]==AI_XO and move[4]==AI_XO and move[6]!=userXO):
        set(6,AI_XO)

    elif(move[6]==AI_XO and move[4]==AI_XO and move[2]!=userXO):
        set(2,AI_XO)

    elif(move[6]==AI_XO and move[2]==AI_XO and move[4]!=userXO):
        set(4,AI_XO)


### blocks across the top
    elif(move[0]==userXO and move[1]==userXO and move[2]!=userXO and move[2]!=AI_XO):
        set(2,AI_XO)

    elif(move[2]==userXO and move[1]==userXO and move[0]!=userXO and move[0]!=AI_XO):
        set(0,AI_XO)

    elif(move[0]==userXO and move[2]==userXO and move[1]!=userXO and move[1]!=AI_XO):
        set(1,AI_XO)

### blocks across the middle
    elif(move[3]==userXO and move[4]==userXO and move[5]!=userXO and move[5]!=AI_XO):
        set(5,AI_XO)
        ###
    elif(move[5]==userXO and move[4]==userXO and move[3]!=userXO and move[3]!=AI_XO):
        set(3,AI_XO)

    elif(move[3]==userXO and move[5]==userXO and move[4]!=userXO and move[4]!=AI_XO):
        set(4,AI_XO)


### blocks across the bottom
    elif(move[6]==userXO and move[7]==userXO and move[8]!=userXO and move[8]!=AI_XO):
        set(8,AI_XO)


    elif(move[8]==userXO and move[7]==userXO and move[6]!=userXO and move[6]!=AI_XO):
        set(6,AI_XO)

    elif(move[6]==userXO and move[8]==userXO and move[7]!=userXO and move[7]!=AI_XO):
        set(7,AI_XO)


### blocks down the right

    elif(move[0]==userXO and move[3]==userXO and move[6]!=userXO and move[6]!=AI_XO):
        set(6,AI_XO)

    elif(move[6]==userXO and move[3]==userXO and move[0]!=userXO and move[0]!=AI_XO):
        set(0,AI_XO)


    elif(move[0]==userXO and move[6]==userXO and move[3]!=userXO and move[3]!=AI_XO):
        set(3,AI_XO)


### blocks down the middle

    elif(move[1]==userXO and move[4]==userXO and move[7]!=userXO and move[7]!=AI_XO):
        set(7,AI_XO)

    elif(move[7]==userXO and move[4]==userXO and move[1]!=userXO and move[1]!=AI_XO):
        set(1,AI_XO)


    elif(move[1]==userXO and move[7]==userXO and move[4]!=userXO and move[4]!=AI_XO):
        set(4,AI_XO)

### blocks down the left

    elif(move[2]==userXO and move[5]==userXO and move[8]!=userXO and move[8]!=AI_XO):
        set(8,AI_XO)

    elif(move[8]==userXO and move[5]==userXO and move[2]!=userXO and move[2]!=AI_XO):
        set(2,AI_XO)

    elif(move[8]==userXO and move[2]==userXO and move[5]!=userXO and move[5]!=AI_XO):
        set(5,AI_XO)

### blocks diagonal

    elif(move[0]==userXO and move[4]==userXO and move[8]!=userXO and move[8]!=AI_XO):
        set(8,AI_XO)

    elif(move[8]==userXO and move[4]==userXO and move[0]!=userXO and move[0]!=AI_XO):
        set(0,AI_XO)

    elif(move[8]==userXO and move[0]==userXO and move[4]!=userXO and move[4]!=AI_XO):
        set(4,AI_XO)

### blocks diagonal
    elif(move[2]==userXO and move[4]==userXO and move[6]!=userXO and move[6]!=AI_XO):
        set(6,AI_XO)
    elif(move[6]==userXO and move[4]==userXO and move[2]!=userXO and move[2]!=AI_XO):
        set(2,AI_XO)
    elif(move[6]==userXO and move[2]==userXO and move[4]!=userXO and move[4]!=AI_XO):
        set(4,AI_XO)

### generates random move for AI
    elif(move[ai]=="X" or move[ai]=="O"):
        while(move[ai]=="X" or move[ai]=="O"):
            ai=randrange(0,9)
            if(chechIfBoardIsFull()==1):
                break
        set(ai,AI_XO)
    else:
        set(ai,AI_XO)


## function that class user and AI move  and look for a winner or for a tie

def user_AI_move():
    board()
    resetBoard()

    for i in range(0,8):
         if(userXO=="X"):
             userMove()
             AI_Move()
             board()
             if(checkForWinner()==1):
                   print("\'"+AI_XO+"\'"+"is the winner")
                   print("Computer won!")
                   board()
                   break
             elif(checkForWinner()==-1):
                   print("\'"+userXO+"\'"+"is the winner!")
                   print("You won!")
                   board()
                   break
             elif(chechIfBoardIsFull()==1):
                   print("DRAW!")
                   break

         else:
             
              AI_Move()
              board()

              if(checkForWinner()==1):
                   print("\'"+AI_XO+"\'"+"is the winner")
                   print("Computer won!")
                   board()
                   break
              elif(checkForWinner()==-1):
                   print("\'"+userXO+"\'"+"is the winner!")
                   print("You won!")
                   board()
                   break
              elif(chechIfBoardIsFull()==1):
                   print("DRAW!")
                   break

              userMove()
def play():

    while True:
        try:
            user_AI_move()
            break
        except ValueError:
            print("Oops! Wrong input. Try again...")
            print("Board will be reset. Start over..." )


play()