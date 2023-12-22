word = input("File name: ")

word = word.lower().strip()

if ".gif" in word:
    print("image/gif")

elif ".jpg"in word:
    print("image/jpeg")

elif ".jpeg" in word:
    print("image/jpeg")

elif ".png" in word:
    print("image/png")

elif ".pdf" in word:
    print("application/pdf")

elif ".txt" in word:
    print("text/plain")

elif ".zip" in word:
    print("application/zip")

else:
    print("application/octet-stream")
