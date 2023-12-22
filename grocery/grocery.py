def main():
    my_list = {}

    counter = 0

    while True:
        counter = counter + 1
        amount = 0
        order = get_item()

        if order == 1:
            myKeys = list(my_list.keys())
            myKeys.sort()

            sorted_dict = {}
            for i in myKeys:
                sorted_dict.update({i: my_list[i]})
                print(f"{my_list[i]} {i}")

            break
        if counter == 1:
            my_list.update({order: amount + 1})
            my_keys = []
            my_keys = my_list.keys()

        else:
            try:
                value_key_item_doppio = my_list[order]
            except:
                value_key_item_doppio = 0
                pass
            my_list.update({order: amount})
            my_keys = my_list.keys()
            for key in my_keys:
                if order in my_list.keys():
                    my_list.update({order: (value_key_item_doppio + 1)})


def get_item():
    while True:
        try:
            item = input()
            item = item.upper()

        except EOFError:
            return 1

        else:
            return item


main()
