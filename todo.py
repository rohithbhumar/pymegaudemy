list_of_todos = []

while True:
    actions = input('Type add, edit, show, done, exit: ')
    actions = actions.lower()

    match actions:
        case 'add':
            task = input('Enter a to-do task: ')
            list_of_todos.append(task.lower())

        case 'show' | 'display':
            if list_of_todos:
                for index, todo in enumerate(list_of_todos, start=1):
                    print(index, todo)

            else:
                print('List is empty. Add a task to show!')

        case 'edit':
            number_todo = int(input('Enter the number to edit: '))
            number_todo = number_todo - 1
            editable = list_of_todos[number_todo]
            confirms = input(f'Are you use you want edit {editable.capitalize()}?: [y] or [n] ')
            if confirms.lower() == 'y':
                new_edit = input('Enter the new to-do: ')
                list_of_todos[number_todo] = new_edit
                # list_of_todos.__setitem__(number_todo, new_edit)
                print(list_of_todos)
            else:
                pass

        case 'done':
            number = int(input('Enter the task number to be completed: ')) - 1
            task = list_of_todos[number]
            print(task)
            list_of_todos.remove(task)

        case 'exit' | 'clear':
            break

        case _:
            print('Hey, enter a valid command!')

print('Bye!')

# list_of_todos = []
#
# while True:
#     action = input('Type add, show, exit: ').lower()
#
#     if action == 'add':
#         todo = input('Enter a todo task: ')
#         list_of_todos.append(todo)
#
#     elif action == 'show':
#         for todo in list_of_todos:
#             print(todo.capitalize())
#
#     elif action == 'exit':
#         print('Bye')
#         break
#
#     else:
#         print('Hey, enter a valid command!')

