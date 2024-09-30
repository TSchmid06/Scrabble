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
    
    def getPointsSack(self, sack):  # Analyses the Points of the letter that are currently in possession of the player
        points = []
        for letter in sack:
            points.append(self.pointDict[letter])
        return points
    
    def getPointsGame(self, letters):   # Adds the Points of this turn to the total points of the player
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
    
    def place_words(self, sack, player):
        stop = False
        while True: # Eingabeschleife
            testBoard = self.board.copy()
            while True:
                try:    # wenn falsch, neu eingeben
                    word = input("Enter your Word: ").upper()
                    x = int(input("Enter x coordinate (TOP): "))
                    y = int(input("Enter y coordinate (LEFT): "))
                    dir = str(input("Enter Right(r) or Downwards(d): "))
                    break
                except ValueError:
                    print("Not the right Value. Please try again.")
                
            for i in list(word):
                if i not in sack:
                    print("Letters are not in Sack. Please try again.")
                    break
            
            if(Board.checkCrossing(dir, y, x, word, self.board) and (dir == "r" or dir == "d")):   # if theres no crossing of words or it is ok AND dir = "r" or "d"
                if dir == "r":
                    for i in range(len(list(word))): # sideways
                            testBoard[int(y)][int(x+i)] = ("-" + list(word)[i] + "--")
                elif dir == "d":
                    for i in range(len(list(word))): # down 
                            testBoard[int(y)+i][int(x)] = ("-" + list(word)[i] + "--")
                player.del_letters(list(word))
                player.points += points.getPointsGame(list(word))
                break
            else:
                print("Please try again.")
        
    def checkCrossing(dir, cord1, cord2, word, testBoard):  # Checks if words cross and if it is ok
        if dir == "r":  # sideways
            for i in range(len(word)):
                if(("-"+str(*list(word[i]))+"--") == testBoard[int(cord1)][int(cord2+i)]):  #if letter == planned field on the board
                    continue
                elif("----" != testBoard[int(cord1)][int(cord2+i)]):
                    print("Crossed words don't fit.")
                    return False
        else:   # down
            for i in range(len(word)):
                if(("-"+str(*list(word[i]))+"--") == testBoard[int(cord1+i)][int(cord2)]):
                    continue
                elif("----" != testBoard[int(cord1+i)][int(cord2)]):
                    print("Crossed words don't fit.")
                    return False
        return True
class Letter_sack():
    def __init__(self, numb_letters: int = 100):
        self.numb_letters = numb_letters
        self.sack = ["A", "A", "A", "A", "A"]
        # self.sack = ["A", "A", "A", "A", "A", "B", "B",  "C", "C", "D",  "D",  "D",  "D",   # all the letters in the game
        #              "F",  "F", "G",  "G",  "G", "H",  "H",  "H",  "H", "I",  "I",  "I",  "I",  "I",  "I", 
        #              "J", "K",  "K", "L",  "L",  "L", "M",  "M",  "M",  "M", "N",  "N",  "N",  "N",  "N",  "N",  "N",  "N",  "N", 
        #              "O",  "O",  "O", "P", "Q", "R",  "R",  "R",  "R",  "R",  "R",
        #              "S",  "S",  "S",  "S",  "S",  "S",  "S", "T",  "T",  "T",  "T",  "T",  "T",
        #              "U",  "U",  "U",  "U",  "U",  "U", "V", "W", "X", "Y", "Z", "Ä", "Ö", "Ü"]
    
    def dist_letter(self):  # distributes letters to the players
        if len(self.sack) == 0: # if sack is empty return 0
            return 0
        
        letter = self.sack[random.randint(0, len(self.sack))-1 ]
        self.sack.remove(letter)    # removes chosen letter from the sack
        return letter   
class Player():
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.sack = [] # The sack can hold 7 letters
    
    def del_letters(self, letters): # delete letters from sack after being placed on the board
        for i in range(len(letters)):
            self.sack.remove(letters[i-1])

os.system("cls")
letter_sack = Letter_sack()
board = Board()
points = Points()
players = []
#i = int(input("Enter Number of Players: "))

while True:
    inp = input("Enter Number of Players: ")
    if inp.isnumeric():
        if int(inp)<4 and int(inp)>1:
            for i in range(int(inp)):
                player = Player(input("Player " + str(i+1) + ", Enter your Name: "))
                players.append(player)
            break

print(len(letter_sack.sack))

while True: #game
    for player in players: #round
        os.system("cls")
        
        while len(player.sack) < 7:  # Distribute letters to players
            letter = letter_sack.dist_letter()
            if letter == 0 and len(player.sack) == 0:    # if sack and player sack is empty = game over
                print("Game Over")
                print("Winner: ", *points.getWinner(players))
                exit()
            elif letter == 0:   # if sack is empty you can choose if you want to keep playing
                print("Sack is empty.")
                inp = input("Want to end the game (y/n)?: ")
                if inp == "y":
                    print("Winner: ", *points.getWinner(players))
                    exit()
                break
            
            player.sack.append(letter)
        
        print(player.name, ":", player.points)
        board.print_board()
        print(*player.sack)
        print(*points.getPointsSack(player.sack))  # Print Points of the letters currently in Players possession
        board.place_words(player.sack, player)