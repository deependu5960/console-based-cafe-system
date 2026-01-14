# class contain product details
class Product() :
  def __init__(self,name,price,ID):
    self.name = name
    self.price = price
    self.M_ID = ID

# Class contain Objects having product details
class Menu():
  def Beverages(self):
    global b1,b2,b3,b4,b5,b6,b7,b8
    # p4 = Product("chocolate",120,1004)
    b1 = Product("Espresso",80,"b01")
    b2 = Product("Cappuccino",120,"b02")
    b3 = Product("Latte",130,"b03")
    b4 = Product("Americano",100,"b04")
    b5 = Product("Cold-Coffee",150,"b05")
    b6 = Product("Masala-chai",50,"b06")
    b7 = Product("Green-Tea",70,"b07")
    b8 = Product("Hot-chocolate",140,"b08")



  def Desserts(self):
    global d1,d2,d3,d4,d5,d6
    d1 = Product("Chocolate Brownie",160,"d01")
    d2 = Product("Blueberry Muffin",110,"d02")
    d3 = Product("Cheesecake",180,"d03")
    d4 = Product("Croissant",90,"d04")
    d5 = Product("Donut",60,"d05")
    d6 = Product("Ice Cream Scoop",70,"d06")

  def Snacks(self):
    global s1,s2,s3,s4,s5,s6
    s1 = Product("Veg Sandwich",120,"s01")
    s2 = Product("Grilled Cheese Sandwich",140,"s02")
    s3 = Product("French Fries",100,"s03")
    s4 = Product("Garlic Bread",130,"s04")
    s5 = Product("Paneer Wrap",160,"s05")
    s6 = Product("Veg Burger",150,"s06")


# class for cart-modification
class Cart_mod():
  global Menu_details
  Menu_details = {}

  def add(self,p):
    Menu_details.update({p.name:{"price" : p.price,"Menu-ID": p.M_ID}})
    return Menu_details

  def remove(self,p):
    del Menu_details[p.name]
    return Menu_details

  def products(self):
    return Menu_details

  def total_price(self):
    sum = 0
    for i in Menu_details:
      sum+=Menu_details[i]["price"]
    return sum


# class for Cart-User-Interface
class Cart_page():
   global cart
   cart = Cart_mod()
   def cart_opt(self):
        print('''
        select one option :
        1. Your Order
        2. Add Menu
        3. Remove Menu
        4. Total-Bill
        5. Home Back
        ''')

        try:
         ct_opt = int(input("Enter your option no. : "))

         if ct_opt==1:
            if len(cart.products())>0:
               for i in cart.products():
                  print(f"\n{i}\n{cart.products()[i]}")
            else:
               print("\nNo Order Yet\nPlease order something...\n")
               # print(cart.products())
        
         elif ct_opt==2:
               Menu_page.page()

         elif ct_opt==3:
               if len(cart.products())>0:
                  for i in cart.products():
                     print(f"\n{i}\n{cart.products()[i]}")
                  
                  print("\n* Type \"back\" if You dont want to remove menu *\n")
                  rm_menu = input("Enter the Menu_ID of removing menu : ").lower()
                  if rm_menu in M_details:
                     cart.remove(M_details[rm_menu])
                     print("Menu removed...")
                  elif rm_menu=="back":
                     ct_pg.cart_opt()
                  else:
                     print("Invalid Menu - ID ")
               else:
                  print("No Order to remove...\n")

         elif ct_opt==4:
            print(f"\nYour Total Bill : {cart.total_price()}") 
            if cart.total_price()==0:
               print("Please order something...\n")

         elif ct_opt==5:
            execute.start()
         else:
            print("Invalid Option")
          #   ct_pg.cart_opt()
         ct_pg.cart_opt()

        except ValueError:
           print("Please Enter Valid option no. ")
           ct_pg.cart_opt()


# class contain main page 
class Main():
    global ct_pg
    ct_pg = Cart_page()
    def start(self):
        global Menu_page
        Menu_page = Menu_bar()
        print('''
        Welcome to our cafe...
        please select your option
        1. Menu
        2. Cart
        ''')
        try :
            st_opt = int(input("Enter your option no. : "))

            if st_opt==1:
                Menu_page.page()
            elif st_opt==2:
                ct_pg.cart_opt()
            # elif st_opt==3:
            #     print(cart.products())
            else:
                print("Invalid option no. ")
        
        except ValueError:
           print("Please Enter Valid option no. ")

        except Exception as e:
           print(e)



# class contain Menu page
class Menu_bar():
    global M_details
    M_details = {}
    def next_menu(self):
        next_menu_input = input("Enter the menu ID by above to Order : ").lower()
        # Cart = Cart_mod()
        if next_menu_input in M_details:
            cart.add(M_details[next_menu_input])
            print("Ordered successfully")
            Menu_page.page()
        elif next_menu_input == "back":
            Menu_page.page()
        else:
            print("Invalid Menu-ID")
            Menu_page.next_menu()


    def page(self):
        M = Menu()
        print('''
        WELCOME TO OUR CAFE...
        What would you like to try :
        1. Beverages
        2. Desserts
        3. Snacks
        4. Back
        ''')
        try:
            
            Main_page_input = int(input("Enter the menu no. : "))
      
            if Main_page_input==1:
               M.Beverages()
               for i in [b1,b2,b3,b4,b5,b6,b7,b8]:
                  print(f"{i.M_ID} : {i.name} : {i.price}")
                  M_details.update({i.M_ID:i})
               print("\n* Type \"back\" if you don't want to order *\n ")
               Menu_page.next_menu()
        
            elif Main_page_input==2:
               M.Desserts()
               for i in [d1,d2,d3,d4,d5,d6]:
                     print(f"{i.M_ID} : {i.name} : {i.price}")
                     M_details.update({i.M_ID:i})
               print("\n* Type \"back\" if you don't want to order *\n ")
               Menu_page.next_menu()

            elif Main_page_input==3:
               M.Snacks()
               for i in [s1,s2,s3,s4,s5,s6]:
                     print(f"{i.M_ID} : {i.name} : {i.price}")
                     M_details.update({i.M_ID:i})
               print("\n* Type \"back\" if you don't want to order *\n ")
               Menu_page.next_menu()
        
            elif Main_page_input==4:
               ct_pg.cart_opt()
        
            else:
               print("Invalid Menu no.")
               Menu_page.page()

        except ValueError:
           print("Please enter Valid optiion no.")
           Menu_page.page()


execute = Main()
while True:
    execute.start()
              



