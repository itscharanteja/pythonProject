stuff = list()
while True:
    inp = input("Enter A number")
    if  inp == 'done': break
    value = float(inp)
    stuff.append(value)

average = sum(stuff)/len(stuff)

