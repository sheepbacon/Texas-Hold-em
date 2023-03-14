from Card import cardset
import numpy as np
import sys

if __name__ == '__main__':
    
    while 1:
        
        newgame = cardset()
        player = [newgame.draw(0),newgame.draw(1)]
        print (player[0],player[1])
        flop = [newgame.draw(3),newgame.draw(4),newgame.draw(5)]
        print (flop[0],flop[1],flop[2])
        turn = [newgame.draw(7)]
        print (turn[0])
        river = [newgame.draw(9)]
        print (river[0])
        input("Press Enter to continue next game...")
        
