def highest_occurrence_char(input_string):
#  an empty dictionary is intialized to store character with corresponding count
    frequency = {}

    for char in input_string:
#check the character is aplhabet or not(if it number or symbol it ignores)
        if char.isalpha():
#converts it lower to take capitsl or small letter same only
            char = char.lower()
# Update the count of the character in the dictionary and if it is not present it intialize to zero         
            frequency[char] = frequency.get(char, 0) + 1

    if not frequency:
        return None, 0

    max_char = max(frequency, key=frequency.get)
#return the max_char with highest frequency count
    return max_char, frequency[max_char]

input_string = "hippopotamus"
char, count = highest_occurrence_char(input_string)
print("Highest occurring character:", char)
print("Occurrence count:", count)