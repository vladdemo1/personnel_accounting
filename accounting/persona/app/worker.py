"""
This module contains model Worker - base unit
"""

from unit import Unit


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


if __name__ == '__main__':
    pass
