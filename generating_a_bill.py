import time
bill = 0
name = input("Hi ! Welcome to xyz restaurant! may i know your name? ")

def menu():
    global bill
    user_input = int(input("Choose an option: 1.Cake 2.Coffee 3.Cookies 4.Choclates 5.Hot Chips Press a number to continue: "))
    if user_input == 1:
        print("price of cake is 20/- per piece",name)
        bill = bill+20
        
    elif user_input == 2:
        print("price of coffee is 20/- per cup",name)
        bill = bill+20
        
    elif user_input == 3:
        print("price of cookies is 10/- per piece",name)
        bill = bill+10
        
    elif user_input == 4:
        print("price of choclates is 50/-",name)
        bill = bill+50
        
    elif user_input == 5:
        print("price of Hot Chips is 30/- per piece",name)
        bill = bill + 30
        
    else:
        print("You entered a invalid input.Please try again.")


    user_input = int(
        input(
            "\nPress 1 to order something else\notherwise Press 2 to complete your order\nPress a number to continue: \n"
        ))

    if user_input == 1:
        menu()
    elif user_input == 2:
        time.sleep(5)
        thanks()
    else:
        print("You entered a wrong input")


def thanks():
    print("Hope you enjoyed the snacks!! Visit Again")
    print("Your bill is",bill)


menu()
