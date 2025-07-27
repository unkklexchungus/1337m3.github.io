#!/usr/bin/env python3
"""
Main Python file for coding environment setup
"""

def main():
    print("🐍 Python coding environment is ready!")
    print(f"Python version: {__import__('sys').version}")
    print(f"Current working directory: {__import__('os').getcwd()}")
    
    # Example calculations
    numbers = [1, 2, 3, 4, 5]
    total = sum(numbers)
    average = total / len(numbers)
    
    print(f"\nExample calculation:")
    print(f"Numbers: {numbers}")
    print(f"Sum: {total}")
    print(f"Average: {average}")
    
    # Example with some basic data manipulation
    data = {"name": "Python Environment", "status": "Ready", "features": ["REPL", "Scripts", "Packages"]}
    print(f"\nEnvironment info: {data}")

if __name__ == "__main__":
    main()