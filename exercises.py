#######################################################################
# The ranking list given in the coding area represents the ranking of three athletes, John, Sen, and Lisa. John won 1st
# place, Sen got 2nd, and Lisa 3rd.
#
# Your task is to create a program that:
#
# 1. Contains the above list.
#
# 2. Prompts the user to input a rank number.
#
# 3. Returns the person who has the given rank.

rank_names_list = ["John", "Sen", "Lisa"]

rank_num = int(input("Enter the rank number: "))
if rank_num == 0:
    print('0 is not a valid rank')

elif rank_num <= len(rank_names_list):
    print(rank_names_list[rank_num - 1])

else:
    print('That rank does not exist')

#######################################################################
# Your task is to create a program that:
#
# 1. Contains the above list.
#
# 2. Prompts the user to input the name.
#
# 3. Returns the rank who has the given name.

rank_name = input("Enter a name: ")
if rank_name in rank_names_list:
    standing = rank_names_list.index(rank_name) + 1
    print(standing)
else:
    print('NO such name')
#######################################################################
# Create three variables mood, strength, and rank
# and assign a string to mood, a float to strength, and an integer to rank.
# The values you assign can be anything as long as they are of the correct type.

mood = "moody"
strength = 10.56
rank_names_list = 1

#######################################################################
# Create a color_codes variable and assign a tuple to it. The tuple should contain three tuples as items.
# The three tuples can contain any type of data inside them.
# In other words, your variable should be equal to a tuple of tuple of three items each.
color_codes = (("ad", 10, 90.5), (10, "rad", "45"), (12.3, 4, 54))

#######################################################################
# String immutability
my_str = "I have 0 balls"
print(my_str[0])
position_of_zero = my_str.index('0')
print(position_of_zero)

print(my_str.replace('0', '8', 1))

#######################################################################
# We have a list of three strings defined in the code area.
#
# Extend the code so your program prints out the following out of that list:
#
# 0-Document.txt
# 1-Report.txt
# 2-Presentation.txt

filenames = ['document', 'report', 'presentation']
for index, item in enumerate(filenames):
    print(f'{index}-{item.capitalize()}.txt')

#######################################################################
# We have a list of two IPs in the code area.
#
# Extend the code so your program:
#
# 1. Prompts the user to input an index (e.g., 0 or 1).
#
# 2. Depending on the user input, the program should return either You chose 100.122.133.111 or You chose 100.122.133.111
ips = ['100.122.133.105', '100.122.133.111']
numer = int(input('Enter 0 or 1: '))
print(ips[numer])

# Iterating through multiple items
buttons = [('John', 'Sen', 'Morro'), ('Lin', 'Ajay', 'Filip')]
for index, items in enumerate(buttons):
    print(index, items)
    for i, j in enumerate(items):
        print(i, j)

