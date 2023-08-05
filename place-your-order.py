print("Welcome to Sheikh Kabab")

order = []
bill = []

def billing(order, bill):
      for a in order:
            if a == "KungPaoChicken":
                  bill.append(12)
            elif a == "ChowMein":
                  bill.append(7.37)
            elif a == "ChineseHotPot":
                  bill.append(9.5)
            elif a == "SpringRolls":
                  bill.append(5)
            elif a == "ChickenManchurian":
                  bill.append(6.8)
            elif a == "Rice":
                  bill.append(3)
            elif a == "ZingerBurger":
                  bill.append(2.25)
            elif a == "BeefBurger":
                  bill.append(4.37)
            elif a == "ChickenTikkaPizza":
                  bill.append(5)
            elif a == "ChickenShawarma":
                  bill.append(2.5)
            elif a == "ChickenParathaRoll":
                  bill.append(2.7)
            elif a == "ChickenMakhniHandi":
                  bill.append(8.5)
            elif a == "ChickenKarahi":
                  bill.append(8.5)
            elif a == "MuttonKarahi":
                  bill.append(11)
            elif a == "ChickenBiryani":
                  bill.append(3.25)
            elif a == "Naan":
                  bill.append(0.4)
            elif a == "ChickenSeekhKabab":
                  bill.append(2.5)
            elif a == "BeefKabab":
                  bill.append(3.5)
            elif a == "ChickenTikkaBoti":
                  bill.append(4)
            elif a == "ChickenMalaiBoti":
                  bill.append(3)
            elif a == "CocaCola":
                  bill.append(1)
            elif a == "Fanta":
                  bill.append(1)
            elif a == "Pepsi":
                  bill.append(1)
            elif a == "Sprite":
                  bill.append(1)
            elif a == "SevenUp":
                  bill.append(1)
            elif a == "Milo":
                  bill.append(1)
            elif a == "MangoSmoothie":
                  bill.append(2)
            elif a == "MilkShakes":
                  bill.append(2)
            elif a == "Juices":
                  bill.append(1.5)
      totalBill = sum(bill)
      print(f"Your Order Includes {order}")
      print(f"Your Total Bill is '{round(totalBill,2)}'$")
      moneystr = input("How much money do you have?: ")
      money = int(moneystr)
      if money < totalBill:
            print("Sorry you don't have enough money for this order please comeback later. Thank You!!")
            exit()
      else:
            change = money - totalBill
            print(f"This is your change '{change}'$ \n Thanks a lot for ordering from SHEIKH KABAB, Hope You like our Food and also hope to see you again")
            exit()
      exit()
def drinks(order):
      print("Coca Cola:$1  "
            "Fanta:$1  "
            "Pepsi:$1  "
            "Sprite:$1  "
            "Seven Up:$1  "
            "Milo:$1  "
            "Mango Smoothie:$2  "
            "Milk Shakes:$2  "
            "Juices:$1.5  ")
      order1 = input("What Would you like to drink: ").title().replace(" ", "")
      order.append(order1)
      order2 = input("Would you like to order anything else (yes or no)?: ").title()
      if order2 == "Yes":
            menu(order)
      billing(order, bill)

def menu(order):
      print("Chinese, Fast Food, Traditional, Bar-B-Q")
      typeOfFood = input("What type of food would You Like To Eat: ")
      if typeOfFood.title() == "Chinese":
            print("Kung Pao Chicken: $12.25\n"
                  "Chow Mein: $7.37\n"
                  "Chinese Hot Pot: $9.5\n"
                  "Spring Rolls: $5\n"
                  "Chicken Manchurian: $6.8")
            order1 = input("What would you like to order: ").title().replace(" ", "")
            print(order1)
            if order1 == "KungPaoChicken" or order1 == "ChowMein" or order1 == "ChineseHotPot" or order1 == "SpringRolls" or order1 == "ChickenManchurian":
                  rice = input("Would you like to order rice which will cost $3 (yes or no)?: ").title()
                  if rice == "Yes":
                        order.append("Rice")
                  order.append(order1)
                  order1 = input("Would you like to order anything else (yes or no)?: ").title()
                  if order1 == "Yes":
                        menu(order)
                  else:
                        print()
                  drinks(order)
            else:
                  print("Please Check your spellings and try again")
                  isContinue2 = input("Do you want to try again (yes or no): ").title()
                  if isContinue2 == "Yes":
                        menu(order)
                  else:
                        exit()

      elif typeOfFood.title() == "Fast Food":
            print("Zinger Burger: $2.25\n"
                  "Beef Burger: $4.37\n"
                  "Chicken Tikka Pizza: $5\n"
                  "Chicken Shawarma: $2.5\n"
                  "Chicken Paratha Roll: $2.7")
            order1 = input("What would you like to order: ").title().replace(" ", "")
            if order1 == "ZingerBurger" or order1 == "BeefBurger" or order1 == "ChickenTikkaPizza" or order1 == "ChickenShawarma" or order1 == "ChickenParathaRoll":
                  fries = input("Would You Like some Fries for just $1.25 (yes or no): ").title()
                  if fries == "Yes":
                        order.append("Fries")
                  order.append(order1)
                  order1 = input("Would you like to order anything else (yes or no)?: ").title()
                  if order1 == "Yes":
                        menu(order)
                  else:
                        print()
                  drinks(order)
            else:
                  print("Please Check your spellings and try again")
                  isContinue2 = input("Do you want to try again (yes or no): ").title()
                  if isContinue2 == "Yes":
                        menu(order)
                  else:
                        exit()

      elif typeOfFood.title() == "Traditional":
            print("Chicken Makhni Handi: $8.5\n"
                  "Chicken Karahi: $8.5\n"
                  "Mutton Karahi: $11\n"
                  "Chicken Biryani: $3.25\n"
                  "Naan: $0.4")
            order1 = input("What would you like to order: ").title().replace(" ", "")
            if order1 == "ChickenMakhniHandi" or order1 == "ChickenKarahi" or order1 == "MuttonKarahi" or order1 == "ChickenBiryani":
                  Naans = input("Would You Like some Naans for just $0.4 (yes or no): ").title()
                  if Naans == "Yes":
                        order.append("Naans")
                  order.append(order1)
                  order1 = input("Would you like to order anything else (yes or no)?: ").title()
                  if order1 == "Yes":
                        menu(order)
                  else:
                        print()
                  drinks(order)
            else:
                  print("Please Check your spellings and try again")
                  isContinue2 = input("Do you want to try again (yes or no): ").title()
                  if isContinue2 == "Yes":
                        menu(order)
                  else:
                        exit()

      elif typeOfFood.title() == "Bar-B-Q":
            print("Chicken Seekh Kabab: $2.5\n"
                  "Beef Kabab: $3.5\n"
                  "Chicken Tikka Boti: $4\n"
                  "Chicken Malai Boti: $3\n"
                  "Naan: $0.4")
            order1 = input("What would you like to order: ").title().replace(" ", "")
            if order1 == "ChickenSeekhKabab" or order1 == "BeefKabab" or order1 == "ChickenTikkaBoti" or order1 == "ChickenMalaiBoti":
                  Naans = input("Would You Like some Naans for just $0.4 (yes or no): ").title()
                  if Naans == "Yes":
                        order.append("Naans")
                  order.append(order1)
                  order1 = input("Would you like to order anything else (yes or no)?: ").title()
                  if order1 == "Yes":
                        menu(order)
                  else:
                        print()
                  drinks(order)
            else:
                  print("Please Check your spellings and try again")
                  isContinue2 = input("Do you want to try again (yes or no): ").title()
                  if isContinue2 == "Yes":
                        menu(order)
                  else:
                        exit()

      else:
            print("incorrect input, Please check your spellings")
            isContinue1 = input("Do you want to try again (yes or no): ").title()
            if isContinue1 == "Yes":
                  menu(order)
            else:
                  exit()


menu(order)