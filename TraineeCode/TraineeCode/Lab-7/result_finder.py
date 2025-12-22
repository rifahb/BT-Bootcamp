class ResultFinder:
    """
    Properties of the fields of this class
    """
    def __init__(self):
        self._marks1 = 0
        self._marks2 = 0
        self._marks3 = 0

    @property
    def marks1(self):
        return self._marks1

    @marks1.setter
    def marks1(self, value):
        self._marks1 = value

    @property
    def marks2(self):
        return self._marks2

    @marks2.setter
    def marks2(self, value):
        self._marks2 = value

    @property
    def marks3(self):
        return self._marks3

    @marks3.setter
    def marks3(self, value):
        self._marks3 = value

    """
    Method to display marks obtained
    """
    def display_marks(self):
        print("Marks entered------------- ")
        print("Marks 1 : " + str(self._marks1))
        print("Marks 2 : " + str(self._marks2))
        print("Marks 3 : " + str(self._marks3))
    

    """
    Method to get the total of the marks in subjects
    """
    def get_total(self):
        return self._marks1 + self._marks2 + self._marks3

    """
    Method to calculate the average of the marks
    """
    def get_average(self):
        return self.get_total() / 3.0

    """
    Method to get the result for the marks given
    """
    def get_result(self):
        # Simple pass/fail rule: all marks must be at least 35
        if self._marks1 >= 35 and self._marks2 >= 35 and self._marks3 >= 35:
            return "Pass"
        return "Fail"
