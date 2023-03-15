from Card import cardset
from Judge import hand_result
import numpy as np

if __name__ == '__main__':
    
    while True:
        
        # Pre-flop
        newgame = cardset()
        deck = newgame.gettotaldeck()
        player = [deck[0],deck[1]]
        print("Player cards: ")
        print(player[0],", ",player[1])
        input()
        
        # Flop
        flop_1 = deck[3]
        flop_2 = deck[4]
        flop_3 = deck[5]
        print("Flop cards:")
        print(flop_1)
        print(flop_2)
        print(flop_3)
        input()
        
        # Turn
        turn = deck[7]
        print("Turn card:")
        print(turn)
        input()
        
        # River
        river = deck[9]
        print("River card:")
        print(river)
        input()
        
        # Result
        board = [flop_1,flop_2,flop_3,turn,river] + player
        for i in range(len(board)):
            print(board[i])
        #player_hand = hand_result(board)
        #print(player_hand.handrank)
        
        user = input("Press enter to continue next game. Enter e to leave: ")
        
        if (user == "e"):
            break
    
    print ("Thank you for playing!")
    input("Press enter to leave...")
        
