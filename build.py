#!/usr/bin/env python3
"""
Build script for the Window-81 game
This script creates a standalone executable that doesn't require Python or pygame installation.
"""

import os
import sys
import subprocess
import shutil
import platform

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
    
    # Clean up previous builds
    print("\nCleaning up previous builds...")
    for cleanup_dir in ["dist", "build"]:
        if os.path.exists(cleanup_dir):
            shutil.rmtree(cleanup_dir)
            print(f"✓ Removed {cleanup_dir} directory")
    
    # Remove spec file if it exists
    spec_file = "Window-81.spec"
    if os.path.exists(spec_file):
        os.remove(spec_file)
        print(f"✓ Removed {spec_file}")
    
    # Create the executable
    print("\nBuilding executable...")
    
    # Determine platform-specific settings
    is_windows = platform.system() == "Windows"
    data_separator = ";" if is_windows else ":"
    console_option = "--noconsole" if is_windows else "--windowed"
    
    # PyInstaller command with optimizations for faster loading
    pyinstaller_cmd = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",  # Create a single executable file
        console_option,  # Don't show console window
        "--name=Window-81",  # Name of the executable
        "--icon=icon.png",  # Use the game icon
        f"--add-data=icon.png{data_separator}.",  # Include icon file
        f"--add-data=instructions.png{data_separator}.",  # Include instructions image
        "--hidden-import=pygame",  # Ensure pygame is included
        "--hidden-import=os",  # Ensure os module is included
        "--hidden-import=sys",  # Ensure sys module is included
        "--strip",  # Remove debug symbols to reduce size
        "--exclude-module=tkinter",  # Exclude unused modules
        "--exclude-module=matplotlib",
        "--exclude-module=numpy",
        "--exclude-module=pandas",
        "--exclude-module=scipy",
        "--exclude-module=PIL",
        "--exclude-module=IPython",
        "--exclude-module=jupyter",
        "--exclude-module=notebook",
        "--exclude-module=qtpy",
        "--exclude-module=PyQt5",
        "--exclude-module=PySide2",
        "--exclude-module=wx",
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
    
    if is_windows:
        print(f"Executable name: Window-81.exe")
    else:
        print(f"Executable name: Window-81 (macOS/Linux)")
    
    print("\nTo distribute your game:")
    print("1. Copy the entire 'dist' folder")
    print("2. Share it with others - they won't need Python or pygame installed!")
    print("3. Users can run the executable directly")
    
    print(f"\n=== Performance Tips ===")
    print("• The executable may take 10-30 seconds to start on first run")
    print("• Subsequent runs will be faster")
    print("• For even faster loading, consider using --onedir instead of --onefile")
    print("  (This creates a folder with the executable and dependencies)")

if __name__ == "__main__":
    main() 