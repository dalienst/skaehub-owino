def is_power_of_four(num):
    if(num == 0):
        return False
    while (num != 1):
        if (num % 4 != 0):
            return False
        num = num // 4
    return True

print(is_power_of_four(64))
print(is_power_of_four(50))