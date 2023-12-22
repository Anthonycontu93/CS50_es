formula = input("Expression: ")

x, y, z = formula.split(" ")

x = int(x)
z = int(z)

match y:
    case "+":
       tot = x + z
       print(float(tot))
    case "-":
        tot = x - z
        print(float(tot))
    case "*":
        tot = x * z
        print(float(tot))
    case "/":
        tot = float(x) / float(z)
        print(tot)
    case _ :
        print("error symbol")