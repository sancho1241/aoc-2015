with open('1.txt', 'r') as file:
    data = file.read()

i = 0

for l, n in enumerate(data):
    if n == '(':
        i += 1
    elif n == ')':
        i -= 1
    else:
        print 'error with ' + n

    if i == -1:
        print l+1
        break