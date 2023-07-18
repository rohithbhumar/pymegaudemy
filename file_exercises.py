##########################################
import os

contents = ["All carrots are tobe sliced longitudinally.",
            "The carrots were reportedly sliced",
            "The slicing was smooth"]
filenames = ["doc.txt", "report.txt", "presentation.txt"]

# with open('textfiles/doc.txt', 'w') as doc:
#     doc.writelines(contents[0])
#
# with open('textfiles/report.txt', 'w') as doc:
#     doc.writelines(contents[1])
#
# with open('textfiles/presentation.txt', 'w') as doc:
#     doc.writelines(contents[2])

# OR

print(list(zip(contents, filenames)))
for content, filename in zip(contents, filenames):
    print(content, filename)
    with open(f'textfiles/{filename}', 'w') as file:
        file.writelines(content)

# Open your computer IDE and place the following in a Python file:
# filenames = ['doc.txt', 'report.txt', 'presentation.txt']
# Then, create a program that:
# 1. generates multiple text files by iterating over the filenames list,
# 2. and writes the text Hello  inside each generated text file.

filenames = ['doc.txt', 'report.txt', 'presentation.txt']
text = "Hello"

for filename in filenames:
    with open(f'textfiles/{filename}', 'w') as file:
        file.writelines(text)

#######################################################
textfiles = []
with os.scandir('textfiles/') as files:
    for file in files:
        if file.is_file():
            textfiles.append(f'textfiles/{file.name}')
    # textfiles = [file.name for file in files if file.is_file()]

print(textfiles)
for file_name in textfiles:
    with open(file_name, 'r') as file:
        print(file.read())

names = ["1.doc", "1.report", "1.presentation"]
new_names = [name.replace('.', '-') + '.txt' for name in names]
print(new_names)

# for name in names:
#     nam = name.split('.')
#     mod_nam = '-'.join(nam)
#     new_names_list.append(mod_nam + '.txt')
#
# print(new_names_list)

# Extend the given code (in the exercise area) so the code capitalizes
# all the names and surnames of the list and then prints the new list.
# The output of your code should be as below: ['John Smith', 'Jay Santi', 'Eva Kuki']

names = ["john smith", "jay santi", "eva kuki"]
new_names = [name.title() for name in names]
print(new_names)

# Extend the given code so the code prints out a list containing the number of characters for each username.
# The output of your code should be as below:
# [9, 11, 11]
usernames = ["john 1990", "alberta1970", "magnola2000"]
print([len(name) for name in usernames])

# SUM
user_entries = ['10', '19.1', '20']

converted = [float(item) for item in user_entries]
print(sum(converted))

# Write a program that:
# 1. asks users to enter a password.
# 2. returns "Great password there!" if the password has more than 7 characters.
# For example: Enter a new password: my_cool_password3001
# Great password there!
# 3. returns "Your password is weak." if the password has 7 or fewer characters. For example:


result_dic = {"length": False, "digit": False, "upper": False, "spl": False}
spl_char = "!@#$%~^&*()_+={}][|/?"
password = input('Enter the password to check for strength: ')

if len(password) >= 7:
    result_dic["length"] = True
else:
    result_dic["length"] = False

for i in password:
    if i.isdigit():
        result_dic["digit"] = True

for i in password:
    if i.isupper():
        result_dic["upper"] = True

for i in password:
    if i in spl_char:
        result_dic["spl"] = True

print(result_dic)

if all(result_dic.values()):
    print('Great Password')
else:
    print('Weak Password')
###########################################################################
string = "Enter a paragraph hit a ball Bob hit a ball of a new bar bat"

dic = {}
banned_word = ['hit', 'ball']

for word in string.split():
    if word not in dic:
        dic[word] = 1
    else:
        dic[word] += 1

print(dic)

# max_value = max(dic.values())
# print(max_value)

max_freq = 0
result = ''

for word, freq in dic.items():
    if word not in banned_word and freq > max_freq:
        max_freq = freq
        result = word


print(result, max_freq)


