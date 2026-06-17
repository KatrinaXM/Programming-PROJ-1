# Start of programme
# Self Note: To-settle alignment and decoration last - gna work on functionailty first
print("#" * 10, "Welcome to The Penyet and Bakar Lab!","#" * 10)
print(""
      "+---------------------------------------------------------------------------------------------+ \n"
      "|                             WELCOME TO THE PENYET AND BAKAR LAB!                            | \n"
      "+---------------------------------------------------------------------------------------------+ \n"
      "|                                     LANGUAGES AVALIABLE:                                    | \n"
      "|                                      1) ENGLISH                                             | \n"
      "|                                      2) CHINESE                                             | \n"
      "|                                      3) MALAY                                               | \n"
      "|                                      4) TAMIL                                               | \n"
      "+---------------------------------------------------------------------------------------------+ ")
lang = input("                    CHOOSE A LANGUAGE YOU WISH TO USE [1/2/3/4]:                         ")
print("+---------------------------------------------------------------------------------------------+ \n")

Cart = 0.00
Quantity = 0
New_Quantity = 0
ChosenFooditem = None
total = 0.00
choosenaddon = None
u_confirm = None
whichtoedit = None
purchased_sets = []
purchased_addons = []




# try adding cart inside as a param if there is any future issues
def mmeng():
    global Cart
    print(""
          "+---------------------------------------------------------------------------------------------+ \n"
          "|                                   PENYET AND BAKAR LAB                                      | \n"
          "+---------------------------------------------------------------------------------------------+ \n"
          "|                                         OPTIONS                                             | \n"
          "|                              [1] SETS                                                       | \n"
          "|                              [2] ADD-ONS                                                    | \n"
          "|                              [3] EXIT                                                       | \n"
          "|                              [4] VIEW/EDIT CART & CHECKOUT                                  | \n"
          "+---------------------------------------------------------------------------------------------+ ")
    print(f"CART:${Cart:.2f} ")
    print("+---------------------------------------------------------------------------------------------+ ")


    choice = input("Choose Option[1/2/3]: ")
    return choice

def set_mainmenu():
    global Cart
    print("+---------------------------------------------------------------------------------------------+ \n"
          "|                                  OUR SETS                                                   | \n"
          "+---------------------------------------------------------------------------------------------+ \n"
          "|                                [1] BAKAR SETS                                               | \n"
          "|                                [2] PENYET SETS                                              | \n"
          "|                                [3] RETURN TO MAIN MENU                                      | \n"
          "+---------------------------------------------------------------------------------------------+")
    print(f"CART: ${Cart:.2f}")
    print("+---------------------------------------------------------------------------------------------+")
    chosenset = input("Choose sets to view [1/2] or choose to return to main menu[3]: ")
    return chosenset

def add_onsmenu():
   global Cart
   print("+---------------------------------------------------------------------------------------------+ \n"
          "|                                  OUR ADD-ONS                                                | \n"
          "+---------------------------------------------------------------------------------------------+")
   add_onsopt = {
       "1" : ["Rice","...........................................................", 0.50],
       "2" : ["Egg","............................................................", 0.80],
       "3" : ["Chilli",".........................................................", 0.50],
       "4" : ["Fried/Grilled Dori Fish (Per Piece)","............................", 3.50],
       "5" : ["Fried/Grilled Chicken Leg Quarter (Per Piece)","..................",3.50],
       "6" : ["Fried Chicken Wing (1pc)",".......................................",1.50],
       "E":  ["Choose this option to", "return to main menu", "..........................."],
   }

   for key, value in add_onsopt.items():
       if key == "E":
           print(f"|   {key:<10} {value[0]} {value[1]} {value[2]:<36} |")

       elif key == "1":
           print(f"|   {key:<8} {value[0]:>6} {value[1]} ${value[2]:<13}|")

       elif key == "2":
           print(f"|   {key:<7} {value[0]:>6} {value[1]} ${value[2]:<13}|")

       elif key == "4":
           print(f"|   {key:<10} {value[0]:>6} {value[1]} ${value[2]:<13}|")

       elif key == "5":
           print(f"|   {key:<10} {value[0]:>6} {value[1]} ${value[2]:<13}|")
       elif key == "6":
           print(f"|   {key:<10} {value[0]:>6} {value[1]} ${value[2]:<13}|")
       else:
           print(f"|   {key:<10} {value[0]} {value[1]} ${value[2]:<13}|")


   print("+---------------------------------------------------------------------------------------------+")
   print(f"CART: ${Cart:.2f}")
   print("+---------------------------------------------------------------------------------------------+")
   chooseadd_on = input("Choose Option[1/2/3/4/5/6/E]: ")
   return chooseadd_on,add_onsopt

def display_BakarMenu():
    global Cart
    print(
        "+---------------------------------------------------------------------------------------------+ \n"
        "|                                  OUR BAKAR SETS                                             | \n"
        "+---------------------------------------------------------------------------------------------+")
    setsBakarmenu = {""
                     "1": ["Ayam Bakar Set (Grilled Chicken Set)", "....................",  5.80],
                     "2": ["Dori Bakar Set (Grilled Dori Set)", ".......................",  5.90],
                     "3": ["Ayam Bakar Set (Grilled Boneless Chicken Set)", "...........",  6.30],
                     "4": ["Gulai Ayam Set (Curry Chicken Whole Leg Set)", "............",  6.20],
                     "E": ["Choose this option to", "return to main menu", "...................."],
                     }

    for key, options in setsBakarmenu.items():
        if key == "E":
            print(f"|  {key:<8} {options[0]:^20} {options[1]:^0}  {options[2]:<37}  |")
        else:
            print(f"|  {key:<8} {options[0]:^20} {options[1]:^0}  ${options[2]:<20}  |")


    print("+---------------------------------------------------------------------------------------------+")
    print(f"CART: ${Cart:.2f}")
    print("+---------------------------------------------------------------------------------------------+ \n")
    chooseBakarset = input("Choose Option[1/2/3/4/E]: ")
    return setsBakarmenu, chooseBakarset




def display_PenyetMenu():
    global Cart
    print(
        "+---------------------------------------------------------------------------------------------+ \n"
        "|                                  OUR PENYET SETS                                            | \n"
        "+---------------------------------------------------------------------------------------------+")

    setsPenyetmenu = {
                      "5": ["Ayam Penyet Set (Fried Chicken Set)", ".....................",  5.80],
                      "6": ["Dori Penyet Set (Fried Chicken Set)", ".....................",  5.90],
                      "7": ["Ayam Penyet Set (Fried Boneless Chicken Set)", "............",  6.30],
                      "8": ["Ayam Penyet Set (Fried Chicken Wing Set)", "................",  5.80],
                      "E": ["Choose this option to", "return to main menu", "...................."],
                      }

    for key, options in setsPenyetmenu.items():
        if key == "E":
            print(f"|  {key:<8} {options[0]:^20} {options[1]:^0}  {options[2]:<37}  |")

        else:
            print(f"|  {key:<8} {options[0]:^20} {options[1]:^0}  ${options[2]:<20}  |")

    print("+---------------------------------------------------------------------------------------------+")
    print(f"CART: ${Cart:.2f}")
    print("+---------------------------------------------------------------------------------------------+ \n")
    choosePenyetset = input("Choose Option[5/6/7/8/E]: ")
    return setsPenyetmenu,choosePenyetset

def move_on():
    print(""
          "A)  Back to Main Menu \n" 
          "B)  View/Edit Cart \n"
          "C)  Go to Checkout\n"
           )

    choicemoveon = input("Choose Option[A/B/C]: ").upper()
    return choicemoveon




def confirm(Cart,total,Quantity):

    u_confirm = input("To confirm and continue, type [y]. To edit quantity, type [n]: ").lower()
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
        New_Quantity = int(input("Enter New Quantity: "))
        if chooseBakarset in setsBakarmenu.keys():
            total = float(setsBakarmenu[chooseBakarset][2]) * New_Quantity
            New_Cart = total
            Cart = New_Cart
            print("Item Quantity Changed to ", New_Quantity)
            print("Cart updated")
            print(f"CART: ${Cart:.2f}")
          #  purchased[len(purchased)]={ "Sets" : ChosenFooditem, "Add-ons" : choosenaddon,"Quantity" : New_Quantity,"Cost":total  }
    if ChosenFooditem is not None:
        purchased_sets.append({"SET":ChosenFooditem, "QUANTITY":New_Quantity,"COST":total})
    else:
        purchased_addons.append({"ADD-ON":choosenaddon,"QUANTITY":New_Quantity,"COST":total})

    return Cart,New_Quantity,total,choosenaddon,ChosenFooditem

def displaycart():
    print(
        "+---------------------------------------------------------------------------------------------+ \n"
        "|                                          CART                                               | \n"
        "+---------------------------------------------------------------------------------------------+")
    print(f"{"SETS"} {"QUANTITY":<20} {"COST":<20} ")
    print("+---------------------------------------------------------------------------------------------+")
    for i in purchased_sets:
        print(f"| {i["SET"]}  {i["QUANTITY"]}  ${i["COST"]} |")
    print("+---------------------------------------------------------------------------------------------+")
    print(f"{"ADD-ONS"} {"QUANTITY"} {"COST"} ")
    print("+---------------------------------------------------------------------------------------------+")
    for r in purchased_addons:
        print(f"| {r["ADD-ON"]}  {r["QUANTITY"]}  ${r["COST"]} |")
    print("+---------------------------------------------------------------------------------------------+")

def editcart():
    global Cart
    confirmcartqns = input("To proceed to pay,press [y]. To edit cart,press [n]: ").lower()

    if confirmcartqns == "n":
        whichtoedit = input("CART EDIT OPTIONS"
                            "1) ADD SETS/ADD-ONS"
                            "2) REMOVE SETS/ADD-ONS"
                            "3) CHANGE QUANTITY"
                            )

        if whichtoedit == "1":
            mmeng()

        elif whichtoedit == "2":
            edit = input("1) TO REMOVE SETS"
                         "2) TO REMOVE ADD-ONS"
                         )
            if edit == "1":
                print("SETS ORDERED:")
                for n in range(1,len(purchased_sets)+1):
                    for i in purchased_sets:
                        print(f"|{n}) {i["SET"]}")
                        n += 1
                removewhichset = input("Enter the set to remove [enter the index number shown above only]: ")
                purchased_sets.pop(int(removewhichset) - 1)
                print("SET REMOVED")

            if edit == "2":
                print("ADD-ONS ORDERED:")
                for n in range(1,len(purchased_addons)+1):
                    for i in purchased_addons:
                        print(f"|{n}) {i["ADD-ON"]}")
                        n += 1
                removewhichadd_on = input("Enter the add-on to remove [enter the index number shown above only]: ")
                purchased_addons.pop(int(removewhichadd_on) - 1)
                print("ADD-ON REMOVED")


        elif whichtoedit == "3":
            setsoradd_onquantity = input("WHICH QUANTITY TO CHANGE?"
                                         "1) SETS"
                                         "2) ADD-ONS"
                                         )
            if setsoradd_onquantity == "1":
                print("SETS ORDERED:")
                for n in range(1,len(purchased_sets)+1):
                    for i in purchased_sets:
                        print(f"|{n}) {i["SET"]} {i["QUANTITY"]}")
                        n += 1
                changesetquantity = int(input("Enter the which set's quantity to change[enter the index number shown above only]:  "))
                #purchased_sets.remove({"QUANTITY":changesetquantity})
                newsetquantity = int(input(f"Enter the new quantity: "))
                Cart -= purchased_sets[changesetquantity-1]["COST"]
                oldcost = purchased_sets[changesetquantity-1]["COST"] / purchased_sets[changesetquantity-1]["QUANTITY"]
                newcost  = oldcost * newsetquantity
                Cart += newcost
                purchased_sets[changesetquantity-1]["COST"] = newcost
                purchased_sets[changesetquantity-1]["QUANTITY"] = newsetquantity
                print("SET QUANTITY CHANGED, COST UPDATED")

            if setsoradd_onquantity == "2":
                print("ADD-ONS ORDERED:")
                for n in range(1, len(purchased_addons) + 1):
                    for i in purchased_addons:
                        print(f"|{n}) {i["ADD-ON"]} {i["QUANTITY"]}")
                        n += 1
                changeadd_onquantity = int( input("Enter the which set's quantity to change[enter the index number shown above only]:  "))
                newsaddonquantity = int(input(f"Enter the new quantity: "))
                Cart -= purchased_addons[changeadd_onquantity - 1]["COST"]
                oldcost = purchased_addons[changeadd_onquantity - 1]["COST"] / purchased_sets[changeadd_onquantity - 1]["QUANTITY"]
                newcost = oldcost * newsaddonquantity
                Cart += newcost
                purchased_addons[changeadd_onquantity - 1]["COST"] = newcost
                purchased_sets[changeadd_onquantity - 1]["QUANTITY"] = newsaddonquantity
                print("ADD-ON QUANTITY CHANGED, COST UPDATED")


while True:
    if lang == "1":
        mainmenu = mmeng()

        if mainmenu == "1":
            chosenset = set_mainmenu()

            if chosenset == "1":
                setsBakarmenu, chooseBakarset = display_BakarMenu()

                while chooseBakarset not in ["1", "2", "3", "4","E"]:
                    print("Invalid Option, please choose again.")
                    setsBakarmenu, chooseBakarset = display_BakarMenu()

                if chooseBakarset in ["1","2","3","4"]:
                  ChosenFooditem =  setsBakarmenu[chooseBakarset][0]
                  print("Option Chosen: ", ChosenFooditem)
                  price = float(setsBakarmenu[chooseBakarset][2])
                  Quantity = int(input("Please indicate Quantity:  "))
                  total = price * Quantity
                  print(f"|  {"Item":<36} {"Quantity":^10} {"Cost":>11}  |")
                  print(f"|  {ChosenFooditem:<10} {Quantity:^10} {total:>10}   |")
                  Cart,New_Quantity, total,choosenaddon,ChosenFooditem = confirm(Cart,total,Quantity)
                  choicemoveon = move_on()
                  if choicemoveon == "A":
                      #set_mainmenu()
                      continue

                  #elif choicemoveon == "B":
                      #continue
                      # elif choicemoveon == "C":
                      # Need to display add-ons menu
                      # elif choicemoveon == "D":
                      # Need to write code to view Cart
                      # elif choicemoveon == "E":
                      # Need to write code for checkout phase
                  while choicemoveon not in ["A", "B", "C", "D", "E"]:
                      print("Invalid Option.Please Try again.")
                      choicemoveon = move_on()


                if chooseBakarset == "E":
                    mmeng()


            if chosenset == "2":
                setsPenyetmenu,choosePenyetset = display_PenyetMenu()

                while choosePenyetset not in ["5","6","7","8","E"]:
                    print("Invalid Option, please choose again.")
                    setsPenyetmenu, choosePenyetset = display_PenyetMenu()

                if choosePenyetset in ["5", "6", "7", "8"]:
                    ChosenFooditem = setsPenyetmenu[choosePenyetset][0]
                    print("Option Chosen: ", ChosenFooditem)
                    price = float(setsPenyetmenu[choosePenyetset][2])
                    Quantity = int(input("Please indicate Quantity:  "))
                    total = price * Quantity
                    print(f"|  {"Item":<36} {"Quantity":<6} {"Cost":>11}  |")
                    print(f"|  {ChosenFooditem:<10} {Quantity:^10} {total:>10}   |")
                    Cart, New_Quantity, total,choosenaddon,ChosenFooditem= confirm(Cart, total,Quantity)
                    choicemoveon = move_on()
                    if choicemoveon == "A":
                        #set_mainmenu()
                        continue

                    elif choicemoveon == "B":
                        continue
                        # elif choicemoveon == "C":
                        # Need to display add-ons menu
                        # elif choicemoveon == "D":
                        # Need to write code to view Cart
                        # elif choicemoveon == "E":
                        # Need to write code for checkout phase
                    while choicemoveon not in ["A", "B", "C", "D", "E"]:
                        print("Invalid Option.Please Try again.")
                        choicemoveon = move_on()

                if choosePenyetset == "E":
                    mmeng()




        if mainmenu == "2":
            chooseadd_on,add_onsopt =add_onsmenu()

            while chooseadd_on not in ["1", "2", "3", "4","5","6","E"]:
                print("Invalid Option, please choose again.")
                chooseadd_on, add_onsopt = add_onsmenu()

            if chooseadd_on in ["1","2","3","4","5","6"]:
                choosenaddon = add_onsopt[chooseadd_on][0]
                ChosenFooditem = None
                print("Option Chosen: ", choosenaddon)
                Quantity = int(input("Please indicate Quantity:  "))
                price = add_onsopt[chooseadd_on][2]
                total = Quantity * price
                print(f"|  {"Add-on":<36} {"Quantity":^10} {"Cost":>11}  |")
                print(f"|  {choosenaddon:<10} {Quantity:>32} {total:>14}   |")
                Cart, New_Quantity, total,choosenaddon,ChosenFooditem = confirm(Cart, total,Quantity)
                choicemoveon = move_on()
                if choicemoveon == "A":
                    # set_mainmenu()
                    continue

                elif choicemoveon == "B":
                    continue
                    # elif choicemoveon == "C":
                    # Need to display add-ons menu
                    # elif choicemoveon == "D":
                    # Need to write code to view Cart
                    # elif choicemoveon == "E":
                    # Need to write code for checkout phase

                while choicemoveon not in ["A", "B", "C", "D", "E"]:
                    print("Invalid Option.Please Try again.")
                    choicemoveon = move_on()

            if chooseadd_on == "E":
                mmeng()




        if mainmenu == "3":
            print("Have a nice day ahead!")
            break

        if mainmenu == "4":
            displaycart()
            wanttocontinueaction = input("What would you like to do now? "
                                         "1) VIEW/EDIT CART"
                                        "2) RETURN TO MAIN MENU"
                                       "3) PROCEED TO CHECKOUT"
                                      "4) CHECKOUT")

            if wanttocontinueaction == "1":
                displaycart()
                editcart()

            if wanttocontinueaction == "2":
                mmeng()

            # need to code for option 3

            # need to code for option 4




















