class SalaryCalculator:
    """
    Method to calculate the salary of an employee
    """
    @staticmethod
    def get_salary(emp):
        allowance = SalaryCalculator.get_allowance(emp)
        return emp.basic + emp.hra + allowance

    """
    Method to get the allowance for an employee based on the percentage
    """
    @staticmethod
    def get_allowance(emp):
        return emp.basic * emp.allowance_percentage / 100.0
