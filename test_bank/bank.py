def main():
    try:
        word = value(input("Greetig: "))

    except ValueError:
        pass

    print(word)


def value(greeting):
    try:
        word = greeting.lower().strip()
        if word[0] == "h" and word[1:5] == "ello":
            amount = 0
            return f"${amount}"

        elif word[0] == "h" and not word[1:5] == "ello":
            amount = 20
            return f"${amount}"
        else:
            amount = 100
            return f"${amount}"
    except:
        return


if __name__ == "__main__":
    main()
