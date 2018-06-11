def display(lst):
    for line in lst:
        for i in line:
            print(i, end=' ')
        print()

def displayBoth(a, b):
    c = []
    for i in range(len(a)):
        c.append(a[1]+b[1])
    display(c)
