#1 Write a program that takes two numbers as input and prints their sum.
a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
print("SUM: ", a+b)
#2 Write a python program that checks whether a given number is even or odd
n = int(input("Enter a number"))
if(n%2==0):
    print("EVEN")
else:
    print("ODD")
#3 Write a python program that calculates the factorial of a given number
n = int(input("Enter a number"))
fact = 1
for i in range(1,n+1):
    fact = fact*i
print("Factorial: ", fact)

#4 Write a program that asks the user for their name and then prints a greeting message.
name = input("Enter your name")
print("Welcome ", name," to the programmming world" )
#5 Write a program that takes a string input from the user and writes it to a text file.
def write_to_file(filename):
    user_input = input("Please enter the string you want to write to the file: ")
    
    with open(filename, 'w') as file:
        
        file.write(user_input)
    
    print(f"The string has been written to {filename}")


filename = "output.txt"


write_to_file(filename)

#6 . Write a program that reads the content of a text file and prints it to the console.
def read_from_file(filename):
    try:
        
        with open(filename, 'r') as file:
            
            content = file.read()
            
            print(content)
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


filename = "output.txt"
read_from_file(filename)
#7 . Write a python program that takes a string as input and returns its length.
st = input("Enter a string")
print("length: ",len(st))
#8 Write a python program that concatenates two strings and returns the result.
str1 = input("Enter a string")
str2 = input("Enter a string")
print(str1+str2)'
#9 Write a python program that checks if a substring is present in a given string.
str = input("Enter a string")
sub = input("Enter a substring to be checked")
if sub in str:
    print("present")
else:
    print("Not present")
#10 Write a python prograthm that converts a given string to uppercase.
str = input("Enter a string")
print(str.upper())
#11 Write a python program that generates the first n numbers in the Fibonacci sequence.
n = int(input("Enter a number"))
for i in range(n):
    x = i+ (i+1)
    print(x," ")

#12 Write a python program that calculates the sum of the digits of a given number.
def sum_of_digits(number):
    # Initialize the sum to 0
    total_sum = 0
    
    # Iterate through each character in the string representation of the number
    for digit in str(number):
        # Convert the character to an integer and add it to the sum
        total_sum += int(digit)
    
    return total_sum

# Take input from the user
user_input = input("Please enter a number: ")

# Ensure the input is a valid number
if user_input.isdigit():
    # Convert the input to an integer
    number = int(user_input)
    
    # Call the function to calculate the sum of digits
    result = sum_of_digits(number)
    
    # Print the result
    print("The sum of the digits is:", result)
else:
    print("Invalid input! Please enter a valid number.")


#13 Write a program that asks the user for their birth year and calculates their age
n = int(input("Enter your birth year"))
print("age: ",2024-n)
#14 Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.

#15 Write a program that reads data from a CSV file and prints it to the console.
#16 . Write a program in python that counts the frequency of each character in a string.
def count_char_frequencies(input_string):
    # Create an empty dictionary to store character frequencies
    frequency_dict = {}
    
    # Iterate through each character in the string
    for char in input_string:
        # If the character is already in the dictionary, increment its count
        if char in frequency_dict:
            frequency_dict[char] += 1
        # If the character is not in the dictionary, add it with a count of 1
        else:
            frequency_dict[char] = 1
    
    return frequency_dict

# Take input from the user
user_input = input("Please enter a string: ")

# Call the function to count character frequencies
result = count_char_frequencies(user_input)

# Print the result
print("Character frequencies:")
for char, freq in result.items():
    print(f"'{char}': {freq}")


#17 Write a program in python that converts a given string to title case (first letter of each word capitalized).
str = input("Enter the string")
print(str.title())

#18 Write a python program that checks if two strings are anagrams of each other.
def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase for accurate comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the sorted characters of both strings are the same
    return sorted(str1) == sorted(str2)

# Take input from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Call the function to check if they are anagrams
if are_anagrams(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")

#19 Write a python program that removes all punctuation from a given string.
str = input("Enter a string")
new = ""
for i in range(len(str)):
    if str[i] not in [',','"',"'","?","!","[","]","{","}","(",")",";",":"]:
        new = new+str[i]
print(new)
#20 Write a python program that takes a list of numbers and returns their sum.
n = int(input("How many elements you want in your list"))
l = []
sum = 0
for i in range(n):
    a = int(input("Enter the element"))
    l.append(a)
for i in range(n):
    sum = sum+l[i]
print(sum)
#21 Write a python program that counts the occurrences of a specific element in a list.
n = int(input("How many elements you want in your list"))
l = []
sum = 0
for i in range(n):
    a = int(input("Enter the element"))
    l.append(a)
x = int(input("Enter the element you want to know the frequency"))
count = 0
for i in range(n):
    if(l[i]==x):
        count = count+1
print(count)
#22 Write a python program that returns the minimum and maximum values in a list of numbers
n = int(input("How many elements you want in your list"))
l = []
for i in range(n):
    a = int(input("Enter the element"))
    l.append(a)
print("Max: ", l.max())
print("Min: ", l.min())
#23. Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.
cel = int(input("Enter temperature in celcius"))
far = (cel*1.8)+32
print("Temp in farenhite: ", far)
#24 . Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result.
a = int(input("Enter first number"))
b = int(input("Enter second number"))
c = input("Enter an operator")
if(c=="+"):
    print(a+b)
elif(c=='-'):
    print(a-b)
elif(c=='*'):
    print(a*b)
elif(c=="/"):
    print(a/b)
else:
    print("Not a valid operator")
#25Write a program that copies the contents of one text file to another
#26 Write a program in python that checks if a string starts with a given prefix or ends with a given suffix
str = input("Enter a string")
pre = input("Enter prefix")
suf = input("Enter a suffix")
revStr = str[::-1]
if (str[:len(pre)]==pre) or(revStr[:len(suf)]==suf[::-1]):
    print("Present")
else:
    print("Absent")
#27 Write a program in python that converts a string into a list of its characters.
str = input("Enter a string")
x = list(str)
print(x)


