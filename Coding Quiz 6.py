# First, create a variable called start, and set it equal to "I am ".
# Remember the space after the word "am" !


# Next, create a variable called age and set it equal to your age in years.
# This must be a number


# Next, create a variable called end, and set it equal to " years old".
# Remember the space before the word "years"


# Next, create a variable called output, and use the format() function to add
# together the start, age and end variables. 

# An example output string would be "I am 15 years old"


# Finally, print the output to the screen using the print() function.

start = "I am "

age = 27

end = " years old"


string = "{}{}{}"
output = string.format(start, age, end)
print(output)
