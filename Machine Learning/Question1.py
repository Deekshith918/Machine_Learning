list1= [2, 7, 4, 1, 3, 6]
pairs = []
for i in range(len(list1)):
    for j in range(i + 1, len(list1)):
     if list1[i] + list1[j] == 10:
            pairs.append((list1[i], list1[j]))
print("Pairs with sum 10:", pairs)
print("Number of pairs:", len(pairs))


