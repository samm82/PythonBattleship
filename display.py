def display(lst):
    for line in lst:
        for i in line:
            print(i, end=' ')
        print()

def displayBoth(a, b):
    c = []
    for i in range(len(a)):
        c.append(a[i]+["   "]+b[i])
    display(c)
