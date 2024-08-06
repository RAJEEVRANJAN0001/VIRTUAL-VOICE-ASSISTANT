# from utilities import takeCommand, speak
#
#
# def clear_old_tasks():
#     with open("tasks.txt", "w") as file:
#         file.write("")  # Clearing old tasks
#     speak("Old tasks cleared.")
#
#
# def add_tasks(num_tasks):
#     tasks = []
#     for i in range(num_tasks):
#         speak(f"Please say task number {i + 1}")
#         task = takeCommand()
#         tasks.append(task)
#         with open("tasks.txt", "a") as file:
#             file.write(f"{i + 1}. {task}\n")
#     return tasks
#
#
# def remove_task():
#     with open("tasks.txt", "r") as file:
#         tasks = file.readlines()
#
#     speak("Here are the tasks for today:")
#     for task in tasks:
#         speak(task.strip())
#
#     speak("Please say the number of the task you want to remove.")
#     task_number = int(takeCommand())
#
#     with open("tasks.txt", "w") as file:
#         for i, task in enumerate(tasks, start=1):
#             if i != task_number:
#                 file.write(task)
#
#     speak(f"Task {task_number} removed.")
#
#
# def display_schedule():
#     with open("tasks.txt", "r") as file:
#         tasks = file.read()
#     speak("Here are the tasks for today:")
#     speak(tasks)
#
#
# def schedule_my_day():
#     speak("Would you like to clear old tasks? Please say YES or NO")
#     query = takeCommand().lower()
#     if "yes" in query:
#         clear_old_tasks()
#
#     speak("How many tasks would you like to schedule?")
#     num_tasks = int(takeCommand())
#
#     tasks = add_tasks(num_tasks)
#
#     speak("Tasks scheduled successfully.")
#
#     display_schedule()
#
#     speak("Do you want to remove any completed tasks? Please say YES or NO")
#     query = takeCommand().lower()
#     if "yes" in query:
#         display_schedule()
#         speak("Please say the number of the completed task to remove")
#         task_number = int(takeCommand())
#         remove_task(task_number)
#
#
# schedule_my_day()
