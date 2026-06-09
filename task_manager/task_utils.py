from datetime import datetime
from .validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date,
)

# Shared tasks list — imported and used by main.py
tasks = []


def add_task(title, description, due_date):
    """
    Validate inputs and append a new task dict to the tasks list.
    Raises ValueError (from validation) if any field is invalid.
    """
    title       = validate_task_title(title)
    description = validate_task_description(description)
    due_date    = validate_due_date(due_date)

    task = {
        "title":       title,
        "description": description,
        "due_date":    due_date,
        "completed":   False,
    }
    tasks.append(task)
    print("Task added successfully!")


def mark_task_as_complete(index, tasks=tasks):
    """
    Mark the task at the given 1-based index as complete.
    Raises ValueError if the index is out of range or the task is already done.
    """
    if not tasks:
        raise ValueError("There are no tasks to mark as complete.")
    if not isinstance(index, int) or index < 1 or index > len(tasks):
        raise ValueError(f"Invalid index. Enter a number between 1 and {len(tasks)}.")
    task = tasks[index - 1]
    if task["completed"]:
        raise ValueError(f"'{task['title']}' is already marked as complete.")
    task["completed"] = True
    print("Task marked as complete!")


def view_pending_tasks(tasks=tasks):
    """
    Print all tasks whose 'completed' field is False.
    Returns the list of pending tasks.
    """
    pending = [t for t in tasks if not t["completed"]]
    if not pending:
        print("No pending tasks.")
    else:
        print("\nPending Tasks:")
        print("-" * 40)
        for i, task in enumerate(pending, start=1):
            print(f"{i}. {task['title']}")
            print(f"   Description : {task['description'] or '(none)'}")
            print(f"   Due         : {task['due_date']}")
        print("-" * 40)
    return pending


def calculate_progress(tasks=tasks):
    """
    Calculate and print the percentage of completed tasks.
    Returns the progress as a float (0.0 – 100.0).
    """
    if not tasks:
        print("No tasks found.")
        return 0.0

    completed = sum(1 for t in tasks if t["completed"])
    progress  = (completed / len(tasks)) * 100

    print(f"\nProgress: {completed}/{len(tasks)} tasks complete ({progress:.1f}%)")
    bar_len = 30
    filled  = int(bar_len * progress / 100)
    print("[" + "█" * filled + "░" * (bar_len - filled) + "]")

    return progress