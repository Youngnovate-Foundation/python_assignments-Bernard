# basic variables exercise 1
name = 'bernard'
age = 22
favprogramming_language = 'python'
completed_class_today = True

#variable operations exercise 2
num1 = 15
num2 = 4 

sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2 #Note the division will give a float number

#Output
print("Sum:",sum)
print("Difference:",difference)
print("Product:",product)
print("Quotient:",quotient)

#User Input exercise 3
favorite_food = input("What is your favorite food? ")
no_of_times = int(input("How many times do you eat it per week: "))

print(f"You love {favorite_food} and eat it {no_of_times} times per week.")

# Type Conversion exercise 4
age = "25"
height = 5.8

# Convert age to string and height to string properly for concatenation
print("I am " + age + " years old and " + str(height) + " feet tall")

# Alternative solution using f-strings
print(f"I am {age} years old and {height} feet tall")