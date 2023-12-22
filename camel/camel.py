word = input("camelCase: ")

modify_word = []
add_Underscore = 0
position = []

for l in word:
        modify_word.append(l)
        add_Underscore = add_Underscore + 1
        if ord(l) >= 41 and ord(l) <= 90:
            n_w = l.lower()
            modify_word.pop(add_Underscore-1)
            modify_word.insert(add_Underscore, n_w)
            position.append(add_Underscore)
            continue
j = 1
if len(position) >= 1:
      for i in range(len(position)):
            modify_word.insert(position[i] - j,"_")
            j = j - 1

      for w in modify_word:
            print(w, end="")

      print()
else:
      print(word)


