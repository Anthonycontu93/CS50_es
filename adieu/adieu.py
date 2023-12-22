import inflect

p =  inflect.engine()

def main():


     names = []
     counter = 0

     while True:

        counter = counter + 1
        name = get_name()

        if not name:
             # se 2 condzione estrema
             if counter == 2:
                 if len(names) <=1:
                     print(f"Adieu, adieu, to {names[0]}")
                     break
                 else:
                     print(f"Adieu, adieu, to {names[0]} and {names[1]}")
                     break
             # aggiungi , e and
             else:
                 x = int(len(names))
                 names = p.join((names))
                 print(f"Adieu, adieu, to {names}")
                 break

        else:
            try:
                # only 1 and at the end and always a , after a name if >2
                names.append(name)

            except
                pass




def get_name():


    while True:
        try:
            item = input("Name: ")
            item = item.capitalize()


        except EOFError:
            return False

        else:
            return item




main()
