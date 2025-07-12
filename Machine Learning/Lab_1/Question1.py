#taking a list 
list1= [2, 7, 4, 1, 3, 6]
#creating a empty list ,later we append the pair whose sum is equal to 10 
pairs = []
for i in range(len(list1)):
    for j in range(i + 1, len(list1)):
#check the corresponding two numbers sum is equal to 10  we add the pair to pairs list
     if list1[i] + list1[j] == 10:
            pairs.append((list1[i], list1[j]))
print("Pairs with sum 10:", pairs)
print("Number of pairs:", len(pairs))

