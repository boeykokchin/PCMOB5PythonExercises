

### Exercise 1 ###
print('### EXERCISE 1 - Area of Rectangle ###')
width = input("Enter width: ")
height = input("Enter height: ")
area = int(width) * int(height)
print ("The area of your rectangle is " + str(area) + "\n")
### Exercise 1 ###

### Exercise 2 ###
print('### EXERCISE 2 - BMI Calculator ###')
weight = input("What is your weight in kg? ")
floatweight = float(weight)

height = input("What is your height in m? ")
floatheight = float(height)

bmi = floatweight/(floatheight*floatheight)
print("Your BMI is", str(bmi) + "\n")
### Exercise 2 ###

### Exercise 3 ###
print('### Exercise 3 - Temperature ###')
def convertfunction(celsius):
    celsius = input("What is the temperature in degree Celsius? ") 
    fahrenheit = float(celsius) * (9/5)+32
    print("When the temperature is " + str(celsius) + " degrees Celsius, it's " + str(fahrenheit) + " Farenheit.\n")
convertfunction(0)
### Exercise 3 ###
