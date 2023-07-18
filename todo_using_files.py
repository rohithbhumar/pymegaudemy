import os

while True:

    up = input('Enter add to add a task or done to remove a task: ')

    if up == 'add':

        task = input('Enter the task to be added: ')
        task = task.strip()

        if os.path.exists('todo.txt'):
            with open('todo.txt', 'a') as todo_file:
                todo_file.writelines(task + '\n')

        else:
            with open('todo.txt', 'w') as todo_file:
                todo_file.writelines(task + '\n')

        with open('todo.txt', 'r') as todo_file:
            todo_items = todo_file.readlines()
            enu_items = enumerate(todo_items)
            # print(dict(enu_items))
            for i, item in enu_items:
                print(i, item, end="")

    elif up == 'done':
        if os.path.exists('todo.txt'):
            with open('todo.txt', 'r') as todo_file:
                todo_items = todo_file.readlines()
                for i, j in enumerate(todo_items):
                    print(i, j, end="")
            remove_index = int(input('Enter the number to remove the task: '))

            if remove_index <= len(todo_items):
                task_to_be_removed = todo_items[remove_index]
                todo_items.remove(task_to_be_removed)
                # or just use -> del todo_items[remove_index]
                print(todo_items)

                with open('todo.txt', 'w') as todo_file:
                    todo_file.writelines(todo_items)
            else:
                print('Choose the number from the list of tasks')

    elif up == 'break':
        break

    else:
        print('Enter a valid command!')

print('Bye!')

