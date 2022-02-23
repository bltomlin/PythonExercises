#Convert the temperature from Fahrenheit to Celsius

def fahrenheit_to_celsius(temperature_f):
    num = 32
    temperature_c = (temperature_f - num) * (5 / 9)
    return round(temperature_c, 3)
