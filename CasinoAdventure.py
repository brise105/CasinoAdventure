#Coded by Brandon Briseno and Travis Mayer
#Casino Arcade
    #Blackjack, Cross the River (7UP), Two D6 Dice Roll, Coin Flipper

import random


####################################################################################################
tickets = 4

def addTickets(value):
    current = value + 1
    print(">>You recieved 1 munny!\n" + "You currently have " + str(current) + " munny(s)!")
    return current

def subTickets(value):
    current = value - 1
    print(">>You lost 1 munny!\n" + "You currently have " + str(current) + " munny(s)!")
    return current

def openMessage():
  print("WELCOME TO THE EZ$$$ CASINO!!!")



openMessage()  
print("\nHere take some munny! It's on the house.")
print(">>>You recieve 4 munny")  
def main():
    decideMain = input('''\nWhich game would you like to play?\n(a)Coin Flipper (b)High Roll (c)Cross the River (d)Blackjack (e)Gift Shop \n(f)Check Munny (g)Exit\n''')
    if decideMain == "a":
        print(coinSelect())
    if decideMain == "b":
        print(pairRoll())
    if decideMain == "c":
        print(riverGame())
    if decideMain == "d":
        print(twentyOneMain())
    if decideMain == "e":
        print(giftShopFunction())
    if decideMain == "f":
        print(checkMunny(tickets))
    if decideMain == "g":
        print(exitDoor())
    else:
        print(main())
        
def exitDoor():        
    decideExit = input("\nAre you sure? (y or n)\n")
    if decideExit == "n":
        print(main())
    if decideExit == "y":
        print("\nHave a good one!")
        exit()
    else:
        print(exitDoor())

####################################################################################################


class coinType():
    def __init__(self, weight, flavorText):
        self.weight = weight
        self.flavorText = flavorText
        return None

    def setWeight(self, w):
        self.weight = w

    def getWeight(self):
        return self.weight

    def setflavorText(self, fT):
        self.flavorText = fT

    def getflavorText(self):
        return self.flavorText

coin1 = coinType("\n5.00 grams", "This coin is one of rarest ever printed by the US Treasurary (1913).")
coin2 = coinType("\n26.96 grams", "This coin was the first dollar coin issued by the United States federal government (1794).")
coin3 = coinType("\n5.670 grams", "This is just a regular quarter (2016).")

def playAgainFunction():
    playagain = 'y'
    playagainBool = True

    while playagainBool == True:
        if playagain == 'y':
            playagain = input('Would you like to play again? (y or n)\n')
        if playagain == 'y':
            print (coinSelect())
        if playagain == 'n':
            playagainBool = False
            print(main())
        else:
            playagainBool = False
            print(playAgainFunction())

def coinFlip():
    global tickets
    repeatsTotal = 0
    while True:
        try:
            repeatsTotal = int(input('How many times do you want to flip the coin?: '))
        except ValueError:
            print('The input is incorrect. Please try again.')
            continue
        else:
            break
    repeatsCurrent = 0
    headsTotal = 0
    tailsTotal = 0
    loop = True
    while loop == True:
        value = random.random()
        #print(value)
        if (value >= .5):
            headsTotal = headsTotal + 1
        else:
            tailsTotal = tailsTotal + 1
        repeatsCurrent = repeatsCurrent + 1
        if (repeatsCurrent >= int(repeatsTotal)):
            loop = False
    while True:
        try:
            guessCoin = input('Call it: (a)Heads or (b)Tails?\n')
            for letter in guessCoin:
                if letter != 'a' and letter != 'b':
                  raise TypeError
            break
        except ValueError:
            print('The input is incorrect. Please try again.')
        except TypeError:
            print('The input is incorrect. Please try again.')
        else:
            break
    if headsTotal >= tailsTotal and guessCoin == 'a':
        print('\nYou win!')
        tickets = (addTickets(tickets))
    elif tailsTotal >= headsTotal and guessCoin == 'b':
        print('\nYou win!')
        tickets = (addTickets(tickets))
    else:
        print('\nYou lose!')
        tickets = (subTickets(tickets))
    print('Heads Total: ' + str(headsTotal) + '\nTails Total: ' + str(tailsTotal))
    print(playAgainFunction())
    
        
def coinSelect():
    coin = input("\nSelect your coin:\n(a)Liberty Head Nickel (b)Flowing Hair Silver Dollar (c)Regular Quarter\n")
    if coin == "a":
        print(coin1.getWeight())
        print(coin1.getflavorText())
        print(coinFlip())
        exit()
    elif coin == "b":
        print(coin2.getWeight())
        print(coin2.getflavorText())
        print(coinFlip())
        exit()
    elif coin == "c":
        print(coin3.getWeight())
        print(coin3.getflavorText())
        print(coinFlip())
        exit()
    else:
        print(coinSelect())

####################################################################################################

def playAgainDiceFunction():
    playagain = 'y'
    playagainBool = True

    while playagainBool == True:
        if playagain == 'y':
            playagain = input('\nWould you like to play again? (y or n)\n')
        if playagain == 'y':
            (diceRoll())
        if playagain == 'n':
            playagainBool = False
            print(main())
        else:
            playagainBool = False
            print(playAgainDiceFunction())

class diceFace():
    def __init__(self, face):
        self.face = face
        return None

    def setFace(self, f):
        self.face = f

    def getFace(self):
        return self.face

dice1 = diceFace(''' 
         _________
        |         |
        |         |
        |    •    |
        |         |
        |_________|''')
dice2 = diceFace(''' 
         _________
        |         |
        |         |
        |   • •   |
        |         |
        |_________|''')
dice3 = diceFace(''' 
         _________
        |         |
        |     •   |
        |    •    |
        |   •     |
        |_________|''')
dice4 = diceFace(''' 
         _________
        |         |
        |  •   •  |
        |         |
        |  •   •  |
        |_________|''')
dice5 = diceFace(''' 
         _________
        |         |
        |  •   •  |
        |    •    |
        |  •   •  |
        |_________|''')
dice6 = diceFace(''' 
         _________
        |         |
        |  •   •  |
        |  •   •  |
        |  •   •  |
        |_________|''')


def diceRoll():
    global tickets
    yourNumber1 = random.randint(1, 6)
    if yourNumber1 == 1:
        print(dice1.getFace())
    if yourNumber1 == 2:
        print(dice2.getFace())
    if yourNumber1 == 3:
        print(dice3.getFace())
    if yourNumber1 == 4:
        print(dice4.getFace())
    if yourNumber1 == 5:
        print(dice5.getFace())
    if yourNumber1 == 6:
        print(dice6.getFace())
        
    yourNumber2 = random.randint(1, 6)
    if yourNumber2 == 1:
        print(dice1.getFace())
    if yourNumber2 == 2:
        print(dice2.getFace())
    if yourNumber2 == 3:
        print(dice3.getFace())
    if yourNumber2 == 4:
        print(dice4.getFace())
    if yourNumber2 == 5:
        print(dice5.getFace())
    if yourNumber2 == 6:
        print(dice6.getFace())
    
    compNumber1 = random.randint(1, 6)
    compNumber2 = random.randint(1, 6)
    
    compTotal = int(compNumber1+compNumber2)
    
    yourTotal = int(yourNumber2+yourNumber1)
    
    if yourTotal > compTotal:
        print("\nThe Dealer rolled a:")
        print(compTotal)
        print("\nYou rolled a:")
        print (yourTotal)
        print("\nYou win!")
        tickets = (addTickets(tickets))
        print(playAgainDiceFunction())
    if yourTotal == compTotal:
        print("\nThe Dealer rolled a:")
        print(compTotal)
        print("\nYou rolled a:")
        print (yourTotal)
        print("\nAw, it's a tie!")
    else:
        print("\nThe Dealer rolled a:")
        print(compTotal)
        print("\nYou rolled a:")
        print(yourTotal)
        print("\nYou lose!")
        tickets = (subTickets(tickets))
        print(playAgainDiceFunction())

def pairRoll():
    print("\nWelcome to the Dice Roller: Input any key (2 x d6, high roll)")
    input()
    (diceRoll())
    print(playAgainDiceFunction())

####################################################################################################

def playAgainRiverFunction():
    playagain = 'y'
    playagainBool = True

    while playagainBool == True:
        if playagain == 'y':
            playagain = input('\nWould you like to play again? (y or n)\n')
        if playagain == 'y':
            (riverGame())
        if playagain == 'n':
            playagainBool = False
            print(main())
        else:
            playagainBool = False
            print(playAgainRiverFunction())

# Constants for name of suits
SPADES = 'Spades'
CLUBS = 'Clubs'
HEARTS = 'Hearts'
DIAMONDS = 'Diamonds'

# List of the suits
suits = [SPADES, CLUBS, HEARTS, DIAMONDS]

# Dictionary of ranks
rank = {1: 'Ace', 11: 'Jack', 12: 'Queen', 13: 'King'}

def riverGame():
  global tickets
  # Create the deck of cards
  deck = []
  # Iterate through [1, 14)
  for val in range(1, 14):
    # Iterate through the 4 suits
    for s in suits:
      # Add the card to the deck
      deck.append([val, s])

  print('''\nWelcome to the River! You must reach a streak of 7 to cross! \nRun out of card and you lose!\n''')
  # Shuffle the deck
  random.shuffle(deck)
  
  # Start progress at 0
  progress = 0
  # Keep track of the previous card
  previousCard = None
  # Play the game until the deck is empty or the player won
  while (len(deck) > 0 and progress < 7):
    print('Current streak:', progress)
    # Draw the top card that the player must guess
    top = deck.pop()
    # If this is the first card or the last card, then player must guess red/black
    if progress == 0 or progress == 6:
      # Take user input
      ans = input('Red or Black? (r or b):')
      # If the user input is illegal, keep prompting for input
      while len(ans) != 1 or ans not in 'rb':
        print('Invalid response\n')
        ans = input('Red of Black? (r or b):')
      # Check if the player was correct
      if (ans == 'r' and top[1] in [HEARTS, DIAMONDS]) or \
         (ans == 'b' and top[1] in [SPADES, CLUBS]):
        print('Correct, please continue!\n')
        # Increment progress and record the current card for comparison
        progress += 1
        previousCard = top
      else:
        # Reset progress
        print('Incorrect, you fell in!\n')
        progress = 0
    else:
      # Guess if it was higher or lower than the previous card
      ans = input('Higher or Lower? (h or l):')
      # If the user input is illegal, keep prompting for input
      while len(ans) != 1 or ans not in 'hl':
        print('Invalid response\n')
        ans = input('Higher or Lower? (h or l):')
      # Check if the player was correct
      if (ans == 'h' and top[0] > previousCard[0]) or \
         (ans == 'l' and top[0] < previousCard[0]) or \
         top[0] == previousCard[0]:
        # Increment progress and record the current card for comparison
        print('Correct, please continue!\n')
        previousCard = top
        progress += 1
      else:
        # Reset progress
        print('Incorrect, you fell in!\n')
        progress = 0
    
    # Display the last card
    # If the card is a 1, 11, 12, or 13, look up its actual name in the dictionary for printing
    rankName = top[0]
    if rankName in rank:
      rankName = rank[rankName]
    # Display the top card
    print('The card was:', rankName, 'of', top[1])
  
  # If the player won 7 times they win
  if progress < 7:
    print('You ran out of stepping stones, you lose!')
    tickets = (subTickets(tickets))
    print(playAgainRiverFunction())
  else:
    print('You made it across the river, you win!')
    tickets = (addTickets(tickets))
    print(playAgainRiverFunction())


def deal(cardList, deck):
    cardList.append(deck.pop(0))
   
def initDeal(deck, player, computer):
    random.shuffle(deck)
    deal(player, deck)
    deal(computer, deck)
    deal(player, deck)
    deal(computer, deck)

def sumHand(hand, dictionary):
    sum = 0
    for x in range(len(hand)):
        sum += dictionary[hand[x]]
    return sum

def gui(player, dictionary, deck, computer):
    print("\nYour hand: " + str(player))
    handSum = sumHand(player, dictionary)
    print("Your hand value is " + str(handSum))
    while (sumHand(computer, dictionary) < 17):
        deal(computer, deck)
    if(sumHand(player, dictionary) >= 21):
            return False
    while True:
        try:
            word = (input("Would you like to hit or stay? (h/s): "));
            for letter in word:
                if letter != 'h' and letter != 'H' and letter != 's' and letter != 'S':
                    raise TypeError
            break
            print("Please enter a valid string")
        except ValueError:
            print("Please enter a valid string")
        except TypeError:
            print("Please enter a valid string")
    if(word == 'h' or word == 'H'):
        deal(player, deck)
        if(sumHand(player, dictionary) >= 21):
            return False
        return True
    if(word == 's' or word == 'S'):
        return False

def endGame(player, computer, dictionary):
    global tickets
    print('\nOpponent value is ' + str(sumHand(computer, dictionary)))
    print('Your value is ' + str(sumHand(player, dictionary)))
    if (sumHand(player, dictionary) > 21 and sumHand(computer, dictionary) <= 21):
        print('You Lose!')
        tickets = (subTickets(tickets))
    elif (sumHand(computer, dictionary) > 21 and sumHand(player, dictionary) <= 21):
        print('You Win!')
        tickets = (addTickets(tickets))
    elif (sumHand(player, dictionary) > 21 and sumHand(computer, dictionary) > 21):
        print('You Lose!')
        tickets = (subTickets(tickets))
    elif (sumHand(player, dictionary) == sumHand(computer, dictionary)):
        print('Tie Game!')
    elif (sumHand(player, dictionary) > sumHand(computer,dictionary)):
        print('You Win!')
        tickets = (addTickets(tickets))
    else:
        print('You Lose!')
        tickets = (subTickets(tickets))
    
def twentyOneMain():
    print("Hello! Welcome to Blackjack!")
    while True:
        playingDeck = ['Ace of Clubs', '2 of Clubs', '3 of Clubs', '4 of Clubs', '5 of Clubs', '6 of Clubs', '7 of Clubs', '8 of Clubs', '9 of Clubs', '10 of Clubs', 'Jack of Clubs', 'Queen of Clubs', 'King of Clubs', 'Ace of Diamonds', '2 of Diamonds', '3 of Diamonds', '4 of Diamonds', '5 of Diamonds', '6 of Diamonds', '7 of Diamonds', '8 of Diamonds', '9 of Diamonds', '10 of Diamonds', 'Jack of Diamonds', 'Queen of Diamonds', 'King of Diamonds', 'Ace of Hearts', '2 of Hearts', '3 of Hearts', '4 of Hearts', '5 of Hearts', '6 of Hearts', '7 of Hearts', '8 of Hearts', '9 of Hearts', '10 of Hearts', 'Jack of Hearts', 'Queen of Hearts', 'King of Hearts', 'Ace of Spades', '2 of Spades', '3 of Spades', '4 of Spades', '5 of Spades', '6 of Spades', '7 of Spades', '8 of Spades', '9 of Spades', '10 of Spades', 'Jack of Spades', 'Queen of Spades', 'King of Spades']
        dictionaryDeck = {'Ace of Clubs': 1, '2 of Clubs': 2, '3 of Clubs': 3, '4 of Clubs': 4, '5 of Clubs': 5, '6 of Clubs': 6, '7 of Clubs': 7, '8 of Clubs': 8, '9 of Clubs': 9, '10 of Clubs': 10, 'Jack of Clubs': 10, 'Queen of Clubs': 10, 'King of Clubs': 10, 'Ace of Diamonds': 1, '2 of Diamonds': 2, '3 of Diamonds': 3, '4 of Diamonds': 4, '5 of Diamonds': 5, '6 of Diamonds': 6, '7 of Diamonds': 7, '8 of Diamonds': 8, '9 of Diamonds': 9, '10 of Diamonds': 10, 'Jack of Diamonds': 10, 'Queen of Diamonds': 10, 'King of Diamonds': 10, 'Ace of Hearts': 1, '2 of Hearts': 2, '3 of Hearts': 3, '4 of Hearts': 4, '5 of Hearts': 5, '6 of Hearts': 6, '7 of Hearts': 7, '8 of Hearts': 8, '9 of Hearts': 9, '10 of Hearts': 10, 'Jack of Hearts': 10, 'Queen of Hearts': 10, 'King of Hearts': 10, 'Ace of Spades': 1, '2 of Spades': 2, '3 of Spades': 3, '4 of Spades': 4, '5 of Spades': 5, '6 of Spades': 6, '7 of Spades': 7, '8 of Spades': 8, '9 of Spades': 9, '10 of Spades': 10, 'Jack of Spades': 10, 'Queen of Spades': 10, 'King of Spades': 10}
        playerHand = []
        computerHand = []
        initDeal(playingDeck, playerHand, computerHand)
        while (gui(playerHand, dictionaryDeck, playingDeck, computerHand) == True and (sumHand(playerHand, dictionaryDeck) < 21)):
            continue
        endGame(playerHand, computerHand, dictionaryDeck)
        while True:
            try:
                cont = (input("\nPress q to quit (or anything else to play again): "));
                break
                print("Please enter a valid string")
            except ValueError:
                print("Please enter a valid string")
            except TypeError:
                print("Please enter a valid string")
        if cont == 'q' or cont == 'Q':
            break
    print(main())
    
class giftShop():
  
    def __init__(self, pay, meme):
        self.pay = pay
        self.meme = meme
        return None

    def setpay(self, pay):
        self.pay = pay

    def getpay(self):
        return self.pay
    
    def setmeme(self, meme):
        self.meme = meme

    def getmeme(self):
        return self.meme
    
meme1 = giftShop('>>>You pay 3 munny', '''\n
 ROFL:ROFL:ROFL:ROFL
         _^___
 L    __/   [] \    
LOL===__        \ 
 L      \________]
         I   I
        --------/
LOL WUT ROFLCOPTER!?''')
meme2 = giftShop('>>>You pay 30 munny', '''\n
░░░░░░░▄▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▄░░░░░░
░░░░░░█░░▄▀▀▀▀▀▀▀▀▀▀▀▀▀▄░░█░░░░░
░░░░░░█░█░▀░░░░░▀░░▀░░░░█░█░░░░░
░░░░░░█░█░░░░░░░░▄▀▀▄░▀░█░█▄▀▀▄░
█▀▀█▄░█░█░░▀░░░░░█░░░▀▄▄█▄▀░░░█░
▀▄▄░▀██░█▄░▀░░░▄▄▀░░░░░░░░░░░░▀▄
░░▀█▄▄█░█░░░░▄░░█░░░▄█░░░▄░▄█░░█
░░░░░▀█░▀▄▀░░░░░█░██░▄░░▄░░▄░███
░░░░░▄█▄░░▀▀▀▀▀▀▀▀▄░░▀▀▀▀▀▀▀░▄▀░
░░░░█░░▄█▀█▀▀█▀▀▀▀▀▀█▀▀█▀█▀▀█░░░
░░░░▀▀▀▀░░▀▀▀░░░░░░░░▀▀▀░░▀▀░░░░
NYAN NYAN NYAN NYAN NYAN NYAN NYAN 
NYAN NYAN NYAN NYAN NYAN NYAN NYAN 
NYAN NYAN NYAN NYAN NYAN NYAN NYAN. . .''')
meme3 = giftShop('>>>You pay 300 munny', '''\n
      very luck
─────────▄──────────────▄
────────▌▒█───────────▄▀▒▌
────────▌▒▒▀▄───────▄▀▒▒▒▐
───────▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐
─────▄▄▀▒▒▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐
───▄▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀██▀▒▌
──▐▒▒▒▄▄▄▒▒▒▒▒▒▒▒▒▒▒▒▒▀▄▒▒▌
──▌▒▒▐▄█▀▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐
─▐▒▒▒▒▒▒▒▒▒▒▒▌██▀▒▒▒▒▒▒▒▒▀▄▌
─▌▒▀▄██▄▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▌
─▌▀▐▄█▄█▌▄▒▀▒▒▒▒▒▒░░░░░░▒▒▒▐
▐▒▀▐▀▐▀▒▒▄▄▒▄▒▒▒▒▒░░░░░░▒▒▒▒▌
▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒░░░░░░▒▒▒▐
─▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒▒▒░░░░▒▒▒▒▌
─▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐
──▀▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▒▒▒▒▌
────▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀
───▐▀▒▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀
──▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀▀
doge tiem
                      wow
      much munny''')


def giftShopFunction():
  global tickets
  while True:
    decideShop = input("\n~WELCOME TO THE EZ$$$$$ GIFT SHOP~\nWhat would you like to buy?\n(a)Cardboard Chest: 3 munny  (b)Aether Chest: 30 munny (c)Diamond Chest: 300 munny (d)Leave\n")
    if decideShop == "a" and tickets < 3:
      print("You don't have enough munny")
      print(giftShopFunction())
    if decideShop == "b" and tickets < 30:
      print("You don't have enough munny")
      print(giftShopFunction())
    if decideShop == "c" and tickets < 300:
      print("You don't have enough munny")
      print(giftShopFunction())
    break
  if decideShop == "a":
    tickets = tickets - 3
    print(meme1.getpay())
    print(meme1.getmeme())
    print("\n>>>Alright have a good day! See you next time!")
    print(main()) 
  elif decideShop == "b":
    tickets = tickets - 30
    print(meme2.getpay())
    print(meme2.getmeme())
    print("\n>>>Alright have a good day! See you next time!")
    print(main())
  elif decideShop == "c":
    tickets = tickets - 300
    print(meme3.getpay())
    print(meme3.getmeme())
    print("\n>>>Alright have a good day! See you next time!")
    print(main())
  elif decideShop == "d":
    print(main())
  else:
    print(giftShopFunction())


def checkMunny(tickets):
  print('You have ' + str(tickets) + ' munny!')
  print(main())

####################################################################################################
print(main())
