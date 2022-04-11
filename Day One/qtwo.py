# COUNTING THE LAST WORD IN A SENTENCE
str = input("Enter Sentence: ")

def convert(str):
    li = list(str.split(" "))
    return li

str_list = convert(str)
print(len(str_list[-1]))