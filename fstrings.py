print(8/3) # returns 2.6666666666666665 a floating point number

print(int(8/3)) # returns 2 as an integer

print(round(8/3)) # will return 3 rounding to a whole number

print(round(8 / 3, 2)) # to specifify a decial placement e.g. 2 decimal places

print( 8 // 3) # floored divisions that'll return 2

# if you wanted to continue an operation, you can store equation to a variable and
# you can use shorthands e.g. if you're trying to keep score of a sports score



answer = 4 / 2
answer /= 2
print(answer)




# f-string
# make sure to write f in front of your strings
score = 0
height = 1.8
isWinning = True
print(f"your score is {score}, your height is {height}, you are wnning is {isWinning}")