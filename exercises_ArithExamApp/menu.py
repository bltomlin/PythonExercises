#The restaurant has just opened so its menu contains only a few options:
#pizza: Margherita, Four Seasons, Neapolitan, Vegetarian, Spicy
#salad: Caesar salad, Green salad, Tuna salad, Fruit salad
#soup: Chicken soup, Ramen, Tomato soup, Mushroom cream soup
#If the visitors ask for something that is not on the menu, the program should write "Sorry, we don't have it in the menu".

food_item = input()
if food_item == "pizza":
    print("Margherita, Four Seasons, Neapolitan, Vegetarian, Spicy")
elif food_item == "salad":
    print("Caesar salad, Green salad, Tuna salad, Fruit salad")
elif food_item == "soup":
    print("Chicken soup, Ramen, Tomato soup, Mushroom cream soup")
else:
    print("Sorry, we don't have it in the menu")