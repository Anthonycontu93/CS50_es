def main():

    sentence = input("Input an happy smile or an unhappy smile:")

    output = convert(sentence)





def convert(smile):

    replace = smile.replace(":)", "🙂").replace(":(", "🙁")

    print(replace)




main()