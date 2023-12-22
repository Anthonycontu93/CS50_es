def main():

    elements = get_int("Input a fraction: ")



def get_int(prompt):

    while True:
        try:
            elements = input(prompt)
            x,y = elements.split("/")
            x = int(x)
            y = int(y)

        except ValueError:
            pass

        except ZeroDivisionError:
            pass

        else:
             if x <= y and y != 0:
                 tot = x / y
                 tot = round(tot, 2)
                 percent = tot * 100
                 percent = int(percent)

                 if percent >= 98 and percent <= 100:
                     print("F")
                 elif percent >= 0 and percent <= 2:
                     print("E")
                 else:
                     print(str(percent), end="")
                     print("%")


                 break


main()