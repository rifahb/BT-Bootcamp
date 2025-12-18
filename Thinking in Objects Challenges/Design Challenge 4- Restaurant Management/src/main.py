from restaurant import Restaurant
from menu import Menu
from special_menu import SpecialMenu
from course_category import CourseCategory
from menu_item import MenuItem

restaurant = Restaurant("Food Palace")

menu1 = Menu("Regular Menu")
menu2 = SpecialMenu("Festival Menu")

starters = CourseCategory("Starters")
starters.add_item(MenuItem("Soup", 120))
starters.add_item(MenuItem("Salad", 100))

main_course = CourseCategory("Main Course")
main_course.add_item(MenuItem("Pasta", 250))

desserts = CourseCategory("Desserts")
desserts.add_item(MenuItem("Ice Cream", 90))

menu1.add_category(starters)
menu1.add_category(main_course)
menu2.add_category(desserts)

restaurant.add_menu(menu1)
restaurant.add_menu(menu2)

print("Total Menu Items:", restaurant.total_menu_items())
print("Starters Items:", [item.name for item in restaurant.items_by_category("Starters")])
print("Special Menus:", [menu.name for menu in restaurant.special_discount_menus()])
