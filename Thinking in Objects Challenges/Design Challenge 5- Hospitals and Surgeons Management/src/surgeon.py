class Surgeon:
    def __init__(self, surgeon_id, name):
        self.surgeon_id = surgeon_id
        self.name = name
        self.operations = []

    def add_operation(self, operation):
        self.operations.append(operation)
