#!/usr/bin/env python3
"""
Build script for the Window-81 game
This script creates a standalone executable that doesn't require Python or pygame installation.
"""

import os
import sys
import subprocess
import shutil

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"Running: {description}")
    print(f"Command: {command}")
    
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        sys.exit(1)
    else:
        print(f"Success: {result.stdout}")
        return result

def main():
    print("=== Window-81 Game Builder ===")
    
    # Check if PyInstaller is installed
    try:
        import PyInstaller
        print("✓ PyInstaller is available")
    except ImportError:
        print("Installing PyInstaller...")
        run_command("pip install pyinstaller", "Installing PyInstaller")
    
    # Check if pygame is installed
    try:
        import pygame
        print("✓ Pygame is available")
    except ImportError:
        print("Installing pygame...")
        run_command("pip install pygame", "Installing pygame")
    
    # Create the executable
    print("\nBuilding executable...")
    
    # PyInstaller command with optimizations
    pyinstaller_cmd = [
        "pyinstaller",
        "--onefile",  # Create a single executable file
        "--windowed",  # Don't show console window on Windows
        "--name=Window-81",  # Name of the executable
        "--icon=icon.png",  # Use the game icon
        "--add-data=icon.png;.",  # Include icon file
        "--add-data=instructions.png;.",  # Include instructions image
        "--hidden-import=pygame",  # Ensure pygame is included
        "--hidden-import=os",  # Ensure os module is included
        "--hidden-import=sys",  # Ensure sys module is included
        "main.py"
    ]
    
    # Join the command for execution
    command = " ".join(pyinstaller_cmd)
    run_command(command, "Building executable with PyInstaller")
    
    # Copy additional files to dist folder
    print("\nCopying additional files...")
    dist_dir = "dist"
    
    # Ensure dist directory exists
    if not os.path.exists(dist_dir):
        os.makedirs(dist_dir)
    
    # Copy README to dist folder
    if os.path.exists("Readme.md"):
        shutil.copy("Readme.md", os.path.join(dist_dir, "README.md"))
        print("✓ Copied README.md")
    
    print(f"\n=== Build Complete ===")
    print(f"Your executable is located in: {os.path.abspath(dist_dir)}")
    print(f"Executable name: Window-81.exe (Windows) or Window-81 (macOS/Linux)")
    print("\nTo distribute your game:")
    print("1. Copy the entire 'dist' folder")
    print("2. Share it with others - they won't need Python or pygame installed!")
    print("3. Users can run the executable directly")

if __name__ == "__main__":
    main() 