def main():
    plate = input("Inputyour plate: ")

    plate = is_valid(plate)

    if plate:
        print("Valid")
    else:
        print("Invalid")

""""
:( input of ECTO88 yields output of Valid
    expected "Valid", not "Invalid\n"
:( input of NRVOUS yields output of Valid
    expected "Valid", not "Invalid\n"
"""""

def is_valid(s):

    plate = s.upper()

    first_rule = plate[0:2]
    check_numb = plate[-2:]
    check_numb_6 = plate[-3:]
    number_in_middle = plate[0:3]

    # no longer the 6 char or less then 2
    if len(plate) < 2:
        return False
    if len(plate) > 6:
        return False

    # chck space or punctuation
    for s in plate:
         if ord(s) >= 61 and ord(s) <= 122:
              continue
         elif ord(s) >= 65 and ord(s) <= 90:
              continue
         elif ord(s) >= 48 and ord(s) <= 57:
              continue
         else:
              return False

    # check if the first 2 elements are char
    for s in first_rule:
        if not ord(s) >= 65 and not ord(s) <= 90:
            return False

    # check if the last is a number
    c = 0 # counter
    check = 0

    if len(plate) > 4:
         f = check_numb_6[0:1]
    else:
         f = check_numb[0:1]
    # 0 is not ok as first number
    if  ord(f) == 48:
         return False

    for n in check_numb:
        if ord(n) >= 48 and ord(n) <= 57:
            c = c + 1
            check = check + 1

    if check >= 1:
        if c != len(check_numb):
                    return False
    ########### blocco check sopra



    # check the middle if is more lenght then 5
    if len(plate) > 5:
         for s in number_in_middle:
              if ord(s) >= 48 and ord(s) <= 57:
                   return False



    return True


if __name__ == "__main__":
     main()