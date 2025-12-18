from special_menu import SpecialMenu

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menus = []

    def add_menu(self, menu):
        self.menus.append(menu)

    # 1. Total number of menu items
    def total_menu_items(self):
        count = 0
        for menu in self.menus:
            for category in menu.categories:
                count += len(category.items)
        return count

    # 2. Menu items by course category
    def items_by_category(self, category_name):
        items = []
        for menu in self.menus:
            for category in menu.categories:
                if category.name == category_name:
                    items.extend(category.items)
        return items

    # 3. List all special discount menus
    def special_discount_menus(self):
        return [menu for menu in self.menus if isinstance(menu, SpecialMenu)]
