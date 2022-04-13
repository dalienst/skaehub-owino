#Check if is a power of four
def is_power_of_four(num):
    while num and not (num & 0b11):
        num >>= 2
    return (num == 1)

#Examples
print(is_power_of_four(256)) #output is True
print(is_power_of_four(63))  #output is false