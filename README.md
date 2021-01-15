# topics covering data types, numbers, operations, type conversion & f-strings

### table of contents


### exercise1
![exercise1challenge](/assets/exercise1demo.gif)
[repl.it link](https://repl.it/@jrdugue/day-2-1-exercise)
https://repl.it/@jrdugue/day-2-1-exercise#README.md
### exercise2
![](/assets/exercise2demo.gif)
[repl.it link](https://repl.it/@jrdugue/day-2-2-exercise#README.md)

#### notes
![len() error](/assets/len_error.jpg)
- we can use len() on string, not numbers/integers
- if we wanted to use len() on integers, we'd have to add quotes/double quotes around the numbers e.g. `print(len(12345))` -> 5 or convert them using int()

![printing 1st character of a string](/assets/1st_character.jpg)
- 'subscripting'

---
![string function](/assets/str_function.jpg)
- type conversion / type casting, where we change 1 piece of data type to another
  * we can set a bunch of data types into a string, not just numbers
  * a = 123
print(type(a)) # would print <class 'int'>

  * A = str(123)
print(type(A)) # would print <class 'str'>

  * b = float(123)
print(type(b)) # would print <class 'float'>

  * print(70 + float("100.5")) # would print 170.5 because the string would be converted to a float number, that will later get added to 70

  * print(str(70) + str(100)) # would print 70100 

  - **int() would convert strings into integers
  ---

# # string
* print("123" + "345") #123345

# integer
* print(123 + 345) #468
* print(1,000,000)
* print(1_000_000)
* large numbers.. 342,654,896 can be replaced with 342_654_896 and the computer will understand

# decimals = 'float'
* float = 3.14159
* print(float)
* print(type(float))

# boolean
* True # has to be captialized
* False # has to be capitalized

----

# operations and shorthand

`print(8/3) # returns 2.6666666666666665 a floating point number`

`print(int(8/3)) # returns 2 as an integer`

`print(round(8/3)) # will return 3 rounding to a whole number`

`print(round(8 / 3, 2)) # to specify a decimal placement e.g. 2 decimal places`

`print( 8 // 3) # floored divisions that'll return 2`

#### if you wanted to continue an operation, you can store equation to a variable and
#### you can use shorthands e.g. if you're trying to keep score of a sports score
`answer = 4 / 2
answer /= 2
print(answer)`

---

# f strings

#### make sure to write f in front of your strings
`score = 0
height = 1.8
isWinning = True
print(f"your score is {score}, your height is {height}, you are wnning is {isWinning}")`