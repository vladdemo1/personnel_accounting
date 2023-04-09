"""
This module contains all models for the program
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


class Worker(Unit):
    """
    Worker - base unit
    """

    @staticmethod
    def came_to_the_office() -> None:
        """
        This func register when unit came to office
        """
        pass

    @staticmethod
    def register_activity() -> None:
        """
        This func register current employee activity
        """
        pass

    @staticmethod
    def left_the_office() -> None:
        """
        This func register when unit left the office
        """
        pass

    @staticmethod
    def get_work_hours() -> None:
        """
        This func return current count hours at work in office
        """
        pass

    @staticmethod
    def get_work_time() -> None:
        """
        This func return how long and when the employee worked
        """
        pass

    @staticmethod
    def get_salary() -> None:
        """
        This func return current salary of this unit
        """
        pass


class Manager(Unit):
    """
    Manager - middle unit
    """

    @staticmethod
    def show_worker_reporting(personnel_number: int) -> None:
        """
        This func return reporting about worker by personnel number
        """
        pass

    @staticmethod
    def set_premium_for_worker(personnel_number: int) -> None:
        """
        This func set premium for current worker by personnel number
        """
        pass

    @staticmethod
    def set_new_worker() -> None:
        """
        This func can create new worker for office
        """
        pass

    @staticmethod
    def fire_worker() -> None:
        """
        This func can throw out of the window of the office -> worker
        """
        pass

    @staticmethod
    def set_new_index_salary(new_salary_index: float) -> None:
        """
        This func can change salary index
        """
        pass


class SalaryIndex:
    """
    This class contains salary index and functions about this process
    """
    pass


if __name__ == '__main__':
    pass
