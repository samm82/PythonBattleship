def display(lst):
    for line in lst:
        for i in line:
            print(i, end=' ')
        print()

def displayBoth(a, b):
    if len(b) == len(a) + 1:
        b = b[:-1]
    c = []
    for i in range(len(a)):
        c.append(a[i]+["   "]+b[i])
    display(c)
