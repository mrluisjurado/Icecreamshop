print "\t\tEnjoy Ice Cream from my own Cream Shop\n\n"

choice = "z"        # initialize choice with any value that will # set the while loop to true

scopePrice = ""
iceCreamName = ""
iceCreamFlavor = "9"

def iceCremPrice():
        print u"""
                a. 1 scoop  cost you   \u00A3 Pound
                b. 2 scoops cost you  \u00A3 Pound
                c. 3 scoops cost you  \u00A3 Pound
                d. 4 scoops cost you  \u00A3 Pound
                e. 5 scoops cost you  \u00A3 Pound
                """

def iceCreamScope(iceCreamName):
    print "\n How much Scope you want to Order ? ?"
    orderScope = raw_input("\n Type in your choice(a,b,c,d,e (or 0 to exit): ")
    if orderScope == 'a':
        scopePrice = u"\u00A3 2 "
        print "You Order "+ iceCreamName + " With a price of " + scopePrice
        iceCreamOrderd()
    elif orderScope == 'b':
        scopePrice = u"\u00A3 3 "
        print "You Order "+ iceCreamName + " With a price of " + scopePrice
        iceCreamOrderd()
    elif orderScope == 'c':
        scopePrice = u"\u00A3 4 "
        print "You Order "+ iceCreamName + " With a price of " + scopePrice
        iceCreamOrderd()
    elif orderScope == 'd':
        scopePrice = u"\u00A3 5 "
        print "You Order "+ iceCreamName + " With a price of " + scopePrice
        iceCreamOrderd()
    elif orderScope == 'e':
        scopePrice = u"\u00A3 6 "
        print "You Order "+ iceCreamName + " With a price of " + scopePrice
        iceCreamOrderd()
    else:
        print("You choose nothing, Please try again")

def iceCreamOrderd():
        choice = raw_input("\n want to eat now type (eat) or take away (away) : ")
        if choice == 'eat':
             print "\nYou eat your IceCream"
        elif choice == 'away':
             print "\nThanks! Come again in our shop\n"


while choice != "q":
    
    print """
        Kindly Choose the Ice Cream Flavours you would like to Choose from the following menu (or q to exit)"
        a: Order IceCream
        """
    choice = raw_input("\nType in your choice( (a. Order Ice Cream) Or (q. Exit): \n")

    if choice == "a":
        print """
          Dear Customer We offer these flavours Of IceCreams, what would you like to choose\n
          1.Chocolate
          2.Coffee
          3.Mint 
          4.Strawberry
          5.Vanilla 
          """
        choice = raw_input("\nChoose your IceCream Flavour(1,2,3,4,5 (or 0 to exit): ")
        if choice == "1":
            iceCreamName = "Chocolate"
            iceCremPrice()
            iceCreamScope(iceCreamName)
        elif choice == "2":
            iceCreamName = "Coffee"
            iceCremPrice()
            iceCreamScope(iceCreamName)
        elif choice == "3":
            iceCreamName = "Mint"
            iceCremPrice()
            iceCreamScope(iceCreamName)
        elif choice == "4":
            iceCreamName = "Strawberry"
            iceCremPrice()
            iceCreamScope(iceCreamName)
        elif choice == "5":
            iceCreamName = "Vanilla"
            iceCremPrice()
            iceCreamScope(iceCreamName)
        else:
            print "You have not Choose IceCream Flavour"
        
            

                       

            



            
            
        
