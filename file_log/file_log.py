"""Decorator to register functions execution in a log"""

import time
def file_log(func):
    """Registers the execution of a funcion in a log file"""
    def wrapper(*args, **kwargs):

        with open("file_log/log.txt", "a", encoding="utf-8") as file:
            func(*args, **kwargs)
            times = time.strftime("%d-%m-%Y %H:%M:%S")
            file.write(f"[{times}] The function <{func.__name__}> was executed.\n")
    return wrapper

@file_log
def send_email(recipient: str) -> None:
    """Simulates sending an email to the specified recipient."""

    print(f"Sending email to {recipient}...")


@file_log
def calculate_salary(worked_hours: int, hourly_rate: float) -> None:
    """Calculates an employee's salary based on worked hours and hourly rate."""

    print(f"The employee's salary is {worked_hours * hourly_rate}.")


if __name__ == "__main__":
    send_email("joao@example.com")
    calculate_salary(200, 30.5)
    send_email("joao@example.com")
