from menu import Menu

class SpecialMenu(Menu):
    def __init__(self, name):
        super().__init__(name)
        self.discount = 0.30
