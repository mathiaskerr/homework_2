# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
even_num = []

for num in numbers:
    if num % 2 == 0 :
        even_num.append(num)
print(even_num)       

# 2. Print the difference between the largest and smallest value:
highest_num = 0
lowest_num = 100
for num in numbers:
    if num > highest_num :
        highest_num = num
print(highest_num)
for num in numbers:
    if num < lowest_num:
        lowest_num = num
print(lowest_num)        
total = highest_num - lowest_num
print(total)

# 3. Print True if the list contains a 2 next to a 2 somewhere.
num = 0
for i in numbers:
    if i == num:
        print(True)
    if i == 2:
        num = i
# not sure if this is correct

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22


# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 






