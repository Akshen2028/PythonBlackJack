#Black Jack
from random import *
from Graphics import *
game = "yes"
while (not game[0] == "n"):
    gamesPlayed = 0
    gamesWon = 0
    play = "yes"
    print("                              WELCOME TO BLACK JACK                            ")
    print(" -----------------   -----------------   -----------------   ----------------- ")    
    print("|                 | |                 | |                 | |                 |")
    print("|  J              | |  J              | |  J              | |  J              |")
    print("|     __   __     | |                 | |    _   _   _    | |     _______     |")
    print("|    /  \_/  \    | |        /\       | |   / \_/ \_/ \   | |    /       \    |")
    print("|    \       /    | |       /  \      | |   |         |   | |   |         |   |")
    print("|     \     /     | |       \  /      | |    \       /    | |    \       /    |")
    print("|      \   /      | |        \/       | |     \     /     | |     \     /     |")
    print("|       \ /       | |                 | |       \_/       | |      \___/      |")
    print("|                 | |                 | |                 | |                 |")
    print("|              J  | |              J  | |              J  | |              J  |")
    print(" -----------------   -----------------   -----------------   ----------------- ")
    print()
    #Instructions-------
    firstGame = input("Is it your first time playing? ")
    firstGame = firstGame.lower()
    if firstGame[0] == "y": #Displays the list of instructions 
        print()
        print("How to Play:")
        instructions = ["1. You and the dealer (computer player) will get 2 cards and you will know one of the computers cards.", "2. The object of the game is to get the value of your cards as close to 21 as possible.", "3. Every time you are asked to hit, it means if you would like another card from the deck to add to the ones you have (don't have to hit).", "4. At anytime anyone reaches any value above 21, they lose.","5. If no one loses after both players have been given the chance to hit, the player closest to the value of 21 wins.", "6. Any royal card is worth 10 and the other cards are worth the amount that is their number (Ace is 1).","7. If you obtain a jack of spades or clubs through hitting, you can make the value of that card any number you like (only you have the power to do this and the dealer does not).", "8. You will be granted an amount of money to play with and you can keep betting with that money until you are done playing and want to walk away with what you have won, or until you lose all your money.", "9. When you are happy with the amount you have won, you can move on to obtaining prizes with the money you have won. (Make sure you don't lose all your money!)"]
        print(instructions[0]) #prints each instruction of the list 
        print(instructions[1])
        print(instructions[2])
        print(instructions[3])
        print(instructions[4])
        print(instructions[5])
        print(instructions[6])
        print(instructions[7])
        print(instructions[8])
    print()

    #Money-------
    name = input("First Name: ")
    name = name[0].upper()+name[1:].lower()
    print("Welcome",name+"!")
    moneyValue = randint(1,100)
    userMoney = len(name)*moneyValue*1.0 #generates a value for the user to use to bet 
    print("You have been granted",userMoney,"dollars to play.")
    betAmount = float(input("How much do you want to bet? (can bet amount with cents): "))
    firstBet = True
    while(betAmount>userMoney): #makes sure user bets a number within their given value 
        print("You do not have that much money")
        betAmount = int(input("Enter new amount: "))
    moneyLeft = userMoney-betAmount

    Table = GraphWin("BlackJack",400,200)
    loopNum = 0
    def FillSpace(p1,p2,color):
        Shape = Rectangle(p1,p2)
        Shape.setFill(color)
        Shape.setOutline(color)
        Shape.draw(Table)
    #Saved Drawings--------------------------------
    def Heart(x,y): #Function to draw a heart 
        Cir = Circle(Point(x+7,y+7),7)
        Cir.draw(Table)
        Cir = Circle(Point(x+21,y+7),7)
        Cir.draw(Table)
        Line(Point(x+14,y+35),Point(x,y+9)).draw(Table)
        Line(Point(x+14,y+35),Point(x+28,y+9)).draw(Table)
        FillSpace(Point(x+4,y+7),Point(x+24,y+15),'white')
    def Spade(x,y): #Function to draw a spade 
        Circle(Point(x+7,y+25),7).draw(Table)
        Circle(Point(x+21,y+25),7).draw(Table)
        Line(Point(x,y+22),Point(x+14,y)).draw(Table)
        Line(Point(x+28,y+22),Point(x+14,y)).draw(Table)
        FillSpace(Point(x+4,y+25),Point(x+24,y+17),'white')
        Line(Point(x+13,y+30),Point(x+10,y+36)).draw(Table)
        Line(Point(x+15,y+30),Point(x+18,y+36)).draw(Table)
        Line(Point(x+10,y+36),Point(x+18,y+36)).draw(Table)
    def Club(x,y): #Function to draw a club 
        Circle(Point(x+7,y+21),7).draw(Table)
        Circle(Point(x+21,y+21),7).draw(Table)
        Circle(Point(x+14,y+8),7).draw(Table)
        FillSpace(Point(x+10,y+15),Point(x+18,y+21),'white')
        Line(Point(x+13,y+26),Point(x+10,y+32)).draw(Table)
        Line(Point(x+15,y+26),Point(x+18,y+32)).draw(Table)
        Line(Point(x+10,y+32),Point(x+18,y+32)).draw(Table)
    def Diamond(x,y): #Function to draw a diamond 
        Line(Point(x+14,y),Point(x+5,y+18)).draw(Table)
        Line(Point(x+5,y+18),Point(x+14,y+36)).draw(Table)
        Line(Point(x+14,y),Point(x+23,y+18)).draw(Table)
        Line(Point(x+23,y+18),Point(x+14,y+36)).draw(Table)
    def CardBack(x,y):#Function to draw the back of a card 
        incX = 5
        incY = 5
        while incY < 51:
            Rec = Rectangle(Point(x+incX,y+incY),Point(x+incX+5,y+incY+5))
            Rec.setFill('black')
            Rec.draw(Table)
            incX += 10
            if incX > 40 and incX < 46:
                incX = 10
                incY += 5
            elif incX > 45:
                incX = 5
                incY += 5
    while (not play[0] == "n"):
        #TableGraphics------------------------------------------------------------------
        lin = list(range(1,21))
        FillSpace(Point(0,0),Point(400,200),'green')#Green Background
        Line(Point(30,200),Point(30,100)).draw(Table)#Trace Table V
        Line(Point(40,200),Point(40,103)).draw(Table)
        Line(Point(30,100),Point(100,30)).draw(Table)
        Line(Point(40,103),Point(100,43)).draw(Table)
        Line(Point(100,43),Point(301,43)).draw(Table)
        Line(Point(100,30),Point(301,30)).draw(Table)
        Line(Point(360,103),Point(300,43)).draw(Table)
        Line(Point(370,100),Point(300,30)).draw(Table)
        Line(Point(360,200),Point(360,103)).draw(Table)
        Line(Point(370,200),Point(370,100)).draw(Table)
                
        FillSpace(Point(31,200),Point(39,100),'brown') #Fill in Table
        FillSpace(Point(361,200),Point(369,100),'brown')
        FillSpace(Point(100,42),Point(300,31),'brown')
                
        Slantx = 31
        Slanty = 100
        while loopNum < 11: #Fill in Table
            lin[loopNum] = Line(Point(Slantx,Slanty),Point(Slantx+69,Slanty-69))
            lin[loopNum].setOutline('brown')
            lin[loopNum].draw(Table)
            loopNum += 1
            Slantx += 1
            lin[loopNum] = Line(Point(Slantx,Slanty),Point(Slantx+69,Slanty-69))
            lin[loopNum].setOutline('brown')
            lin[loopNum].draw(Table)
            Slanty += 1
            loopNum += 1
        loopNum = 0
                
        Slantx = 295
        Slanty = 37
        while loopNum < 11: #Fill in Table
            lin[loopNum] = Line(Point(Slantx,Slanty),Point(Slantx+69,Slanty+69))
            lin[loopNum].setOutline('brown')
            lin[loopNum].draw(Table)
            loopNum += 1
            Slantx += 1
            lin[loopNum] = Line(Point(Slantx,Slanty),Point(Slantx+69,Slanty+69))
            lin[loopNum].setOutline('brown')
            lin[loopNum].draw(Table)
            Slanty -= 1
            loopNum += 1
        loopNum = 0

        YrCrds = Rectangle(Point(0,145),Point(99,170)) #Orange Box Drawing 
        YrCrds.setFill('orange')
        YrCrds.draw(Table)
        ComCrds = Rectangle(Point(0,65),Point(99,90))
        ComCrds.setFill('orange')
        ComCrds.draw(Table)

        You = Text(Point(50,157),"Your Cards")
        You.setFace("courier")
        You.setSize(8)
        You.draw(Table)
        Com = Text(Point(50,77),"Dealer's Cards")
        Com.setFace("courier")
        Com.setSize(8)
        Com.draw(Table)

        if moneyLeft > 0 and firstBet == False: #asks user for new amount to bet if they are playing another round and it is not their first bet
            print()
            print("You have this much money left to bet:",moneyLeft)
            betAmount = int(input("Enter bet amount: "))
            while(betAmount>moneyLeft):
                print("You do not have that much money")
                betAmount = int(input("Enter new amount: "))
            moneyLeft = moneyLeft-betAmount
        #-------------Deck of Cards--------------
        Let = ["Ace","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King"]
        Suit = ["Hearts","Spades","Clubs","Diamonds"]
        Initial = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

        Card = list(range(1,54))#Creates 53 (0 is not counted for simplicity) Variables that represent each card

        def Shuffle():
            global Card
            global uCard
            Card = list(range(1,54))
            loopNum = 1 #Counts times looped
            num1 = 1
            while num1 < 53:
                for x in Let: #Grabs a string from list 'Let'
                    while loopNum <= 4:
                        string = x+" of "
                        Card[num1] = string
                        num1 += 1
                        loopNum += 1
                    loopNum = 1
            #At this point, all cards are given a number but not a suit
            num1 = 1
            while num1 < 53:
                while loopNum <= 13:
                    for y in Suit: #Grabs a string from list 'Suit'
                        Card[num1] += y #Combines strings
                        num1 += 1
                    loopNum += 1
            uCard = []
            #At this point, all cards are defined from Card[1] to Card[52] with numbers and
            #suits
                    
        #Next I want to give the player a random card without the cards being able to be dealt twice
        cardsDealt = []#Empty list to be filled with cards

        def DealUser(cardNum): #Deals cards into the deck (basically shuffles)
            global uCard
            global maxList
            listFormat = list(range(1,cardNum+1))
            uCard.extend(listFormat)
            num2 = 0
            maxList = 52
            while num2 < cardNum: #Assigns a string value to the uCard variable and removes that string from the card list (runs 52 times)  
                random = randint(1,maxList)
                uCard[num2] = Card[random]
                num2 += 1
                maxList -= 1
                cardsDealt.append(Card[random])
                Card.remove(Card[random])

        def DrawCard(num,suit,x,y):
            Cir = Circle(Point(x+5,y+5),5)#Each Corner of card V
            Cir.setFill('white')
            Cir.draw(Table)
            Cir = Circle(Point(x+45,y+5),5)
            Cir.setFill('white')
            Cir.draw(Table)
            Cir = Circle(Point(x+5,y+55),5)
            Cir.setFill('white')
            Cir.draw(Table)
            Cir = Circle(Point(x+45,y+55),5)
            Cir.setFill('white')
            Cir.draw(Table)
            FillSpace(Point(x+1,y+5),Point(x+49,y+55),'white')#Fills Cards V
            FillSpace(Point(x+5,y+1),Point(x+45,y+59),'white')
            Line(Point(x+5,y),Point(x+45,y)).draw(Table)#Card Outline V
            Line(Point(x+5,y+60),Point(x+45,y+60)).draw(Table)
            Line(Point(x,y+5),Point(x,y+55)).draw(Table)
            Line(Point(x+50,y+5),Point(x+50,y+55)).draw(Table)
            T = Text(Point(x+10,y+10),num)#Card Text V
            T.setFace("courier")
            T.setSize(12)
            T.draw(Table)
            if suit == "Hearts": #Draws heart
                Heart(x+15,y+15)
            if suit == "Clubs": #Draws a club
                Club(x+15,y+15)
            if suit == "Spades": #Draws a Spade
                Spade(x+15,y+15)
            if suit == "Diamonds": #Draws a Diamond 
                Diamond(x+15,y+15)
    #---------^Deck of Cards^-----------

    #Game Start---------------------------------------------------------               
        Shuffle()
        DealUser(52)
        cardValue = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51] 
        def Values(User,y): #sets the card values of each card depending on their face
            for x in Suit:
                loopNum = 1
                for z in Let:
                    if uCard[User].replace(" of "+x,"") == z:
                        if loopNum > 10:
                            loopNum = 10
                        cardValue[y] = loopNum
                    loopNum += 1

        letVisual = list(range(0,52))
        suitVisual = list(range(0,52))
        def CardVisual(CardNumber): #Gives each card a visual representation  
            for x in Suit:  
                loopNum = 0
                for z in Let:
                    if uCard[CardNumber].replace(" of "+x,"") == z:
                        letVisual[CardNumber] = Initial[loopNum]
                    loopNum += 1
                    if uCard[CardNumber].replace(z+" of ","") == x:
                        suitVisual[CardNumber] = x
                      
        print("Your Cards:")
        print(uCard[0])
        print(uCard[1])

        VisualNum = 0
        while VisualNum <= 51: #Defines the graphics on each Card
            CardVisual(VisualNum)
            VisualNum += 1
        
        Vnum = 0
        while Vnum <= 51: #Assigning all card values to the deck
            Values(Vnum,Vnum)
            Vnum += 1  

        DrawCard(letVisual[0],suitVisual[0],100,130)
        DrawCard(letVisual[1],suitVisual[1],155,130)
        DrawCard(letVisual[2],suitVisual[2],100,50)
        DrawCard("","",155,50)
        CardBack(155,50)
        
        total = cardValue[0]+cardValue[1] #User's total card value
        print()
        print("The dealer smiles and flips over one card face up being", uCard[2], "and one card faced down.")
        print()
        print("Your total:", total)

        hitCounter = 0
        hit = input("hit? (Yes/No): ")
        hit = hit.lower()
        nextCard = 4 #The next card in the deck is the 5th card (index counting starts at 0 so 5 would be 4)
        while (not hit[0] == "n"): #Runs until the user stops hitting
            print("Your next card is a(n)",uCard[nextCard])
            DrawCard(letVisual[nextCard],suitVisual[nextCard],155+(55*(nextCard-3)),130)
            if uCard[nextCard] == "Jack of Spades" or uCard[nextCard] == "Jack of Clubs": #If a Blackjack is drawn, user gets to make the card any value
                print("You got a Black Jack!")
                cardValue[nextCard] = int(input("Enter a card value that you want for this card from 0-10: "))
            hitCounter += 1
            total = total + cardValue[nextCard]
            nextCard = nextCard +1
            print("Your new total:", total)
            if total>21: #what happens when the user loses or not 
                print()
                print("YOU LOSE")
                gamesPlayed +=1
                player = "loser"
                hit = "no"
            else:
                hit = input("hit? (Yes/No): ")
                hit = hit.lower()
        comTotal = cardValue[2]+cardValue[3]

        hitCounterC = 0
        if total<=21: #Only runs if the user has not lost
            if (not moneyLeft == 0): #gives the user the chance to raise their bet amount if they have any moneey left 
                print()
                askRaise = input("Do you want to raise your bet amount? (Yes/No): ")
                askRaise = askRaise.lower()
                if (not askRaise == "no"): 
                    raiseMoney = float(input("Enter raise amount: "))
                    while (raiseMoney > moneyLeft): #makes sure they only bet within what they have left 
                        print("You do not have that much money to bet.")
                        raiseMoney = float(input("Enter new raise amount: "))
                    moneyLeft = moneyLeft-raiseMoney
                    betAmount = betAmount+raiseMoney
            else:
                print("You have no more money to bet.")
            print()
            
            while comTotal <=15: #Com keeps hitting until they get a value of 15 or higher
                print("After thinking, the dealer decides to hit and gets a(n)", uCard[nextCard])
                comTotal = comTotal + cardValue[nextCard]
                hitCounterC += 1
                DrawCard(letVisual[nextCard],suitVisual[nextCard],155+(55*(nextCard-3-hitCounter)),50)
                nextCard = nextCard + 1
            if comTotal>21: #Computer loses
                print("The dealer's flipped card was a", uCard[3])
                print("The dealer's total:", comTotal)
                DrawCard(letVisual[3],suitVisual[3],155,50)
                print()
                print("YOU WIN!")
                gamesPlayed +=1
                gamesWon += 1
                player = "winner"
            elif comTotal <=21: #Computer Stays
                print("Dealer decides to stay.")
                print()
                hit = input("One more chance to hit? (Yes/No): ") #User gets one more chance to hit (Only is computer doesn't lose)
                hit = hit.lower()
                while (not hit[0] == "n"):
                    print("Your next card is a(n)",uCard[nextCard])
                    if uCard[nextCard] == "Jack of Spades" or uCard[nextCard] == "Jack of Clubs":
                        print("You got a Black Jack!")
                        cardValue[nextCard] = int(input("Enter a card value that you want for this card from 0-10: "))
                    hitCounter += 1
                    DrawCard(letVisual[nextCard],suitVisual[nextCard],155+(55*(nextCard-3-hitCounterC)),130)
                    total = total + cardValue[nextCard]
                    nextCard = nextCard +1
                    print("Your new total:", total)
                    if total>21: #Double Checking if the user lost or not
                        print()
                        print("YOU LOSE")
                        gamesPlayed +=1
                        player = "loser"
                        hit = "no"
                    else:
                        hit = input("hit? (Yes/No): ")
                        hit = hit.lower()
            if total <=21 and comTotal <=21: #Finds winner of both players are still in the game 
                print()
                print("The dealer's flipped card was a", uCard[3])
                DrawCard(letVisual[3],suitVisual[3],155,50)
                print("The dealer's total:", comTotal)
                if total > comTotal: #User Wins
                    print()
                    print("YOU WIN!")
                    gamesPlayed +=1
                    gamesWon += 1
                    player = "winner"
                elif total == comTotal: #Tie
                    print()
                    print("Split Pot.")
                    gamesPlayed +=1
                    player = "tie"
                else: #Computer Wins
                    print()
                    print("YOU LOSE")
                    gamesPlayed +=1
                    player = "loser"
        if player == "loser": #final money calculations if the user loses 
            userMoney = moneyLeft+betAmount
            finalMoney = userMoney - betAmount
            moneyLeft = finalMoney
        elif player == "winner": #final money calculations if the user wins 
            finalMoney = moneyLeft + (betAmount*2)
            moneyLeft = finalMoney
            userMoney = finalMoney
        elif player == "tie": #final money calculations if the user ties 
            finalMoney = moneyLeft + betAmount
            moneyLeft = finalMoney
        print("Your total after this game is", finalMoney, "dollars.")
        firstBet = False
        if moneyLeft == 0: #stops the user from playing another round when they have no more money left to bet
            print()
            print("GAME OVER - You have no more money to bet.")
            play = "n"
        else:
            print()
            print("You may play again to try and win some more money or you can move on to the prizes.")
            play = input("play another round? (Yes/No): ")
            play = play.lower()
    #Game Finished--------------------------------------------
    #Prizes
    prizes = ["Gum","Teddy Bear","Plastic Necklace","Black Jack T-shirt","Bottle of \"sparkling water\"","Ray Bans Sunglasses","iPhone X", "Jordan Shoes", "A weeks stay in Ritz Carlton"]
    gum = randint(1,100) #Assigning random money value to prizes based of how valuable they are 
    bear = randint(1,100)
    neck = randint(1,100)
    shirt = randint(1,250)
    drink = randint(1,250)
    sun = randint(1,250)
    phone = randint(250,500)
    shoe = randint(250,500)
    ritz = randint(250,500)
    print()
    if finalMoney>0: #prizes show if user has more than 0 dollars 
        if (gamesPlayed < 4 or gamesWon < 2) and finalMoney <=100: #prizes for small amount of games played/won, and small amount of money won 
            print("Prizes:")
            print()
            print(prizes[0])
            print("Value: ",gum,"dollars (type gum)")
            print()
            print(prizes[1])
            print("Value: ",bear,"dollars (type bear)")
            print()
            print(prizes[2])
            print("Value: ",neck,"dollars (type necklace)")
            print()
            if finalMoney < gum and finalMoney < bear and finalMoney < neck: #the user cannot afford any of the prizes 
                print("Wow, you can't even afford the prizes? Just leave the Casino with what you have.")
            else:
                buy = input("Which do you want? Choose one of the above: ")
                buy = buy.lower()
                while (buy[0] == "g" and gum>finalMoney) or (buy[0] == "b" and bear>finalMoney) or (buy[0] == "n" and neck>finalMoney): #asks user to pick another prize they can afford if they choose one that is too expensive
                    print("Cannot afford this prize.")
                    buy = input("Which do you want? Choose one of the above: ")
                    buy = buy.lower()
                if buy[0] == "g": #subrtacts cost of prize from total amount of final money
                    finalMoney = finalMoney - gum
                    print("You have taken home",prizes[0],"and have walked away with", finalMoney,"dollars.")
                if buy[0] == "b":
                    finalMoney = finalMoney - bear
                    print("You have taken home",prizes[1],"and have walked away with", finalMoney,"dollars.")
                if buy[0] == "n":
                    finalMoney = finalMoney - neck
                    print("You have taken home",prizes[2],"and have walked away with", finalMoney,"dollars.")

        elif (gamesPlayed < 4 or gamesWon < 2) and finalMoney > 100:
            print("Prizes:")
            print()
            print(prizes[3])
            print("Value: ",shirt,"dollars (type shirt)")
            print()
            print(prizes[4])
            print("Value: ",drink,"dollars (type bottle)")
            print()
            print(prizes[5])
            print("Value: ",sun,"dollars (type glasses)")
            print()
            if finalMoney < shirt and finalMoney < drink and finalMoney < sun:
                print("Wow, you can't even afford the prizes? Just leave the Casino with what you have.")
            else:
                buy = input("Which do you want? Choose one of the above: ")
                buy = buy.lower()
                while (buy[0] == "s" and shirt>finalMoney) or (buy[0] == "b" and drink>finalMoney) or (buy[0] == "g" and sun>finalMoney): #asks user to pick another prize they can afford if they choose one that is too expensive
                    print("Cannot afford this prize.")
                    buy = input("Which do you want? Choose one of the above: ")
                    buy = buy.lower()
                if buy[0] == "s":
                    finalMoney = finalMoney - shirt
                    print("You have taken home",prizes[3],"and have walked away with", finalMoney,"dollars.")
                if buy[0] == "b":
                    finalMoney = finalMoney - drink
                    print("You have taken home",prizes[4],"and have walked away with", finalMoney,"dollars.")
                if buy[0] == "g":
                    finalMoney = finalMoney - sun
                    print("You have taken home",prizes[5],"and have walked away with", finalMoney,"dollars.")
        elif (gamesPlayed < 6 or gamesWon < 4) and finalMoney <=100: #prizes for played a medium amount of games played/won, and small amount of money won
            print("Prizes:")
            print()
            print(prizes[3])
            print("Value: ",shirt,"dollars (type shirt)")
            print()
            print(prizes[4])
            print("Value: ",drink,"dollars (type bottle)")
            print()
            print(prizes[5])
            print("Value: ",sun,"dollars (type glasses)")
            print()
            if finalMoney < shirt and finalMoney < drink and finalMoney < sun: #user cannot afford any of the prizes 
                print("Wow, you can't even afford the prizes? Just leave the Casino with what you have.")
            else:
                buy = input("Which do you want? Choose one of the above: ")
                buy = buy.lower()
                while (buy[0] == "s" and shirt>finalMoney) or (buy[0] == "b" and drink>finalMoney) or (buy[0] == "g" and sun>finalMoney): #asks user to pick another prize they can afford if they choose one that is too expensive
                    print("Cannot afford this prize.")
                    buy = input("Which do you want? Choose one of the above: ")
                    buy = buy.lower()
                if buy[0] == "s": #subrtacts cost of prize from final money total 
                    finalMoney = finalMoney - shirt
                    print("You have taken home",prizes[3],"and have walked away with", finalMoney,"dollars.")
                if buy[0] == "b":
                    finalMoney = finalMoney - drink
                    print("You have taken home",prizes[4],"and have walked away with", finalMoney,"dollars.")
                if buy[0] == "g":
                    finalMoney = finalMoney - sun
                    print("You have taken home",prizes[5],"and have walked away with", finalMoney,"dollars.")
        elif (gamesPlayed < 6 or gamesWon < 4) and finalMoney > 100: #prizes for medium amount of games played/won, and large amount of money won
            print("Prizes:")
            print()
            print(prizes[3])
            print("Value: ",shirt,"dollars (type shirt)")
            print()
            print(prizes[4])
            print("Value: ",drink,"dollars (type bottle)")
            print()
            print(prizes[5])
            print("Value: ",sun,"dollars (type glasses)")
            print()
            if finalMoney < shirt and finalMoney < drink and finalMoney < sun: #user cannot afford prize 
                print("Wow, you can't even afford the prizes? Just leave the Casino with what you have.")
            else:
                buy = input("Which do you want? Choose one of the above: ")
                buy = buy.lower()
                while (buy[0] == "s" and shirt>finalMoney) or (buy[0] == "b" and drink>finalMoney) or (buy[0] == "g" and sun>finalMoney):#asks user to pick another prize they can afford if they choose one that is too expensive
                    print("Cannot afford this prize.")
                    buy = input("Which do you want? Choose one of the above: ")
                    buy = buy.lower()
                if buy[0] == "s": #Subtracts prize money from total final money 
                    finalMoney = finalMoney - shirt
                    print("You have taken home",prizes[3],"and have walked away with", finalMoney,"dollars.")
                if buy[0] == "b":
                    finalMoney = finalMoney - drink
                    print("You have taken home",prizes[4],"and have walked away with", finalMoney,"dollars.")
                if buy[0] == "g":
                    finalMoney = finalMoney - sun
                    print("You have taken home",prizes[5],"and have walked away with", finalMoney,"dollars.")
        elif (gamesPlayed > 5 or gamesWon > 3) and finalMoney <=100: #prizes for large amount of games played/won, and small amount of money won
            print("Prizes:")
            print()
            print(prizes[6])
            print("Value: ",phone,"dollars (type phone)")
            print()
            print(prizes[7])
            print("Value: ",shoe,"dollars (type shoe)")
            print()
            print(prizes[8])
            print("Value: ",ritz,"dollars (type ritz)")
            print()
            if finalMoney < phone and finalMoney < shoe and finalMoney < ritz: #user cannot afford any prizes 
                print("Wow, you can't even afford the prizes? Just leave the Casino with what you have.")
            else:
                buy = input("Which do you want? Choose one of the above: ")
                buy = buy.lower()
                while (buy[0] == "p" and phone>finalMoney) or (buy[0] == "s" and shoe>finalMoney) or (buy[0] == "r" and ritz>finalMoney): #asks user to pick another prize they can afford if they choose one that is too expensive
                    print("Cannot afford this prize.")
                    buy = input("Which do you want? Choose one of the above: ")
                    buy = buy.lower()
                if buy[0] == "p": #subtracts cost of prizes from total final money 
                    finalMoney = finalMoney - phone
                    print("You have taken home",prizes[6],"and have walked away with", finalMoney,"dollars.")
                if buy[0] == "s":
                    finalMoney = finalMoney - shoe
                    print("You have taken home",prizes[7],"and have walked away with", finalMoney,"dollars.")
                if buy[0] == "r":
                    finalMoney = finalMoney - ritz
                    print("You have taken home",prizes[8],"and have walked away with", finalMoney,"dollars.")
        elif (gamesPlayed > 5 or gamesWon > 3) and finalMoney > 100: #prizes for large amount of games played/won, and large amount of money won
            print("Prizes:")
            print()
            print(prizes[6])
            print("Value: ",phone,"dollars (type phone)")
            print()
            print(prizes[7])
            print("Value: ",shoe,"dollars (type shoe)")
            print()
            print(prizes[8])
            print("Value: ",ritz,"dollars (type ritz)")
            print()
            if finalMoney < phone and finalMoney < shoe and finalMoney < ritz: #user cannot afford prizes 
                print("Wow, you can't even afford the prizes? Just leave the Casino with what you have.")
            else:
                buy = input("Which do you want? Choose one of the above: ")
                buy = buy.lower()
                while (buy[0] == "p" and phone>finalMoney) or (buy[0] == "s" and shoe>finalMoney) or (buy[0] == "r" and ritz>finalMoney): #asks user to pick another prize they can afford if they choose one that is too expensive
                    print("Cannot afford this prize.")
                    buy = input("Which do you want? Choose one of the above: ")
                    buy = buy.lower()
                if buy[0] == "p": #subtracts cost of prizes from total final money
                    finalMoney = finalMoney - phone
                    print("You have taken home",prizes[6],"and have walked away with", finalMoney,"dollars.")
                if buy[0] == "s":
                    finalMoney = finalMoney - shoe
                    print("You have taken home",prizes[7],"and have walked away with", finalMoney,"dollars.")
                if buy[0] == "r":
                    finalMoney = finalMoney - ritz
                    print("You have taken home",prizes[8],"and have walked away with", finalMoney,"dollars.")
    else: #user has no money at all for no prizes 
        print("No money left eh? Please leave the Casino, there is an ATM outside.")
    print()
    game = input("Do you want to play the entire game again? (Yes/No): ")
    game = game.lower()
    Table.close()
    print("-"*80)
print("Thanks for playing BLACK JACK.")
