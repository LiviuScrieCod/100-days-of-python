import random

print("So you FINALLY decided to be bad at math... fine, I'll do your work for you, you overfed munchkin!\n")
calculate = True

while calculate:
    # Make sure the user inputs a valid number; delete spaces, check for symbols
    while True:
        bill_total = input("How much is the bill? What do you mean you don't know?! Check the total! The TOTAL not the date... jeez ").strip()
        try:
            bill_total = float(bill_total)
            if bill_total <= 0:
                print("Unless this is Ratatouille or they took pity on you, enter a positive number!")
                continue
            break
        except ValueError:
            print("I need numbers, not your life story in symbols!")

    # Set tip value; validate number and round to the closest available in given list
    while True:
        valid_tips = [5, 10, 15, 20]
        tip_total = input("How generous are you feeling right now? 5, 10, 15, 20, 90 <- P.S. those are tip percentages; I don't do other values! ")
        try:
            tip_total = float(tip_total)
            if tip_total == 0:
                tip_total = 0
            elif tip_total == 20:
                tip_total = 20
            elif tip_total > 20 or tip_total < 0:
                tip_total = 90
            else:
                tip_total = next(t for t in valid_tips if t>= tip_total)
            match tip_total:
                case 0:
                    print("Do you even math, bro?")
                case 5 | 10:
                    print(f"I can't even read that so I set it to {tip_total}%. Careful not to go bankrupt, you cheapskate!")
                case 15 | 20:
                    print(f"Look at you giving the bare minimum! {tip_total}% it is then")
                case 90:
                    print(f"Somebody's rich... I just signed you up for a monthly subscription to myself! And set the tip to {tip_total}%")
                case _:
                    print("Do you even math, bro?")
            break
        except ValueError:
            print("I need numbers, not your life story in symbols!")

    # Establish the number of people at the table; get a random name for a dialog option
    customers_total_int=0
    while customers_total_int < 1:
        customers_total_string = input("Who was at the table? I want NAMES! Separate them by commas! ").strip()

        customer_names = [name.strip().lower().capitalize() for name in customers_total_string.split(",") if name.strip()]
        customers_total_int = len(customer_names)

    # Calculate total amount to pay
    personal_share = (bill_total + bill_total*(tip_total/100))/customers_total_int

    #Solo diner case
    if customers_total_int == 1:
        print(f"Still no friends I take it? Good! Pay the total (${personal_share:.2f}) and get out! Others need to use that table too, you know!")
    else:
    # Dine and Dash dialog option
        grifter = input("Are you a grifter? y/n  ").lower().strip()
        if grifter == "y":
            print(f"Make a run for it! I hear {random.choice(customer_names)} is loaded!")
        else:
            print("You goody two-shoes... Why do I even bother?!")
            print(f"Anyway, lo and behold! Your total comes to ${personal_share:.2f}. All bow down to my amazing ability!")

    while True:
        again = input("Need any more tips calculated? y/n ").lower().strip()
        if again == "n":
            calculate=False
            break
        if again == "y":
            break
        else:
            print("It's just one of two letters, how hard can this be?! --> y/n <--")
