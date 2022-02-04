def cube(num):
    return num * num * num


print(cube(3))
print(cube(-5))


def oddEvenOther(num):
    if num == 0:
        return "neither"
    elif num % 2 == 1:
        return "odd"
    elif num % 2 == 0:
        return "even"
    else:
        return "neither"


print(oddEvenOther(2))
print(oddEvenOther(3))
print(oddEvenOther(0))


def diff17(num):
    if num > 17:
        return (num - 17) * 2
    else:
        return 17 - num


print(diff17(14))
print(diff17(22))


def sumOrThreeX(num1, num2, num3):
    if num1 == num2 == num3:
        return (3 * (num1 + num2 + num3))
    else:
        return (num1 + num2 + num3)


print(sumOrThreeX(2, 2, 2))
print(sumOrThreeX(3, 4, 5))


def sumOrZero(num1, num2, num3):
    if num1 == num3 or num1 == num2 or num2 == num3:
        return (0)
    else:
        return (num1 + num2 + num3)


print(sumOrZero(2, 2, 1))
print(sumOrZero(3, 2, 3))
print(sumOrZero(3, 3, 3))
print(sumOrZero(3, 2, 1))

print("hi")


def countRepeat(num):
    for i in range(num):
        print(i)
        print(i)
    print(num)


countRepeat(10)
