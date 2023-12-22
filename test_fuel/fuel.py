def main():

    elements = input("Input a fraction: ")
    fraction = convert(elements)
    print(gauge(fraction))


def convert(fraction):

    while True:


        x,y = fraction.split("/")
        x = int(x)
        y = int(y)

        if y == 0:
            raise ZeroDivisionError
        elif x > y:
            raise ValueError #vuole prima gli errori (RAISE), altrimenti si arrabbia. Poi il calcolo se CORRETTO
        else:
            tot = x / y
            tot = round(tot, 2)
            percent = tot * 100
            percent = int(percent)

        return percent


def gauge(percent):


    try:
        if 0 <= percent <= 1:
            percent ="E"
            return percent
        elif 99 <= percent <= 100:
            percent ="F"
            return percent
        elif 1 < percent < 99:
            return f"{int(percent)}%"
        else:
            raise TypeError
    except TypeError:
        pass




if __name__ == "__main__":
    main()