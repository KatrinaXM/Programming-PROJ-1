# Start of programme
# Self Note: To-settle alignment and decoration last - gna work on functionailty first

#print("╔═══════════════════🐠✨(๑ᵔ⤙ᵔ๑)🍖🌟 PENYET & BAKAR HEAVEN 🌟🍖(๑ᵔ⤙ᵔ๑)✨🐠═══════════════╗")
#print("║                             WELCOME TO PENYET & BAKAR HEAVEN!                               ║")
#print("║                                                                                             ║")
#print("║                                   LANGUAGES AVAILABLE:                                      ║")
#print("║                                        1) ENGLISH                                           ║")
#print("║                                        2) CHINESE                                           ║")
#print("║                                         3) MALAY                                            ║")
#print("║                                         4) TAMIL                                            ║")
#print("║                                                                                             ║")
#print("╚═══════════════════🐠✨(๑ᵔ⤙ᵔ๑)🍖🌟 PENYET & BAKAR HEAVEN 🌟🍖(๑ᵔ⤙ᵔ๑)✨🐠═══════════════╝")
#lang = input("                    CHOOSE A LANGUAGE YOU WISH TO USE [1/2/3/4]: ")
#print("╚═══════════════════🐠✨(๑ᵔ⤙ᵔ๑)🍖🌟 PENYET & BAKAR HEAVEN 🌟🍖(๑ᵔ⤙ᵔ๑)✨🐠═══════════════════╝")

#Variables Initialised:
Cart = 0.00
New_Cart = 0.00
Quantity = 0
New_Quantity = 0
total = 0.00
price = 0.00

ChosenFooditem = None
choosenaddon = None
u_confirm = None
whichtoedit = None
chooseBakarset = None
choosePenyetset = None
chosenadd_on = None
whichdiscount = None

programrunning = True

setsBakarmenu = {}
setsPenyetmenu = {}
add_onopt = {}
paymenttypes = {}
purchased_sets = []
purchased_addons = []

typeofdiscounts = {
        "1": ["NYP STUDENT"],
        "2": ["NYP STAFF"],
        "3": ["NONE OF THE ABOVE"]
    }


# try adding cart inside as a param if there is any future issues
#This is the main menu function that will be called to display the main menu and get the user's choice
def mmeng():
    global Cart
    print(""
          "     ♡ ∩_∩ \n"
          "     (๑ᵔ⤙ᵔ๑) ♡ \n"
          "❀------U U-----------------------------------------------------------------------------------❀ \n"
          "|                                   PENYET & BAKAR HEAVEN                                     | \n"
          "❀--------------------------------------------------------------------------------------------❀ \n"
          "|                                   PENYET & BBQ SET MEAL                                     | \n"
          "❀--------------------------------------------------------------------------------------------❀ \n"
          "|                                         OPTIONS                                             | \n"
          "|                              [1] SETS                                                       | \n"
          "|                              [2] ADD-ONS                                                    | \n"
          "|                              [3] EXIT                                                       | \n"
          "|                              [4] VIEW/EDIT CART & CHECKOUT                                  | \n"
          "❀--------------------------------------------------------------------------------------------❀ ")
    print(f"CART:${Cart:.2f} ")
    print("❀--------------------------------------------------------------------------------------------❀ ")


    choice = input("Choose Option[1/2/3/4]: ")
    return choice

#This is the set main menu function that will be called to display the sets menu and get the user's choice.
#The set main menu conprises of two sub-menus, the Bakar sets menu and the Penyet sets menu. The user can choose to view either of the two sub-menus or return to the main menu.
def set_mainmenu():
    global Cart
    print("❀--------------------------------------------------------------------------------------------❀ \n"
          "|                                    OUR SETS                                                 | \n"
          "❀--------------------------------------------------------------------------------------------❀ \n"
          "|                                [1] BAKAR SETS                                               | \n"
          "|                                [2] PENYET SETS                                              | \n"
          "|                                [3] RETURN TO MAIN MENU                                      | \n"
          "❀--------------------------------------------------------------------------------------------❀")
    print(f"CART: ${Cart:.2f}")
    print("❀--------------------------------------------------------------------------------------------❀")
    chosenset = input("Choose sets to view [1/2] or choose to return to main menu[3]: ")
    return chosenset

#This is the add_ons menu function that will be called to display the add-ons menu and get the user's choice
def add_onsmenu():
   global Cart
   print( "❀--------------------------------------------------------------------------------------------❀ \n"
          "|                                  OUR ADD-ONS                                                | \n"
          "❀--------------------------------------------------------------------------------------------❀")
   add_onsopt = {
       "A1" : ["Rice","...........................................................", 0.50],
       "A2" : ["Egg","............................................................", 0.80],
       "A3" : ["Chilli",".........................................................", 0.50],
       "A4" : ["Fried/Grilled Dori Fish (Per Piece)","............................", 3.50],
       "A5" : ["Fried/Grilled Chicken Leg Quarter (Per Piece)","..................",3.50],
       "A6" : ["Fried Chicken Wing (1pc)",".......................................",1.50],
       "E":  ["Choose this option to", "return to main menu", "..........................."],
   }

   for key, value in add_onsopt.items():
       if key == "E":
           print(f"|   {key:<10} {value[0]} {value[1]} {value[2]:<36} |")

       elif key == "A1":
           print(f"|   {key:<8} {value[0]:>6} {value[1]} ${value[2]:<13.2f}|")

       elif key == "A2":
           print(f"|   {key:<7} {value[0]:>6} {value[1]} ${value[2]:<13.2f}|")

       elif key == "A4":
           print(f"|   {key:<10} {value[0]:>6} {value[1]} ${value[2]:<13.2f}|")

       elif key == "A5":
           print(f"|   {key:<10} {value[0]:>6} {value[1]} ${value[2]:<13.2f}|")
       elif key == "A6":
           print(f"|   {key:<10} {value[0]:>6} {value[1]} ${value[2]:<13.2f}|")
       else:
           print(f"|   {key:<10} {value[0]} {value[1]} ${value[2]:<13.2f}|")


   print("❀--------------------------------------------------------------------------------------------❀")
   print(f"CART: ${Cart:.2f}")
   print("❀--------------------------------------------------------------------------------------------❀")
   chooseadd_on = input("Choose Option[A1/A2/A3/A4/A5/A6/E]: ").upper()
   return chooseadd_on,add_onsopt

#This is the Bakar sets menu function that will be called to display the Bakar sets menu and get the user's choice
def display_BakarMenu():
    global Cart
    print(
        "❀--------------------------------------------------------------------------------------------❀ \n"
        "|                                  OUR BAKAR SETS                                             | \n"
        "❀--------------------------------------------------------------------------------------------❀")
    setsBakarmenu = {""
                     "01": ["Ayam Bakar Set (Grilled Chicken Set)", "....................",  5.80],
                     "02": ["Dori Bakar Set (Grilled Dori Set)", ".......................",  5.90],
                     "03": ["Ayam Bakar Set (Grilled Boneless Chicken Set)", "...........",  6.30],
                     "04": ["Gulai Ayam Set (Curry Chicken Whole Leg Set)", "............",  6.20],
                     "E": ["Choose this option to", "return to main menu", "...................."],
                     }
# For alignment purposes to keep the Bakar menu neat
    for key, options in setsBakarmenu.items():
        if key == "E":
            print(f"|  {key:<8} {options[0]:^20} {options[1]:^0}  {options[2]:<37}  |")
        else:
            print(f"|  {key:<8} {options[0]:^20} {options[1]:^0}  ${options[2]:<20.2f}  |")


    print("❀--------------------------------------------------------------------------------------------❀")
    print(f"CART: ${Cart:.2f}")
    print("❀--------------------------------------------------------------------------------------------❀ \n")
    chooseBakarset = input("Choose Option[01/02/03/04/E]: ").upper()
    return setsBakarmenu, chooseBakarset



#This is the Penyet sets menu function that will be called to display the Penyet sets menu and get the user's choice
def display_PenyetMenu():
    global Cart
    print(
        "❀--------------------------------------------------------------------------------------------❀  \n"
        "|                                  OUR PENYET SETS                                            | \n"
        "❀--------------------------------------------------------------------------------------------❀")

    setsPenyetmenu = {
                      "05": ["Ayam Penyet Set (Fried Chicken Set)", ".....................",  5.80],
                      "06": ["Dori Penyet Set (Fried Dori Set)", ".....................",  5.90],
                      "07": ["Ayam Penyet Set (Fried Boneless Chicken Set)", "............",  6.30],
                      "08": ["Ayam Penyet Set (Fried Chicken Wing Set 2pcs)", "................",  5.80],
                      "E": ["Choose this option to", "return to main menu", "...................."],
                      }
# For alignment purposes to keep the Penyet menu neat
    for key, options in setsPenyetmenu.items():
        if key == "E":
            print(f"|  {key:<8} {options[0]:^20} {options[1]:^0}  {options[2]:<37}  |")
        
        elif key == "06":
            print(f"|  {key:<8} {options[0]:^20} {options[1]:^0}  ${options[2]:<23.2f}  |")

        elif key == "08":
            print(f"|  {key:<8} {options[0]:^20} {options[1]:^0}  ${options[2]:<15.2f}  |")

        else:
            print(f"|  {key:<8} {options[0]:^20} {options[1]:^0}  ${options[2]:<20.2f}  |")

    print("❀--------------------------------------------------------------------------------------------❀")
    print(f"CART: ${Cart:.2f}")
    print("❀--------------------------------------------------------------------------------------------❀ \n")
    choosePenyetset = input("Choose Option[05/06/07/08/E]: ").upper()
    return setsPenyetmenu,choosePenyetset


#This is the function that will be called to display the move on options and get the user's choice
def move_on():
    print(""
        "❀--------------------------------------------------------------------------------------------❀  \n"
        "|                                  WHAT WOULD YOU LIKE TO DO?                                 | \n"
        "❀--------------------------------------------------------------------------------------------❀  \n"
          "A)  Back to Main Menu \n" 
          "B)  View/Edit Cart \n"
          "C)  Go to Checkout\n"
          "❀--------------------------------------------------------------------------------------------❀"
           )
    print(f"CART: ${Cart:.2f}")
    print("❀--------------------------------------------------------------------------------------------❀ \n")

    choicemoveon = input("Choose Option[A/B/C]: ").upper()
    return choicemoveon

#This is the function that will be called to get a valid integer input from the user-Part of my error handling system for invalid inputs
def getvalidint(prompt, min_value=1):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")
            continue
        if value < min_value:
            print(f"Invalid input. Please enter a whole number of at least {min_value}.")
            continue
        return value
    
#This is the function that will be called to get a valid index input from the user-Part of my error handling system for invalid inputs

def getvalidindex(prompt, list_length):
    if list_length == 0:
        return None
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")
            continue
        if value < 1 or value > list_length:
            print(f"Invalid input. Please enter a number between 1 and {list_length}.")
            continue
        return value


#This is the function that will be called to confirm the user's order and update the cart accordingly. It also asks the user to edit the quantity of the chosen food item if they wish to do so.
def confirm(Cart,total,Quantity,ChosenFooditem,price):
    while True:
        try:
            u_confirm = input("To confirm and continue, type [y]. To edit quantity, type [n]: ").lower()
            break
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")
    New_Quantity = Quantity
    New_Cart = Cart
    #sets = choosePenyetset,chooseBakarset
    #add_ons = chooseadd_on

    while u_confirm not in ["y", "n"]:
        print("Invalid input. Please try again.")
        u_confirm = input("To confirm and continue, type [y]. To edit quantity, type [n]: ").lower()

    if u_confirm == "y":
        Cart += total
        print("Cart updated")
        print(f"CART: ${Cart:.2f}")
#        purchased[len(purchased)] = {"Sets": ChosenFooditem, "Add-ons": choosenaddon, "Quantity": New_Quantity,"Cost": total}

    elif u_confirm == "n":
        New_Quantity = getvalidint("Please indicate new Quantity:  ",min_value=1)
        #old_total = total
        total = price * New_Quantity
        Cart += total
        print("Item Quantity Changed to ", New_Quantity)
        print("Cart updated")
        print(f"CART: ${Cart:.2f}")

        #if chooseBakarset in setsBakarmenu.keys():
         #   total = float(setsBakarmenu[chooseBakarset][2]) * New_Quantity
          #  Cart += total
           # New_Cart = Cart
            #Cart += (old_total - total) 
            #New_Cart = Cart 
#            print("Item Quantity Changed to ", New_Quantity)
 #           print("Cart updated")
  #          print(f"CART: ${Cart:.2f}")

   #     elif choosePenyetset in setsPenyetmenu.keys():
    #        total = float(setsPenyetmenu[choosePenyetset][2]) * New_Quantity
     #       Cart += total
            #Cart += (old_total - total) 
      #      New_Cart = Cart
       #     #Cart = New_Cart
        #    print("Item Quantity Changed to ", New_Quantity)
         #   print("Cart updated")
          #  print(f"CART: ${Cart:.2f}")

#        elif chosenadd_on in add_onsopt.keys():
 #           total = float(add_onsopt[chosenadd_on][2]) * New_Quantity
  #          Cart += total
   #         New_Cart = Cart
            #Cart += (old_total - total) 
           # New_Cart = Cart
    #        print("Item Quantity Changed to ", New_Quantity)
     #       print("Cart updated")
      #      print(f"CART: ${Cart:.2f}")
          #  purchased[len(purchased)]={ "Sets" : ChosenFooditem, "Add-ons" : choosenaddon,"Quantity" : New_Quantity,"Cost":total  }

# to display the purchased items in the cart

    if ChosenFooditem in [setsBakarmenu[k][0] for k in setsBakarmenu] + [setsPenyetmenu[k][0] for k in setsPenyetmenu]:
        purchased_sets.append({"SET": ChosenFooditem, "QUANTITY": New_Quantity, "PRICE": price, "COST": total})
    else:
        purchased_addons.append({"ADD-ON": ChosenFooditem, "QUANTITY": New_Quantity, "PRICE": price, "COST": total})

    return Cart
    

    #return Cart,New_Quantity,total,ChosenFooditem,chooseBakarset,setsBakarmenu,choosePenyetset,setsPenyetmenu,chosenadd_on,add_onopt,ChosenFooditem,New_Cart,price

# This is the function that will be called to order a set. It takes in the sets menu and the chosen set as parameters, and updates the cart accordingly.
def order_set(setsmenu, chosenset):
    global Cart
    ChosenFooditem = setsmenu[chosenset][0]
    print("Option Chosen: ", ChosenFooditem)
    price = round(float(setsmenu[chosenset][2]),2)
    Quantity = getvalidint("Please indicate Quantity:  ")
    total = round(price * Quantity, 2)
    print(f"|  {'Item':<47} {'Quantity':^10} {'Cost':>30}  |")
    print(f"|  {ChosenFooditem:<47} {Quantity:^10} ${total:>30.2f} |")
    Cart = confirm(Cart, total, Quantity, ChosenFooditem, price)
    return Cart

# This is the function that will be called to order an add-on. It takes in the add-ons menu and the chosen add-on as parameters, and updates the cart accordingly.
def order_addon(add_onsopt, chosenadd_on):
    global Cart
    choosenaddon = add_onsopt[chosenadd_on][0]
    print("Option Chosen: ", choosenaddon)
    Quantity = getvalidint("Please indicate Quantity:  ")
    price = round(float(add_onsopt[chosenadd_on][2]),2)
    total = round(Quantity * price, 2)
    print(f"|  {'Add-on':<47} {'Quantity':^10} {'Cost':>30}  |")
    print(f"|  {choosenaddon:<47} {Quantity:^10} ${total:>30.2f} |")
    Cart = confirm(Cart, total, Quantity, choosenaddon, price)
    return Cart 

# This is the function that will be called to display the cart. It shows the items in the cart, their quantities, and their costs.
# The costs both before and after discount are displayed in the receipt function.
def displaycart():
    print(
        "❀--------------------------------------------------------------------------------------------❀ \n"
        "|                                          CART                                               | \n"
        "❀--------------------------------------------------------------------------------------------❀")
    print(f"| {"SETS":<50} {"QUANTITY":<10}   {"COST":<28}|")
    print("❀--------------------------------------------------------------------------------------------❀")
    for i in purchased_sets:
        print(f"| {i["SET"]:<50}  {i["QUANTITY"]:<10}  ${i["COST"]:<26.2f} |")
    if len(purchased_sets) == 0:
        print("| No sets in cart. Please add sets to cart.                                                   |" )
    print("❀--------------------------------------------------------------------------------------------❀")
    print(f"| {"ADD-ONS":<50} {"QUANTITY":<10}   {"COST":<28}|")
    print("❀--------------------------------------------------------------------------------------------❀")
    for r in purchased_addons:
        print(f"| {r["ADD-ON"]:<50}  {r["QUANTITY"]:<10}  ${r["COST"]:<27.2f}|")
    if len(purchased_addons) == 0:
        print("| No add-ons in cart. Please add add-ons to cart.                                             |")

    print("❀--------------------------------------------------------------------------------------------❀")
    print(f"| {"YOUR TOTAL(Before Discount):":<61}   ${Cart:<27.2f}|")
    print("❀--------------------------------------------------------------------------------------------❀")

# This is the function that will be called to display the options after the cart has been viewed.
# It shows the user the options to view/edit the cart, return to the main menu, proceed to checkout, or cancel the order and exit.
def actionaftercart():
    print("❀--------------------------------------------------------------------------------------------❀ \n"
          "|                             WHAT WOULD YOU LIKE TO DO NOW?                                  | \n"
          "❀--------------------------------------------------------------------------------------------❀ \n"
          "|                                  1) VIEW/EDIT CART                                          | \n"
          "|                                  2) RETURN TO MAIN MENU                                     | \n"
          "|                                  3) PROCEED TO CHECKOUT                                     | \n"
          "|                                  4) CANCEL ORDER AND EXIT                                   | \n"
          "❀--------------------------------------------------------------------------------------------❀")
    print(f"CART: ${Cart:.2f}")
    print("❀--------------------------------------------------------------------------------------------❀")

# This is the function that will be called to check for discounts. It takes in the cart as a parameter, and applies the appropriate discount based on the user's choice.
def checkfordiscounts(New_Cart):
    global whichdiscount
    print("❀--------------------------------------------------------------------------------------------❀ \n"
          "|                                   DISCOUNT CHECKER                                          | \n"
          "❀--------------------------------------------------------------------------------------------❀ ")
    
    for key,value in typeofdiscounts.items():
        print(f"| {key:<34} {value[0]:<56} |")
    print("❀--------------------------------------------------------------------------------------------❀")
    whichdiscount = input("Choose option [1/2/3]: ")
    print("❀--------------------------------------------------------------------------------------------❀")

    while whichdiscount not in ["1", "2", "3"]:
        print("Invalid input. Please try again.")
        whichdiscount = input("Choose option [1/2/3]: ")

    if whichdiscount == "1":
        New_Cart = round(Cart * 0.90, 2)
        print("Discount Applied, CART updated")
        print(f"CART (After discount applied): ${New_Cart:.2f}")

    elif whichdiscount == "2":
        New_Cart = round(Cart * 0.95, 2)
        print("Discount Applied, CART updated")
        print(f"CART(After discount applied): ${New_Cart:.2f}")

    else:
        print("No Discount applicable")
        New_Cart = Cart

    print("Proceeding to checkout.....")
    return New_Cart



       


def receipt():
    print("❀--------------------------------------------------------------------------------------------❀ \n"
          "|                                          RECEIPT                                            | \n"
          "❀--------------------------------------------------------------------------------------------❀ ")
    displaycart()
    print("❀--------------------------------------------------------------------------------------------❀")
    if whichdiscount in ["1", "2", "3"]:
        print(f"| Discount applied: {typeofdiscounts[whichdiscount][0]:<72}  |")
    
    print("❀--------------------------------------------------------------------------------------------❀")
    print(f"| {"YOUR CART (After discount applied):":<30} ${New_Cart:<54.2f} |")
    print("❀--------------------------------------------------------------------------------------------❀")


def paymentmethod():
    global programrunning
    print("❀--------------------------------------------------------------------------------------------❀ \n"
          "|                               HOW WOULD YOU LIKE TO PAY?                                    | \n"
          "❀--------------------------------------------------------------------------------------------❀ ")
    paymenttypes = {
        "1":["PAYNOW"],
        "2":["CASH"],
        "3":["NETS"],
        "4":["CREDIT CARD"],
    }


    for key,value in paymenttypes.items():
        print(f"| {key:<34} {value[0]:<57}|")
    
    print("❀--------------------------------------------------------------------------------------------❀")
    print(f"YOUR TOTAL(Before Discount):   ${Cart:<62.2f}|")
    print(f"YOUR CART (After discount applied): ${New_Cart:<57.2f}|")
    print("❀--------------------------------------------------------------------------------------------❀")

    howtopay = input("Choose option [1/2/3/4]: ")

    while howtopay not in ["1", "2", "3", "4"]:
        print("Invalid input. Please try again.")
        howtopay = input("Choose option [1/2/3/4]: ")

    if howtopay == "1":
        print("Our Paynow QR code")
        print("⡏⣭⡍⡇⢖⠃⣘⠇⢸⢩⣭⢹\n"
              "⠧⠭⠥⠇⡏⡯⢳⡳⠸⠬⠭⠼\n"
              "⢟⠬⠶⢍⣐⡐⡛⠘⣞⡩⠈⠵\n"
              "⣠⢾⡽⣡⢥⠙⠝⣨⣙⣣⣓⠝\n"
              "⡖⣒⡒⡆⢳⣫⡣⢿⣐⣸⡧⠞\n"
              "⣇⣛⣃⡇⡭⠬⠞⣢⢆⡛⠝⣐")
        print("Transaction Processing.....................")
       
        print("Transaction Approved! ✅")


    elif howtopay == "2":
        print("Please pay via at cashier")


    else:
        print("Please pay via the card terminal")
        print("Transaction Processing.....................")
        print("Transaction Approved! ✅")


    receipt()
    print("THANK YOU FOR PATRONISING BAKAR AND PENYET HEAVEN. ENJOY YOUR MEAL! ⸜(｡ ˃ ᵕ ˂ )⸝♡")

    programrunning = False

    return True

# in case have issues remove the parameter in this function:
def editcart(skip_first_prompt = False):
    global Cart,setsBakarmenu,setsPenyetmenu
    first = True
    while True:
        if not (first and skip_first_prompt):
            displaycart()
            confirmcartqns = input("To proceed to pay,press [y]. To edit cart,press [n]: ").lower()
        
        else:
            confirmcartqns = "n"

        first = False

        if confirmcartqns == "n":
            print("❀--------------------------------------------------------------------------------------------❀ \n"
                  "|                                      CART EDIT OPTIONS                                      | \n"
                  "❀--------------------------------------------------------------------------------------------❀ \n"
                  "|                                     1) ADD SETS/ADD-ONS                                     | \n"
                  "|                                     2) REMOVE SETS/ADD-ONS                                  | \n"
                  "|                                     3) CHANGE QUANTITY                                      | \n"
                  "|                                     4) BACK TO VIEW CART                                    | \n"
                  "❀--------------------------------------------------------------------------------------------❀"
                  )
            print(f"CART: ${Cart:.2f}")
            print("❀--------------------------------------------------------------------------------------------❀")
            whichtoedit = input("SELECT CART EDIT OPTION [1/2/3/4]")

            while whichtoedit not in ["1", "2", "3", "4"]:

                print("Invalid input. Please try again.")
                whichtoedit = input("SELECT CART EDIT OPTION [1/2/3/4]")

            if whichtoedit == "1":
                # return False
                print("❀--------------------------------------------------------------------------------------------❀ \n"
                      "|                                  WHAT WOULD YOU LIKE TO ADD?                                | \n"
                      "❀--------------------------------------------------------------------------------------------❀ \n"
                      "|                                     1) SETS                                                 | \n"
                      "|                                     2) ADD-ONS                                              | \n"
                      "❀--------------------------------------------------------------------------------------------❀")
                addchoice = input("CHOOSE OPTION [1/2]: ")
                while addchoice not in ["1", "2"]:
                    print("Invalid input. Please try again.")
                    addchoice = input("CHOOSE OPTION [1/2]: ")

                if addchoice == "1":
                    chosenset = set_mainmenu()
                    while chosenset not in ["1", "2", "3"]:
                        print("Invalid Option, please choose again.")
                        chosenset = set_mainmenu()
                    if chosenset == "3":
                        return None
                    if chosenset == "1":
                        setsBakarmenu, chooseBakarset = display_BakarMenu()
                        while chooseBakarset not in ["01", "02", "03", "04", "E"]:
                            print("Invalid Option, please choose again.")
                            setsBakarmenu, chooseBakarset = display_BakarMenu()
                        if chooseBakarset in ["01", "02", "03", "04"]:
                            Cart = order_set(setsBakarmenu, chooseBakarset)
                        elif chooseBakarset == "E":
                            return None
                        
                    elif chosenset == "2":
                        setsPenyetmenu, choosePenyetset = display_PenyetMenu()
                        while choosePenyetset not in ["05", "06", "07", "08", "E"]:
                            print("Invalid Option, please choose again.")
                            setsPenyetmenu, choosePenyetset = display_PenyetMenu()
                        if choosePenyetset in ["05", "06", "07", "08"]:
                            Cart = order_set(setsPenyetmenu, choosePenyetset)
                        elif choosePenyetset == "E":
                            return None

                elif addchoice == "2":
                    chosenadd_on, add_onsopt = add_onsmenu()
                    while chosenadd_on not in ["A1", "A2", "A3", "A4", "A5", "A6", "E"]:
                        print("Invalid Option, please choose again.")
                        chosenadd_on, add_onsopt = add_onsmenu()
                    if chosenadd_on in ["A1", "A2", "A3", "A4", "A5", "A6"]:
                        Cart = order_addon(add_onsopt, chosenadd_on)
                    elif chosenadd_on == "E":
                        return None

                continue   # back to top of editcart's loop, shows the updated cart
            
                #  To add mmeng() instead? ....Ill need to reconsider


            elif whichtoedit == "2":
                print(
                    "❀--------------------------------------------------------------------------------------------❀ \n"
                    "|                                      WHICH TO REMOVE?                                       | \n"
                    "❀--------------------------------------------------------------------------------------------❀ \n"
                    "|                                     1) TO REMOVE SETS                                       | \n"
                    "|                                     2) TO REMOVE ADD-ONS                                    | \n"
                    "|                                     3) BACK TO CART                                         | \n"
                    "❀--------------------------------------------------------------------------------------------❀"
                    )
                edit = input("CHOOSE OPTION [1/2/3]: ")

                while edit not in ["1", "2", "3"]:
                    print("Invalid input. Please try again.")
                    edit = input("CHOOSE OPTION [1/2/3]: ")

                if edit == "1":

                    if not purchased_sets:
                        print("No sets in cart to remove.")
                        continue

                    print("SETS ORDERED:")

                    for n,s in enumerate(purchased_sets, start=1):
                        print(f"|{n}) {s['SET']}")
                    
    
                    idx = removewhichset = getvalidindex("Enter the set to remove [enter the index number shown above only]: ", len(purchased_sets))

                    Cart -= round(purchased_sets[idx - 1]["COST"], 2)
                    purchased_sets.pop(idx - 1)
                    print("SET REMOVED")
                    #continue

                    #if removewhichset == "E":
                       # continue

                if edit == "2":
                    if not purchased_addons:
                        print("No add-ons in cart to remove.")
                        continue

                    print("ADD-ONS ORDERED:")
                    for n, a in enumerate(purchased_addons, start=1):
                        print(f"|{n}) {a['ADD-ON']}")
                    
                    idx = removewhichadd_on = getvalidindex("Enter the add-on to remove [enter the index number shown above only]: ", len(purchased_addons))

                    

                    Cart -= round(purchased_addons[idx - 1]["COST"], 2)
                    purchased_addons.pop(idx - 1)
                    print("ADD-ON REMOVED")
                    #continue

                if edit == "3":
                    #displaycart()
                    #confirmcartqns = input("To proceed to pay,press [y]. To edit cart,press [n]: ").lower()
                    continue


            elif whichtoedit == "3":
                print(
                    "❀--------------------------------------------------------------------------------------------❀ \n"
                    "|                                      WHICH QUANTITY TO CHANGE?                              | \n"
                    "❀--------------------------------------------------------------------------------------------❀ \n"
                    "|                                     1) SETS                                                 | \n"
                    "|                                     2) ADD-ONS                                              | \n"
                    "❀--------------------------------------------------------------------------------------------❀"
                    )
                setsoradd_onquantity = input("CHOOSE OPTION [1/2]: ")

                while setsoradd_onquantity not in ["1", "2"]:
                    print("Invalid input. Please try again.")
                    setsoradd_onquantity = input("CHOOSE OPTION [1/2]: ")

                if setsoradd_onquantity == "1":
                    if not purchased_sets:
                        print("No sets in cart to change quantity.")
                        continue
                    
                    print("SETS ORDERED:")
                    for n, s in enumerate(purchased_sets, start=1):
                        print(f"|{n}) {s['SET']} {s['QUANTITY']}")
                      
                    idx = changesetquantity = getvalidindex("Enter the set you want to change quantity [enter the index number shown above only]: ", len(purchased_sets))
                    # purchased_sets.remove({"QUANTITY":changesetquantity})

                    newsetquantity = getvalidint("Enter the new quantity: ",min_value=1)
                    thingset = purchased_sets[idx-1]
                    Cart -= round(thingset["COST"], 2)
                    #oldcost = thingset["COST"] / thingset["QUANTITY"]
                    newcost = round(thingset["PRICE"] * newsetquantity, 2)
                    Cart += newcost
                    thingset["COST"] = newcost
                    thingset["QUANTITY"] = newsetquantity
                    print("SET QUANTITY CHANGED, COST UPDATED")
                    #continue
                
            


                if setsoradd_onquantity == "2":
                    if not purchased_addons:
                        print("No add-ons in cart to change quantity.")
                        continue

                    print("ADD-ONS ORDERED:")
                    for n, a in enumerate(purchased_addons, start=1):
                        print(f"|{n}) {a['ADD-ON']} {a['QUANTITY']}")

                    idx = changeadd_onquantity = getvalidindex("Enter the add-on you want to change quantity [enter the index number shown above only]: ", len(purchased_addons))
                    newsaddonquantity = getvalidint("Enter the new quantity: ",min_value=1)
                    thingaddon = purchased_addons[idx-1]
                    Cart -= round(thingaddon["COST"], 2)
                    #oldcost = thingaddon["COST"] / thingaddon["QUANTITY"]
                    newcost = round(thingaddon["PRICE"] * newsaddonquantity, 2)
                    Cart += round(newcost, 2)
                    thingaddon["COST"] = newcost
                    thingaddon["QUANTITY"] = newsaddonquantity
                    print("ADD-ON QUANTITY CHANGED, COST UPDATED")
                    #continue

            elif whichtoedit == "4":
                continue
                #break

        if confirmcartqns == "y":
            global New_Cart
            if not purchased_sets and not purchased_addons:
                 print("Your cart is empty. Please add items to your cart before proceeding to checkout.")
                 return False
            #actionaftercart()
            New_Cart = checkfordiscounts(New_Cart)
            return paymentmethod()
            break
        
def checkout():
    global New_Cart

    if not purchased_sets and not purchased_addons:
        print("Your cart is empty. Please add items to your cart before proceeding to checkout.")
        return False
    
    print("❀--------------------------------------------------------------------------------------------❀ \n"
          "|                                        YOUR ORDER                                           | \n"
          "❀--------------------------------------------------------------------------------------------❀ \n")
    displaycart()
    #checkfordiscounts(New_Cart)
    #displaycart()

    checkcart = input("Select [y] to confirm all items for payment. To make any changes to cart, select [n]: ").lower()
   

    while checkcart not in ["y", "n"]:
        print("Invalid input. Please try again.")
        displaycart()
        checkcart = input("Select [y] to confirm all items for payment. To make any changes to cart, select [n]: ")

    if checkcart == "n":
        return editcart(skip_first_prompt=True)

    if checkcart == "y":

        New_Cart = checkfordiscounts(New_Cart)

        #return paymentmethod()

       # print("+---------------------------------------------------------------------------------------------+ \n"
       #       "|                                        YOUR ORDER                                           | \n"
        #      "+---------------------------------------------------------------------------------------------+ \n")
       # displaycart()
       # if whichdiscount in ["1", "2","3"]:
       #     print(f"Discount applied: {typeofdiscounts[whichdiscount][0]}")

        #print(f"YOUR CART (After discount applied): ${New_Cart:.2f}")

    return paymentmethod()

def checkoutphase():
    global programrunning
    
    #if not checkout():
     #   paymentmethod()
    
    if checkout() == True:
        programrunning = False

    #programrunning = False
    

while programrunning:
    #if lang == "1":
        #mainmenu = mmeng()
    choice = mmeng()
        
    while choice not in ["1", "2", "3", "4"]:
        print("Invalid Option, please choose again.")
        choice =mmeng()

    if choice == "1":
        chosenset = set_mainmenu()

        while chosenset not in ["1", "2", "3"]:
            print("Invalid Option, please choose again.")
            chosenset = set_mainmenu()



        if chosenset == "1":
            setsBakarmenu, chooseBakarset = display_BakarMenu()

            while chooseBakarset not in ["01", "02", "03", "04","E"]:
                print("Invalid Option, please choose again.")
                setsBakarmenu, chooseBakarset = display_BakarMenu()

            if chooseBakarset in ["01","02","03","04"]:
                Cart = order_set(setsBakarmenu, chooseBakarset)
                choicemoveon = move_on()

                while choicemoveon not in ["A", "B", "C"]:
                    print("Invalid Option.Please Try again.")
                    choicemoveon = move_on()

                if choicemoveon == "A":
                    
                    continue
                  
                elif choicemoveon == "C":
                    checkoutphase()
                     
                      

                elif choicemoveon == "B":
                     if editcart() == True:
                        programrunning = False
                     else:
                         continue
                     
                    #programrunning = False
                      # To add display cart function here?? - to check on this and reconsider this option.....
                      #actionaftercart()
                     # wanttocontinueaction = input("CHOOSE OPTION [1/2/3/4]: ")

                      #while wanttocontinueaction not in ["1", "2", "3", "4"]:
                       #   print("Invalid Option, please choose again.")
                        #  actionaftercart()
                         # wanttocontinueaction = input("CHOSE OPTION [1/2/3/4]: ")

                      #if wanttocontinueaction == "1":
                       #   editcart()

                      #if wanttocontinueaction == "2":
                       #   continue

                      #if wanttocontinueaction == "3":
                          # checkfordiscounts()
                       #   checkout()

                      # need to code for option 4
                      #if wanttocontinueaction == "4":
                       #   break



                  

            if chooseBakarset == "E":
                continue


        if chosenset == "2":
            setsPenyetmenu,choosePenyetset = display_PenyetMenu()

            while choosePenyetset not in ["05","06","07","08","E"]:
                print("Invalid Option, please choose again.")
                setsPenyetmenu, choosePenyetset = display_PenyetMenu()

            if choosePenyetset in ["05", "06", "07", "08"]:
                Cart = order_set(setsPenyetmenu, choosePenyetset)
                   
                  
                choicemoveon = move_on()

                while choicemoveon not in ["A", "B", "C"]:
                    print("Invalid Option.Please Try again.")
                    choicemoveon = move_on()

                if choicemoveon == "A":
                       
                    continue

                elif choicemoveon == "C":
                    checkoutphase()
                        #checkfordiscounts(New_Cart)
                        #paymentmethod()
                        #receipt()


                elif choicemoveon == "B":
                    if editcart() == True:
                        programrunning = False
                    else:
                        continue
                    
                        
                    programrunning = False
                        # To add display cart function here?? - to check on this and reconsider this option.....
                        #actionaftercart()
                        #wanttocontinueaction = input("CHOOSE OPTION [1/2/3/4]: ")

                        #while wanttocontinueaction not in ["1", "2", "3", "4"]:
                         #   print("Invalid Option, please choose again.")
                          #  actionaftercart()
                           # wanttocontinueaction = input("CHOSE OPTION [1/2/3/4]: ")

                        #if wanttocontinueaction == "1":
                         #   editcart()

                        #if wanttocontinueaction == "2":
                         #   continue

                        #if wanttocontinueaction == "3":
                            # checkfordiscounts()
                         #   checkout()

                        # need to code for option 4
                        #if wanttocontinueaction == "4":
                         #   break


                    



            if choosePenyetset == "E":
                continue




    if choice == "2":
        chosenadd_on,add_onsopt =add_onsmenu()

        while chosenadd_on not in ["A1", "A2", "A3", "A4","A5","A6","E"]:
            print("Invalid Option, please choose again.")
            chosenadd_on, add_onsopt = add_onsmenu()

        if chosenadd_on in ["A1","A2","A3","A4","A5","A6"]:
            Cart = order_addon(add_onsopt, chosenadd_on)
                
            choicemoveon = move_on()

            while choicemoveon not in ["A", "B", "C"]:
                print("Invalid Option.Please Try again.")
                choicemoveon = move_on()

            if choicemoveon == "A":
            
                continue

            elif choicemoveon == "B":
                if editcart() == True:
                    programrunning = False
                else:
                    continue
                
                    # To add display cart function here?? - to check on this and reconsider this option.....
                    #actionaftercart()
                    #wanttocontinueaction = input("CHOOSE OPTION [1/2/3/4]: ")

                    #while wanttocontinueaction not in ["1", "2", "3", "4"]:
                     #   print("Invalid Option, please choose again.")
                      #  actionaftercart()
                       # wanttocontinueaction = input("CHOSE OPTION [1/2/3/4]: ")

                    #if wanttocontinueaction == "1":
                     #   editcart()

                    #if wanttocontinueaction == "2":
                     #   continue

                    #if wanttocontinueaction == "3":
                        # checkfordiscounts()
                     #   checkout()

                    # need to code for option 4
                    #if wanttocontinueaction == "4":
                     #   break

                    #checkout()
                    #paymentmethod()

            elif choicemoveon == "C":
                checkoutphase()
                    #checkfordiscounts(New_Cart)
                    #paymentmethod()
                    #receipt()

                

        if chosenadd_on == "E":
            continue

    if choice == "3":
        print("Have a nice day ahead! (ˊ•͈ ◡ •͈ˋ)")
        break

    if choice == "4":

        if not purchased_sets and not purchased_addons:
            print("Your cart is empty. Please add items to your cart before proceeding to checkout.")
            #return False
            continue
        if editcart() == True:
            programrunning = False
        else: 
            actionaftercart()
            wanttocontinueaction = input("CHOOSE OPTION [1/2/3/4]: ")

            while wanttocontinueaction not in ["1", "2", "3", "4"]:
                print("Invalid Option, please choose again.")
                actionaftercart()
                wanttocontinueaction = input("CHOSE OPTION [1/2/3/4]: ")

            if wanttocontinueaction == "1":
                if editcart():
                    programrunning = False

            if wanttocontinueaction == "2":
                continue


            if wanttocontinueaction == "3":
                checkoutphase()
                    #checkfordiscounts(New_Cart)
                # paymentmethod()
                    #receipt()

                # need to code for option 4
            if wanttocontinueaction == "4":
                print("Order Cancelled. Have a nice day ahead! (ˊ•͈ ◡ •͈ˋ)")
                break
            
            #displaycart()
            #editcart()
            #To add display cart function here?? - to check on this and reconsider this option.....
            

         
            #checkfordiscounts(New_Cart)
            #paymentmethod()
            #receipt()
