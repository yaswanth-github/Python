from collections import defaultdict

class Food:
    def __init__(self, name, calories, protein, carbs, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat

class FoodTracker:
    def __init__(self):
        self.foods = {}
        self.meals = defaultdict(list)

    def add_food(self, name, calories, protein, carbs, fat):
        food = Food(name, calories, protein, carbs, fat)
        self.foods[name] = food

    def add_meal(self, meal_name, food_name, serving_size):
        food = self.foods[food_name]
        self.meals[meal_name].append((food, serving_size))

    def get_nutritional_info(self, meal_name):
        meal = self.meals[meal_name]
        total_calories = sum(food.calories * serving_size / 100 for food, serving_size in meal)
        total_protein = sum(food.protein * serving_size / 100 for food, serving_size in meal)
        total_carbs = sum(food.carbs * serving_size / 100 for food, serving_size in meal)
        total_fat = sum(food.fat * serving_size / 100 for food, serving_size in meal)
        return (total_calories, total_protein, total_carbs, total_fat)

    def get_daily_nutrition(self):
        total_calories = 0
        total_protein = 0
        total_carbs = 0
        total_fat = 0
        for meal in self.meals.values():
            meal_calories, meal_protein, meal_carbs, meal_fat = self.get_nutritional_info(meal)
            total_calories += meal_calories
            total_protein += meal_protein
            total_carbs += meal_carbs
            total_fat += meal_fat
        return (total_calories, total_protein, total_carbs, total_fat)

if __name__ == '__main__':
    tracker = FoodTracker()

    tracker.add_food('Egg', 155, 13, 1, 11)
    tracker.add_food('Apple', 52, 0, 14, 0)
    tracker.add_food('Chicken breast', 165, 31, 0, 3.6)
    tracker.add_food('White rice', 130, 2.7, 28, 0.3)
    tracker.add_food('Salmon', 206, 22, 0, 13)
    tracker.add_food('Broccoli', 55, 4, 11, 1)

    tracker.add_meal('Breakfast', 'Egg', 100)
    tracker.add_meal('Breakfast', 'Apple', 120)

    tracker.add_meal('Lunch', 'Chicken breast', 150)
    tracker.add_meal('Lunch', 'White rice', 100)
    tracker.add_meal('Lunch', 'Broccoli', 50)

    tracker.add_meal('Dinner', 'Salmon', 200)
    tracker.add_meal('Dinner', 'Broccoli', 100)

    print('Nutritional info for Lunch:', tracker.get_nutritional_info('Lunch'))
    print('Total daily nutrition:', tracker.get_daily_nutrition())
