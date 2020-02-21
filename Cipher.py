import numpy as np

# Transposition Cipher Function
def transposition(string):
    print('\n[TRANSPOSITION CIPHER]')
    # taking the key input for transposition cipher
    key = int(input('Select the key:\n1.reverse\n2.odd even\nYour Choice: '))
    # if else for each key type
    if key == 1:
        string = string[::-1] # reversing the string
    elif key == 2:
        str1 = string[::2] # Even indexes
        str2 = string[::-2] # Reversed Odd indexes
        string = str1 + str2[::-1] # add even+odd(reversed)
    # returning results
    return string, key

# function for shift cipher
def shift(string):
    # list to store ascii values of characters
    ascii_list =[]
    print('\n[SHIFT CIPHER]')
    key = int(input("Enter The Key: ")) # getting the key
    for i in string: # converting the characters to 0-25
        # using ord to get ascii values, subtract 65 to get values b/w 0-25
        ascii_list.append(ord(i)-65) # add to the list we made
    # covert to np array and add key, the mod 26
    # using numpy because it save you from mannualy coding
    ascii_list = (np.array(ascii_list) + key)%26

    charlst = [] # list for storing chars
    for i in ascii_list:
        # chr to get char from ascii value
        # add 65 since we subtracted it before
        charlst.append(chr(i+65))

    # logic from converting list to string
    cipher = ''
    for char in charlst:
        cipher += char
    
    return cipher, key # returning results

# main function in python
if __name__ == "__main__":
    # open the file, using f as file pointer in write mode
    f = open('data.txt', 'w')
    # got the input
    print('[MAIN INPUT]')
    message = input('Enter the message: ')
    f.write(message) # write to file
    f.close() # close the file
    # function call for ciphers
    cipher, shiftKey = shift(message)
    cipher, transKey = transposition(cipher)
    # open the file, using f as file pointer in write mode
    f = open('data.txt', 'w')
    f.write(cipher) # write to file
    print(f'\n[CIPHERED TEXT] {cipher}')
    f.close() # close the file
