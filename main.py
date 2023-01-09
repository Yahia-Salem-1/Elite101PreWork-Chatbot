# NOTICE: This was made before the Elite101 request of making a chatbot, except for the chatbot itself and a couple of other features. The shop was premade (and a lot of its features were made by me), but the chatbot was NOT PREMADE. In addition, some features, such as adding items, are modified to help make the chatbot. I am the owner of the shop and the chatbot.

#############
#Section 1 - Import Modules and Global Variables
#############
import random  # used to generate random PID o
isUsed = True # True= program is running and False = program ends o
sales_list =[] # empty list of product to store sales o 


inventory = [
  {'prod_Id': 4327, 'type': 'Shoes', 'price': 100.0, 'total': 20},
  {'prod_Id': 3915, 'type': 'Tshirts', 'price': 43.5, 'total': 32},
  {'prod_Id': 2119, 'type': 'Pants', 'price': 34.0, 'total': 19},
  {'prod_Id': 1194, 'type': 'Jumpers', 'price': 250.0, 'total': 5},  
  {'prod_Id': 1300, 'type': 'Blouse', 'price': 24.76, 'total': 3},
  {'prod_Id': 1118, 'type': 'Dress', 'price': 50.0, 'total': 10}, 
  {'prod_Id': 1664, 'type': 'Suits', 'price': 250, 'total': 5}
] 
# create an empty list then add the above data in it as inventory o 



#############
#Section 2 - Functions Definition
#############


#Displays the main menu o
def display_menu():
  print("\n **WALMART STORE INVENTORY SYSTEM**")  
  print("1. Show Inventory ") 
  print("2. Add A New Product")  
  print("3. Order A Product")  
  print("4. Remove Products") 
  print("5. Show Shopping History")
  print("6. Restock Products")
  print("7. Customer Service")
  print("8. Exit\n")  
        

  #used to capture and process user selections o
def user_selection():
    global isUsed #global variable isUsed
    display_menu()
    user_choice = int(input("Enter a number between 1-8: "))
    
    if user_choice == 1:  #Go to Store Inventory. o
        display_inventory() #print('show inventory') o
    elif user_choice == 2:  #Initiate New Product Processes
        add_new_product()
    elif user_choice == 3:  #Initiate Buying a New Product.
        order_product()
    elif user_choice == 4:  #Initiate Removing a Product.
         remove_product()
    elif user_choice == 5:
      see_cart()
    elif user_choice == 6:
      restock_products()
    elif user_choice == 7:
      chatbot()
    elif user_choice == 8:
        print("Thank you for shopping at Walmart!"
              )  # adds thank you message before exiting the program
        isUsed = False  #print("program ends.")  # changes the value of isUsed to False
    else:
        print("\nSorry, Not a Valid Choice. Please try again!")

#This functions makes a money system depending on how much you want.
def money_syst():
  global money
  choice_money = input('Do you want us to choose how much money you have, or do you want to do that? (choose opt1/opt2):\n')

  if choice_money == "opt1":
    money = random.randint(5000, 10000)
    print(f'\nMoney: {money}\n')
  
  elif choice_money == "opt2":
    try:
      money = float(input('\nHow much do you want to have?: '))
      print(f'\nMoney: {money}\n')

    except ValueError:
      print('\nInvalid Input.\n')
      return money_syst()
      
  elif choice_money != "opt1" "opt2":
    print('\nSorry! Invalid input. Please try again\n')
    return money_syst()
    
    

  else:
    print('\nInvalid option. Please try again.\n')
    return money_syst()


# this function displays story inventory
def display_inventory():
    print("\n **GEN-Z STORE INVENTORY**")
    for product in inventory:
        print("----------------------------")
        for key, value in product.items():
            print("{0}\t\t{1}".format(key, value))
    print("___________________________")
    


# add a new product function
def add_new_product():
  global type, price, total
  print("\n **Adding A New Product To The Inventory**")
  print("------------------------------------")
  type = input("Enter a type: ")
  price = float(input("Enter a price: "))
  total = int(input("Enter a total: "))
  age_categorization()
  
def age_categorization():
  global age_cat
  print("------------------------------------")
  print("Age categorization: ")
  print("1. under 11")
  print("2. 11 to 19")
  print("3. 20 to 40")
  print("4. 41 to 65")
  print("5. 65 and above")
  print("6. Skip")
  try:
    age_cat = int(input("\nEnter a number between 1-6: "))
    if  6 >= age_cat >= 1:
      gender_categorization()
    else:
      print("Invalid input! Please try again.")
      return age_categorization()
  except Exception:
    print("\nInvalid input! Please try again.")
    return age_categorization()
    
def gender_categorization():
  global gen_cat
  print("------------------------------------")
  print("Gender categorization: ")
  print("1. Female")
  print("2. Male")
  print("3. Other")
  print("4. Skip")
  try:
    gen_cat = int(input("\nEnter a number between 1-4: "))
    if  4 >= gen_cat >= 1:
      new_product()
    else:
      print("Invalid input! Please try again.")
      return gender_categorization()
  except Exception:
    print("\nInvalid input! Please try again.")
    return age_categorization()
    
def new_product():
  global age_cat
  global gen_cat
  new_product = Product(type, price, total) 
  inventory.append(new_product.features()) # adds new product features to the inventory
      

  if gen_cat == 1 and age_cat == 1: #lists for gender and age.
    global gen1Age1
    gen1Age1 = []
    gen1Age1.append(new_product.features())
    
  elif gen_cat == 2 and age_cat == 1:
    global gen2Age1
    gen2Age1 = []
    gen2Age1.append(new_product.features())
    
  elif gen_cat == 3 or 4 and age_cat == 1:
    global gen34Age1
    gen34Age1 = []
    gen34Age1.append(new_product.features())
  
    
  elif gen_cat == 1 and age_cat == 2: 
    global gen1Age2
    gen1Age2 = []
    gen1Age2.append(new_product.features())
    
  elif gen_cat == 2 and age_cat == 2:
    global gen2Age2
    gen2Age2 = []
    gen2Age2.append(new_product.features())
    
  elif gen_cat == 3 or 4 and age_cat == 2:
    global gen34Age2
    gen34Age2 = []
    gen34Age2.append(new_product.features())
  
  
  elif gen_cat == 1 and age_cat == 3: 
    global gen1Age3
    gen1Age3 = []
    gen1Age3.append(new_product.features())
    
  elif gen_cat == 2 and age_cat == 3:
    global gen2Age3
    gen2Age3 = []
    gen2Age3.append(new_product.features())
    
  elif gen_cat == 3 or 4 and age_cat == 3:
    global gen34Age3
    gen34Age3 = []
    gen34Age3.append(new_product.features())
  
  
  elif gen_cat == 1 and age_cat == 4: 
    global gen1Age4
    gen1Age4 = []
    gen1Age4.append(new_product.features())
    
  elif gen_cat == 2 and age_cat == 4:
    global gen2Age4
    gen2Age4 = []
    gen2Age4.append(new_product.features())
    
  elif gen_cat == 3 or 4 and age_cat == 4:
    global gen34Age4
    gen34Age4 = []
    gen34Age4.append(new_product.features())
  
  
  elif gen_cat == 1 and age_cat == 5: 
    global gen1Age5
    gen1Age5 = []
    gen1Age5.append(new_product.features())
    
  elif gen_cat == 2 and age_cat == 5:
    global gen2Age5
    gen2Age5 = []
    gen2Age5.append(new_product.features())
    
  elif gen_cat == 3 or 4 and age_cat == 5:
    global gen34Age5
    gen34Age5 = []
    gen34Age5.append(new_product.features())

  
  elif gen_cat == 1 and age_cat == 6: 
    global gen1Age6
    gen1Age6 = []
    gen1Age6.append(new_product.features())
    
  elif gen_cat == 2 and age_cat == 6:
    global gen2Age6
    gen2Age6 = []
    gen2Age6.append(new_product.features())
    
  elif gen_cat == 3 or 4 and age_cat == 6:
    global gen34Age6
    gen34Age6 = [] 
    gen34Age6.append(new_product.features())

  
 # creates a new product 



  
    
# delete a product from inventory
def remove_product():
  toDeleteIndex = -99
  display_inventory()
  print("\n **Removing A Product From The Inventory**")
  print("------------------------------------")
  try:
    PID = int(input("Enter Product Id number to Remove: "))
  except Exception:
    print("Invalid input")
    exit(1)
  for i in range(len(inventory)):
        if inventory[i]["prod_Id"] == PID:
            toDeleteIndex = i 
            break
  if toDeleteIndex > 0:
    inventory.pop(toDeleteIndex)
    print("Product deleted: ", PID)

# Order product
def order_product():
  global avail_quantity
  display_inventory() 
  global PID
  print("\n **Placing an Order**")
  print("-----------------")

  avail_quantity = 0  #available quantity in stock
  cost = 0  # cost of the purchase
  type = ''  # type of the product
  price = 0  #price of a unit
  isFound = False  #a product associated with the PID is found
  quantity = 0
  try:
    PID = int(input("Enter Product Id: "))
    quantity = int(input("How many do you want: "))
  except Exception:
    print("Invalid input")
    exit(1)
  for i in range(len(inventory)):
        if inventory[i]["prod_Id"] == PID:
          isFound = True
          avail_quantity = inventory[i]["total"]
          break

  if isFound == False:
    print("Product Id not found: ", PID)
    
  
  if quantity <= avail_quantity and quantity > 0:
                global money
                
                inventory[i]["total"] -= quantity  # update the inventory
                price = inventory[i]["price"]
                type = inventory[i]["type"]
                cost = quantity * price * 1.08 # add taxes later
                sales_list.append([PID, type, quantity,cost])#record the new sale
                if money - cost >= 0:
                  money = money - cost
                  print(f'Money left: {money}')

                elif money - cost < 0:
                  inventory[i]["total"] += quantity
                  print('\nYou do not have enough money.\n')
                  choice_goBack =  input('Would you like to go back to display menu, or would you like to order something else? (opt1/opt2): ')

                  if choice_goBack == 'opt2':
                    return order_product()

                  else:
                    return user_selection()
    
  else:
    print(f"Quantity specified is not in inventory:\n{inventory[i]}. Instead, you can buy {inventory[i]['total']} of the {inventory[i]['type']}.")
    return order_product()

  
def see_cart():
  cart = sales_list
  
  if cart == []:
    print('\nSorry, you have not ordered anything yet!')
  else:
    print(f'\nThis is what you ordered: {cart}')


  
  
def restock_products():
  display_inventory()
  try:
    restock_input = int(input('\nWhat item do you want to restock? (prod_ID): '))
    restock_quantity = int(input('\nHow much do you want to add?: '))
  except ValueError:
    print('\nInvalid Input')
    return restock_products()

  for i in range(len(inventory)):
        if inventory[i]["prod_Id"] == restock_input:
          isFound = True
          break

  if isFound == False:
    print("\nProduct Id not found: ", PID)

  inventory[i]["total"] += restock_quantity
    
  
  

  
class Product:
    #constructor method used to instantiate any new class
    def __init__(self, type, price, total):
        self.prod_Id = random.randint(1000,5000)  # new attribute added
        self.type = type        
        self.price = price        
        self.total = total

    def features(self):
      return {"prod_Id":self.prod_Id,
              "type":self.type,
              "price":self.price,
              "total":self.total
             }

def chatbot():
  
  name = str(input('\nHi, what is your name? ')).capitalize()
  print("\n------------------------------------\n")
  print(f"\n{name}, I'm Simon and I'm here to help you.")
  print("But first, I'll have to get some background information, if you may.")
  print("\n------------------------------------\n")
    
    ###----Age----###
  def age_func():
    try:
      global age
      age = int(input('\nHow old are you? (Type "-1" to skip this question)\n')) # The prompt.
      if 0<= age < 11:
        print("\nOh. You are still pretty young!")
      elif 11 <= age <= 19:
        print("\nYou are in your tween/teen years! Pretty cool.") # The answers to the input.
      elif 20 <= age <= 40:
          print("\nYou are an adult. You rock!")
      elif 41 <= age <= 65:
          print("\nAs you age, you get wiser.")
      elif 65 < age:
          print("\nI wish you the best health.")
      elif age == -1:
          print("")
      else: 
          print("\nThat's unrealistic. Try again.")
          return age()
    except Exception:
        print("\nInvalid input.")
        return age()
          
    ###----Gender----###
  def gender_func():
    try:
        global gender
        print("\n------------------------------------\n") # Make sure to make function for gender.
        print('\nWhat is your gender?\n')
        print("1. Female")
        print("2. Male")
        print("3. Other")
        print("4. Skip")
        gender = int(input('\nPlease choose a number from 1-4: '))
        if 1 > gender:
          print("Invalid input!")
          return chatbot()
        elif 4 < gender:
          print("Invalid input!")
          return chatbot()
    except Exception:
        print("\nInvalid input.")
        return gender()  


      
    print("\n------------------------------------\n")
  def feeling():
    try:
        day = input("\nIf you had one word to describe your day, what would it be? ").lower()
  
        good = ["good", "awesome", "nice", "alright", "okay", "ok", "alr", "rad", "cool", "best", "bright", "super", "splendid", "lovely", "exciting", "happy", "smooth", "pleasant", "lucky", "fine", "great"]
        bad = ["bad", "awful", "not good", "horrible", "long", "miserable", "sad", "rough", "crappy", "worst", "unpleasant", "dissapointing", "dreadful", "difficult", "none of your business", "horrendous", "long"]
        boring = ["meh", "eh", "boring", "repetitive", "dull", "unvaried", "in between", "not bad, not good", "usual"]
        interesting = ["interesting", "fascinating", "surprising", "shocking", "weird", "strange", "confusing", "unusual"]
  
        good_response = ["\n I agree! What a pleasant day it is.",
                         "\nWhat a lovely day for both of us!",
                         f"\nThat's {day}!",
                         "\nKeep smiling!",
                         "\nWhat an awesome smile you might be having!"]
        bad_response = ["\nI hope you feel better.",
                        "\nTomorrow’s a new day.",
                        "\nWell, that stinks!"
        ]
  
        boring_response = ["\nIf you're bored, how about seeing some of our recommendations!",
                           "\nWell then, let me spice things up for you with our recommendations!",
                           "\nLet me make your day exciting with our recommendations!"
        ]
  
        interesting_response = ["\nThat's interesting.",
                                "\nHuh.",
                                "\nCool."
        ]
  
        generic_response = ["Okay. Let's proceed."
        ]
        
        if day in good:
          print(random.choice(good_response))
        elif day in bad:
          print(random.choice(bad_response))
        elif day in boring:
          print(random.choice(boring_response))
        elif day in interesting:
          print(random.choice(interesting_response))
        else:
          print(random.choice(generic_response))
          
        print("\n----------------------------") 
    except Exception:
      print("Invalid input. Please try again!")
      return feeling()
   
    # ----------- RECOMMENDATIONS -----------
      
        
 
  def recommendations():
    global age_cat
    global gen_cat
    global gen1Age1
    
    list_allAges_genF = [4, 5]
    list_allAges_genE_1 = [0, 1]
    list_allAges_genE_2 = [2, 3]
    list_allAges_genM = [6]
    
    new_list_allAges_genF = [inventory[index] for index in list_allAges_genF]
    new_list_allAges_genE_1 = [inventory[index] for index in list_allAges_genE_1]
    new_list_allAges_genE_2 = [inventory[index] for index in list_allAges_genE_2]
    new_list_allAges_genM = [inventory[index] for index in list_allAges_genM]
    
    list_allAges_genE = [new_list_allAges_genE_1, new_list_allAges_genE_2]
    #learned from https://bobbyhadz.com/blog/python-access-multiple-elements-in-list-by-index
    
    print("\nHere are some recommendations for you:\n\n")
    print("1. I am interested.")
    print("2. I am not interested\n")
    
    if 0 <= age < 11 and gender == 1:
      
      for product in new_list_allAges_genF:
        print("----------------------------")   
        for key, value in product.items():
          print("{0}\t\t{1}".format(key, value))
      try:
        for product in gen1Age1:  
          print("----------------------------")   
          for key, value in product.items():
            print("{0}\t\t{1}".format(key, value))

      except Exception: 
        pass

      for product in random.choice(list_allAges_genE):
        print("----------------------------")   
        for key, value in product.items():
          print("{0}\t\t{1}".format(key, value))
      print("____________________________")

    elif 11 <= age <= 19 and gender == 1:
    
      for product in new_list_allAges_genF:
        print("----------------------------")   
        for key, value in product.items():
          print("{0}\t\t{1}".format(key, value))
      
      try:
        for product in gen1Age2:  
          print("----------------------------")   
          for key, value in product.items():
            print("{0}\t\t{1}".format(key, value))

      except Exception: 
        pass

      for product in random.choice(list_allAges_genE):
        print("----------------------------")   
        for key, value in product.items():
          print("{0}\t\t{1}".format(key, value))
      print("____________________________")

    elif 20 <= age <= 40 and gender == 1:
    
      for product in new_list_allAges_genF:
        print("----------------------------")   
        for key, value in product.items():
          print("{0}\t\t{1}".format(key, value))
      
      try:
        for product in gen1Age3:  
          print("----------------------------")   
          for key, value in product.items():
            print("{0}\t\t{1}".format(key, value))

      except Exception: 
        pass

      for product in random.choice(list_allAges_genE):
        print("----------------------------")   
        for key, value in product.items():
          print("{0}\t\t{1}".format(key, value))
      print("____________________________")

    elif 41 <= age <= 65 and gender == 1:
    
      for product in new_list_allAges_genF:
        print("----------------------------")   
        for key, value in product.items():
          print("{0}\t\t{1}".format(key, value))
      
      try:
        for product in gen1Age4:  
          print("----------------------------")   
          for key, value in product.items():
            print("{0}\t\t{1}".format(key, value))

      except Exception: 
        pass

      for product in random.choice(list_allAges_genE):
        print("----------------------------")   
        for key, value in product.items():
          print("{0}\t\t{1}".format(key, value))
      print("____________________________")

    elif 65 < age and gender == 1:
    
      for product in new_list_allAges_genF:
        print("----------------------------")   
        for key, value in product.items():
          print("{0}\t\t{1}".format(key, value))
      
      try:
        for product in gen1Age5:  
          print("----------------------------")   
          for key, value in product.items():
            print("{0}\t\t{1}".format(key, value))

      except Exception: 
        pass

      for product in random.choice(list_allAges_genE):
        print("----------------------------")   
        for key, value in product.items():
          print("{0}\t\t{1}".format(key, value))
      print("____________________________")

    elif age == -1 and gender == 1:
    
      for product in new_list_allAges_genF:
        print("----------------------------")   
        for key, value in product.items():
          print("{0}\t\t{1}".format(key, value))
      
      try:
        for product in gen1Age6:  
          print("----------------------------")   
          for key, value in product.items():
            print("{0}\t\t{1}".format(key, value))

      except Exception: 
        pass

      for product in random.choice(list_allAges_genE):
        print("----------------------------")   
        for key, value in product.items():
          print("{0}\t\t{1}".format(key, value))
      print("____________________________")



    elif 0 <= age < 11 and gender == 2:
      
      for product in new_list_allAges_genM:
        print("----------------------------")   
        for key, value in product.items():
          print("{0}\t\t{1}".format(key, value))
      try:
        for product in gen2Age1:  
          print("----------------------------")   
          for key, value in product.items():
            print("{0}\t\t{1}".format(key, value))

      except Exception: 
        pass

      for product in random.choice(list_allAges_genE):
        print("----------------------------")   
        for key, value in product.items():
          print("{0}\t\t{1}".format(key, value))
      print("____________________________")

    elif 11 <= age <= 19 and gender == 2:
    
      for product in new_list_allAges_genM:
        print("----------------------------")   
        for key, value in product.items():
          print("{0}\t\t{1}".format(key, value))
      
      try:
        for product in gen2Age2:  
          print("----------------------------")   
          for key, value in product.items():
            print("{0}\t\t{1}".format(key, value))

      except Exception: 
        pass

      for product in random.choice(list_allAges_genE):
        print("----------------------------")   
        for key, value in product.items():
          print("{0}\t\t{1}".format(key, value))
      print("____________________________")

    elif 20 <= age <= 40 and gender == 2:
    
      for product in new_list_allAges_genM:
        print("----------------------------")   
        for key, value in product.items():
          print("{0}\t\t{1}".format(key, value))
      
      try:
        for product in gen2Age3:  
          print("----------------------------")   
          for key, value in product.items():
            print("{0}\t\t{1}".format(key, value))

      except Exception: 
        pass

      for product in random.choice(list_allAges_genE):
        print("----------------------------")   
        for key, value in product.items():
          print("{0}\t\t{1}".format(key, value))
      print("____________________________")

    elif 41 <= age <= 65 and gender == 2:
    
      for product in new_list_allAges_genM:
        print("----------------------------")   
        for key, value in product.items():
          print("{0}\t\t{1}".format(key, value))
      
      try:
        for product in gen2Age4:  
          print("----------------------------")   
          for key, value in product.items():
            print("{0}\t\t{1}".format(key, value))

      except Exception: 
        pass

      for product in random.choice(list_allAges_genE):
        print("----------------------------")   
        for key, value in product.items():
          print("{0}\t\t{1}".format(key, value))
      print("____________________________")

    elif 65 < age and gender == 2:
    
      for product in new_list_allAges_genM:
        print("----------------------------")   
        for key, value in product.items():
          print("{0}\t\t{1}".format(key, value))
      
      try:
        for product in gen2Age5:  
          print("----------------------------")   
          for key, value in product.items():
            print("{0}\t\t{1}".format(key, value))

      except Exception: 
        pass

      for product in random.choice(list_allAges_genE):
        print("----------------------------")   
        for key, value in product.items():
          print("{0}\t\t{1}".format(key, value))
      print("____________________________")

    elif age == -1 and gender == 2:
    
      for product in new_list_allAges_genM:
        print("----------------------------")   
        for key, value in product.items():
          print("{0}\t\t{1}".format(key, value))
      
      try:
        for product in gen2Age6:  
          print("----------------------------")   
          for key, value in product.items():
            print("{0}\t\t{1}".format(key, value))

      except Exception: 
        pass

      for product in random.choice(list_allAges_genE):
        print("----------------------------")   
        for key, value in product.items():
          print("{0}\t\t{1}".format(key, value))
      print("____________________________")

    
    elif 0 <= age < 11 and gender == 3 or 4:

      for product in new_list_allAges_genE_1 and new_list_allAges_genE_2:
        print("----------------------------")   
        for key, value in product.items():
          print("{0}\t\t{1}".format(key, value))
      print("____________________________")

      try:
        for product in gen34Age1:  
          print("----------------------------")   
          for key, value in product.items():
            print("{0}\t\t{1}".format(key, value))

      except Exception: 
        pass

    elif 11 <= age <= 19 and gender == 3 or 4:

      for product in new_list_allAges_genE_1 and new_list_allAges_genE_2:
        print("----------------------------")   
        for key, value in product.items():
          print("{0}\t\t{1}".format(key, value))
      print("____________________________")

      try:
        for product in gen34Age2:  
          print("----------------------------")   
          for key, value in product.items():
            print("{0}\t\t{1}".format(key, value))

      except Exception: 
        pass

    elif 20 <= age <= 40 and gender == 3 or 4:

      for product in new_list_allAges_genE_1 and new_list_allAges_genE_2:
        print("----------------------------")   
        for key, value in product.items():
          print("{0}\t\t{1}".format(key, value))
      print("____________________________")

      try:
        for product in gen34Age3:  
          print("----------------------------")   
          for key, value in product.items():
            print("{0}\t\t{1}".format(key, value))

      except Exception: 
        pass

    elif 41 <= age <= 65 and gender == 3 or 4:

      for product in new_list_allAges_genE_1 and new_list_allAges_genE_2:
        print("----------------------------")   
        for key, value in product.items():
          print("{0}\t\t{1}".format(key, value))
      print("____________________________")

      try:
        for product in gen34Age4:  
          print("----------------------------")   
          for key, value in product.items():
            print("{0}\t\t{1}".format(key, value))

      except Exception: 
        pass


    elif age < 65 and gender == 3 or 4:

      for product in new_list_allAges_genE_1 and new_list_allAges_genE_2:
        print("----------------------------")   
        for key, value in product.items():
          print("{0}\t\t{1}".format(key, value))
      print("____________________________")

      try:
        for product in gen34Age5:  
          print("----------------------------")   
          for key, value in product.items():
            print("{0}\t\t{1}".format(key, value))

      except Exception: 
        pass

    elif age == -1 and gender == 3 or 4:
      
      for product in new_list_allAges_genE_1 and new_list_allAges_genE_2:
        print("----------------------------")   
        for key, value in product.items():
          print("{0}\t\t{1}".format(key, value))
      print("____________________________")

      try:
        for product in gen34Age6:  
          print("----------------------------")   
          for key, value in product.items():
            print("{0}\t\t{1}".format(key, value))

      except Exception: 
        pass

    try:
      interested_question = int(input("\nEnter a number: "))

    except Exception:
      print("Invalid Input! Please Try Again.\n")
      return recommendations()

    if interested_question == 1:
      order_product()
    elif interested_question == 2:
      chatbot_menu()

    else:
      print("Invalid Input! Please Try Again.\n")
      return recommendations()
      
  def chatbot_menu():
    
    def feedback():
      topic = input("\n\nTopic: ")
      description = input("\nDescribe your issue or recommendation: ")
      print("\n1. Submit")
      print("\n2. Cancel")
      
      try:
        submission = int(input("\nEnter a number: "))
      except Exception:
        print("\nInvalid Input! Please Try Again.\n")
        return feedback()
        
      if submission == 1:
        print("\nThank you for your feedback!")
        chatbot_menu()
      elif submission == 2:
        return chatbot_menu()
      else:
        print("\nInvalid Input! Please Try Again.\n")
        feedback()
        
      
    def help_customer():
      print(f"\n\nHey, {name}! What do you need help with?")
      print("\n1. Selecting")
      print("\n2. Adding new products")
      print("\n3. Removing products")
      print("\n4. Ordering products")
      print("\n5. Restocking products")
      print("\n6. Other")
      
      try:
        help_me = int(input("\nEnter a number between 1-5: "))
      except Exception:
        print("\nInvalid Input! Please Try Again.\n")
        return help_me()

      if help_me == 1:
        print('\nTo select, all you have to do is look at the number to the left of the option (bullet) and type it in where it says, "Enter a number." \n\nAfter typing in the number, you selected the option you wanted to select and will be enjoying its features.')
        return chatbot_menu()
      
      elif help_me == 2: 
        print("\nTo add a new product, enter a type, which is the name of the product. Then, enter the price of the product. Next, type in the quantity, or total, you want to add. Finally, select a specific gender and age group the product will most likely appeal to, or skip the question. \n\nNow you added a new product. It should be added to the inventory and be added to a list based on age and gender that it can appeal to.")
        return chatbot_menu()

      elif help_me == 3: 
        print('\nTo remove an existing product, select "Remove product" from the menu, then enter the product ID of the thing you want to remove provided in the list of items.\n\nNow, you removed the product from the inventory and therefore, cannot be ordered again.')
        return chatbot_menu()

      elif help_me == 4: 
        print("\nTo order a product, enter the product ID of the item provided on the list above. Then, select the quantity you want.\n\nTwo things to keep in mind is that ordering a product takes away some of your money and that you can not order a quantity larger than the available ones. To do that, you have to restock the product.")
        return chatbot_menu()
        
      elif help_me == 5:
        print("\nTo restock a product, you must enter the product ID listed above. Then, enter the amount you want to add to the existing inventory.\n\nNow, you restocked a product.")
        return chatbot_menu()

      elif help_me == 6:
        feedback()

      else: 
        print("\nInvalid Input! Please Try Again.\n")
        return help_customer()
        

      
    print("\n----------------------------")
    print("***CUSTOMER SERVICE***")
    print("\n1. Feedback")
    print("\n2. Help")
    print("\n3. See Recommendations")
    print("\n4. Exit Customer Service")
    try:
      chatbot_menu_s = int(input("\n\nEnter a number: "))
    
    except Exception:
      print("\nInvalid Input! Please Try Again.\n")
      return chatbot_menu()

    if chatbot_menu_s == 1:
      feedback()
    elif chatbot_menu_s == 2:
      help_customer()
    elif chatbot_menu_s == 3:
      recommendations()
    elif chatbot_menu_s == 4:
      return user_selection()
    else:
      print("\nInvalid Input! Please Try Again.\n")
      return chatbot_menu()

         
    
  age_func()
  gender_func()
  feeling()
  recommendations()
    
    
      
  
    

  
             
  
  

#############
#Section 3 - Running Section
#############

money_syst()

while isUsed:
  user_selection()
    
    

