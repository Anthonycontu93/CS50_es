def main():
    bot_price = 50
    money1 = 25
    money2 = 10
    money3 = 5

    insert = 0


    due = bot_price - insert
    update_due = 0

    while True:

        if due == 0:
             print("Change Owed:", due)
             break

        amount_due = print("Amount Due:", due)
        insert = get_number()




        match insert:
               case 25:
                    update_due = due - insert
               case 10:
                    update_due = due - insert
               case 5:
                    update_due = due - insert
               case _:
                     continue

        check_due = due
        due = update_due


        if insert > check_due:
            if due != 0:
                due = insert - check_due
                print("Change Owed:", due)
                break



def get_number():

    money = int(input("Insert Coin: "))

    return money








main()