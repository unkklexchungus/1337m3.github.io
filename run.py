#!/usr/bin/env python3
"""
Python code runner with clear output separation
"""
import sys
import subprocess
import os
from datetime import datetime

def run_python_file(filename):
    """Run a Python file and display output with clear separation"""
    print("=" * 60)
    print(f"🚀 Running: {filename}")
    print(f"⏰ Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    try:
        # Run the Python file
        result = subprocess.run([sys.executable, filename], 
                              capture_output=True, 
                              text=True, 
                              cwd=os.getcwd())
        
        if result.stdout:
            print("📤 OUTPUT:")
            print("-" * 40)
            print(result.stdout)
        
        if result.stderr:
            print("⚠️  ERRORS:")
            print("-" * 40)
            print(result.stderr)
        
        print("=" * 60)
        print(f"✅ Completed with exit code: {result.returncode}")
        
    except Exception as e:
        print(f"❌ Error running {filename}: {e}")
    
    print("=" * 60)

def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        if os.path.exists(filename):
            run_python_file(filename)
        else:
            print(f"❌ File not found: {filename}")
    else:
        # Default to running main.py
        if os.path.exists("main.py"):
            run_python_file("main.py")
        else:
            print("❌ No file specified and main.py not found")
            print("Usage: python run.py [filename.py]")

if __name__ == "__main__":
    main()