class DecimalSplitter:
    """
    Method to get the whole number from a double
    """
    @staticmethod
    def get_whole(number):
        # Truncate toward zero to get the whole part
        return int(number)

    """
    Method to get the fractional part of a double number
    """
    @staticmethod
    def get_fraction(number):
        whole = DecimalSplitter.get_whole(number)
        return number - whole

    """
    Method to check if a given number is odd or even
    """
    @staticmethod
    def is_odd(number):
        return DecimalSplitter.get_whole(number) % 2 != 0
