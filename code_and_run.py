#!/usr/bin/env python3
"""
Interactive Python coding with immediate output
"""
import sys
import os
from datetime import datetime

def run_code_block(code, description="Code Block"):
    """Execute a code block and display results with formatting"""
    print("\n" + "=" * 60)
    print(f"🔥 Executing: {description}")
    print(f"⏰ Time: {datetime.now().strftime('%H:%M:%S')}")
    print("=" * 60)
    print("📝 CODE:")
    print("-" * 40)
    print(code)
    print("-" * 40)
    
    try:
        # Create a local namespace for execution
        local_vars = {}
        exec(code, globals(), local_vars)
        
        # If there are any local variables created, show them
        if local_vars:
            print("📊 VARIABLES CREATED:")
            print("-" * 40)
            for var, value in local_vars.items():
                if not var.startswith('__'):
                    print(f"{var} = {repr(value)}")
        
    except Exception as e:
        print("❌ ERROR:")
        print("-" * 40)
        print(f"{type(e).__name__}: {e}")
    
    print("=" * 60)

def main():
    print("🐍 Interactive Python Coding Environment")
    print("Type your Python code and see immediate output!")
    print("Commands: 'quit' to exit, 'clear' to clear screen")
    print("=" * 60)
    
    while True:
        try:
            print("\n💡 Enter Python code (press Enter twice to execute):")
            lines = []
            while True:
                line = input(">>> " if not lines else "... ")
                if line.strip() == "":
                    if lines:
                        break
                    else:
                        continue
                elif line.strip().lower() == "quit":
                    print("👋 Goodbye!")
                    return
                elif line.strip().lower() == "clear":
                    os.system('clear' if os.name == 'posix' else 'cls')
                    print("🐍 Interactive Python Coding Environment")
                    print("=" * 60)
                    lines = []
                    continue
                else:
                    lines.append(line)
            
            if lines:
                code = '\n'.join(lines)
                run_code_block(code, "Interactive Code")
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except EOFError:
            print("\n\n👋 Goodbye!")
            break

if __name__ == "__main__":
    main()