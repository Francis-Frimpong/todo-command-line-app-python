file = 'todos.txt'
choose_options = ['Add-Todos', 'Display-Todos','Exit']
print(choose_options)
while True:

    # choose your options
    input_option = input('Choose your option: ')
    # input data only if options == 'input-todos
    if input_option == 'input-todos':
        todo_input = input('Add your todos')
        with open('todos.txt', 'a') as file:
            file.write(f'\n{todo_input}')

    # display input date or text
    elif input_option == 'display-todos':
        with open('todos.txt', 'r') as file:
            content = file.read()
            print(content)
            
    # exit
    else:
        exit()
