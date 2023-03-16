for i in range(6):
    if i == 0:
        print(' '*(5-i) + "*" + " "*(i*2-1))
    else:
        print(' '*(5-i) + "*" + " "*(i*2-1) + "*")
for i in range(5,0,-1):
    if i == 1:
        print(' '*5 + "*")
    else:
        print(' '*(5-i) + "*" + " "*(i*2-1) + "*")
