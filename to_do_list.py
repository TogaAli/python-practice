todo_list=[]
running=True

while running:
    task=input("Enter a task (type quit to stop): ")

    if task=="quit":
        running=False
    else:
        todo_list.append(task)
        print(f"Current list: {todo_list}")

print(f"Final to-do list: {todo_list}")

