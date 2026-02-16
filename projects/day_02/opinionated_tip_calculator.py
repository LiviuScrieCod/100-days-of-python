import random

print("So you FINALLY decided to be bad at math... fine, I'll do your work for you, you overfed munchkin!\n")

while True:
    while True:
        bill_total = input("How much is the bill? What do you mean you don't know?! Check the total! The TOTAL not the date... jeez ").strip()
        try:
            bill_total = float(bill_total)
        except ValueError:
            print("I need numbers, not your life story in symbols!")






    # print(customers_total_int)
    # print(customer_names)
    #
    # customers_total_string = input("Who was at the table? I want NAMES! Separate them by commas! ")
    #
    # customer_names = []
    # for _ in customers_total_string.split(","):
    #     customer_names.append(_.strip().lower().capitalize())
    #
    # customers_total_int = len(customer_names)
    #
    # grifter = input("Are you a grifter? y/n  ")
    # if grifter == "y":
    #     sucker = str(random.choice(customer_names))
    #     print(f"Make a run for it! I hear {sucker} is loaded!")
    #     break
    # else:
    #     print("You goody too shoes...")

    # tip_total = int(input("How generous are you feeling right now? 5%, 10%, 15%, 90% <- P.S. that's the tip "))
    #
    # amount_total = (bill_total + bill_total*(tip_total/100))/customers_total_int
    #
    # print(f"Read it and pay it: ${round(amount_total, 2)} . I hope it was worth it!")



