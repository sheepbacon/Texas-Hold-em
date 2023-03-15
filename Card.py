import numpy as np

number = [ "2" , "3" , "4" , "5" , "6" , "7" , "8", "9" , "10" , "J" , "Q", "K" , "A" ]
color = [ " Spade♠", " Heart♥" , " Diamond♦", " Club♣" ]
number_value = range (13)
color_order = range (4)

card_set = []

# card information
class card:
    
    def __init__(self, number, number_value, color, color_order, card_number):
        self.number = number
        self.color = color
        self.number_value = number_value
        self.color_order = color_order
        self.card_number = card_number
        
    def __str__ (self):
        return self.number +  self.color

# create card set
num = 0
for n in range(13):
    for c in range(4):
        cd = card(number[n],number_value[n], color[c], color_order[c], num)
        card_set.append (cd)
        num = num+1


class cardset:
    
    def __init__(self):
        np.random.shuffle(card_set)

    def draw(self, d):
        return card_set[d]
    
    def gettotaldeck(self):
        return card_set
    
if __name__ == '__main__':
    
    gg = cardset()
    lista = gg.gettotaldeck()
    print(lista[0])
    print(lista[0].number_value)
    print(lista[0].number_value*lista[0].number_value)
    print(lista[0].card_number)