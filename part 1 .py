# Python Practice Solutions
# Run one section at a time in VS Code / Jupyter using # %% cells.
# Note: Questions 33, 43, 44 and 52 were not provided.
# Note: Question 40 needs the "given below style" example.

# %% 1. Convert Celsius into Fahrenheit
celsius = float(input("Enter Celsius: "))
fahrenheit = (celsius * 1.8) + 32
print("Fahrenheit:", fahrenheit)

# %% 2. Swap two variables (without a third variable)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a, b = b, a
print("After swap:", a, b)

# %% 3. Swap two variables (using a third variable)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
temp = a
a = b
b = temp
print("After swap:", a, b)

# %% 4. Convert decimal into binary
number = int(input("Enter a decimal number: "))
print("Binary:", bin(number)[2:])

# %% 5. Convert decimal into octal and hexadecimal
number = int(input("Enter a decimal number: "))
print("Octal:", oct(number)[2:])
print("Hexadecimal:", hex(number)[2:].upper())

# %% 6. Check positive or negative; positive ho to square print karo
number = int(input("Enter a number: "))
if number > 0:
    print("Positive; square =", number ** 2)
elif number < 0:
    print("Negative")
else:
    print("Zero")

# %% 7. Check odd; odd ho to cube print karo
number = int(input("Enter a number: "))
if number % 2 != 0:
    print("Odd; cube =", number ** 3)
else:
    print("Even")

# %% 8. Check alphabet; alphabet ho to Hello World print karo
character = input("Enter one character: ")
if len(character) == 1 and character.isalpha():
    print("Hello World")
else:
    print("Not an alphabet")

# %% 9. Check uppercase; uppercase ho to character print karo
character = input("Enter one character: ")
if len(character) == 1 and character.isupper():
    print(character)
else:
    print("Not uppercase")

# %% 10. Check divisibility by both 3 and 7
number = int(input("Enter a number: "))
if number % 3 == 0 and number % 7 == 0:
    print("The number is divisible by both")
else:
    print("The number is not divisible by both")

# %% 11. Print whether a number is even or odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# %% 12. Even ho to square, odd ho to cube
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Square =", number ** 2)
else:
    print("Cube =", number ** 3)

# %% 13. Check whether character is a vowel
character = input("Enter one character: ").lower()
if len(character) == 1 and character in "aeiou":
    print("Vowel")
else:
    print("Not a vowel")

# %% 14. Check whether character is a consonant
character = input("Enter one character: ").lower()
if len(character) == 1 and character.isalpha() and character not in "aeiou":
    print("Consonant")
else:
    print("Not a consonant")

# %% 15. Find the largest among two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Largest:", a)
elif b > a:
    print("Largest:", b)
else:
    print("Both are equal")

# %% 16. Find the smallest among two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a < b:
    print("Smallest:", a)
elif b < a:
    print("Smallest:", b)
else:
    print("Both are equal")

# %% 17. Check whether a number has three digits
number = int(input("Enter a number: "))
if 100 <= abs(number) <= 999:
    print("Three-digit number")
else:
    print("Not a three-digit number")

# %% 18. Check whether a string is palindrome
text = input("Enter a string: ").lower()
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

# %% 19. Check positive, negative, or zero
number = int(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# %% 20. Find largest and smallest among three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("Largest:", max(a, b, c))
print("Smallest:", min(a, b, c))

# %% 21. Check leap year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Leap year")
else:
    print("Not a leap year")

# %% 22. Simple calculator (+, -, *, /)
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")
if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
elif operator == "/":
    if b != 0:
        print(a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")

# %% 23. Grade from percentage
percentage = float(input("Enter percentage: "))
if percentage >= 90:
    print("Grade A")
elif percentage >= 75:
    print("Grade B")
elif percentage >= 60:
    print("Grade C")
elif percentage >= 40:
    print("Grade D")
else:
    print("Fail")

# %% 24. Age group (Teenager interpreted as age 12 to 19)
age = int(input("Enter age: "))
if age >= 60:
    print("Senior citizen")
elif age >= 20:
    print("Adult")
elif age >= 12:
    print("Teenager")
else:
    print("Child")

# %% 25. Display day of week from number 1 to 7
day_number = int(input("Enter day number (1-7): "))
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
if 1 <= day_number <= 7:
    print(days[day_number - 1])
else:
    print("Invalid day number")

# %% 26. Calculate tax from salary
salary = float(input("Enter annual salary: "))
if salary > 2000000:
    print("Tax:", salary * 0.30)
elif salary > 1500000:
    print("Tax:", salary * 0.15)
elif salary > 1200000:
    print("Tax:", salary * 0.10)
else:
    print("No tax")

# %% 27 and 28. Check vowel or consonant
character = input("Enter one character: ").lower()
if len(character) == 1 and character.isalpha():
    if character in "aeiou":
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Not an alphabet")

# %% 29. Loan eligibility using nested if
age = int(input("Enter age: "))
monthly_income = float(input("Enter monthly income: "))
if age > 21:
    if monthly_income > 30000:
        print("Eligible for loan")
    else:
        print("Not eligible for loan")
else:
    print("Not eligible for loan")

# %% 30. Employee bonus using nested if
experience = int(input("Enter experience in years: "))
salary = float(input("Enter salary: "))
if experience >= 5:
    if salary < 50000:
        print("Bonus: 10000")
    else:
        print("Bonus: 5000")
else:
    print("Not eligible for bonus")

# %% 31. Student grade using nested if
marks = float(input("Enter marks: "))
if marks >= 35:
    print("Pass")
    if marks >= 90:
        print("Grade A")
    elif marks >= 75:
        print("Grade B")
    elif marks >= 60:
        print("Grade C")
    else:
        print("Grade D")
else:
    print("Fail")

# %% 32. Print your name 5 times
name = input("Enter your name: ")
i = 1
while i <= 5:
    print(name)
    i += 1

# %% 34. Display numbers from 1 to 7
i = 1
while i <= 7:
    print(i)
    i += 1

# %% 35. Display numbers from 7 to 21 (interpreted from "721")
i = 7
while i <= 21:
    print(i)
    i += 1

# %% 36. Display even numbers from 1 to 10
i = 1
while i <= 10:
    if i % 2 == 0:
        print(i)
    i += 1

# %% 37. Display odd numbers from 1 to 10
i = 1
while i <= 10:
    if i % 2 != 0:
        print(i)
    i += 1

# %% 38. Display numbers in a range entered by the user
start = int(input("Enter start: "))
stop = int(input("Enter stop: "))
while start <= stop:
    print(start)
    start += 1

# %% 39. Add 5 to evens and multiply odds by 5 from 1 to 7
i = 1
while i <= 7:
    if i % 2 == 0:
        print(i, "+ 5 =", i + 5)
    else:
        print(i, "x 5 =", i * 5)
    i += 1

# %% 40. Question incomplete: "given below style" was not provided.

# %% 41. Print lowercase alphabets from a to z
i = 97
while i <= 122:
    print(chr(i))
    i += 1

# %% 42. Print lowercase alphabets from z to a
i = 122
while i >= 97:
    print(chr(i))
    i -= 1

# %% 45. Print table of 7
i = 1
while i <= 10:
    print("7 x", i, "=", 7 * i)
    i += 1

# %% 46. Print table of a user-given number
number = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(number, "x", i, "=", number * i)
    i += 1

# %% 47. Add all numbers from 1 to 5
i = 1
total = 0
while i <= 5:
    total += i
    i += 1
print("Sum:", total)

# %% 48. Multiply all numbers from 1 to 5
i = 1
product = 1
while i <= 5:
    product *= i
    i += 1
print("Product:", product)

# %% 49. Add all even numbers from 1 to 10
i = 1
total = 0
while i <= 10:
    if i % 2 == 0:
        total += i
    i += 1
print("Sum of even numbers:", total)

# %% 50. Multiply all odd numbers between 5 and 15
i = 5
product = 1
while i <= 15:
    if i % 2 != 0:
        product *= i
    i += 1
print("Product of odd numbers:", product)

# %% 51. Count digits in a number using a while loop
number = abs(int(input("Enter a number: ")))
count = 0
if number == 0:
    count = 1
else:
    while number != 0:
        count += 1
        number //= 10
print("Number of digits:", count)


