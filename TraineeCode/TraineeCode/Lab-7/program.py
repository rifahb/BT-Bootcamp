from result_finder import ResultFinder

class Program:
    @staticmethod
    def main(args):
        # Accept the values from console
        marks1 = int(input("Enter Marks 1 : "))
        marks2 = int(input("Enter Marks 2 : "))
        marks3 = int(input("Enter Marks 3 : "))

        # Store the values entered in the object
        finder = ResultFinder()
        finder.marks1 = marks1
        finder.marks2 = marks2
        finder.marks3 = marks3

        # Display all the information with the help of get and other methods
        finder.display_marks()
        print("Total : " + str(finder.get_total()))
        print("Average : " + str(finder.get_average()))
        print("Result : " + str(finder.get_result()))

        input()


if __name__ == "__main__":
    Program.main([])
