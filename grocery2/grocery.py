def main():

     my_list = {}


     counter = 0

     while True:
        counter = counter + 1
        order = get_item()

        if order == 1:

             myKeys = list(my_list.keys())
             myKeys.sort()
             sorted_dict = {}
             for i in myKeys:
                 sorted_dict.update({i : my_list[i]})
                 print(f"{my_list[i]} {i}")


             break

        my_list.update({order : counter})







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
