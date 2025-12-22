from employee_report import EmployeeReport
from role_builder import RoleBuilder
from roles import Roles
from employee import Employee

class Program:
    @staticmethod
    def main(args):
        # Employee array to hold the employees' information
        employees = [None] * 4
        emp = None

        emp_id = ""
        name = ""
        report_date = ""
        allowance_percentage = 0.0
        basic = 0.0
        hra = 0.0
        role = 0

        # Accept employee information from the user
        print("Enter employee information")

        for i in range(len(employees)):
            print("Employee No : " + str(i+1))
            print("Id : ")
            emp_id = input()

            print("Name : ")
            name = input()

            print("Basic : ")
            basic = float(input())

            print("HRA : ")
            hra = float(input())

            print("Percentage of Allowance : ")
            allowance_percentage = float(input())

            print("Enter Role Id : ")
            print(str(Roles.DEVELOPER) + ". " + RoleBuilder.get_role_description(Roles.DEVELOPER))
            print(str(Roles.TEST_ENGINEER) + ". " + RoleBuilder.get_role_description(Roles.TEST_ENGINEER))
            print(str(Roles.SR_DEVELOPER) + ". " + RoleBuilder.get_role_description(Roles.SR_DEVELOPER))
            print(str(Roles.DESIGNER) + ". " + RoleBuilder.get_role_description(Roles.DESIGNER))
            role = int(input())

            emp = Employee()
            emp.emp_id = emp_id
            emp.name = name
            emp.basic = basic
            emp.hra = hra
            emp.allowance_percentage = allowance_percentage
            emp.role = role

            employees[i] = emp

        print("Enter the date of the report (dd/mm/yyyy) : ")
        report_date = input()

        report = EmployeeReport()
        report.report_date = report_date

        report.display_employees(employees)

        input()


if __name__ == "__main__":
    import sys
    Program.main(sys.argv[1:])
