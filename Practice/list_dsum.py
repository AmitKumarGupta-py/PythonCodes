def dsum(value):
    total = 0
    while value > 0:
        total+= value%10
        value //= 10
    return total

a = [123, 456, 789]

res = [dsum(val) for val in a]
print("result : ", res)



res1 = [sum(int(digit) for digit in str(val)) for val in a ]

print("2nd method: ", res1)