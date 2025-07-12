def find_range(numbers):
    if len(numbers) < 3:
        #if the length of the number(list) is less than 3 it will return the statement
        return "Range determination not possible"
#it returns the difference of maximum number of the numbers list to the minimum number of the numbers list
    return max(numbers) - min(numbers)

#taking input for number list
numbers = list(map(int, input("Enter the numbers  ").split()))
result = find_range(numbers)
print(f'Range={max(numbers)}-{min(numbers)}={result}')
