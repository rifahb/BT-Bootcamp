from employee import Employee
from address import Address

class Program:
    @staticmethod
    def main(args):
        emp = Employee()
        Program.store_data(emp)
        Program.show_data(emp)

    @staticmethod
    def store_data(emp):
        # Populate employee
        emp.emp_id = 1001
        emp.emp_name = "Nitesh"
        emp.emp_gender = "M"

        # Populate address
        addr = Address()
        addr.addr1 = "45/2"
        addr.addr2 = "MG Road"
        addr.city = "Bangalore"
        addr.pincode = "560042"

        emp.emp_address = addr

    @staticmethod
    def show_data(emp):
        # ----------------Display the employee information
        print("Employee Id : " + str(emp.emp_id))
        print("Employee Name : " + str(emp.emp_name))
        print("Employee Gender : " + str(emp.emp_gender))

        print("Employee Address : --------------")
        if emp.emp_address:
            print("Address 1 : " + str(emp.emp_address.addr1))
            print("Address 2 : " + str(emp.emp_address.addr2))
            print("City : " + str(emp.emp_address.city))
            print("PinCode : " + str(emp.emp_address.pincode))
        print("----------------------------------")


if __name__ == "__main__":
    Program.main([])
