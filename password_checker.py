# password_checker.py
import re
import sys
from getpass import getpass

def check_password(password: str):
    """Return dict with rule checks and score."""
    rules = {
        'length': len(password) >= 8,
        'lower': re.search(r'[a-z]', password) is not None,
        'upper': re.search(r'[A-Z]', password) is not None,
        'digit': re.search(r'\d', password) is not None,
        'special': re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
    }

    score = sum(bool(v) for v in rules.values())  # 0..5

    if score == 5:
        strength = 'Strong'
    elif score >= 3:
        strength = 'Moderate'
    elif score >= 1:
        strength = 'Weak'
    else:
        strength = 'Very Weak'

    missing = [k for k, v in rules.items() if not v]

    return {
        'strength': strength,
        'score': score,
        'missing': missing,
        'rules': rules
    }

def pretty_print(result):
    print(f"\nPassword strength: {result['strength']} ({result['score']}/5)\n")
    if result['missing']:
        print("Missing requirements:")
        if 'length' in result['missing']:
            print(" - Minimum 8 characters")
        if 'lower' in result['missing']:
            print(" - At least one lowercase letter (a-z)")
        if 'upper' in result['missing']:
            print(" - At least one uppercase letter (A-Z)")
        if 'digit' in result['missing']:
            print(" - At least one digit (0-9)")
        if 'special' in result['missing']:
            print(" - At least one special character (e.g. !@#$%)")
    else:
        print("All requirements met ✅")

def main():
    print("Password Complexity Checker")
    # getpass hides typed password in terminal (safer)
    password = getpass("Enter password to check (input hidden): ").strip()
    if not password:
        print("No password entered. Exiting.")
        sys.exit(0)

    result = check_password(password)
    pretty_print(result)

if __name__ == "__main__":
    main()
