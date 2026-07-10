#Create task list with functions to add/remove items

# tasks = []
#
# def addTask():
#     task = input("Enter tasks (comma separated): ")
#     return task.split(",")
#
# def remove_task(tasks):
#     task = input("Enter task to remove: ")
#     if task in tasks:
#         tasks.remove(task)
#     else:
#         print("Task not found!")
#     return tasks
#
# tasks=addTask()
# tasks=remove_task(tasks)
#
# print(f"Remaining task {tasks}")

#Build dictionary for book titles and authors
books = {}
def addBook():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    books[title] = author

def showBooks():
    print(books)

addBook()
showBooks()