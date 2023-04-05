"""
This module contains controller
"""

from models import Worker, Manager, Unit


# "First_Name", "Middle_Name", "Last_Name", "Login", "Password", 1, 100


def main() -> None:
    """
    Main func of this module
    """
    pass


def storage_access(func):
    """
    Custom decorator about security for storage - only stuff
    """

    def wrapper(user, *args, **kwargs):
        if user.__class__ is Worker or user.__class__ is Manager:
            func(user, *args, **kwargs)
    return wrapper


if __name__ == "__main__":
    main()
