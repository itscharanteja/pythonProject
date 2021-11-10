total = 0
count = 0

while True:
    inp = input('Enter A Number: ')
    if inp == "done":
        break
    value = float(inp)
    total = total + value
    count = count + 1

Average = total / count
print('Average: ', Average)
