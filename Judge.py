from Card import cardset
import numpy as np

class highcard():
    
    def __init__(self) -> None:
        pass


class pair():
    def __init__(self) -> None:
        pass


class twopair():
    def __init__(self) -> None:
        pass
    
class threeofakind():
    def __init__(self) -> None:
        pass

class straight():
    
    def __init__(self, number):
        # default result
        self.result = False
        self.kicker = None
        self.handrank = None
        
        count = 0
        for rank in (*range(12,-1,-1),12):   # check number order from high ace to low ace
            if rank in number:  # number order includes in board number
                count += 1
                if count == 5:  # find 5 continue numbers, rank represents lowest number of the straight
                    kicker = (3 if (rank+4)==16 else rank+4) # consider low ace
                    self.result = True
                    self.kicker = kicker
                    self.handrank = 4
                    break
            else:
                count = 0 # if board does not have continue number, count reset
            
    def __bool__(self):
        return self.result


class flush():
    
    def __init__(self,num,color):
        # default result
        self.result = False
        self.flushnumber = None
        self.kicker = None
        self.handrank = None

        board = np.c_[num,color]    # combine card's number and color into (7,2)
        sortcards = sorted(board, key = lambda i: i[0]) # sort number from low to high in card
        sortcolor = [i[1] for i in sortcards]   # extract color from sorted card
        sortnumber = [i[0] for i in sortcards]
        # find flush
        for i in np.unique(sortcolor):  # scan all on-board color
            idx = np.argwhere(sortcolor == i)   # find same color position
            if (len(idx)>=5):
                self.result = True
                flushnumber = [sortnumber[i] for i in idx.reshape(1, -1).squeeze(0)]
                self.flushnumber = flushnumber
                self.kicker = flushnumber
                self.handrank = 5
                break
                
    def __bool__(self):
        return self.result

class fullhouse():
    def __init__(self) -> None:
        pass

class fourofakind():
    def __init__(self, num):
        self.result = 0
        self.handrank = 2

class straightflush():
    
    def __init__(self, num, color):
        # default result
        self.result = False
        self.handrank = None
        self.kicker = None
        # find
        if (flush(num,color)):  # check whether flush or not
            if (straight(flush(num,color).flushnumber)): # check whether flush numbers are straight or not
                self.result = True
                self.handrank = 8
                self.kicker = straight(flush(num,color).flushnumber).kicker
            
            
    def __bool__(self):
        return self.result

def judge(num, color):
    
    if (straight(num).result):
        return straight(num).handrank
    else:
        return 0

class hand_result():
    
    def __init__(self, board):
        print("Your hand is: ")
        
        # list out own cards
        for i in range(7):
            print(board[i])
        
        #------------prepare judge cards' data------------
        # record all own card's number
        card_number = np.zeros(7)
        for i in range(7):
            card_number[i] = board[i].number_value
        
        # record all own card's color
        card_color = np.zeros(7)
        for i in range(7):
            card_color[i] = board[i].color_order
        ##------------------------------------------------
        
        
        # store the player's board information
        self.handrank = judge(card_number, card_color)
        self.field_card = board
        self.number = card_number
        self.color = card_color

#testing   
if __name__ == '__main__':
    
    newgame = cardset()
    deck = newgame.gettotaldeck()
    player = [deck[0],deck[1]]
    
    # Flop
    flop_1 = deck[3]
    flop_2 = deck[4]
    flop_3 = deck[5]
    
    # Turn
    turn = deck[7]
    
    # River
    river = deck[9]
    
    # Result
    board = [flop_1,flop_2,flop_3,turn,river]+player
    test_number =  [12,0,2,5,3,0,1]
    test_color = [3,3,3,1,3,2,3]
    print (bool(straight(test_number)))
    print (straight(test_number).kicker)
    print (bool(flush(test_number,test_color)))
    print (flush(test_number,test_color).kicker)
    print (bool(straightflush(test_number,test_color)))