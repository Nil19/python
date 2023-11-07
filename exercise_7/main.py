# Take the following Python code that stores a string:`

# str = 'X-DSPAM-Confidence:0.8475'

# Use find and string slicing to extract the portion of the string after 
# the colon character and then use the float function to convert the extracted string into a floating point number.

str = "X-DSPAM-Confidence:0.8475"

# find the colon
number = str.find(":")
print(number)

# extract info 
fl = str[number + 1 :]
print(fl)

# convert to float
convert = float(fl)
print(convert)