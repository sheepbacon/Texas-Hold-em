from Card import cardset
import numpy as np

class highcard():
    
    def __init__(self,number):
        # any board should be highcard above
        self.result = True
        self.handrank = 0
        numberkind = np.unique(number)
        sort = sorted(numberkind)
        # kickers are the top 5 largest numbers on the board, sort length must be 7
        if (len(sort)==7):
            kicker = [sort[i] for i in range(-5,0)]
            self.kicker = kicker
        else:
            self.result = False
            self.kicker = None
        
    
    def __bool__(self):
        return self.result


class pair():
    
    def __init__(self, number):
        # default
        self.result = False
        self.handrank = None
        self.kicker = None
        self.pairnumber = None
        
        pair = -1 # this is to find the greatest pair number
        for i in np.unique(number):  # scan all on-board number
            idx = np.argwhere(number == i)   # find same number position
            if (len(idx)>=2 and pair<i):
                self.result = True
                self.handrank = 1
                pairnumber = [number[i] for i in idx.reshape(1, -1).squeeze(0)]
                pair = pairnumber[0] # refresh the pair number
                self.pairnumber = pair
                numberkind = np.unique(number)
                sort = sorted(numberkind)
                if (len(sort)>=5):  # pair's kickers are the top 5 largest number on the board
                    kicker = [sort[i] for i in range(-5,0)]
                else:
                    kicker = [sort[i] for i in range(len(sort))]
                self.kicker = kicker
    
    def __bool__(self):
        return self.result

class twopair():
    
    def __init__(self):
        pass
    
class threeofakind():
    
    def __init__(self, number):
        # default
        self.result = False
        self.handrank = None
        self.kicker = None
        
        kicker = -1 # this is to find the greatest three of a kind number
        for i in np.unique(number):  # scan all on-board number
            idx = np.argwhere(number == i)   # find same number position
            if (len(idx)==3 and kicker<i):
                self.result = True
                self.handrank = 3
                threekindnumber = [number[i] for i in idx.reshape(1, -1).squeeze(0)]
                kicker = threekindnumber[0] # refresh the kicker number
                self.kicker = kicker
    
    def __bool__(self):
        return self.result

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
    
    def __init__(self, number):
        # default setting
        self.result = False
        self.handrank = None
        self.kicker = None
        
        for i in np.unique(number):  # scan all on-board number
            idx = np.argwhere(number == i)   # find same number position
            if (len(idx)==4):
                self.result = True
                self.handrank = 7
                fourkindnumber = [number[i] for i in idx.reshape(1, -1).squeeze(0)]
                self.kicker = fourkindnumber[0]
                break
        
    def __bool__(self):
        return self.result

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

# This part should be rethink
def judge(num, color):
    
    if (straight(num)):
        return straight(num).handrank
    else:
        return 0

#undone
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
    test_number =  [9,10,11,8,7,4,1]
    test_color = [10,10,10,1,10,2,3]
    print (bool(highcard(test_number)))
    print (highcard(test_number).kicker)
    print (pair(test_number).pairnumber)