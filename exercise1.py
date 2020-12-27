# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

# Warning. Do not change the code on lines 1-3. Your program should work for different inputs. e.g. any two-digit number.

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

# a = two_digit_number
# b = two_digit_number
# print(type(two_digit_number))
# currently it's printing out a str data type, we'd need to convert it to an integer

# a = int(two_digit_number)
# would result in e.g. using 32 ---> 64

# a = (two_digit_number)
# would result in e.g. using 32 ---> 3232


# using the subscript, since i was dealing with a string that accepted 2 #'s, i targeted the first index and 2nd index of the 2#'s, i tried to print with operations but all it did was print the results together because they were a string, so i reprinted with the int function
first = two_digit_number[0]
second = two_digit_number[1]

print(int(first) + int(second))