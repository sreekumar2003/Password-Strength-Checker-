"""
Password Strength Checker - Console Version
Simple and effective password validation tool
"""

# List of common passwords to avoid
COMMON_PASSWORDS = ['password', '123456', 'qwerty', 'abc123', '12345678', 
                    'password1', '111111', 'welcome', 'admin', 'letmein']


def check_password(password):
    """
    Check if password meets all security requirements
    Returns: score (0-100+) and list of feedback messages
    """
    score = 0
    feedback = []
    
    # Check 1: Length (minimum 8 characters)
    if len(password) >= 8:
        score += 25
        feedback.append("✓ Good length (8+ characters)")
    else:
        feedback.append("✗ Too short - need at least 8 characters")
    
    # Check 2: Uppercase letter
    if any(char.isupper() for char in password):
        score += 25
        feedback.append("✓ Contains uppercase letter")
    else:
        feedback.append("✗ Add at least one uppercase letter (A-Z)")
    
    # Check 3: Lowercase letter
    if any(char.islower() for char in password):
        score += 25
        feedback.append("✓ Contains lowercase letter")
    else:
        feedback.append("✗ Add at least one lowercase letter (a-z)")
    
    # Check 4: Number
    if any(char.isdigit() for char in password):
        score += 25
        feedback.append("✓ Contains number")
    else:
        feedback.append("✗ Add at least one number (0-9)")
    
    # Check 5: Special character (bonus points)
    if any(not char.isalnum() for char in password):
        score += 10
        feedback.append("✓ Contains special character (bonus!)")
    
    # Check 6: Not a common password
    if password.lower() in COMMON_PASSWORDS:
        score = 0
        feedback.insert(0, "⚠ WARNING: This is a commonly used password!")
    
    return score, feedback


def get_strength_label(score):
    """
    Convert score to strength rating
    """
    if score < 25:
        return "Very Weak 🔴"
    elif score < 50:
        return "Weak 🟠"
    elif score < 75:
        return "Medium 🟡"
    elif score < 100:
        return "Strong 🟢"
    else:
        return "Very Strong 💚"


def display_results(password, score, feedback):
    """
    Display password strength results in a nice format
    """
    strength = get_strength_label(score)
    
    print("\n" + "="*60)
    print("           PASSWORD STRENGTH ANALYSIS")
    print("="*60)
    print(f"Password: {'*' * len(password)}")
    print(f"Strength: {strength}")
    print(f"Score: {score}/100")
    print("-"*60)
    print("Feedback:")
    for item in feedback:
        print(f"  {item}")
    print("="*60)
    
    if score >= 75:
        print("✅ Your password is strong! Good job!")
    else:
        print("⚠️  Your password could be stronger. See feedback above.")
    print()


def show_requirements():
    """
    Display password requirements
    """
    print("\n" + "="*60)
    print("         PASSWORD STRENGTH CHECKER")
    print("="*60)
    print("\nPassword Requirements:")
    print("  • At least 8 characters long")
    print("  • At least one uppercase letter (A-Z)")
    print("  • At least one lowercase letter (a-z)")
    print("  • At least one number (0-9)")
    print("  • At least one special character (!@#$%^&* etc.)")
    print("  • Should not be a common password")
    print("\n" + "="*60 + "\n")


def main():
    """
    Main function - runs the password checker
    """
    show_requirements()
    
    while True:
        # Get password from user
        password = input("Enter password to check (or 'quit' to exit): ")
        
        # Exit if user wants to quit
        if password.lower() == 'quit':
            print("\n👋 Thanks for using Password Strength Checker!")
            break
        
        # Check if password is empty
        if not password:
            print("⚠️  Password cannot be empty. Please try again.\n")
            continue
        
        # Check the password
        score, feedback = check_password(password)
        
        # Display results
        display_results(password, score, feedback)
        
        # Ask if user wants to check another password
        if score >= 75:
            choice = input("Check another password? (yes/no): ")
            if choice.lower() != 'yes':
                print("\n👋 Thanks for using Password Strength Checker!")
                break
            print()

# Run the program
if __name__ == "__main__":
    main()


'''
Password Strength Checker | Python
- Developed CLI tool for password validation with 5-criteria scoring algorithm
- Implemented efficient character validation using generator expressions and any() function
- Integrated common password detection to prevent dictionary attacks
- Designed user-friendly interface with real-time feedback and strength ratings (0-100+ scale)
'''    
    