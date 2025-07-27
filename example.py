#!/usr/bin/env python3
"""
Example Python script demonstrating various features
"""
import math
import random
from datetime import datetime

def demonstrate_basics():
    """Demonstrate basic Python features"""
    print("🔹 Basic Python Operations")
    
    # Variables and calculations
    x = 10
    y = 3
    print(f"x = {x}, y = {y}")
    print(f"x + y = {x + y}")
    print(f"x * y = {x * y}")
    print(f"x ** y = {x ** y}")
    print(f"x / y = {x / y:.2f}")

def demonstrate_data_structures():
    """Demonstrate Python data structures"""
    print("\n🔹 Data Structures")
    
    # Lists
    fruits = ["apple", "banana", "cherry", "date"]
    print(f"Fruits: {fruits}")
    print(f"First fruit: {fruits[0]}")
    print(f"Last fruit: {fruits[-1]}")
    
    # Dictionary
    person = {
        "name": "Alice",
        "age": 30,
        "city": "New York",
        "skills": ["Python", "JavaScript", "SQL"]
    }
    print(f"Person: {person}")
    print(f"Skills: {', '.join(person['skills'])}")

def demonstrate_functions():
    """Demonstrate function usage"""
    print("\n🔹 Functions and Math")
    
    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n-1) + fibonacci(n-2)
    
    # Calculate some Fibonacci numbers
    fib_sequence = [fibonacci(i) for i in range(8)]
    print(f"Fibonacci sequence (8 terms): {fib_sequence}")
    
    # Math operations
    angle = 45
    radians = math.radians(angle)
    print(f"sin({angle}°) = {math.sin(radians):.3f}")
    print(f"cos({angle}°) = {math.cos(radians):.3f}")
    print(f"√16 = {math.sqrt(16)}")

def demonstrate_random():
    """Demonstrate random operations"""
    print("\n🔹 Random Operations")
    
    # Random numbers
    random_int = random.randint(1, 100)
    random_float = random.random()
    print(f"Random integer (1-100): {random_int}")
    print(f"Random float (0-1): {random_float:.3f}")
    
    # Random choice
    colors = ["red", "green", "blue", "yellow", "purple"]
    chosen_color = random.choice(colors)
    print(f"Random color: {chosen_color}")
    
    # Random sample
    sample = random.sample(range(1, 21), 5)
    print(f"Random sample of 5 numbers (1-20): {sample}")

def main():
    print("🐍 Python Feature Demonstration")
    print(f"📅 Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)
    
    demonstrate_basics()
    demonstrate_data_structures()
    demonstrate_functions()
    demonstrate_random()
    
    print("\n" + "=" * 50)
    print("✨ Demonstration complete!")

if __name__ == "__main__":
    main()