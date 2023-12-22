word = input("What is the Answer to the Great Question of life, the Universe, and Everything?")

word = word.lower().strip()

match word:
    case "42":
        print("Yes")
    case "forty-two":
        print("Yes")
    case "forty two":
        print("Yes")
    case _:
        print("No")
