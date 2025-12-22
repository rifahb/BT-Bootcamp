from employee import Employee
from role_builder import RoleBuilder

class EmployeeReport:
    """
    Property of the class
    """
    def __init__(self, report_date=""):
        self.report_date = report_date

    """
    Method to print a line in a report
    """
    def print_line(self):
        print("---------------------------------------------------------------------------")

    """
    Method to display header information of the report
    """
    def display_header(self):
        self.print_line()
        print("EMPLOYEE REPORT\t\t\t\t")
        print("Date : " + self.report_date)
        self.print_line()

    """
    Method to display footer information in the report
    """
    def display_footer(self, count):
        self.print_line()
        print("Total Employees : " + str(count))
        self.print_line()

    """
    Method to display employees information
    """
    def display_employees(self, employees):
        self.display_header()

        print("EMP_ID\tNAME\tROLE\t\tBASIC\tHRA\tALLOW\tSALARY")
        self.print_line()

        for emp in employees:
            if emp is None:
                continue

            role_desc = emp.get_role_description()
            allowance = emp.get_allowance()
            salary = emp.get_salary()

            print(
                str(emp.emp_id)
                + "\t"
                + str(emp.name)
                + "\t"
                + role_desc
                + ("\t" if len(role_desc) < 8 else "")
                + "\t"
                + str(emp.basic)
                + "\t"
                + str(emp.hra)
                + "\t"
                + str(allowance)
                + "\t"
                + str(salary)
            )

        self.display_footer(len(employees))
