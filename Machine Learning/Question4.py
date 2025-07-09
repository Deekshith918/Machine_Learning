def highest_occurrence_char(input_string):
    frequency = {}

    for char in input_string:
        if char.isalpha():
            char = char.lower()
            frequency[char] = frequency.get(char, 0) + 1

    if not frequency:
        return None, 0

    max_char = max(frequency, key=frequency.get)
    return max_char, frequency[max_char]

input_string = "hippopotamus"
char, count = highest_occurrence_char(input_string)
print("Highest occurring character:", char)
print("Occurrence count:", count)