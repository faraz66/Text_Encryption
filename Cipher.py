import numpy as np
def transposition(string):
    key = int(input('Select the key:\n1.reverse\n2.odd even'))
    if key == 1:
        string = string[::-1]
    elif key == 2:
        str1 = string[::2]
        str2 = string[::-2]
        string = str1 + str2[::-1]
    # print(string)
    return string


def shift(string):
    ascii_list =[]
    key=int(input("Enter The Key"))
    for i in string:
        ascii_list.append(ord(i)-65)
    ascii_list = (np.array(ascii_list) + key)%26
    # print(ascii_list
    charlst = []
    for i in ascii_list:
        charlst.append(chr(i+65))
    print(charlst)





# f = open('data.txt', w+)
message = input('Enter the message: ')
# f.write(message)
# cipher = transposition(message)
cipher = shift(message)
