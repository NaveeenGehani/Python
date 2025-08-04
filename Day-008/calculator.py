print("---- Welcome to the calculator ----")
a = float(input("Enter the first number: "))
b =  float(input("Enter the second number: "))

print("Enter the operation you want to perform: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
c = int(input("Enter your choice: "))

if(c == 1):
    print("The value of", a, "+", b, "is: ", a + b)
elif(c == 2):
    print("The value of", a, "-", b, "is: ", a - b)
elif(c == 3):
    print("The value of", a, "*", b, "is: ", a * b)
elif(c == 4):
    print("The value of", a, "/", b, "is: ", a / b)
else :
    print("Invalid choice, Enter available choice between 1 to 4")
    
print()
print("Thank you for using the calculator")