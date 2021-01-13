# Data Types

# String + subscript
print("Junior"[0])

# challenge.. 0 printed out J, try to print r using subscripts
print("Junior"[5])

print(len("12345"))

#len function will give an error if you try to print #s e.g. print(len(12345))
# print(len(12345))


# type() function can be used to check data type
hourly = 40
print(type(hourly))

# if you're not sure of the data type, you can use type() function


# type conversions
# str() function

example = 123
# print(len(example)) will print an error
newExample = str(example) #converting 123 to "123"
print(len(newExample))

print(70 + float("100.5"))
print(str(70) + str(100))


# subscripting
subscript = 'january'
print(subscript[0])