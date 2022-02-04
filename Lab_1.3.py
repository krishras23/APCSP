# Exercise 1
print("BothPositive")

def both_positive(x, y):
    if x > 0 and y > 0:
        return True
    else:
        return False

print(both_positive(-1,1))
print(both_positive(1,1))

# Exercise 2
print("Check Condition")

def check_condition(c1, c2, c3):

    if c1 == True and c2 == True and c3 == True:
        print("All true")
    elif c1 == True and c2 == True or c1 == True and c3 == True or c2 == True and c3 == True: 
        print("Only 2 True")
    elif c1 == True or c2 == True or c3 == True:
        print("Only 1 True")
    else:
        print("None True")

x = 3
y = 4
z = 5

check_condition(x == y, y > z, z == 4)
check_condition(x > y, y < z, z == 5)
check_condition(x < y, y < z, z == 5)
check_condition(x > y, y > z, z == 5)

# *** Write your own function for Exercise 3 here. ***
print("AnyNumber7")

def any_number_seven(s):
    for i in s:
        if i == "7":
            return True
    return False

print(any_number_seven("1234"))
print(any_number_seven("127347"))
print(any_number_seven("12734"))
print(any_number_seven("asd7jkl"))

# *** Write your own function for Exercise 4 here. ***
print("Jackpot")

def jackpot(s):
    condition = s.find("777")
    if condition == -1:
        return False
    else:
        return True 

print(jackpot("1177177722"))
print(jackpot("1234"))
print(jackpot("037179777"))

# *** Write your own function for Exercise 5 here. ***
print("Any7x7")

def any_7x7(s):
    index1 = s.find("7")
    index2 = s.find("7", index1+1)
    if index2 - index1 == 2:
        return True
    return False

print(any_7x7("123707221"))
print(any_7x7("12370"))
print(any_7x7("abc787def"))



