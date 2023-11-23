
# This function is adding two numbers
def add(x, y):
    return x + y

# This function is subtracting two numbers
def subtract(x, y):
    return x - y

#This function is multiplying two numbers
def multiply(x, y):
    return x * y

# This function is dividing two numbers
def divide(x,y):
    return x / y

# Main Manu Screen
print("Select oepration.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # Taking input from the user
    choice = input("Enter choice (1/2/3/4): ")

    # Checking if the choice is one of the options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input, Please enter a number.")
            continue
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # Checking if user want another calculation
        # Breaking the while loop if answer is NO
        next_calculation = input("Let's do next calculation? (Please write Yes/No): ")
        if next_calculation == "No":
            break
    else: 
        print("Invalid Input")
