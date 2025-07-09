def find_range(numbers):
    if len(numbers) < 3:
        return "Range determination not possible"
    return max(numbers) - min(numbers)


numbers = list(map(int, input("Enter the numbers  ").split()))

result = find_range(numbers)
print(f'Range={max(numbers)}-{min(numbers)}={result}')
