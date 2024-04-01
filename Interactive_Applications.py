#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Code 1
temperature = float(input("Temperature in Fahrenheit:"))
converted = (temperature - 32) / 1.8
print("Converted:", converted)


# In[ ]:


# Code 2
firstNumber = float(input("Enter firstNumber:"))
secondNumber = float(input("Enter secondNumber:"))
print("Menu:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
operation = int(input("Enter an operation (1/2/3/4):"))
if operation == 1:
    result = firstNumber + secondNumber
    print("Results:", result)
elif operation == 2:
    result = firstNumber - secondNumber
    print("Results:", result)
elif operation == 3:
    result = firstNumber * secondNumber
    print("Results:", result)
elif operation == 4:
    if secondNumber != 0:
        result = firstNumber / secondNumber
        print("Results:", result)


# In[ ]:


# Code 3
currentValue = 2
while currentValue < 1000:
    print("Current Value:", currentValue)
    currentValue = currentValue ** 2

