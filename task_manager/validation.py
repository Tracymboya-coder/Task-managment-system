from datetime import datetime


def validate_task_title(title):
    if not isinstance(title, str) or not title.strip():
        raise ValueError("Title cannot be empty.")
    title = title.strip()
    if len(title) > 100:
        raise ValueError("Title must be 100 characters or fewer.")
    return title


def validate_task_description(description):
    if not isinstance(description, str):
        raise ValueError("Description must be a string.")
    description = description.strip()
    if len(description) > 500:
        raise ValueError("Description must be 500 characters or fewer.")
    return description


def validate_due_date(due_date):
    if not isinstance(due_date, str) or not due_date.strip():
        raise ValueError("Due date cannot be empty.")
    due_date = due_date.strip()
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Due date must be in YYYY-MM-DD format (e.g. 2024-06-26).")
    return due_date