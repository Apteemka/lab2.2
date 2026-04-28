def check_values(a,b):
    if a == True and b == False:
        return True
    elif a == None and b == None:
        return None
    else:
        if a > b:
            return 1
        elif b > a:
            return -1
        elif a == b:
            return 0

flag = True
while flag == True:
    flag = False