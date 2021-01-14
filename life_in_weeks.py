# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# It will take your current age as the input and output a message with our time left in this format: You have x days, y weeks, and z months left.

# Where x, y and z are replaced with the actual calculated numbers.



# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format: You have x days, y weeks, and z months left.
age = (input('how old are you? ' ))

# there's 365 days in a year, 52 weeks in a year, 12 months in a year
lifeExpectancy = 90 - int(age)

days = 365 * lifeExpectancy
weeks = 52 * lifeExpectancy
months = 12 * lifeExpectancy
years = 90 - int(age)

# You have x days, y weeks, and z months left.
# Where x, y and z are replaced with the actual calculated numbers.
print(f"You have {days} days, {weeks} weeks, and {months} months left.")
