import time

print("Welcome to Sheikh Kabab")
print("Chinese, Fast Food, Traditional, Bar-B-Q")


KungPaoChicken = 12
ChowMein = 7.37
ChineseHotPot = 9.5
SpringRolls = 5
ChickenManchurian = 6.8
Rice = 3
ZingerBurger = 2.25
BeefBurger = 4.37
ChickenTikkaPizza = 5
ChickenShawarma = 2.5
ChickenParathaRoll = 2.7
ChickenMakhniHandi = 8.5
ChickenKarahi = 8.5
MuttonKarahi = 11
ChickenBiryani = 3.25
Naan = 0.4
ChickenSeekhKabab = 2.5
BeefKabab = 3.5
ChickenTikkaBoti = 4
ChickenMalaiBoti = 3

def billing(order, bill):
      print(f"Your total bill is '{bill}' and your order is '{order}'")


def chineseFood(order, rice):
      if order == "Kung Pao Chicken":
            bill = 12.25
            billing(order, bill)
      elif order == "Chow Mein":
            bill = 7.37
            billing(order, bill)
      elif order == "Chinese Hot Pot":
            bill = 9.5
            billing(order, bill)
      elif order == "Spring Rolls":
            bill = 5
            billing(order, bill)
      elif order == "Chicken Manchurian":
            bill = 6.8
            billing(order, bill)
      elif rice == "Yes":
            riceprice = 3
            billing(order, riceprice)
      else:
            print("incorrect input, Please check your spellings")
            isContinue2 = input("Do you want to try again (yes or no): ").title()
            if isContinue2 == "Yes":
                  chineseFood(order, rice)
            else:
                  exit()

def fastFood(order, fries):
      if order == "Zinger Burger":
            bill = 2.25
            billing(order, bill)
      elif fries == "Yes":
            friesPrice = 1.25
            billing(order, friesPrice,)
      elif order == "Beef Burger":
            bill = 4.37
            billing(order, bill)
      elif order == "Chicken Tikka Pizza":
            bill = 5
            billing(order, bill)
      elif order == "Chicken Shawarma":
            bill = 2.5
            billing(order, bill)
      elif order == "Chicken Paratha Roll":
            bill = 2.7
            billing(order, bill)
      else:
            print("incorrect input, Please check your spellings")
            isContinue3 = input("Do you want to try again (yes or no): ").title()
            if isContinue3 == "Yes":
                  fastFood(order, fries)
            else:
                  exit()

def traditionalFood(order, naans):
      if order == "Chicken Makhni Handi":
            bill = 8.5
            billing(order, bill)
      elif naans.isnumeric() == "true" and naans > 0:
            naanPrice = 0.4
            billing(order, naanPrice)
      elif order == "Chicken Karahi":
            bill = 8.5
            billing(order, bill)
      elif order == "Mutton Karahi":
            bill = 11
            billing(order, bill)
      elif order == "Chicken Biryani":
            bill = 3.25
            billing(order, bill)
      else:
            print("incorrect input, Please check your spellings or make sure you have entered correct number of naans")
            isContinue4 = input("Do you want to try again (yes or no): ").title()
            if isContinue4 == "Yes":
                  traditionalFood(order, naans)
            else:
                  exit()

def bbqFood(order, naans):
      if order == "Chicken Seekh Kabab":
            bill = 2.5
            billing(order, bill)
      elif naans.isnumeric() == "true" and naans > 0:
            naanPrice = 0.4
            billing(order, naanPrice)
      elif order == "Beef Kabab":
            bill = 3.5
            billing(order, bill)
      elif order == "Chicken Tikka Boti":
            bill = 4
            billing(order, bill)
      elif order == "Chicken Malai Boti":
            bill = 3
            billing(order, bill)
      else:
            print("incorrect input, Please check your spellings or make sure you have entered correct number of naans")
            isContinue5 = input("Do you want to try again (yes or no): ").title()
            if isContinue5 == "Yes":
                  bbqFood(order, naans)
            else:
                  exit()

def orderAgain():
      isorderagain = input("would you like to order anything else: ").title()


def menu():
      typeOfFood = input("What type of food would You Like To Eat: ")
      if typeOfFood.title() == "Chinese":
            print("Kung Pao Chicken: $12.25\n"
                  "Chow Mein: $7.37\n"
                  "Chinese Hot Pot: $9.5\n"
                  "Spring Rolls: $5\n"
                  "Chicken Manchurian: $6.8\n"
                  "Rice: $3")
            order = input("What would you like to order: ").title().replace(" ", "")
            chineseFood(order)

      elif typeOfFood.title() == "Fast Food":
            print("Zinger Burger: $2.25\n"
                  "Beef Burger: $4.37\n"
                  "Chicken Tikka Pizza: $5\n"
                  "Chicken Shawarma: $2.5\n"
                  "Chicken Paratha Roll: $2.7")
            order = input("What would you like to order: ").title()
            fries = input("Would You Like some Fries for just $1.25 (yes or no): ").title()
            fastFood(order, fries)
      elif typeOfFood.title() == "Traditional":
            print("Chicken Makhni Handi: $8.5\n"
                  "Chicken Karahi: $8.5\n"
                  "Mutton Karahi: $11\n"
                  "Chicken Biryani: $3.25\n"
                  "Naan: $0.4")
            order = input("What would you like to order: ").title()
            naans = input("If yes then how many naans would you like: ")
            traditionalFood(order, naans)
      elif typeOfFood.title() == "Bar-B-Q":
            print("Chicken Seekh Kabab: $2.5\n"
                  "Beef Kabab: $3.5\n"
                  "Chicken Tikka Boti: $4\n"
                  "Chicken Malai Boti: $3\n"
                  "Naan: $0.4")
            order = input("What would you like to order: ").title()
            naans = input("If yes then how many naans would you like: ")
            bbqFood(order, naans)
      else:
            print("incorrect input, Please check your spellings")
            isContinue1 = input("Do you want to try again (yes or no): ").title()
            if isContinue1 == "Yes":
                  menu()
            else:
                  exit()


menu()