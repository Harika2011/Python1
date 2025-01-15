weather = (1,0,0,0,1,1,0)

rainy = 0
sunny = 0

for condition in weather:
    if condition == 1:
        rainy+=1
    else:
        sunny +=1

if rainy > sunny:
    prediction = "It's likely to be rainy"
elif sunny > rainy:
    prediction = "It's likely to be sunny"
else:
    "It's seems like the weather is balanced"


print("Weather data ",weather)
print("Rainy days count ",rainy)
print("Sunny days count ",sunny)
print("Prediction ",weather)

