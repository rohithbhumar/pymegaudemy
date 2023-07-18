import json
from pprint import pprint

with open('textfiles/quiz-data.json') as file:
    content = file.read()

data = json.loads(content)

# print(type(data))
# pprint(data)

score = 0
for question in data:
    print(question['question_text'])
    for i, option in enumerate(question['options'], start=1):
        print(f'{i}. {option}')

    try:
        user_data = int(input('Enter the choice: '))
        if user_data == question['correct_answer']:
            print('You are right!')
            score = score+1
        else:
            print('You are wrong!')
    except ValueError as e:
        print('Enter a number choice only!')


print(f'You score is: {round(score/len(data)*100)}%')
