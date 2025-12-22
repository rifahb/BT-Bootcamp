class Cache:
    _MAX_CAPACITY = 0
    _initialized = False

    """
    Static method to get the maximum capacity of the cache
    """
    @staticmethod
    def get_max_capacity():
        # Initialize once, on first access
        if not Cache._initialized:
            user_value = input("Enter MAX_CAPACITY for cache: ")
            try:
                Cache._MAX_CAPACITY = int(user_value)
            except ValueError:
                Cache._MAX_CAPACITY = 0
            Cache._initialized = True
        print("Returning MAX_CAPACITY")
        return Cache._MAX_CAPACITY
