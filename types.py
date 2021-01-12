# will return an error because of the len function
num_char = len(input("what's your name?"))

# print("your name has " + num_char + " characters.")



# you can verify a data type using type function e.g.
# print(type(num_char)) # -> <class 'int'>




# type conversion / type casting, where we change 1 piece of data type to another we can use str()

new_num_char = str(num_char)
print("your name has " + new_num_char + " characers.")



a = 123
print(type(a)) # would print <class 'int'>

A = str(123)
print(type(A)) # would print <class 'str'>

b = float(123)
print(type(b)) # would print <class 'float'>

print(70 + float("100.5")) # would print 170.5 because the string would be converted to a float number, that will later get added to 70

print(str(70) + str(100)) # would print 70100