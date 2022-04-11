# Program to remove duplicates
fist = [1, 3, 4, 8, 7, 8, 3, 5, 4]
print("Original list: " + str(fist))
mes = []
for i in fist:
    if i not in mes:
        mes.append(i)

print("New list: " + str(mes))



# Function to remove duplicates. Option 2
def remove(m):
    return list(dict.fromkeys(m))

youList = remove(["a", "d", "c", "o", "a", "d"])

print(youList)