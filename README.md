# python-pattern
printing pattern using python for loop



Code:
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


![image](https://user-images.githubusercontent.com/104575473/225701965-26614660-8cbc-4014-b659-6ac07f74e4f3.png)
![image](https://user-images.githubusercontent.com/104575473/225702015-1c8751cb-3786-46bf-9cd7-3b51b087a60f.png)
