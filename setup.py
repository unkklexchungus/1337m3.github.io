#!/usr/bin/env python3
"""
Setup script for Python coding environment
"""
import subprocess
import sys
import os

def install_packages():
    """Install packages from requirements.txt"""
    print("📦 Installing Python packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Packages installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing packages: {e}")
        return False
    return True

def create_workspace_structure():
    """Create useful directories for Python development"""
    directories = ["scripts", "tests", "data", "output"]
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"📁 Created directory: {directory}")
    
    # Create a simple test file
    test_content = '''#!/usr/bin/env python3
"""
Example test file
"""
import unittest

class TestExample(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(2 + 2, 4)
        
    def test_string(self):
        self.assertEqual("hello".upper(), "HELLO")

if __name__ == "__main__":
    unittest.main()
'''
    
    with open("tests/test_example.py", "w") as f:
        f.write(test_content)
    print("✅ Created example test file")

def main():
    print("🔧 Setting up Python coding environment...")
    print("=" * 50)
    
    # Create directory structure
    create_workspace_structure()
    
    # Install packages
    print("\n" + "=" * 50)
    choice = input("Install packages from requirements.txt? (y/n): ").lower().strip()
    if choice in ['y', 'yes', '']:
        install_packages()
    
    print("\n" + "=" * 50)
    print("🎉 Python coding environment setup complete!")
    print("\nQuick commands:")
    print("  python3 run.py              # Run main.py with formatted output")
    print("  python3 run.py filename.py  # Run any Python file")
    print("  python3 main.py             # Run main.py directly")
    print("  python3 -m unittest discover tests  # Run all tests")
    print("  python3 -c 'your code here' # Quick one-liner")

if __name__ == "__main__":
    main()