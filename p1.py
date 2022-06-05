#Write a Python function to sum all the numbers in a list 

total = 0
ele = 0

#describe the contents of the list
list1 = [1, 5, 2, 4, 3]

while ele < len(list1):
    total = total + list1[ele]
    ele += 1

print(total)