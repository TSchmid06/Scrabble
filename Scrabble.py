import random, os

class Points():
    def __init__(self):
        self.pointDict = pointDict = {
            "E" : 1, "N" : 1, "S" : 1, "I" : 1, "R" : 1, "T" : 1, "U" : 1, "A" : 1, "D" : 1,
            "H" : 2, "G" : 2, "L" : 2, "O" : 2,
            "M" : 3, "B" : 3, "W" : 3, "Z" : 3,
            "C" : 4, "F" : 4, "K" : 4, "P" : 4,
            "Ä" : 6, "J" : 6, "Ü" : 6, "V" : 6,
            "Ö" : 8, "X" : 8,
            "Q" : 10, "Y" : 10
        }
        pass
    
    def getWinner(self, players):
        winner = players[0]
        for player in players:
            if player.points > winner.points:
                winner = player
        return winner.name
    
    def getPointsSack(self, sack):
        points = []
        for letter in sack:
            points.append(self.pointDict[letter])
        return points
    def getPointsGame(self, letters):
        points = 0
        for letter in letters:
            points += self.pointDict[letter]
        return points  
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
            
            if(Board.checkCrossing(dir, y, x, word, self.board)):   # wenn crossing nicht passiert oder ok ist
                if dir == "r":
                    for i in range(len(list(word))): # sideways
                            testBoard[int(y)][int(x+i)] = ("-" + list(word)[i] + "--")
                elif dir == "d":
                    for i in range(len(list(word))): # sideways  
                            testBoard[int(y)+i][int(x)] = ("-" + list(word)[i] + "--")
                player1.del_letters(list(word))
                stop = True
            else:
                print("Bitte Wort neu eingeben/platzieren")
        player1.points += points.getPointsGame(list(word))
        
    def checkCrossing(dir, cord1, cord2, word, testBoard):
        if dir == "r":
            for i in range(len(word)):
                if(("-"+str(*list(word[i]))+"--") == testBoard[int(cord1)][int(cord2+i)]):  #wenn buchstabe == geplantes feld auf board
                    continue
                elif("----" != testBoard[int(cord1)][int(cord2+i)]):
                    print("Gekreuzte Wörter passen nicht überein!")
                    return False
        else:
            for i in range(len(word)):
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
        self.points = 0
        self.sack = [] # The sack can hold 7 letters
    
    def del_letters(self, letters):
        for i in range(len(letters)):
            self.sack.remove(letters[i-1])

os.system("cls")
letter_sack = Letter_sack()
player1 = Player(input("Enter your Name: "))
board = Board()
points = Points()

print(len(letter_sack.sack))
inp = "" # input
while inp != "e":
    os.system("cls")
    
    while len(player1.sack) < 7:  # Buchstaben an Spieler verteilen
        letter = letter_sack.dist_letter()
        if letter == 0 and player1.sack == None:
            print("Game Over")
            print(*points.getWinner([player1]))
            exit()
        elif letter == 0:
            print("Sack is empty.")
            inp = input("Want to end the game (y/n)?: ")
            if inp == "y":
                print(*points.getWinner([player1]))
                exit()
            break
        
        player1.sack.append(letter)
    
    print(player1.name, ":", player1.points)
    board.print_board()
    print(*player1.sack)
    print(*points.getPointsSack(player1.sack))
    board.place_words()