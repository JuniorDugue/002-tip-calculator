# topics covering data types, numbers, operations, type conversion & f-strings

### table of contents


### exercise1
![exercise1challenge](/assets/exercise1demo.gif)
[repl.it link](https://repl.it/@jrdugue/day-2-1-exercise)

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

