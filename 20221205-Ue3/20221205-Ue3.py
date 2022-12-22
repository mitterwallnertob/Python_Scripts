# Let's build robot Barista!!

print("Hello, welcome to NetworkChuck Coffee!")

# Ask your customer what their name is with the input() function and store that in the variable NAME.
name = input("What is your name?\n")

# Greet the customer with their name and thank them for comingin today using concatenation.

# Added in Ep. 4: if-/else-statements
# If a customer named Ben "walks in" he will be told to get out because he is not welcome in here and the program stops.
if name == "Ben":
    print("You're not welcome here Ben!! Get out!!")
    exit() #the program stops!
else:
    print("Hello " + name + ", thank you so much for coming in today.\n\n\n")

# Coffee menu 
menu = "Black Coffee, Espresso, Latte, Cappuccino, Frappucino"

# Ask the customer what they would like from the menu and store it in the variable order.
order = input(name + ", what would you like from our menu today? Here is what we are serving.\n" + menu + "\n")

# Ask the customer how many coffees they would like and store it in the variable quantity
quantity = input("How many coffees would you like?\n")


# Set the price for the different kinds of coffees
if order == "Frappuccino":
    price = 13
elif order == "Black Coffee":
    price = 3
elif order == "Espresso":
    price = 5
elif order == "Latte":
    extra_wc = input("Do you want extra whipped cream?\n")
    if extra_wc == "Yes":
        price = 11
    else:
        price = 9
elif order == "Cappuccino":
    price = 10
else:
    print("Sorry, we don't have that here.")
    price = 0



#print(price)


total = int(quantity) * price



print("Thank you. Your total is: " + str(total) + "$")

print("Sounds good " + name + ", we'll have your " + quantity + " " + order + " ready for you in a moment.")
