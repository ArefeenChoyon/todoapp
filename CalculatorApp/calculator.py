class Calculator:
    """
    A simple calculator class that performs basic arithmetic operations.
    """
    
    def add(self, x, y):
        """Add two numbers"""
        return x + y
    
    def subtract(self, x, y):
        """Subtract y from x"""
        return x - y
    
    def multiply(self, x, y):
        """Multiply two numbers"""
        return x * y
    
    def divide(self, x, y):
        """
        Divide x by y
        Raises ValueError if attempting to divide by zero
        """
        if y == 0:
            raise ValueError("Cannot divide by zero!")
        return x / y

def main():
    """Main function to run the calculator program"""
    calculator = Calculator()
    
    while True:
        print("\n=== Simple Calculator ===")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        try:
            choice = input("\nEnter choice (1-5): ")
            
            if choice == '5':
                print("Thank you for using the calculator!")
                break
            
            if choice not in ['1', '2', '3', '4']:
                print("Invalid choice! Please try again.")
                continue
            
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                result = calculator.add(num1, num2)
                print(f"\n{num1} + {num2} = {result}")
            
            elif choice == '2':
                result = calculator.subtract(num1, num2)
                print(f"\n{num1} - {num2} = {result}")
            
            elif choice == '3':
                result = calculator.multiply(num1, num2)
                print(f"\n{num1} × {num2} = {result}")
            
            elif choice == '4':
                try:
                    result = calculator.divide(num1, num2)
                    print(f"\n{num1} ÷ {num2} = {result}")
                except ValueError as e:
                    print(f"\nError: {e}")
        
        except ValueError:
            print("\nError: Please enter valid numbers!")
        except Exception as e:
            print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()
