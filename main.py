import sys
def remove_duplicates(word):
    result = ""
    seen = set()  # To keep track of seen characters
    for char in word:
        if char not in seen:
            result += char
            seen.add(char)
    return result

def add_key_1(key_1,alphabet):
    code_word = []
    for letter in word:
        for key in alphabet:
            if letter == alphabet[key]:
                index = (key + int(key_1)) % 26
                code_word.append(index)

    return code_word

def remove_key_1(key_1,alphabet):
    code_word = []
    for letter in word:
        for key in alphabet:
            if letter == alphabet[key]:
                index = (key - int(key_1)) % 26
                code_word.append(index)

    return code_word

def add_key_2(key_2):
    alphabet = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L'
        , 12: 'M', 13: 'N', 14: 'O', 15: "P", 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W'
        , 23: 'X', 24: 'Y', 25: 'Z'}
    for letter in key_2:
        for key in alphabet:
            if letter == alphabet[key]:
                alphabet[key] = None

    for key in alphabet:
        if alphabet[key] == None:
            temp_key = key
            while ((temp_key != 0) and (alphabet[temp_key - 1] != None)):
                alphabet[temp_key] = alphabet[temp_key - 1]
                alphabet[temp_key - 1] = None
                temp_key = temp_key - 1

    for letter in range(0, len(key_2)):
        alphabet[letter] = key_2[letter]

    return alphabet

def input_word():
    while (True):
        try:
            word = input("enter the msg: ")
            word = word.replace(' ', '')
            word = word.upper()
            for letter in word:
                if letter not in alphabet.values():
                    raise ValueError("the msg must only contain latin characters!")
            break
        except ValueError as e:
            print(e)
    return word

def input_key_1():
    while (True):
        try:
            key_1 = input("enter key 1: ")
            if key_1.isnumeric():
                pass
            else:
                raise ValueError("key_1 must only contain numbers")
            break
        except ValueError as e:
            print(e)
    return key_1

def input_key_2():
    while (True):
        try:
            key_2 = input("enter key 2(optional): ")
            key_2 = key_2.replace(' ', '')
            key_2 = key_2.upper()
            key_2 = remove_duplicates(key_2)
            for letter in key_2:
                if letter not in alphabet.values():
                    raise ValueError("key 2 must only contain latin characters!")
            break
        except ValueError as e:
            print(e)
    return key_2

def generate_word(decripted_word,alphabet):
    word = ''
    print(decripted_word)
    if decripted_word:
        for key in decripted_word:
            word = word + alphabet[key]
    return word







choice = '4'
while(True):
    alphabet = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L'
        , 13: 'M', 14: 'N', 15: 'O', 16: "P", 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W'
        , 24: 'X', 25: 'Y', 26: 'Z'}
    print('''1.Decript a message
2.Encript a message
3.Exit''')
    choice = input("enter your choice: ")
    if int(choice) == 1:
        word = input_word()
        key_1 = input_key_1()
        key_2 = input_key_2()

        alphabet = add_key_2(key_2)
        decripted_word = remove_key_1(key_1,alphabet)
        word = generate_word(decripted_word,alphabet)
        print(word)
        print(alphabet.values())


    elif int(choice) == 2:
        word = input_word()
        key_1 = input_key_1()
        key_2 = input_key_2()

        alphabet = add_key_2(key_2)
        encripted_word = add_key_1(key_1,alphabet)
        word = generate_word(encripted_word,alphabet)
        print(word)
        print(alphabet.values())
    elif int(choice) == 3:
        break



    else:
        print("the input must be a number between 1 and 3 !!")





