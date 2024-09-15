braille_to_english = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y', 'O..OOO': 'z',
    '......': ' ', '.....O': 'capital', '.O.OOO': 'number'
}

english_to_braille = {v: k for k, v in braille_to_english.items() if v != 'capital' and v != 'number'}
# print(english_to_braille)

braille_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}
number_to_braille = {v: k for k, v in braille_numbers.items()}
# print(number_to_braille)

def is_braille(input_string):
    result = False
    for char in input_string:
        # check if the input value in 0 or .
        if char not in '0.':
            result=  False
        else:
            result = True
    return result

# Convert Braille to English
def braille_to_text(braille_string):
    result = []
    i = 0
    capital = False
    number_mode = False
    
    while i < len(braille_string):
        char = braille_string[i:i+6]
        i += 6
        
        if char == '.....O': #capital case
            capital = True
            continue
        elif char == '.O.OOO':  #number case
            number_mode = True
            continue
        elif char == '......': #space
            result.append(' ')
            number_mode = False
            continue
        
        if number_mode:
            # Convert Braille to a number
            letter = number_to_braille.get(char)
       
        else:
            # Convert Braille to a letter
            letter = braille_to_english.get(char)
           
            if capital:
                letter = letter.upper()  # Capitalize case
                capital = False
        
        result.append(letter)
    
    return ''.join(result)

         

# Convert English to Braille
def text_to_braille(text):
    finalResult = []
    isNumber = 0
    for char in text:
        if char == ' ': #space case
            finalResult.append('......')  
        elif char.isdigit():  #number case
            if(isNumber >= 1):
                finalResult.append(braille_numbers[char])
            else:
                isNumber = isNumber + 1
                finalResult.append('.O.OOO')  # Number indicator
                finalResult.append(braille_numbers[char])
            
        elif char.isupper():  # Capital letters
            finalResult.append('.....O')  # Capital indicator
            finalResult.append(english_to_braille[char.lower()])
        else:
            finalResult.append(english_to_braille[char])
    
    return ''.join(finalResult)


# main funtion 
def translate(input_value):
    if is_braille(input_value):
        return braille_to_text(input_value)
    else:
        return text_to_braille(input_value)

# test_1
braille_input = "Hello world"
english_output = translate(braille_input)
print(english_output)


# test_2
braille_input = "42"
english_output = translate(braille_input)
print(english_output)

# test_3
braille_input = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."
english_output = translate(braille_input)
print(english_output) 

