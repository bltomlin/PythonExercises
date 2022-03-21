#Imagine you've created a program that plays the cities game with a user. For the game to work, you need to remember the user's city and be able to change it. Below is the code that does that, but if you run it as is, you'll get an error: you won't be able to access the variable user_city outside of the function. Fix this problem by adding one line. Please, don't change the rest of the code.

user_city = "global"
def change_city(new_user_city):
   global user_city
   user_city = new_user_city

change_city("Paris")
print(user_city)

