# Step 1: Importing necessary libraries for the Task Management App
import pandas as pd  # Importing the pandas library to handle data
from sklearn.feature_extraction.text import CountVectorizer  # Importing CountVectorizer for processing text
from sklearn.naive_bayes import MultinomialNB  # Importing the Multinomial Naive Bayes classifier
from sklearn.pipeline import make_pipeline  # Importing make_pipeline to create a task pipeline
import random  # Importing the random library for generating random recommendations

# Step 2: Initializing an empty DataFrame to store tasks
tasks = pd.DataFrame(columns=['description', 'priority'])  # Creating an empty DataFrame to store task information

# Step 3: Attempting to load pre-existing tasks from a CSV file
try:
    tasks = pd.read_csv('tasks.csv')  # Trying to load existing tasks from 'tasks.csv' file
except FileNotFoundError:
    pass  # If file not found, continue with an empty DataFrame

# Step 4: Definition of a function to save the current task list to a CSV file
def save_tasks():
    tasks.to_csv('tasks.csv', index=False)  # Saving the current task list to 'tasks.csv' file without index

# Step 5: Training a machine learning model to predict task priorities
vectorizer = CountVectorizer()  # Initializing CountVectorizer for text vectorization
clf = MultinomialNB()  # Initializing Multinomial Naive Bayes classifier
model = make_pipeline(vectorizer, clf)  # Creating a pipeline for text classification
model.fit(tasks['description'], tasks['priority'])  # Training the model using existing task data

# Step 6: Definition of a function to add a new task to the task list
def add_task(description, priority):
    global tasks  # Accessing the global tasks DataFrame
    new_task = pd.DataFrame({'description': [description], 'priority': [priority]})  # Creating a DataFrame for the new task
    tasks = pd.concat([tasks, new_task], ignore_index=True)  # Adding the new task to the tasks DataFrame
    save_tasks()  # Saving the updated task list to 'tasks.csv' file

# Step 7: Definition of a function to remove a task from the task list
def remove_task(description):
    global tasks  # Accessing the global tasks DataFrame
    tasks = tasks[tasks['description'] != description]  # Removing the task with the specified description
    save_tasks()  # Saving the updated task list to 'tasks.csv' file

# Step 8: Definition of a function to list all tasks in the task list
def list_tasks():
    if tasks.empty:
        print("No tasks available.")  # Printing a message if the task list is empty
    else:
        print(tasks)  # Printing the tasks DataFrame

# Step 9: Definition of a function to recommend a task based on machine learning
def recommend_task():
    if not tasks.empty:  # Checking if the task list is not empty
        high_priority_tasks = tasks[tasks['priority'] == 'High']  # Filtering high-priority tasks
        if not high_priority_tasks.empty:  # If there are high-priority tasks
            random_task = random.choice(high_priority_tasks['description'])  # Choosing a random high-priority task
            print(f"Recommended task: {random_task} - Priority: High")  # Printing the recommended task
        else:
            print("No high-priority tasks available for recommendation.")  # Printing a message if no high-priority tasks
    else:
        print("No tasks available for recommendations.")  # Printing a message if the task list is empty

# Step 10: Main menu loop to interact with the Task Management App
while True:
    print("\nTask Management App")  # Displaying the title of the application
    print("1. Add Task")  # Displaying menu option to add a new task
    print("2. Remove Task")  # Displaying menu option to remove an existing task
    print("3. List Tasks")  # Displaying menu option to list all tasks
    print("4. Recommend Task")  # Displaying menu option to recommend a task
    print("5. Exit")  # Displaying menu option to exit the application

    choice = input("Select an option: ")  # Prompting the user to select an option from the menu

    if choice == "1":  # If the user selects option 1
        description = input("Enter task description: ")  # Prompting the user to enter task description
        priority = input("Enter task priority (Low/Medium/High): ").capitalize()  # Prompting the user to enter task priority
        add_task(description, priority)  # Calling the add_task function to add the new task
        print("Task added successfully.")  # Displaying a success message

    elif choice == "2":  # If the user selects option 2
        description = input("Enter task description to remove: ")  # Prompting the user to enter task description to remove
        remove_task(description)  # Calling the remove_task function to remove the specified task
        print("Task removed successfully.")  # Displaying a success message

    elif choice == "3":  # If the user selects option 3
        list_tasks()  # Calling the list_tasks function to list all tasks

    elif choice == "4":  # If the user selects option 4
        recommend_task()  # Calling the recommend_task function to recommend a task

    elif choice == "5":  # If the user selects option 5
        print("Goodbye!")  # Displaying a farewell message
        break  # Exiting the main menu loop and ending the program

    else:  # If the user selects an invalid option
        print("Invalid option. Please select a valid option.")
