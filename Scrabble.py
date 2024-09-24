import random, os

class Board():
    def __init__(self):
        self.board = [
            ["----", "-1--", "-2--", "-3--", "-4--", "-5--", "-6--", "-7--", "-8--", "-9--", "-10-", "-11-", "-12-", "-13-", "-14-", "-15-"],
            ["-1--", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----"],
            ["-2--", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----"],
            ["-3--", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----"],
            ["-4--", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----"],
            ["-5--", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----"],
            ["-6--", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----"],
            ["-7--", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----"],
            ["-8--", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----"],
            ["-9--", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----"],
            ["-10-", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----"],
            ["-11-", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----"],
            ["-12-", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----"],
            ["-13-", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----"],
            ["-14-", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----"],
            ["-15-", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----", "----"]
        ]
        pass
    
    def print_board(self):
        for row in self.board:
            print(*row)
    
    def place_words(self):
        stop = False
        while stop != True: # Eingabeschleife
            testBoard = self.board.copy()
            word = input("Enter your Word: ").upper()
            x = input("Enter x coordinate (TOP): ")
            x = int(x)
            y = input("Enter y coordinate (LEFT): ")
            y = int(y)
            dir = input("Enter Right(r) or Downwards(d): ")
            
            if(Board.checkCrossing(dir, y, x, word, self.board)):
                if dir == "r":
                    for i in range(len(list(word))): # sideways
                            testBoard[int(y)][int(x+i)] = ("-" + list(word)[i] + "--")
                elif dir == "d":
                    for i in range(len(list(word))): # sideways  
                            testBoard[int(y)+i][int(x)] = ("-" + list(word)[i] + "--")
                player.del_letters(list(word))
                stop = True
            else:
                print("Bitte Wort neu eingeben/platzieren")
        
    def checkCrossing(dir, cord1, cord2, word, testBoard):
        if dir == "r":
            for i in range(len(word)):
                print("-"+str(*list(word[i]))+"--")
                if(("-"+str(*list(word[i]))+"--") == testBoard[int(cord1)][int(cord2+i)]):
                    continue
                elif("----" != testBoard[int(cord1)][int(cord2+i)]):
                    print("Gekreuzte Wörter passen nicht überein!")
                    return False
        else:
            for i in range(len(word)):
                print("-"+str(*list(word[i]))+"--")
                if(("-"+str(*list(word[i]))+"--") == testBoard[int(cord1+i)][int(cord2)]):
                    continue
                elif("----" != testBoard[int(cord1+i)][int(cord2)]):
                    print("Gekreuzte Wörter passen nicht überein!")
                    return False
        return True
class Letter_sack():
    def __init__(self, numb_letters: int = 100):
        self.numb_letters = numb_letters
        self.sack = ["A", "A", "A", "A", "A", "B", "B",  "C", "C", "D",  "D",  "D",  "D", 
                     "F",  "F", "G",  "G",  "G", "H",  "H",  "H",  "H", "I",  "I",  "I",  "I",  "I",  "I", 
                     "J", "K",  "K", "L",  "L",  "L", "M",  "M",  "M",  "M", "N",  "N",  "N",  "N",  "N",  "N",  "N",  "N",  "N", 
                     "O",  "O",  "O", "P", "Q", "R",  "R",  "R",  "R",  "R",  "R",
                     "S",  "S",  "S",  "S",  "S",  "S",  "S", "T",  "T",  "T",  "T",  "T",  "T",
                     "U",  "U",  "U",  "U",  "U",  "U", "V", "W", "X", "Y", "Z", "Ä", "Ö", "Ü"]
    
    def dist_letter(self):
        if len(self.sack) == 0:
            return 0
        
        letter = self.sack[random.randint(0, len(self.sack))-1 ]
        self.sack.remove(letter)
        return letter   
class Player():
    def __init__(self, name):
        self.name = name
        self.sack = [] # The sack can hold 7 letters
    
    def del_letters(self, letters):
        for i in range(len(letters)):
            self.sack.remove(letters[i-1])

os.system("cls")
letter_sack = Letter_sack()
player = Player(input("Enter your Name: "))
board = Board()

print(len(letter_sack.sack))
inp = "" # input
while inp != "e":
    os.system("cls")
    
    while len(player.sack) < 7:  # Buchstaben an Spieler verteilen
        letter = letter_sack.dist_letter()
        if letter == 0:
            print("Sack is empty.")
            break
        player.sack.append(letter)
    
    board.print_board()
    print(player.name, ":", *player.sack)
    board.place_words()