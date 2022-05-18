"""
Anthony keeps track of what he eats: he writes down how many calories are in his meals. Use the list of dictionaries to calculate the total amount of calories per day and print it.
The sample input will look like:
"""
meals = [
        {"title": "Oatmeal pancakes with apple and cinnamon", "kcal": 370},
        {"title": "Italian salad with fusilli and ham", "kcal": 320},
        {"title": "Bulgur with vegetables", "kcal": 350},
        {"title": "Curd souffle with lingonberries and ginger", "kcal": 225},
        {"title": "Oatmeal with honey and peanuts", "kcal": 440}]
"""
The output in this case should be 1705.
"""

total_kcal = 0
for i in meals:
    total_kcal += i.get("kcal")
print(total_kcal)
