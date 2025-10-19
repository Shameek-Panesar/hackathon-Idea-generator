"""
Setup script for the Hackathon Idea Generator.
Run this script to install dependencies and set up the environment.
"""

import subprocess
import sys
import os

def print_header(text):
    """Print a formatted header."""
    print("\n" + "="*60)
    print(f"  {text}")
    print("="*60 + "\n")

def install_requirements():
    """Install required Python packages."""
    print_header("Installing Required Packages")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("\n✅ All packages installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("\n❌ Error installing packages. Please check your internet connection.")
        return False

def setup_env_file():
    """Set up the .env file."""
    print_header("Setting Up Environment Variables")
    
    if os.path.exists(".env"):
        print("⚠️  .env file already exists. Skipping creation.")
        return True
    
    api_key = input("Enter your OpenAI API Key (or press Enter to skip): ").strip()
    
    with open(".env", "w") as f:
        if api_key:
            f.write(f"OPENAI_API_KEY={api_key}\n")
            print("\n✅ .env file created with your API key!")
        else:
            f.write("OPENAI_API_KEY=your_openai_api_key_here\n")
            print("\n⚠️  .env file created. Please add your API key later!")
    
    return True

def main():
    """Main setup function."""
    print_header("🚀 Hackathon Idea Generator - Setup")
    print("This script will set up your environment for the Hackathon Idea Generator.")
    
    # Step 1: Install requirements
    if not install_requirements():
        print("\n❌ Setup failed. Please resolve the errors and try again.")
        return
    
    # Step 2: Set up .env file
    if not setup_env_file():
        print("\n❌ Setup failed. Please resolve the errors and try again.")
        return
    
    # Success message
    print_header("✅ Setup Complete!")
    print("Your Hackathon Idea Generator is ready to use!\n")
    print("Next steps:")
    print("1. Make sure your OpenAI API key is set in the .env file")
    print("2. Run the app with: streamlit run app.py")
    print("\nFor more information, see README.md")
    print("\nHappy hacking! 🚀\n")

if __name__ == "__main__":
    main()
