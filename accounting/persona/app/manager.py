"""
This module contains model Manager - middle unit
"""

from unit import Unit


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


if __name__ == '__main__':
    pass
