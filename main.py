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
  print("6. Restock products")
  print("7. Customer service")
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
      money = int(input('\nHow much do you want to have?: '))
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
  print("\n **Adding A New Product To The Inventory**")
  print("------------------------------------")
  type = input("Enter a type: ")
  price = int(input("Enter a price: "))
  total = int(input("Enter a total: "))
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
      if  6 >= age_cat >= 1 :
        gender_categorization()
      else:
        print("Invalid input! Please try again.")
        return age_categorization()
    except Exception:
      print("\nInvalid input! Please try again.")
      return age_categorization()
  def gender_categorization():
    print('Yay!')
    
  age_categorization()
  
   # creates a new product 
  new_product = Product(type, price, total) 
  inventory.append(new_product.features()) # adds new product features to the inventory

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
  

#############
#Section 4 - Running Section
#############

####Do Not Change this code, only uncomment to test your code
money_syst()

while isUsed:
  user_selection()
    
    

