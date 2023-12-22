def main():

    time = input("What's the time? format ##:## : ")

    time = convert(time)


    if time >= 7.00 and time <= 8.00:
        print("breakfast time")

    elif time >= 12.00 and time <= 13.00:
        print("lunch time")

    elif time >= 18.00 and time <= 19.00:
        print("dinner time")




def convert(time):

    hours, miutes = time.split(":")

    hours = float(hours)
    minutes = float(miutes)

    min = (10 / 60) * minutes
    min = min / 10

    ora = hours + round(min, 2) # arrotondo alla prma decimale ecco l'1

    return ora

if __name__ == "__main__":
    main()



