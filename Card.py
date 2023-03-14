import numpy as np

number = [ "A" , "2" , "3" , "4" , "5" , "6" , "7" , "8", "9" , "10" , "J" , "Q", "K" ]
color = [ "Spade♠", "Heart♥" , "Diamond♦", "Club♣" ]

card_set = []

for n in range(13):
    for c in range(4):
        card_set.append (number[n])
        card_set.append (color[c])

card_set = np.reshape(card_set, (52,2))

class cardset:
    
    def __init__(self):
        np.random.shuffle(card_set)

    def draw(self, d):
        return card_set[d]
    
    def totaldeck(self):
        return card_set
    
if __name__ == '__main__':
    pick = cardset()
    print(card_set[0])
    print(card_set[0][0])
    print(card_set[0][1])