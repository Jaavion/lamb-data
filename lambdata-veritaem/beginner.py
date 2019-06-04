class Restaurant:
    def __init__ (self, type_of_food = 'vegan', 
                 type_of_restaurant = 'classy', hours_of_operation = '10-9'):
        self.type_of_food = type_of_food
        self.type_of_restaurant = type_of_restaurant
        self.hours_of_operation = hours_of_operation
    def style(self):
        if self.type_of_restaurant == 'vegan':
            print('You are healthy')
        else:
            print('You need to eat healthier')

Commanders_palace = Restaurant(type_of_food='non vegan', type_of_restaurant='fast food', hours_of_operation='10-3')
 
