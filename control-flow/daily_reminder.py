task = input("Enter your task description: ")
priority = input("Enter the priority level (high/medium/low): ")
time_bound = input("Is your task time-bound (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high-priority task that requires immediate attention today!")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium-priority task that should be completed soon.")
    case "low":
        if time_bound == "no":
            print(f"Note: '{task}' is a low-priority task. Consider completing it when you have free time.")
    case _ :
        print(f"Reminder: '{task}' has an unrecognized priority or time-bound value.")