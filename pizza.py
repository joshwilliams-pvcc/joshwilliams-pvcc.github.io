# Name: Joshua Williams
# Prog Purpose: This program prepares a receipt for a Palermo Pizza customer's order.
#      Small Pizza:       $  9.99
#      Medium Pizza:      $ 12.99
#      Large Pizza:       $ 14.99
#      Extra Large Pizza: $ 17.99
#      Sales Tax Rate     5.5%  

import datetime

# pizza prices
SMALL_PIZZA_PRICE = 9.99
MEDIUM_PIZZA_PRICE = 12.99
LARGE_PIZZA_PRICE = 14.99
EXTRA_LARGE_PIZZA_PRICE = 17.99
SALES_TAX = .055

#define global variables
pizza_size = "" # S means Small, M means Medium, L means Large, XL means Extra Large

small_pizza_count = 0
medium_pizza_count = 0
large_pizza_count = 0
extra_large_pizza_count = 0


subtotal = 0
total = 0
salestax = 0

###########    define program functions    ############
def main():
    another_pizza = True
    while another_pizza:
        get_user_data()
        perform_calculations()
        yesno = input("\nWould you like another pizza? (Y/N): ")
        if yesno.upper() != "Y":
            another_pizza = False
            display_results()

def get_user_data():
    global pizza_size, small_pizza_count, medium_pizza_count, large_pizza_count, extra_large_pizza_count
    pizza_size = input('What size pizza would you like (S, M, L, XL)?: ')
    if pizza_size.upper() == 'S':
        small_pizza_count += 1  
    if pizza_size.upper() == 'M':
        medium_pizza_count += 1
    if pizza_size.upper() == 'L':
        large_pizza_count += 1 
    if pizza_size.upper() == 'XL':
        extra_large_pizza_count += 1
    
def perform_calculations():
    global total_small_pizza_cost, total_medium_pizza_cost, total_large_pizza_cost, total_extra_large_pizza_cost, subtotal, salestax, total

    total_small_pizza_cost = small_pizza_count * SMALL_PIZZA_PRICE

    total_medium_pizza_cost = medium_pizza_count * MEDIUM_PIZZA_PRICE

    total_large_pizza_cost = large_pizza_count * LARGE_PIZZA_PRICE

    total_extra_large_pizza_cost = extra_large_pizza_count * EXTRA_LARGE_PIZZA_PRICE

    subtotal = total_small_pizza_cost + total_medium_pizza_cost + total_large_pizza_cost + total_extra_large_pizza_cost
    
    salestax = subtotal * SALES_TAX 

    total = subtotal + salestax

def display_results():
    print('\n-------------------------------------------------')
    print('     ******PALERMO PIZZA RECEIPT******')
    
    print('---------------------------------------------------')
    print(small_pizza_count,      'Small pizza total cost:    $',   format(total_small_pizza_cost, '8,.2f'))
    print(medium_pizza_count,     'Medium Pizza total cost:   $',   format(total_medium_pizza_cost, '8,.2f'))
    print(large_pizza_count,      'Large Pizza total cost:    $',   format(total_large_pizza_cost, '8,.2f'))
    print(extra_large_pizza_count,'Extra Large Pizzas:        $',   format(total_extra_large_pizza_cost, '8,.2f'))
    print('         Subtotal:           $', format(subtotal, '8,.2f'))
    print('         Sales Tax:          $', format(salestax, '8,.2f'))
    print('         Total:              $', format(total, '8,.2f'))
    print('---------------------------------------------------')
    print('         ',str(datetime.datetime.now()))
    

main()
