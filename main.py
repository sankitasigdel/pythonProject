b = input("Enter a letter: ")
letter = ""
for i, x in enumerate(b):
    if i % 2 == 0 :
        letter += x.upper()
    else:
        letter += x.lower()

print(letter)
