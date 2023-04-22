"""
This module contains base model for Worker and Manager
"""

from random import randint


class Unit:
    """
    Base model for Worker and Manager
    """

    def __init__(self, first_name: str, middle_name: str, last_name: str,
                 login: str, password: str, personnel_number: int, payroll_number: int) -> None:
        self._first_name = first_name
        self._middle_name = middle_name
        self._last_name = last_name
        self._login = login
        self._password = password  # TODO create password hashing
        self._personnel_number = self._check_number(number=personnel_number)
        self._payroll_number = self._check_number(number=payroll_number)

    @staticmethod
    def _check_number(number: int) -> int:
        """
        Check if number has correct size
        """
        return number if 1_000_000 > number > 0 else randint(1, 1_000_000)

    @property
    def full_name(self) -> dict:
        """Get full name of person"""
        return {
            "first_name": self._first_name,
            "second_name": self._middle_name,
            "last_name": self._last_name,
        }

    @property
    def login(self) -> str:
        """
        Get personal login
        """
        return self._login

    @property
    def personnel_number(self) -> int:
        """
        Get personal number
        """
        return self._personnel_number

    @property
    def payroll_number(self) -> int:
        """
        Get payroll_number of current unit
        """
        return self._payroll_number


if __name__ == '__main__':
    pass
